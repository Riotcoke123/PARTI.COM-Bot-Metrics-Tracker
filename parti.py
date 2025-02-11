import requests
import json
import time
import random

def calculate_real_viewers(total_viewers):
    ratio = random.choice([12, 8])  # Randomly select 12:1 or 8:1 botting behavior
    return total_viewers // ratio

def get_bot_metrics(user_id):
    url = f"https://api-backend.parti.com/parti_v2/profile/user_profile/{user_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        total_viewers = data.get("total_viewers", 0)
        real_viewers = calculate_real_viewers(total_viewers)
        
        metrics = {
            "username": data.get("username"),
            "unique_chatters": data.get("unique_chatters"),
            "total_viewers": total_viewers,
            "real_viewers": real_viewers,
            "monitoring": data.get("monitoring")
        }
        
        with open("bot_metrics.json", "w") as json_file:
            json.dump(metrics, json_file, indent=4)
        
        print("Bot Metrics updated.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    user_id = input("Enter User ID: ")
    while True:
        get_bot_metrics(user_id)
        time.sleep(60)
