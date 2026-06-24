#!/bin/bash

# LinkedIn OAuth Token Exchange Script
# Replace these values with your actual credentials

CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"
AUTH_CODE="YOUR_AUTHORIZATION_CODE"
REDIRECT_URI="http://localhost:3000/callback"

echo "Requesting access token from LinkedIn..."
echo ""

curl -X POST "https://www.linkedin.com/oauth/v2/accessToken" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=${AUTH_CODE}" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "redirect_uri=${REDIRECT_URI}"

echo ""
echo ""
echo "Copy the access_token value from above (without quotes)"

# Made with Bob
