import tweepy
import time
from config.settings import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET
from src.notifier import send_discord_notification

# Tweepyのセットアップ
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# 登録されているXアカウントの情報（仮のデータ）
X_ACCOUNTS = {
    "username1": {"last_tweet": "", "last_follower_count": 1000},
    "username2": {"last_tweet": "", "last_follower_count": 500},
}

# Xアカウントの状態をチェック
def check_x_accounts():
    for username, data in X_ACCOUNTS.items():
        try:
            user = api.get_user(screen_name=username)
            # ツイート内容とフォロワー数を確認
            tweet = user.status.text
            follower_count = user.followers_count

            # 更新があった場合通知
            if tweet != data["last_tweet"]:
                data["last_tweet"] = tweet
                send_discord_notification(f"📢 {username} の新しいツイート: {tweet}")

            if follower_count != data["last_follower_count"]:
                data["last_follower_count"] = follower_count
                send_discord_notification(f"📢 {username} のフォロワー数が {follower_count} に更新されました。")

        except Exception as e:
            print(f"❌ エラーが発生しました: {e}")
            send_discord_notification(f"❌ {username} の情報取得に失敗しました: {e}")

# 15秒ごとにXアカウントをチェック
def start_account_check():
    while True:
        check_x_accounts()
        time.sleep(15)
