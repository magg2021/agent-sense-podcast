# Setting Up LinkedIn MCP Server with Cline (VS Code)

Your LinkedIn MCP server is working! ✅ Now let's connect it to Cline.

## Configuration for Cline

### Option 1: Using Cline's MCP Settings (Recommended)

1. **Open Cline Settings in VS Code:**
   - Click on the Cline icon in VS Code sidebar
   - Click the gear icon (⚙️) or go to Settings
   - Look for "MCP Servers" or "Model Context Protocol" section

2. **Add LinkedIn MCP Server:**
   
   Add this configuration:
   ```json
   {
     "name": "linkedin",
     "command": "node",
     "args": [
       "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js"
     ],
     "env": {
       "LINKEDIN_ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE"
     }
   }
   ```

3. **Replace YOUR_ACCESS_TOKEN_HERE** with your actual LinkedIn Access Token

4. **Restart Cline** or reload VS Code window (Command+Shift+P → "Reload Window")

### Option 2: Using Cline Config File

If Cline uses a config file (usually in `~/.cline/` or VS Code settings):

1. **Find Cline's config file:**
   ```bash
   # Check common locations
   ls ~/.cline/config.json
   # or
   ls ~/Library/Application\ Support/Code/User/settings.json
   ```

2. **Add MCP server configuration** to the appropriate section

### Option 3: Direct Integration (Advanced)

If you want to use the MCP server programmatically:

```javascript
// In your code
const { spawn } = require('child_process');

const mcpServer = spawn('node', [
  '/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js'
], {
  env: {
    ...process.env,
    LINKEDIN_ACCESS_TOKEN: 'your_token_here'
  }
});
```

## Testing the Connection

Once configured, you should be able to use these tools in Cline:

1. **Get Profile:**
   ```
   Use the get_profile tool to retrieve my LinkedIn profile
   ```

2. **Create Post:**
   ```
   Use the create_post tool to share: "Testing my LinkedIn MCP integration!"
   ```

3. **Get Posts:**
   ```
   Use the get_posts tool to show my last 5 posts
   ```

4. **Search People:**
   ```
   Use the search_people tool to find "software engineers"
   ```

5. **Get Connections:**
   ```
   Use the get_connections tool to show my connections
   ```

## Available Tools

Your LinkedIn MCP server provides these tools:

- **get_profile** - Get your LinkedIn profile information
- **create_post** - Create a new LinkedIn post
- **get_posts** - Retrieve your recent posts
- **search_people** - Search for people on LinkedIn
- **get_connections** - Get your LinkedIn connections

## Troubleshooting

### Cline doesn't see the MCP server

1. Check Cline's MCP support is enabled in settings
2. Verify the path to `dist/index.js` is correct
3. Make sure your Access Token is set in the environment
4. Restart VS Code completely

### "LINKEDIN_ACCESS_TOKEN environment variable is required"

- Make sure you added the token in the MCP server configuration
- The token should be in the `env` section of the config

### "401 Unauthorized" errors

- Your Access Token may have expired (LinkedIn tokens expire after 60 days)
- Generate a new token from LinkedIn Developer Portal
- Update both `.env` file and Cline configuration

## Alternative: Use as Standalone Tool

If Cline doesn't support MCP yet, you can:

1. **Run the server in Terminal:**
   ```bash
   cd "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server"
   npm start
   ```

2. **Interact via stdio** (standard input/output)

3. **Or create a simple wrapper script** that Cline can call

## Need Help?

- Check Cline's documentation for MCP support
- See `README.md` for full server documentation
- See `STEP_BY_STEP_SETUP.md` for detailed setup instructions

## Server Status

✅ Server is built and working
✅ Access Token is configured
✅ Server runs successfully with `npm start`

Next step: Configure Cline to use the MCP server!