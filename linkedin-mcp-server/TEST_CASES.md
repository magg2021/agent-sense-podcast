# LinkedIn MCP Server Test Cases

Use these test cases to verify your LinkedIn MCP server is working correctly.

---

## Test Case 1: Get Your LinkedIn Profile ✅

**Tool:** `get_profile`

**Test Command:**
```
Use the get_profile tool to retrieve my LinkedIn profile information
```

**Expected Result:**
- Returns your LinkedIn profile data including:
  - Your LinkedIn ID
  - First name and last name
  - Profile picture URL (if available)
- Status: Success (200)

**What to Check:**
- ✅ Your name appears correctly
- ✅ LinkedIn ID is returned
- ✅ No authentication errors

---

## Test Case 2: Create a Simple Post 📝

**Tool:** `create_post`

**Test Command:**
```
Use the create_post tool to share this message: "Testing my new LinkedIn MCP integration! 🚀 #API #Automation"
```

**Parameters:**
- text: "Testing my new LinkedIn MCP integration! 🚀 #API #Automation"
- visibility: PUBLIC (default)

**Expected Result:**
- Post is created successfully
- Returns post ID/URN
- Post appears on your LinkedIn feed

**What to Check:**
- ✅ Post appears on your LinkedIn profile
- ✅ Text is correct with emojis and hashtags
- ✅ Post is public (visible to everyone)

---

## Test Case 3: Create a Connections-Only Post 🔒

**Tool:** `create_post`

**Test Command:**
```
Use the create_post tool to share this message with visibility set to CONNECTIONS: "This is a private test post visible only to my connections."
```

**Parameters:**
- text: "This is a private test post visible only to my connections."
- visibility: CONNECTIONS

**Expected Result:**
- Post is created successfully
- Post is only visible to your connections
- Returns post ID/URN

**What to Check:**
- ✅ Post appears on your profile
- ✅ Post visibility is set to "Connections only"
- ✅ Not visible when logged out

---

## Test Case 4: Get Your Recent Posts 📋

**Tool:** `get_posts`

**Test Command:**
```
Use the get_posts tool to retrieve my last 5 LinkedIn posts
```

**Parameters:**
- count: 5

**Expected Result:**
- Returns up to 5 of your most recent posts
- Each post includes:
  - Post ID/URN
  - Text content
  - Creation date
  - Visibility settings

**What to Check:**
- ✅ Returns your recent posts
- ✅ Posts are in reverse chronological order (newest first)
- ✅ Includes the test posts you just created

---

## Test Case 5: Get More Posts 📚

**Tool:** `get_posts`

**Test Command:**
```
Use the get_posts tool to retrieve my last 20 LinkedIn posts
```

**Parameters:**
- count: 20

**Expected Result:**
- Returns up to 20 of your most recent posts
- Same data structure as Test Case 4

**What to Check:**
- ✅ Returns more posts than Test Case 4
- ✅ No duplicate posts
- ✅ All posts belong to you

---

## Test Case 6: Search for People by Keyword 🔍

**Tool:** `search_people`

**Test Command:**
```
Use the search_people tool to find people with keywords "software engineer"
```

**Parameters:**
- keywords: "software engineer"
- count: 10 (default)

**Expected Result:**
- Returns up to 10 people matching the search
- Each result includes:
  - Name
  - Headline
  - Profile URL
  - Location (if available)

**What to Check:**
- ✅ Results are relevant to "software engineer"
- ✅ Returns profile information
- ✅ No errors

**Note:** Search results depend on your LinkedIn network and API permissions.

---

## Test Case 7: Search for People in Your Industry 🎯

**Tool:** `search_people`

**Test Command:**
```
Use the search_people tool to find 15 people with keywords "product manager San Francisco"
```

**Parameters:**
- keywords: "product manager San Francisco"
- count: 15

**Expected Result:**
- Returns up to 15 people matching the search
- Results should be relevant to product management in San Francisco

**What to Check:**
- ✅ Results match the search criteria
- ✅ Returns up to 15 results
- ✅ Includes location information

---

## Test Case 8: Get Your Connections (First 10) 👥

**Tool:** `get_connections`

**Test Command:**
```
Use the get_connections tool to retrieve my first 10 LinkedIn connections
```

**Parameters:**
- start: 0 (default)
- count: 10 (default)

**Expected Result:**
- Returns up to 10 of your LinkedIn connections
- Each connection includes:
  - Name
  - Profile information
  - Connection date (if available)

**What to Check:**
- ✅ Returns your actual connections
- ✅ Names are recognizable
- ✅ No duplicate entries

---

