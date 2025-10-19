import requests
import sys

API_TOKEN_KEY = '[REDACTED_DISCORD_BOT_TOKEN]'
TARGET_CHANNEL_ID = '1290060281657036938'

def fetch_recent_messages(bot_secret, chan_id, max_results=10):
    
    api_endpoint = f"https://discord.com/api/v9/channels/{chan_id}/messages"
    
    request_headers = {
        "Authorization": f"Bot {bot_secret}"
    }
    
    query_params = {
        "limit": max_results
    }

    try:
        response = requests.get(api_endpoint, headers=request_headers, params=query_params)
        response.raise_for_status() 
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

message_list = fetch_recent_messages(API_TOKEN_KEY, TARGET_CHANNEL_ID, max_results=10)

if message_list:    
    for item in reversed(message_list):
        author = item['author']['username']
        content = item['content']
        print(f"[{author}] - {content}")
else:
    print("Impossible to get the messages")