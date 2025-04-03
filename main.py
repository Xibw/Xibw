import asyncio
from src.discord_bot import start_discord_bot
from src.api_check import start_account_check

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    
    # Xアカウントのチェックを非同期で開始
    loop.create_task(start_account_check())
    
    # Discord Botを起動
    start_discord_bot()
