import os
import discord
from discord.ext import commands


# =========================================================
# NOVA DISCORD BOT
# VALORANT TIER VERIFICATION PROTOTYPE
# =========================================================


# =========================================================
# 환경변수
# =========================================================

TOKEN = os.getenv("DISCORD_TOKEN")

# NOVA Discord 서버 ID
GUILD_ID = 1541335745753653248

# NOVA 사이트
WEBSITE_URL = "https://nova-fo0d.onrender.com"


# =========================================================
# TOKEN 확인
# =========================================================

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN 환경변수가 설정되어 있지 않습니다."
    )


# =========================================================
# Intents
# =========================================================

intents = discord.Intents.default()

# 필요할 경우 사용
intents.guilds = True
intents.members = True


# =========================================================
# Bot
# =========================================================

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================================================
# Bot 시작
# =========================================================

@bot.event
async def on_ready():

    print("----------------------------------------")
    print("NOVA Bot Online")
    print(f"Bot Name : {bot.user}")
    print(f"Bot ID   : {bot.user.id}")
    print("----------------------------------------")

    try:

        guild = discord.Object(id=GUILD_ID)

        # 현재 NOVA 서버에 Slash Command 동기화
        synced = await bot.tree.sync(guild=guild)

        print(f"Slash Commands Synced : {len(synced)}")

        for command in synced:
            print(f" - /{command.name}")

    except Exception as e:

        print("Slash Command Sync Error:")
        print(e)


# =========================================================
# /티어인증
# =========================================================

@bot.tree.command(
    name="티어인증",
    description="NOVA에서 VALORANT 티어 인증을 진행합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def tier_verify(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="NOVA  |  VALORANT 티어 인증",
        description=(
            "NOVA 서버에서 VALORANT 티어를 인증하려면\n"
            "아래 **Riot 계정 인증하기** 버튼을 눌러주세요."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🔐 인증 방식",
        value="Riot Sign On (RSO)",
        inline=False
    )

    embed.add_field(
        name="🎮 게임",
        value="VALORANT",
        inline=True
    )

    embed.add_field(
        name="🛡️ 개인정보",
        value=(
            "Riot 계정 인증 과정에서 사용자의 동의가 필요합니다."
        ),
        inline=True
    )

    embed.set_footer(
        text="NOVA Tier Verification"
    )

    # -----------------------------------------------------
    # 버튼
    # -----------------------------------------------------

    view = discord.ui.View()

    button = discord.ui.Button(
        label="Riot 계정 인증하기",
        style=discord.ButtonStyle.link,
        url=f"{WEBSITE_URL}/riot-login"
    )

    view.add_item(button)

    await interaction.response.send_message(
        embed=embed,
        view=view,
        ephemeral=True
    )


# =========================================================
# /노바
# =========================================================

@bot.tree.command(
    name="노바",
    description="NOVA 봇 정보를 확인합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def nova_info(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🌌 NOVA",
        description=(
            "한국 VALORANT 커뮤니티 NOVA의 전용 봇입니다.\n\n"
            "VALORANT 티어 인증 및 커뮤니티 기능을 제공합니다."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 게임",
        value="VALORANT",
        inline=True
    )

    embed.add_field(
        name="🔐 티어 인증",
        value="/티어인증",
        inline=True
    )

    embed.add_field(
        name="🌐 Website",
        value=WEBSITE_URL,
        inline=False
    )

    embed.set_footer(
        text="NOVA Community"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /사이트
# =========================================================

@bot.tree.command(
    name="사이트",
    description="NOVA 인증 사이트 링크를 표시합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def website(
    interaction: discord.Interaction
):

    view = discord.ui.View()

    button = discord.ui.Button(
        label="NOVA 인증 사이트",
        style=discord.ButtonStyle.link,
        url=WEBSITE_URL
    )

    view.add_item(button)

    await interaction.response.send_message(
        "🌐 **NOVA 인증 사이트**",
        view=view,
        ephemeral=True
    )


# =========================================================
# /도움말
# =========================================================

@bot.tree.command(
    name="도움말",
    description="NOVA 봇의 명령어를 확인합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def help_command(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🌌 NOVA Bot",
        description="사용 가능한 명령어입니다.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 /티어인증",
        value="VALORANT 티어 인증을 시작합니다.",
        inline=False
    )

    embed.add_field(
        name="🌐 /사이트",
        value="NOVA 인증 사이트를 확인합니다.",
        inline=False
    )

    embed.add_field(
        name="ℹ️ /노바",
        value="NOVA 봇 정보를 확인합니다.",
        inline=False
    )

    embed.add_field(
        name="❓ /도움말",
        value="명령어 목록을 확인합니다.",
        inline=False
    )

    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )


# =========================================================
# 봇 실행
# =========================================================

bot.run(TOKEN)
```
