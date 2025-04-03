README.md（Xibw V0.2）
markdown
コピーする
編集する
# Xibw - Discord Bot for X API Updates  

Xibwは、X（旧Twitter）のAPI更新を自動で監視し、Discordに通知するBotです。  
また、YouTube・Instagram・Twitchリンクの対応も予定されています。  

## 📌 **主な機能 (V0.2)**
- X API の状態を **60秒ごと** にチェック
- Tweepy のバージョンを **1日ごと** に確認
- APIの異常を検知すると **Discordに通知**
- `/status` コマンドで手動でAPIの状態を確認可能  

## 📂 **プロジェクト構成**
Xibw/ ├── src/ │ ├── main.ts # Denoのエントリーポイント │ ├── config.ts # 設定ファイル（APIキーなど） │ ├── discord_bot.ts # Discord Botのロジック │ ├── twitter_api.ts # X APIのロジック │ ├── updater.ts # API自動更新機能 │ ├── utils.ts # ユーティリティ関数 ├── .gitignore ├── deno.json # Deno設定ファイル ├── README.md

bash
コピーする
編集する

## 🚀 **セットアップ**
### 1️⃣ **GitHub からコードを取得**
```sh
git clone https://github.com/yourusername/Xibw.git
cd Xibw
2️⃣ 環境変数の設定
.env ファイルを作成し、以下の情報を追加：

ini
コピーする
編集する
DISCORD_TOKEN=your_discord_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_SECRET=your_access_secret
3️⃣ Deno をインストール
Deno公式サイト からDenoをインストール。
または以下のコマンドでインストール：

sh
コピーする
編集する
curl -fsSL https://deno.land/x/install/install.sh | sh
4️⃣ Bot を起動
sh
コピーする
編集する
deno run --allow-net --allow-env src/main.ts
🔧 Deno Deploy でのデプロイ
Deno Deploy にアクセスし、新しいプロジェクトを作成

GitHubリポジトリを接続し、自動デプロイを設定

環境変数をDeno Deployの "Settings" に追加

デプロイボタンをクリック！

⚙ コマンド一覧
コマンド	説明
/status	X APIとTweepyの状態を確認
/X user [username/@/URL] [class]	Xのユーザーを登録
/X hash [word] [class]	ハッシュタグを登録
/X start [ALL/class]	特定のクラスの監視を開始
/X stop [ALL/class]	監視を停止
/X delete [class]	クラスを削除
🛠 今後の予定
✅ V0.2: API自動更新
✅ V0.5: Xアカウント連携機能追加
✅ V1: Xのデータ読み込み機能
✅ V2: 投稿機能追加
✅ V3: ハート、フォロー、リポスト機能
✅ V4: YouTubeリンク対応
✅ V5: Instagramリンク対応
✅ V6: Twitchリンク対応

📜 ライセンス
MIT License

📢 ご意見・バグ報告
不具合報告や機能の提案があれば、Issues で報告してください！

コピーする
編集する

これでどうでしょう？追加したい内容があれば教えてください！💡
