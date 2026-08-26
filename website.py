import os
import threading

from flask import Flask
import discord
from discord.ext import commands

app = Flask(__name__)

@app.route("/")
def home():
    return "NOVA BOT IS ONLINE!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print("==========================================")
    print("✅ NOVA 봇 온라인!")
    print(f"🤖 봇 이름 : {bot.user}")
    print(f"🆔 봇 ID   : {bot.user.id}")
    print(f"🏠 서버 수 : {len(bot.guilds)}")
    print("==========================================")

    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="NOVA | Valorant")
    )

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! `{latency}ms`")

def run_bot():
    token = os.environ.get("DISCORD_TOKEN")

    if not token:
        print("❌ DISCORD_TOKEN을 찾을 수 없습니다!")
        return

    print("🔄 Discord 봇 연결을 시작합니다...")

    try:
        bot.run(token)
    except Exception as e:
        print(f"❌ 봇 실행 중 오류 발생: {e}")

if __name__ == "__main__":
    web_thread = threading.Thread(
        target=run_web,
        daemon=True
    )
    web_thread.start()

    run_bot()
