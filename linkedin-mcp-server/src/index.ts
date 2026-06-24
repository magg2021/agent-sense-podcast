#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from "@modelcontextprotocol/sdk/types.js";
import axios, { AxiosInstance } from "axios";
import dotenv from "dotenv";

dotenv.config();

// LinkedIn API configuration
const LINKEDIN_API_BASE = "https://api.linkedin.com/v2";
const LINKEDIN_ACCESS_TOKEN = process.env.LINKEDIN_ACCESS_TOKEN;

if (!LINKEDIN_ACCESS_TOKEN) {
  console.error("Error: LINKEDIN_ACCESS_TOKEN environment variable is required");
  process.exit(1);
}

// Create axios instance with LinkedIn API configuration
const linkedinApi: AxiosInstance = axios.create({
  baseURL: LINKEDIN_API_BASE,
  headers: {
    Authorization: `Bearer ${LINKEDIN_ACCESS_TOKEN}`,
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
  },
});

// Define available tools
const tools: Tool[] = [
  {
    name: "get_profile",
    description: "Get the authenticated user's LinkedIn profile information",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
    },
  },
  {
    name: "create_post",
    description: "Create a new post on LinkedIn",
    inputSchema: {
      type: "object",
      properties: {
        text: {
          type: "string",
          description: "The text content of the post",
        },
        visibility: {
          type: "string",
          description: "Post visibility: PUBLIC or CONNECTIONS",
          enum: ["PUBLIC", "CONNECTIONS"],
          default: "PUBLIC",
        },
      },
      required: ["text"],
    },
  },
  {
    name: "get_posts",
    description: "Get recent posts from the authenticated user",
    inputSchema: {
      type: "object",
      properties: {
        count: {
          type: "number",
          description: "Number of posts to retrieve (default: 10, max: 50)",
          default: 10,
        },
      },
      required: [],
    },
  },
  {
    name: "search_people",
    description: "Search for people on LinkedIn",
    inputSchema: {
      type: "object",
      properties: {
        keywords: {
          type: "string",
          description: "Search keywords",
        },
        count: {
          type: "number",
          description: "Number of results to return (default: 10)",
          default: 10,
        },
      },
      required: ["keywords"],
    },
  },
  {
    name: "get_connections",
    description: "Get the authenticated user's connections",
    inputSchema: {
      type: "object",
      properties: {
        start: {
          type: "number",
          description: "Starting position (default: 0)",
          default: 0,
        },
        count: {
          type: "number",
          description: "Number of connections to retrieve (default: 10, max: 50)",
          default: 10,
        },
      },
      required: [],
    },
  },
];

// Create MCP server
const server = new Server(
  {
    name: "linkedin-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handle list tools request
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools };
});

// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "get_profile": {
        const response = await linkedinApi.get("/me", {
          params: {
            projection: "(id,firstName,lastName,profilePicture(displayImage~:playableStreams))",
          },
        });
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(response.data, null, 2),
            },
          ],
        };
      }

      case "create_post": {
        const { text, visibility = "PUBLIC" } = args as {
          text: string;
          visibility?: string;
        };

        // Get user's URN first
        const profileResponse = await linkedinApi.get("/me");
        const authorUrn = `urn:li:person:${profileResponse.data.id}`;

        const postData = {
          author: authorUrn,
          lifecycleState: "PUBLISHED",
          specificContent: {
            "com.linkedin.ugc.ShareContent": {
              shareCommentary: {
                text: text,
              },
              shareMediaCategory: "NONE",
            },
          },
          visibility: {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility,
          },
        };

        const response = await linkedinApi.post("/ugcPosts", postData);
        return {
          content: [
            {
              type: "text",
              text: `Post created successfully!\n${JSON.stringify(response.data, null, 2)}`,
            },
          ],
        };
      }

      case "get_posts": {
        const { count = 10 } = args as { count?: number };
        const profileResponse = await linkedinApi.get("/me");
        const authorUrn = `urn:li:person:${profileResponse.data.id}`;

        const response = await linkedinApi.get("/ugcPosts", {
          params: {
            q: "authors",
            authors: `List(${authorUrn})`,
            count: Math.min(count, 50),
          },
        });

        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(response.data, null, 2),
            },
          ],
        };
      }

      case "search_people": {
        const { keywords, count = 10 } = args as {
          keywords: string;
          count?: number;
        };

        const response = await linkedinApi.get("/people-search", {
          params: {
            keywords,
            count: Math.min(count, 50),
          },
        });

        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(response.data, null, 2),
            },
          ],
        };
      }

      case "get_connections": {
        const { start = 0, count = 10 } = args as {
          start?: number;
          count?: number;
        };

        const response = await linkedinApi.get("/connections", {
          params: {
            q: "viewer",
            start,
            count: Math.min(count, 50),
          },
        });

        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(response.data, null, 2),
            },
          ],
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error: any) {
    const errorMessage = error.response?.data
      ? JSON.stringify(error.response.data, null, 2)
      : error.message;
    return {
      content: [
        {
          type: "text",
          text: `Error: ${errorMessage}`,
        },
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("LinkedIn MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});

// Made with Bob
