import os
import requests
import json

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ["NOTION_INTEGRATION_TOKEN"]

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13',
}

payload = {
    "parent": {"database_id": "a334fba2b64f471cb91940dd135f7d2e"},
    "properties": {
        "Name": {
            "title": [{
                "text": {
                    "content": "Vyvy-vi"
                }
            }]
        }
    }
}

res = requests.post(
    "https://api.notion.com/v1/pages",
    headers=headers,
    data=json.dumps(payload)
)
