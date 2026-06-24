#!/usr/bin/env node

/**
 * Test script for LinkedIn MCP Server - get_profile tool
 * This script directly calls the LinkedIn API to test the get_profile functionality
 */

import axios from 'axios';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

const LINKEDIN_API_BASE = 'https://api.linkedin.com/v2';
const LINKEDIN_ACCESS_TOKEN = process.env.LINKEDIN_ACCESS_TOKEN;

if (!LINKEDIN_ACCESS_TOKEN) {
  console.error('❌ Error: LINKEDIN_ACCESS_TOKEN not found in .env file');
  process.exit(1);
}

console.log('🧪 Testing LinkedIn MCP Server - get_profile tool\n');
console.log('=' .repeat(60));

async function testGetProfile() {
  try {
    console.log('\n📡 Making request to LinkedIn API...');
    console.log(`Endpoint: ${LINKEDIN_API_BASE}/me`);
    console.log(`Token: ${LINKEDIN_ACCESS_TOKEN.substring(0, 20)}...`);
    
    const response = await axios.get(`${LINKEDIN_API_BASE}/me`, {
      headers: {
        'Authorization': `Bearer ${LINKEDIN_ACCESS_TOKEN}`,
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0',
      },
      params: {
        projection: '(id,firstName,lastName,profilePicture(displayImage~:playableStreams))',
      },
    });

    console.log('\n✅ SUCCESS! Profile retrieved successfully\n');
    console.log('=' .repeat(60));
    console.log('📋 Profile Data:');
    console.log('=' .repeat(60));
    console.log(JSON.stringify(response.data, null, 2));
    console.log('=' .repeat(60));
    
    // Extract and display key information
    console.log('\n📊 Summary:');
    console.log(`   LinkedIn ID: ${response.data.id || 'N/A'}`);
    
    if (response.data.firstName) {
      const firstName = response.data.firstName.localized?.[Object.keys(response.data.firstName.localized)[0]] || 
                       response.data.firstName.preferredLocale?.language || 'N/A';
      console.log(`   First Name: ${firstName}`);
    }
    
    if (response.data.lastName) {
      const lastName = response.data.lastName.localized?.[Object.keys(response.data.lastName.localized)[0]] || 
                      response.data.lastName.preferredLocale?.language || 'N/A';
      console.log(`   Last Name: ${lastName}`);
    }
    
    if (response.data.profilePicture) {
      console.log(`   Profile Picture: Available`);
    }
    
    console.log('\n✅ Test PASSED - get_profile tool is working correctly!\n');
    return true;
    
  } catch (error) {
    console.log('\n❌ TEST FAILED\n');
    console.log('=' .repeat(60));
    console.log('Error Details:');
    console.log('=' .repeat(60));
    
    if (error.response) {
      console.log(`Status: ${error.response.status} ${error.response.statusText}`);
      console.log(`Error Data:`, JSON.stringify(error.response.data, null, 2));
      
      // Provide helpful error messages
      if (error.response.status === 401) {
        console.log('\n💡 Troubleshooting:');
        console.log('   - Your access token may have expired (LinkedIn tokens expire after 60 days)');
        console.log('   - Generate a new token from: https://www.linkedin.com/developers/apps');
        console.log('   - Update your .env file with the new token');
      } else if (error.response.status === 403) {
        console.log('\n💡 Troubleshooting:');
        console.log('   - Missing required OAuth scopes');
        console.log('   - Check your LinkedIn app has "Sign In with LinkedIn" product enabled');
      } else if (error.response.status === 429) {
        console.log('\n💡 Troubleshooting:');
        console.log('   - Rate limit exceeded');
        console.log('   - Wait a few minutes before trying again');
      }
    } else if (error.request) {
      console.log('No response received from LinkedIn API');
      console.log('Check your internet connection');
    } else {
      console.log('Error:', error.message);
    }
    
    console.log('=' .repeat(60));
    return false;
  }
}

// Run the test
testGetProfile()
  .then(success => {
    process.exit(success ? 0 : 1);
  })
  .catch(error => {
    console.error('Unexpected error:', error);
    process.exit(1);
  });

// Made with Bob
