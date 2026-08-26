```python
import os
import threading

from flask import Flask
import discord
from discord.ext import commands


# ==========================================
# Flask 웹서버
# ==========================================

app = Flask(__name__)


@app.route("/")
def home():
    return "NOVA BOT IS ONLINE!"


def run_web():
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )


# ==========================================
# Discord 봇 설정
# ==========================================

intents = discord.Intents.default()

# 메시지 내용 읽기
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ==========================================
# 봇 온라인 확인
# ==========================================

@bot.event
async def on_ready():

    print("")
    print("==========================================")
    print("✅ NOVA 봇 온라인!")
    print(f"🤖 봇 이름 : {bot.user}")
    print(f"🆔 봇 ID   : {bot.user.id}")
    print(f"🏠 서버 수 : {len(bot.guilds)}")
    print("==========================================")
    print("")

    # Discord에서 봇 상태를 온라인으로 표시
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="NOVA | Valorant")
    )


# ==========================================
# 테스트 명령어
# ==========================================

@bot.command()
async def ping(ctx):

    latency = round(bot.latency * 1000)

    await ctx.send(
        f"🏓 Pong! `{latency}ms`"
    )


# ==========================================
# Discord 봇 실행
# ==========================================

def run_bot():

    token = os.environ.get("DISCORD_TOKEN")

    if not token:
        print("")
        print("❌ DISCORD_TOKEN을 찾을 수 없습니다.")
        print("❌ Render 환경변수를 확인해주세요.")
        print("")
        return

    print("")
    print("🔄 Discord 봇 연결을 시작합니다...")
    print("")

    try:
        bot.run(token)

    except Exception as e:
        print("")
        print(f"❌ 봇 실행 오류: {e}")
        print("")


# ==========================================
# 프로그램 시작
# ==========================================

if __name__ == "__main__":

    # Flask 웹서버 시작
    web_thread = threading.Thread(
        target=run_web,
        daemon=True
    )

    web_thread.start()

    # Discord 봇 시작
    run_bot()
```
