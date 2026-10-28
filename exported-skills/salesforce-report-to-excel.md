# Skill: salesforce-report-to-excel

**Trigger phrases:** "extract Salesforce report to Excel", "export report to spreadsheet", "Salesforce report to Excel"

---

# Salesforce Report → Excel

This skill walks through extracting data from any Salesforce report and producing a
formatted, hyperlinked Excel workbook. It handles everything from first-time setup
through to the final `.xlsx` file.

---

## Phase 1 — Gather Requirements

Ask the user for:

1. **Salesforce report URL** — the full URL of the report (e.g. `https://myorg.lightning.force.com/lightning/r/Report/00O.../view`)
2. **Output file name** — what to call the Excel file (default: `SalesforceReport.xlsx`)
3. **Output location** — where to save it (default: the current workspace folder)

Also ask: *"Is this your first time running this, or do you already have the Playwright MCP server set up?"*
- If they're unsure, assume **first time** and run Phase 2.
- If they confirm Playwright is already set up, skip to Phase 3.

---

## Phase 2 — One-Time Setup (skip if Playwright MCP already configured)

### 2a — Check Node.js

Run:
```
node --version
```

- If the command succeeds (v18+), continue.
- If it fails or the version is below 18, tell the user to install Node.js from https://nodejs.org and wait for confirmation before continuing.

### 2b — Check Python and create a virtual environment

Run:
```
python3 --version
```

- If it fails, tell the user to install Python 3 from https://www.python.org/downloads/ and wait.

Create a virtual environment inside the workspace (skip if `.venv` already exists):
```
python3 -m venv .venv
```

Install openpyxl into it:
```
.venv/bin/pip install openpyxl -q
```

> All subsequent `python3` calls in this skill must use `.venv/bin/python3` so the dependency is always available regardless of the system Python state.

### 2c — Set up Playwright browser automation

Use the Playwright MCP server (or equivalent browser automation tool available in the AI assistant) to navigate web pages. If Playwright MCP is not configured, set it up before continuing.

---

## Phase 3 — Navigate to the Report and Log In

### 3a — Open the report

Navigate to the Salesforce report URL the user provided using a browser automation tool.

### 3b — Handle login

Check the resulting page URL:
- If it redirects to a login page (e.g. `login.salesforce.com`, `login.w3.ibm.com`, or similar SSO), tell the user:
  > "The browser has opened and is showing the Salesforce login page. Please log in manually in that browser window (complete any MFA if prompted), then come back here and say 'I'm logged in' once the report is fully visible on screen."

  Wait for the user to confirm they are logged in before continuing.

- If the report loads directly (already authenticated), continue immediately.

### 3c — Wait for the report to fully load

Wait for the report title or data to appear on screen before proceeding.

---

## Phase 4 — Capture the Report Data

### 4a — Find the runReport network request

Inspect network requests and filter for `runReport` to find the API call(s) that returned the report data.

- Look for POST requests to URLs containing `runReport` with a `[200]` status.
- If there are multiple, use the one with the most recent timestamp or the largest response.

### 4b — Save the response body

Save the response body to a temp file: `.playwright-mcp/sf-report-data.json`

If no `runReport` request is found:
- Try filtering for `/analytics` or `/aura` as a fallback.
- If still no data, ask the user to refresh the report page in the browser and then repeat steps 4a–4b.

---

## Phase 5 — Run the ETL Script

### 5a — Locate the ETL script

The ETL script is bundled with this skill. Use the path appropriate for your setup:
```
.bob/skills/salesforce-report-to-excel/etl.py
```

### 5b — Run the script

Execute:
```
.venv/bin/python3 .bob/skills/salesforce-report-to-excel/etl.py \
  .playwright-mcp/sf-report-data.json \
  "<output_xlsx_path>" \
  "<salesforce_base_url>"
```

Where:
- `<output_xlsx_path>` is the file name/path the user specified in Phase 1
- `<salesforce_base_url>` is the base URL of their Salesforce org (e.g. `https://myorg.lightning.force.com`) — extract this from the report URL

### 5c — Handle the result

The script prints a line starting with `SUCCESS|` on success, e.g.:
```
SUCCESS|142|MyReport.xlsx
```

- Parse the row count and file path from this line.
- If the script exits with an error instead:
  - If it says `openpyxl is not installed`, run `.venv/bin/pip install openpyxl` and retry.
  - If it says `No such file`, check that the JSON file was saved correctly in Phase 4.
  - Otherwise, report the error to the user with the full message.

---

## Phase 6 — Confirm and Summarise

Tell the user the file is ready. Include:
- ✅ The full file path of the Excel workbook
- The number of rows extracted
- A brief description of the columns included
- The report name (from the Salesforce response)

Example:
> "Your Excel file is ready at `/Users/you/workspace/MyReport.xlsx`. It contains **142 rows** from the Salesforce report **'FSM West 2026-Data Opps by UT20'**, with the following columns: Account Name, Portfolio (UT20), Forecast Category, Stage, Opportunity Owner, Opportunity Name (hyperlinked back to Salesforce), Product Name, Close Date, Estimated Total (USD), Product Family, Revenue Type, and Created Date."

---

## Notes

- **Re-running for a refreshed report:** If the user has already run this skill and just wants to refresh the data, skip Phase 2 entirely and start at Phase 3.
- **Adding new accounts:** If the user needs to add rows for a specific account after the fact, re-run from Phase 3 and pass the saved JSON to the ETL script again — it will rebuild the full file with the latest data.
- **Multiple reports:** Each run produces a separate Excel file. Encourage users to name files descriptively.
- **Salesforce SSO:** Many enterprise Salesforce orgs use SSO (IBM w3id, Okta, etc.). The login step always requires the user to authenticate manually — the AI assistant never handles credentials.
- **Large reports:** Salesforce may paginate reports. If `allData: false` appears in the JSON, inform the user that not all rows were captured and suggest using the Salesforce Analytics REST API for full extraction (requires API access).
