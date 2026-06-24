# Step-by-Step Setup Instructions for LinkedIn MCP Server

Follow these instructions carefully to set up and connect your LinkedIn MCP server to Claude Desktop.

---

## Part 1: Get LinkedIn API Credentials (15-20 minutes)

### Step 1: Create a LinkedIn Developer Account

1. Open your web browser and go to: https://www.linkedin.com/developers/apps
2. Click **"Sign in"** with your LinkedIn account
3. If prompted, agree to the LinkedIn Developer Terms

### Step 2: Create a New LinkedIn App

1. Click the **"Create app"** button
2. Fill in the required information:
   - **App name**: `My MCP LinkedIn Integration` (or any name you prefer)
   - **LinkedIn Page**: Select your company page (or create a test page)
   - **App logo**: Upload any image (can be changed later)
   - **Legal agreement**: Check the box to agree
3. Click **"Create app"**

### Step 3: Configure OAuth Settings

1. In your app dashboard, click on the **"Auth"** tab
2. Scroll down to **"OAuth 2.0 settings"**
3. Under **"Redirect URLs"**, click **"Add redirect URL"**
4. Enter: `http://localhost:3000/callback`
5. Click **"Update"**

### Step 4: Check Available API Products

1. In your app dashboard, click on the **"Products"** tab
2. You'll see available LinkedIn API products. Look for:
   - **Sign In with LinkedIn using OpenID Connect** - Usually auto-approved
   - **Share on LinkedIn** - Usually auto-approved
   - **Advertising API** - Requires application (optional)
   - **Marketing Developer Platform** - Requires application (optional)

3. Click **"Request access"** or **"Select"** for:
   - **Sign In with LinkedIn using OpenID Connect** (for profile access)
   - **Share on LinkedIn** (for posting capabilities)

4. These are typically approved instantly. If you see "Access granted" or a checkmark, you're good to go!

5. **Note**: The available scopes depend on which products you have access to:
   - Sign In with LinkedIn gives you: `openid`, `profile`, `email`
   - Share on LinkedIn gives you: `w_member_social` (posting)

6. If you need additional products, click "Request access" and fill out the application form. Review can take 1-2 business days.

### Step 5: Get Your Client ID and Secret

1. In the **"Auth"** tab, find the **"Application credentials"** section
2. Copy and save these values somewhere safe:
   - **Client ID**: (looks like: 86abc123def456)
   - **Client Secret**: (looks like: AbC123DeF456)
   - ⚠️ **IMPORTANT**: Never share your Client Secret publicly!

### Step 6: Generate an Access Token

**Option A: Using LinkedIn's OAuth 2.0 Tools (Recommended)**

1. In your app's **"Auth"** tab, scroll to **"OAuth 2.0 tools"**
2. Click **"Generate token"** or **"Create token"**
3. You'll be redirected to authorize your app - click **"Allow"**
4. **IMPORTANT**: You'll see an error page saying **"This site can't be reached"** - THIS IS NORMAL! ✅
5. Look at your browser's address bar. The URL will look like:
   ```
   http://localhost:3000/callback?code=AQTxxx...very_long_code...xxx&state=xxx
   ```
6. Copy the ENTIRE URL from the address bar
7. Go back to your LinkedIn app's **"Auth"** tab
8. Paste the URL into the OAuth 2.0 tools section where it says "Enter authorization code URL"
9. LinkedIn will extract the code and generate your access token
10. Copy the access token (starts with: `AQV...`)
11. ⚠️ **Note**: This token expires in 60 days

**If the OAuth 2.0 tools don't work, use Option B below**

