import requests
from config.settings import DISCORD_WEBHOOK_URL

def send_discord_notification(message):
    payload = {
        "content": message
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("✅ 通知をDiscordに送信しました。")
        else:
            print(f"❌ 通知送信に失敗しました: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Discord通知送信時にエラーが発生しました: {e}")
