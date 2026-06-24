# Quick Start Guide

## Installation Steps

1. **Navigate to the server directory:**
   ```bash
   cd linkedin-mcp-server
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your LinkedIn access token:
   ```env
   LINKEDIN_ACCESS_TOKEN=your_actual_access_token_here
   ```

4. **Build the server:**
   ```bash
   npm run build
   ```

5. **Test the server (optional):**
   ```bash
   npm start
   ```
   You should see: "LinkedIn MCP Server running on stdio"

## Connecting to Claude Desktop

### macOS Configuration

1. Open or create the Claude Desktop config file:
   ```bash
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. Add the LinkedIn MCP server configuration:
   ```json
   {
     "mcpServers": {
       "linkedin": {
         "command": "node",
         "args": [
           "/Users/monikaaggarwal/Documents/2024/Blogs and Posts/Podcast - Agent Sense/linkedin-mcp-server/dist/index.js"
         ],
         "env": {
           "LINKEDIN_ACCESS_TOKEN": "your_actual_access_token_here"
         }
       }
     }
   }
   ```

3. **Important:** Replace `your_actual_access_token_here` with your real LinkedIn access token

4. Restart Claude Desktop

5. Verify the connection by asking Claude:
   ```
   Can you use the get_profile tool to show me my LinkedIn profile?
   ```

## Getting a LinkedIn Access Token

### Method 1: Using LinkedIn OAuth Playground

1. Go to https://www.linkedin.com/developers/apps
2. Select or create your app
3. Go to the "Auth" tab
4. Use the OAuth 2.0 tools to generate a token

### Method 2: Manual OAuth Flow

1. **Authorization URL:**
   ```
   https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:3000/callback&scope=r_liteprofile%20r_emailaddress%20w_member_social
   ```

2. **Exchange code for token:**
   ```bash
   curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=authorization_code" \
     -d "code=YOUR_AUTH_CODE" \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET" \
     -d "redirect_uri=http://localhost:3000/callback"
   ```

## Testing the Tools

Once connected to Claude Desktop, try these commands:

1. **Get your profile:**
   ```
   Use the get_profile tool to retrieve my LinkedIn profile
   ```

2. **Create a post:**
   ```
   Use the create_post tool to share: "Testing my new LinkedIn MCP integration!"
   ```

3. **Get your recent posts:**
   ```
   Use the get_posts tool to show my last 5 posts
   ```

4. **Get your connections:**
   ```
   Use the get_connections tool to show my first 10 connections
   ```

## Troubleshooting

### "Cannot find module" errors
- Make sure you ran `npm install`
- Verify the build completed: `npm run build`

### "LINKEDIN_ACCESS_TOKEN environment variable is required"
- Check your `.env` file exists and has the token
- For Claude Desktop, ensure the token is in the config JSON

### "401 Unauthorized" errors
- Your access token may be expired (LinkedIn tokens expire after 60 days)
- Generate a new access token
- Verify you have the required OAuth scopes

### Server won't connect to Claude Desktop
- Verify the absolute path in the config is correct
- Restart Claude Desktop after config changes
- Check Claude Desktop logs for errors

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore all available tools and their parameters
- Set up token refresh for long-term use
- Consider implementing rate limiting for production use