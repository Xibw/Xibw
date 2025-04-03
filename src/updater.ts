import { postToDiscord } from './discord_bot.ts';
import { getXAPIData } from './twitter_api.ts';

// X APIの状態をチェックする関数
export async function checkXAPI() {
  try {
    const data = await getXAPIData();
    console.log("X API Data:", data);

    // X APIのステータスに基づきDiscordに通知
    await postToDiscord(`X APIの状態: ${data.status}`);

  } catch (error) {
    console.error("X APIチェックに失敗:", error);
    await postToDiscord("X APIチェックでエラーが発生しました。");
  }
}
