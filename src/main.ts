import { checkXAPI } from './updater.ts';
import { startDiscordBot } from './discord_bot.ts';

const START_INTERVAL = 15000; // 15秒

// X APIの状態チェックとDiscord Botの起動
async function startBot() {
  // Discord Botを起動
  await startDiscordBot();

  // 15秒ごとにX APIをチェック
  setInterval(async () => {
    await checkXAPI();  // X APIの状態をチェック
  }, START_INTERVAL);
}

// Botを開始
startBot();
