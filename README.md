# Xibw Bot

Xibw Botは、X（旧Twitter）APIと連携したDiscord Botです。Xのアカウントやハッシュタグのデータをリアルタイムで取得し、Discordに通知する機能を提供します。また、YouTube、Instagram、Twitchのリンクにも対応し、関連情報を自動で取得して投稿します。

## 機能一覧
- **X API連携**: Xアカウント、ハッシュタグ、フォロワー、リポストの監視
- **YouTubeリンク対応**: YouTubeリンクを自動的に認識して処理
- **Instagramリンク対応**: Instagramリンクを自動的に認識して処理
- **Twitchリンク対応**: Twitchリンクを自動的に認識して処理
- **Discord Bot**: コマンドを使ってAPIの状態やエラーを確認可能
- **自動API更新機能**: 60秒ごとにX APIをチェックし、Tweepyのバージョンも毎日確認

## 必要なもの
- **Deno Deploy**: Deno環境でホスティング
- **GitHub**: リポジトリ管理
- **Discord Bot Token**: Discordにボットを追加するためのトークン
- **X APIキー**: X（Twitter）APIのアクセス認証情報
- **環境変数**: Botの動作に必要な認証情報を環境変数で設定

## コマンド

- **`/status`**: APIの状態を手動で確認  
- **`/X [user/u] [username/@/URL] [class]`**: Xアカウントを登録  
- **`/X [hash/h] [word] [class]`**: Xハッシュタグを登録  
- **`/X [start/sa] [ALL/class]`**: APIの自動更新を開始  
- **`/X [stop/so] [ALL/class]`**: APIの自動更新を停止  
- **`/X [delete/d] [class]`**: 登録したユーザー、ハッシュタグを削除

## デプロイ後の動作確認
- Discord Botが正常に起動しているか確認  
- APIエラー発生時にDiscord通知が届くことを確認

## 注意事項
- **配布は行っていません**。このBotはhttps://discord.com/oauth2/authorize?client_id=1356841089193087016 から利用はできます。
---
### **Xibw Bot バージョン一覧**  

🔧 V0 シリーズ (基盤構築)

バージョン	機能概要	詳細説明

V0.1	Discord Bot 起動	/ping コマンドで動作確認、基本的なイベントハンドリング

V0.2	カスタムエラー処理	XbiwError クラス実装（エラーコード、スタックトレース取得）

V0.3	エラー通知機能	Discord Webhook で開発者にエラーを自動送信

V0.4	コマンドログ記録	ユーザー操作をデータベースに保存（SQLite/MongoDB）、/logs で検索可能

V0.5	設定管理システム	config.json + 環境変数、サーバーごとのカスタム設定（プレフィックス等）

V0.6	多言語対応 (i18n)	英語/日本語対応、/language set ja で切り替え

V0.7	パフォーマンス最適化	コマンドキャッシュ（Redis）、非同期処理強化

V0.8	管理者デバッグツール	/sysinfo（Botのリソース監視）、/force-error（テスト用エラー生成）

V0.9	セキュリティ強化	コマンド権限制御（レベル1~5）、IPレートリミット

🐦 V1 シリーズ (X/Twitter 連携)

バージョン	機能概要	詳細説明

V1.0	X API 試験導入 (テスター向け)	許可リスト制御、/beta-x post <text>（限定公開）

V1.1	X ログイン機能	OAuth2 連携、アカウント紐付け

V1.2	読み込み機能一般公開	テスター制限解除、/x get <tweet_id> でツイート取得

V1.3	投稿・リツイート機能	/x post <text>, /x retweet <id>

V1.4	API 自動更新	トークンリフレッシュ機能（有効期限切れ防止）

V1.5	リアルタイム通知	特定ユーザーのツイートをDiscordに転送

V1.6	メディア対応	画像/動画のアップロード・ダウンロード

V1.7	ブックマーク機能	/x bookmark add <id>（後で閲覧可能）

V1.8	自動レスポンス	キーワード検知で返信（例: 「#質問」→ 定型文）

V1.9	データバックアップ	GitHub API 連携で設定/ログを自動バックアップ

📺 V2 シリーズ (YouTube 連携)

バージョン	機能概要	詳細説明

V2.0	YouTube API 試験導入	テスター向け /beta-youtube notify <channelID>（新着動画通知）

V2.1	ログイン機能	Google OAuth2 連携

V2.2	一般公開	通知機能の全面開放

V2.3	動画情報取得	/youtube video <ID>（タイトル/視聴回数表示）

V2.4	ライブ配信トラッキング	配信開始/終了を通知

V2.5	プレイリスト管理	動画の追加・削除

V2.6	チャット連携	YouTube Live チャットをDiscordに転送

V2.7	自動字幕生成	YouTube字幕 → Discordテキスト

V2.8	カスタム通知設定	キーワードフィルタリング（例: 「ゲーム」を含む動画のみ通知）

V2.9	データ分析	チャンネル統計を表示（例: 月間視聴回数）

📷 V3 シリーズ (Instagram 連携)

バージョン	機能概要	詳細説明

V3.0	Instagram API 試験導入	テスター向け /beta-instagram story <user>

V3.1	ログイン機能	Instagram OAuth 連携

V3.2	一般公開	ストーリー/投稿取得機能開放

V3.3	メディアダウンロード	画像/動画をDiscordに保存

V3.4	ハッシュタグ追跡	特定タグの新着投稿を通知

V3.5	自動いいね/コメント	条件設定（例: 「#猫」を含む投稿に自動いいね）

V3.6	プロフィール分析	フォロワー数/エンゲージメント率表示

V3.7	複数アカウント管理	ビジネスアカウント切り替え

V3.8	スケジュール投稿	投稿予約機能

V3.9	バックアップ	投稿データをクラウド保存

🎮 V4 シリーズ (Twitch 連携)

バージョン	機能概要	詳細説明

V4.0	Twitch API 試験導入	テスター向け /beta-twitch alert <streamer>

V4.1	ログイン機能	Twitch OAuth 連携

V4.2	一般公開	配信通知機能全面開放

V4.3	チャット連携	TwitchチャットをDiscordに転送

V4.4	サブスクリプション管理	サブスク状況表示

V4.5	視聴者分析	同時接続数/チャット活性度を表示

V4.6	自動モデレーション	DiscordとTwitchチャットの連携BAN

V4.7	カスタムコマンド連携	Twitchの!コマンドをDiscordで反応

V4.8	クラップ/チップ通知	寄付・スタンプをDiscordに通知

V4.9	マルチストリーム監視	複数配信者の同時トラッキング