## Test Case 9: Get More Connections (Pagination) 📄

**Tool:** `get_connections`

**Test Command:**
```
Use the get_connections tool with start position 10 and count 25 to get my next batch of connections
```

**Parameters:**
- start: 10
- count: 25

**Expected Result:**
- Returns connections 11-35
- Different connections than Test Case 8
- Same data structure

**What to Check:**
- ✅ Returns different connections than previous test
- ✅ No overlap with first 10 connections
- ✅ Pagination works correctly

---

## Test Case 10: Create a Post with Special Characters 🌐

**Tool:** `create_post`

**Test Command:**
```
Use the create_post tool to share: "Testing special characters: café, naïve, résumé, 日本語, emoji 🎉🚀💡 and line breaks.

This is a new paragraph.

#Testing #Unicode"
```

**Parameters:**
- text: Multi-line text with special characters
- visibility: PUBLIC

**Expected Result:**
- Post is created with all special characters intact
- Line breaks are preserved
- Emojis display correctly
- Unicode characters work

**What to Check:**
- ✅ All special characters appear correctly
- ✅ Line breaks are preserved
- ✅ Emojis render properly
- ✅ Hashtags are clickable

---

## Test Case 11: Error Handling - Empty Post ❌

**Tool:** `create_post`

**Test Command:**
```
Use the create_post tool to share an empty message: ""
```

**Parameters:**
- text: ""

**Expected Result:**
- Should return an error
- Error message about empty content

**What to Check:**
- ✅ Server handles error gracefully
- ✅ Returns meaningful error message
- ✅ Doesn't crash

---

## Test Case 12: Error Handling - Invalid Count ❌

**Tool:** `get_posts`

**Test Command:**
```
Use the get_posts tool to retrieve 100 posts (exceeds maximum of 50)
```

**Parameters:**
- count: 100

**Expected Result:**
- Should limit to maximum of 50 posts
- Or return an error about exceeding limit

**What to Check:**
- ✅ Server enforces limits
- ✅ Returns appropriate response
- ✅ Doesn't crash

---

## Quick Test Suite (Run All at Once) 🚀

Run these commands in sequence to test all functionality:

```
1. Use the get_profile tool to show my LinkedIn profile

2. Use the create_post tool to share: "MCP Server Test #1 - Basic post 🚀"

3. Use the create_post tool with CONNECTIONS visibility to share: "MCP Server Test #2 - Private post 🔒"

4. Use the get_posts tool to retrieve my last 10 posts

5. Use the search_people tool to find "software engineer" (10 results)

6. Use the get_connections tool to show my first 15 connections

7. Use the get_posts tool to verify my test posts appear in the feed
```

---

## Success Criteria ✅

Your LinkedIn MCP server is working correctly if:

- ✅ All profile data retrieves successfully
- ✅ Posts are created and appear on LinkedIn
- ✅ Both PUBLIC and CONNECTIONS visibility work
- ✅ Recent posts are retrieved correctly
- ✅ Search returns relevant results
- ✅ Connections list is accurate
- ✅ Pagination works for posts and connections
- ✅ Special characters and emojis work
- ✅ Error handling is graceful
- ✅ No authentication errors

---

## Troubleshooting Failed Tests

### "401 Unauthorized"
- Access token expired (LinkedIn tokens expire after 60 days)
- Generate new token from LinkedIn Developer Portal
- Update `.env` file with new token

### "403 Forbidden"
- Missing required OAuth scopes
- Check your LinkedIn app has "Sign In with LinkedIn" and "Share on LinkedIn" products enabled

### "429 Too Many Requests"
- Hit LinkedIn's rate limit
- Wait a few minutes before testing again
- Reduce frequency of API calls

### "500 Internal Server Error"
- Check server logs for details
- Verify `.env` file has correct token
- Restart the server: `npm start`

### No Results Returned
- Your LinkedIn account may have limited data
- Try different search terms
- Check if you have connections/posts to retrieve

---

## Performance Benchmarks

Expected response times:
- **get_profile**: < 1 second
- **create_post**: 1-2 seconds
- **get_posts**: 1-3 seconds (depends on count)
- **search_people**: 2-4 seconds
- **get_connections**: 1-3 seconds (depends on count)

If responses are slower, check your internet connection and LinkedIn API status.

---

## Next Steps After Testing

Once all tests pass:
1. ✅ Server is production-ready
2. ✅ Integrate with Cline (see CLINE_SETUP.md)
3. ✅ Build automation workflows
4. ✅ Create scheduled posting scripts
5. ✅ Implement token refresh logic for long-term use

Happy testing! 🎉