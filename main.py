from src.api_check import start_account_check
from threading import Thread

if __name__ == "__main__":
    # Xアカウントのチェックを別スレッドで開始
    account_check_thread = Thread(target=start_account_check)
    account_check_thread.start()
