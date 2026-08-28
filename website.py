import os
import threading

from flask import Flask

import discord
from discord.ext import commands
from discord import app_commands


# =========================================================
# Flask 웹사이트
# =========================================================

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NOVA BOT</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #0b0b12;
                color: white;
                font-family: Arial, sans-serif;
            }

            .box {
                text-align: center;
                padding: 50px;
                border-radius: 20px;
                background: #151520;
                box-shadow: 0 0 40px rgba(255, 255, 255, 0.08);
            }

            h1 {
                margin-bottom: 10px;
                font-size: 42px;
            }

            p {
                color: #bdbdc8;
                font-size: 17px;
            }

            .online {
                margin-top: 25px;
                color: #7cff9b;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>✦ NOVA</h1>
            <p>VALORANT COMMUNITY BOT</p>
            <div class="online">● BOT ONLINE</div>
        </div>
    </body>
    </html>
    """


def run_web():
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )


# =========================================================
# Discord 설정
# =========================================================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================================================
# 서버 설정
# =========================================================

GUILD_ID = 1541335745753653248


# =========================================================
# 티어 목록
# =========================================================

TIER_LIST = [
    "아이언",
    "브론즈",
    "실버",
    "골드",
    "플래티넘",
    "다이아몬드",
    "초월자",
    "불멸",
    "레디언트"
]


# =========================================================
# 봇 시작
# =========================================================

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
        activity=discord.Game(
            name="NOVA | Valorant"
        )
    )

    # 슬래시 명령어 동기화
    try:
        synced = await bot.tree.sync()

        print(
            f"✅ 슬래시 명령어 {len(synced)}개 동기화 완료"
        )

    except Exception as e:
        print(
            f"❌ 슬래시 명령어 동기화 실패: {e}"
        )


# =========================================================
# 기존 !ping 명령어
# =========================================================

@bot.command()
async def ping(ctx):

    latency = round(
        bot.latency * 1000
    )

    await ctx.send(
        f"🏓 Pong! `{latency}ms`"
    )


# =========================================================
# /ping 슬래시 명령어
# =========================================================

@bot.tree.command(
    name="ping",
    description="NOVA 봇의 응답 속도를 확인합니다."
)
async def slash_ping(
    interaction: discord.Interaction
):

    latency = round(
        bot.latency * 1000
    )

    await interaction.response.send_message(
        f"🏓 Pong! `{latency}ms`"
    )


# =========================================================
# /티어인증
# =========================================================

@bot.tree.command(
    name="티어인증",
    description="NOVA에서 VALORANT 티어 인증을 신청합니다."
)
@app_commands.describe(
    티어="현재 본인의 VALORANT 티어를 선택하세요."
)
@app_commands.choices(
    티어=[
        app_commands.Choice(
            name="아이언",
            value="아이언"
        ),
        app_commands.Choice(
            name="브론즈",
            value="브론즈"
        ),
        app_commands.Choice(
            name="실버",
            value="실버"
        ),
        app_commands.Choice(
            name="골드",
            value="골드"
        ),
        app_commands.Choice(
            name="플래티넘",
            value="플래티넘"
        ),
        app_commands.Choice(
            name="다이아몬드",
            value="다이아몬드"
        ),
        app_commands.Choice(
            name="초월자",
            value="초월자"
        ),
        app_commands.Choice(
            name="불멸",
            value="불멸"
        ),
        app_commands.Choice(
            name="레디언트",
            value="레디언트"
        )
    ]
)
async def tier_verify(
    interaction: discord.Interaction,
    티어: app_commands.Choice[str]
):

    member = interaction.user

    embed = discord.Embed(
        title="✦ NOVA 티어 인증 신청",
        description=(
            "티어 인증 신청이 접수되었습니다.\n\n"
            f"👤 신청자 : {member.mention}\n"
            f"🏆 신청 티어 : **{티어.value}**\n\n"
            "관리진이 인증 자료를 확인한 후\n"
            "티어 역할을 부여합니다."
        ),
        color=discord.Color.blurple()
    )

    embed.set_footer(
        text="NOVA | VALORANT COMMUNITY"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /티어목록
# =========================================================

@bot.tree.command(
    name="티어목록",
    description="NOVA에서 인증 가능한 VALORANT 티어를 확인합니다."
)
async def tier_list(
    interaction: discord.Interaction
):

    tier_text = "\n".join(
        f"・ {tier}"
        for tier in TIER_LIST
    )

    embed = discord.Embed(
        title="🏆 NOVA 티어 목록",
        description=tier_text,
        color=discord.Color.blurple()
    )

    embed.set_footer(
        text="NOVA | VALORANT COMMUNITY"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /서버정보
# =========================================================

@bot.tree.command(
    name="서버정보",
    description="NOVA 서버 정보를 확인합니다."
)
async def server_info(
    interaction: discord.Interaction
):

    guild = interaction.guild

    if guild is None:
        await interaction.response.send_message(
            "❌ 서버에서만 사용할 수 있습니다.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="✦ NOVA SERVER",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="👥 멤버",
        value=f"`{guild.member_count}명`",
        inline=True
    )

    embed.add_field(
        name="💬 채널",
        value=f"`{len(guild.channels)}개`",
        inline=True
    )

    embed.add_field(
        name="🆔 서버 ID",
        value=f"`{guild.id}`",
        inline=False
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# 오류 처리
# =========================================================

@bot.event
async def on_command_error(
    ctx,
    error
):

    if isinstance(
        error,
        commands.CommandNotFound
    ):
        return

    print(
        f"❌ 명령어 오류: {error}"
    )


# =========================================================
# 봇 실행
# =========================================================

def run_bot():

    token = os.environ.get(
        "DISCORD_TOKEN"
    )

    if not token:

        print(
            "❌ DISCORD_TOKEN을 찾을 수 없습니다!"
        )

        return

    print(
        "🔄 Discord 봇 연결을 시작합니다..."
    )

    try:

        bot.run(token)

    except Exception as e:

        print(
            f"❌ 봇 실행 중 오류 발생: {e}"
        )


# =========================================================
# 실행
# =========================================================

if __name__ == "__main__":

    web_thread = threading.Thread(
        target=run_web,
        daemon=True
    )

    web_thread.start()

    run_bot()