**Option B: Manual OAuth Flow (If Option A doesn't work)**

1. Open a new browser tab and paste this URL (replace YOUR_CLIENT_ID with your actual Client ID):
   ```
   https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:3000/callback&scope=openid%20profile%20email%20w_member_social
   ```

2. Press Enter - you'll be asked to authorize your app

3. Click **"Allow"** to authorize

4. **You'll see "This site can't be reached" - THIS IS EXPECTED!** ✅

5. Look at your browser's address bar. The URL will look like one of these:
   ```
   http://localhost:3000/callback?code=AQTxxx...very_long_code...xxx&state=xxx
   ```
   OR (without state parameter):
   ```
   http://localhost:3000/callback?code=AQTxxx...very_long_code...xxx
   ```

6. Copy the entire URL from your browser's address bar

7. Extract just the `code` value:
   - It's everything after `code=`
   - If there's a `&state=` at the end, stop before it
   - If there's no `&state`, the code goes to the end of the URL
   
   **Example 1** (with state):
   - URL: `http://localhost:3000/callback?code=AQT123abc&state=xyz`
   - Your code: `AQT123abc`
   
   **Example 2** (without state):
   - URL: `http://localhost:3000/callback?code=AQQ4-Mj8zJLNENgmyl91qNw...`
   - Your code: `AQQ4-Mj8zJLNENgmyl91qNw...` (everything after `code=`)

8. Open Terminal (you can run this from any directory - it doesn't matter):
   ```bash
   curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=authorization_code" \
     -d "code=YOUR_AUTH_CODE" \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET" \
     -d "redirect_uri=http://localhost:3000/callback"
   ```
   
   **Replace these values:**
   - `YOUR_AUTH_CODE` - The code you extracted in step 7
   - `YOUR_CLIENT_ID` - Your Client ID from Step 5
   - `YOUR_CLIENT_SECRET` - Your Client Secret from Step 5

9. You'll get a JSON response like:
   ```json
   {
     "access_token": "AQVxxx...your_token_here...xxx",
     "expires_in": 5184000
   }
   ```

10. Copy the `access_token` value (without the quotes)

---

## Part 2: Set Up the MCP Server (5 minutes)

### Step 7: Navigate to the Server Directory

1. Open Terminal (Applications → Utilities → Terminal)
2. Navigate to the server directory by running this command:
   ```bash
   cd "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server"
   ```
3. Press Enter. You should now be in the linkedin-mcp-server directory.

### Step 8: Verify Installation

**All commands in this step should be run from the linkedin-mcp-server directory (you're already there from Step 7)**

1. Check that dependencies are installed:
   ```bash
   ls node_modules
   ```
   - If you see a list of folders, you're good!
   - If not, run: `npm install`

2. Check that the server is built:
   ```bash
   ls dist
   ```
   - You should see: `index.js`, `index.d.ts`, and map files
   - If not, run: `npm run build`

### Step 9: Create Environment File

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor:
   ```bash
   open -a TextEdit .env
   ```

3. Replace `your_access_token_here` with your actual LinkedIn access token from Step 6:
   ```env
   LINKEDIN_ACCESS_TOKEN=AQVxxx...your_actual_token_here...xxx
   ```

4. Save and close the file

### Step 10: Test the Server (Optional but Recommended)

1. Run the server:
   ```bash
   npm start
   ```

2. You should see:
   ```
   LinkedIn MCP Server running on stdio
   ```

3. Press `Ctrl+C` to stop the server

---

## Part 3: Connect to Claude Desktop (5 minutes)

### Step 11: Locate Claude Desktop Config File

1. Open Terminal
2. Check if the config file exists:
   ```bash
   ls ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
   - If it exists, you'll see the file path
   - If not, you'll see "No such file or directory" - that's okay!

### Step 12: Create or Edit Config File

**If the file doesn't exist:**
```bash
mkdir -p ~/Library/Application\ Support/Claude
touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Open the config file:**
```bash
open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Step 13: Add LinkedIn MCP Server Configuration

1. If the file is empty, paste this entire configuration:
   ```json
   {
     "mcpServers": {
       "linkedin": {
         "command": "node",
         "args": [
           "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js"
         ],
         "env": {
           "LINKEDIN_ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE"
         }
       }
     }
   }
   ```

2. If the file already has content with other MCP servers, add the linkedin section inside `mcpServers`:
   ```json
   {
     "mcpServers": {
       "existing-server": {
         ...existing config...
       },
       "linkedin": {
         "command": "node",
         "args": [
           "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js"
         ],
         "env": {
           "LINKEDIN_ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE"
         }
       }
     }
   }
   ```

3. **IMPORTANT**: Replace `YOUR_ACCESS_TOKEN_HERE` with your actual LinkedIn access token from Step 6

4. Save the file (Command+S) and close TextEdit

### Step 14: Restart Claude Desktop

1. Quit Claude Desktop completely:
   - Click **Claude** in the menu bar
   - Click **Quit Claude**
   - Or press `Command+Q`

2. Wait 5 seconds

3. Open Claude Desktop again from Applications

---

## Part 4: Test the Connection (2 minutes)

### Step 15: Verify MCP Server is Connected

1. Open a new conversation in Claude Desktop

2. Look for the MCP indicator (usually a small icon or badge showing connected servers)

3. Type this message to Claude:
   ```
   Can you list the available MCP tools?
   ```

4. You should see the LinkedIn tools listed:
   - get_profile
   - create_post
   - get_posts
   - search_people
   - get_connections

### Step 16: Test a Simple Tool

1. Ask Claude:
   ```
   Use the get_profile tool to show me my LinkedIn profile information
   ```

2. If successful, you'll see your LinkedIn profile data!

3. If you get an error, proceed to troubleshooting below

---

## Troubleshooting

### Problem: "LINKEDIN_ACCESS_TOKEN environment variable is required"

**Solution:**
1. Check your `.env` file has the token
2. Verify the token in Claude Desktop config matches
3. Make sure there are no extra spaces or quotes around the token

### Problem: "401 Unauthorized" or "Invalid access token"

**Solution:**
1. Your token may have expired (LinkedIn tokens expire after 60 days)
2. Generate a new access token (repeat Step 6)
3. Update both `.env` and Claude Desktop config with the new token
4. Restart Claude Desktop

### Problem: "Cannot find module" errors

**Solution:**
1. Navigate to the server directory:
   ```bash
   cd "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server"
   ```
2. Reinstall dependencies:
   ```bash
   npm install
   ```
3. Rebuild:
   ```bash
   npm run build
   ```
4. Restart Claude Desktop

### Problem: Server not showing in Claude Desktop

**Solution:**
1. Verify the path in config is correct (no typos)
2. Check the config file is valid JSON (use https://jsonlint.com)
3. Make sure you completely quit and restarted Claude Desktop
4. Check Claude Desktop logs:
   ```bash
   tail -f ~/Library/Logs/Claude/mcp*.log
   ```

### Problem: "Permission denied" when running commands

**Solution:**
1. Make the server executable:
   ```bash
   chmod +x "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js"
   ```

---

## Success Checklist

✅ LinkedIn Developer app created  
✅ OAuth scopes configured  
✅ Access token generated  
✅ Server dependencies installed  
✅ Server built successfully  
✅ `.env` file created with token  
✅ Claude Desktop config updated  
✅ Claude Desktop restarted  
✅ LinkedIn tools visible in Claude  
✅ Successfully tested get_profile tool  

---

## What You Can Do Now

Try these commands in Claude Desktop:

1. **View your profile:**
   ```
   Show me my LinkedIn profile using the get_profile tool
   ```

2. **Create a post:**
   ```
   Use the create_post tool to share: "Just set up my LinkedIn MCP integration! 🚀"
   ```

3. **Get your recent posts:**
   ```
   Use the get_posts tool to show my last 5 LinkedIn posts
   ```

4. **Search for people:**
   ```
   Use the search_people tool to find "software engineers in San Francisco"
   ```

5. **View connections:**
   ```
   Use the get_connections tool to show my first 10 LinkedIn connections
   ```

---

## Need More Help?

- **Full Documentation**: See `README.md` in the linkedin-mcp-server folder
- **Quick Reference**: See `QUICK_START.md`
- **LinkedIn API Docs**: https://docs.microsoft.com/en-us/linkedin/
- **MCP Documentation**: https://modelcontextprotocol.io/

Congratulations! You now have a working LinkedIn MCP server connected to Claude Desktop! 🎉