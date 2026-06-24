# LinkedIn MCP Server

A Model Context Protocol (MCP) server that provides LinkedIn integration capabilities. This server allows you to interact with LinkedIn's API through MCP-compatible clients like Claude Desktop.

## Features

- **Get Profile**: Retrieve authenticated user's LinkedIn profile information
- **Create Post**: Create new posts on LinkedIn
- **Get Posts**: Retrieve recent posts from the authenticated user
- **Search People**: Search for people on LinkedIn
- **Get Connections**: Retrieve user's LinkedIn connections

## Prerequisites

- Node.js 18 or higher
- A LinkedIn Developer account
- LinkedIn API credentials (Client ID, Client Secret, Access Token)

## Setup

### 1. Get LinkedIn API Credentials

1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/apps)
2. Create a new app or use an existing one
3. Note your **Client ID** and **Client Secret**
4. Configure OAuth 2.0 settings:
   - Add redirect URL: `http://localhost:3000/callback`
   - Request the following scopes:
     - `r_liteprofile` - Read basic profile info
     - `r_emailaddress` - Read email address
     - `w_member_social` - Post, comment, and share content
     - `r_basicprofile` - Read basic profile
     - `rw_company_admin` - Manage company pages (if needed)

### 2. Get Access Token

You'll need to obtain an OAuth 2.0 access token. You can use LinkedIn's OAuth flow or tools like Postman to get a token.

**OAuth Flow:**
```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=r_liteprofile%20r_emailaddress%20w_member_social
```

Exchange the authorization code for an access token:
```bash
curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=YOUR_AUTH_CODE" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "redirect_uri=YOUR_REDIRECT_URI"
```

### 3. Install Dependencies

```bash
cd linkedin-mcp-server
npm install
```

### 4. Configure Environment Variables

Copy the example environment file and add your credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your LinkedIn credentials:

```env
LINKEDIN_CLIENT_ID=your_client_id_here
LINKEDIN_CLIENT_SECRET=your_client_secret_here
LINKEDIN_ACCESS_TOKEN=your_access_token_here
LINKEDIN_REDIRECT_URI=http://localhost:3000/callback
```

### 5. Build the Server

```bash
npm run build
```

## Usage

### Running Standalone

```bash
npm start
```

### Integrating with Claude Desktop

Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "linkedin": {
      "command": "node",
      "args": ["/absolute/path/to/linkedin-mcp-server/dist/index.js"],
      "env": {
        "LINKEDIN_ACCESS_TOKEN": "your_access_token_here"
      }
    }
  }
}
```

Replace `/absolute/path/to/linkedin-mcp-server` with the actual path to your server directory.

## Available Tools

### 1. get_profile
Get the authenticated user's LinkedIn profile information.

**Parameters**: None

**Example**:
```
Use the get_profile tool to retrieve my LinkedIn profile
```

### 2. create_post
Create a new post on LinkedIn.

**Parameters**:
- `text` (required): The text content of the post
- `visibility` (optional): Post visibility - "PUBLIC" or "CONNECTIONS" (default: "PUBLIC")

**Example**:
```
Use the create_post tool to share: "Excited to announce our new product launch! #innovation"
```

### 3. get_posts
Get recent posts from the authenticated user.

**Parameters**:
- `count` (optional): Number of posts to retrieve (default: 10, max: 50)

**Example**:
```
Use the get_posts tool to retrieve my last 20 posts
```

### 4. search_people
Search for people on LinkedIn.

**Parameters**:
- `keywords` (required): Search keywords
- `count` (optional): Number of results to return (default: 10)

**Example**:
```
Use the search_people tool to find "software engineers in San Francisco"
```

### 5. get_connections
Get the authenticated user's connections.

**Parameters**:
- `start` (optional): Starting position (default: 0)
- `count` (optional): Number of connections to retrieve (default: 10, max: 50)

**Example**:
```
Use the get_connections tool to get my first 25 connections
```

## Development

### Watch Mode

For development with auto-rebuild:

```bash
npm run watch
```

In another terminal:
```bash
npm start
```

### Project Structure

```
linkedin-mcp-server/
├── src/
│   └── index.ts          # Main server implementation
├── dist/                 # Compiled JavaScript (generated)
├── .env                  # Environment variables (create from .env.example)
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore rules
├── package.json         # Node.js dependencies and scripts
├── tsconfig.json        # TypeScript configuration
└── README.md            # This file
```

## Troubleshooting

### Access Token Issues

If you get authentication errors:
1. Verify your access token is valid and not expired
2. Check that you have the required OAuth scopes
3. LinkedIn access tokens typically expire after 60 days - you may need to refresh them

### API Rate Limits

LinkedIn has rate limits on their API. If you encounter rate limit errors:
- Wait before making additional requests
- Consider implementing caching for frequently accessed data
- Review LinkedIn's [API documentation](https://docs.microsoft.com/en-us/linkedin/) for current limits

### Connection Issues

If the MCP server won't connect:
1. Ensure the server builds successfully (`npm run build`)
2. Check that the path in Claude Desktop config is absolute and correct
3. Verify environment variables are set correctly
4. Check Claude Desktop logs for error messages

## Security Notes

- **Never commit your `.env` file** - it contains sensitive credentials
- Store access tokens securely
- Rotate access tokens regularly
- Use environment-specific credentials for development vs production
- Consider implementing token refresh logic for long-running deployments

## API Limitations

- LinkedIn's API has usage limits and quotas
- Some endpoints may require additional permissions or app review
- The v2 API is used; some features may require migration to newer versions
- Company page management requires additional setup and permissions

## Resources

- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [LinkedIn Developer Portal](https://www.linkedin.com/developers/)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

For issues related to:
- **LinkedIn API**: Check [LinkedIn's developer documentation](https://docs.microsoft.com/en-us/linkedin/)
- **MCP Protocol**: See [MCP documentation](https://modelcontextprotocol.io/)
- **This server**: Open an issue in the repository