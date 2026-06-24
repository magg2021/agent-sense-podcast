# Slack Message: LinkedIn MCP Server Attempt

---

Okay so I just wasted 3 hours trying to build a LinkedIn MCP server and I'm honestly so frustrated right now.

Here's what happened:

I thought "hey, let's connect Bob to LinkedIn so we can automate some stuff." Seemed straightforward enough. Built the entire MCP server - TypeScript, proper error handling, 5 different tools (get profile, create posts, search people, etc.). The code is actually really clean. I'm proud of it.

Then I had to deal with LinkedIn's developer portal.

First, you create an app. Fine. Then you need to configure OAuth. Okay, whatever. Then you need to request "Products" - which is apparently different from OAuth scopes? The UI is confusing as hell. I click "Request access" for "Sign In with LinkedIn" and it just... approves it instantly? But then says I need to wait for review? I don't even know.

Then the OAuth flow. Oh my god. You authorize the app, it redirects you to localhost:3000/callback, which obviously doesn't exist, so you get a "This site can't be reached" error. BUT THAT'S EXPECTED. The docs say "this is normal." Like... what? Why would an error page be the expected behavior? Just give me the token directly!

So I copy the URL from the error page, extract the authorization code, run a curl command to exchange it for an access token. Finally got the token. Updated my .env file. Server builds perfectly. npm start works. Everything looks good.

Then I test it.

```
403 Forbidden - ACCESS_DENIED
"Not enough permissions to access: me.GET.NO_VERSION"
```

ARE YOU KIDDING ME?!

I have the token. I requested the products. I followed every single step in their documentation. And it STILL doesn't have permission to read my own profile data. MY OWN PROFILE.

I spent 3 hours on this. The actual coding took maybe 45 minutes. The rest was fighting with LinkedIn's API permission bureaucracy. And at the end of it all, I have a perfectly working MCP server that can't actually access LinkedIn because their API won't let me.

I'm so done with enterprise APIs right now. This is why people use Zapier. At least that actually works.

The server is sitting there in the repo, fully functional, just waiting for LinkedIn to decide I'm worthy of accessing my own data. Maybe in 1-2 business days after they "review" my request. For an app that only I will use. To access my own profile.

I need a drink.

/rant

Anyone else dealt with LinkedIn's API recently? Please tell me I'm not the only one who finds this absurd.