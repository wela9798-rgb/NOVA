import os
import threading

import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask


# =========================================================
# 설정
# =========================================================

SERVER_ID = 1541335745753653248
TOKEN = os.getenv("DISCORD_TOKEN")


# =========================================================
# Flask 홈페이지
# =========================================================

app = Flask(__name__)


STYLE = """
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background:
        radial-gradient(
            circle at 50% 0%,
            #292f70 0%,
            #0b0d14 45%,
            #07080c 100%
        );

    color: white;
    font-family: Arial, "Noto Sans KR", sans-serif;
    min-height: 100vh;
}

a {
    text-decoration: none;
}

.navbar {
    width: 100%;
    padding: 25px 7%;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    color: white;
    font-size: 25px;
    font-weight: 900;
}

.logo span {
    color: #7c83ff;
}

.nav-menu {
    display: flex;
    gap: 28px;
}

.nav-menu a {
    color: #aeb4c7;
    font-size: 14px;
}

.nav-menu a:hover {
    color: white;
}

.container {
    max-width: 1100px;
    margin: auto;
    padding: 60px 25px;
}

.header {
    text-align: center;
    margin-bottom: 45px;
}

.header-icon {
    font-size: 55px;
    margin-bottom: 15px;
}

.header h1 {
    font-size: 45px;
    margin-bottom: 12px;
}

.header p {
    color: #9299ad;
    line-height: 1.7;
}

.button {
    display: inline-block;
    padding: 13px 22px;
    border-radius: 11px;
    font-weight: bold;
}

.primary {
    background: #6366f1;
    color: white;
}

.primary:hover {
    background: #7477ff;
}

.secondary {
    background: rgba(255,255,255,0.05);
    color: #d8dbea;
    border: 1px solid #303548;
}

.profile {
    max-width: 850px;
    margin: auto;

    display: flex;
    align-items: center;
    gap: 20px;

    padding: 30px;

    background: rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;

    margin-bottom: 20px;
}

.avatar {
    width: 70px;
    height: 70px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #9b7cff
        );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 32px;
}

.profile h2 {
    margin-bottom: 6px;
}

.profile p {
    color: #7f879c;
    font-size: 14px;
}

.rank-card {
    max-width: 850px;
    margin: auto;

    padding: 30px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(99,102,241,0.18),
            rgba(20,23,35,0.95)
        );

    border: 1px solid #303653;

    margin-bottom: 20px;
}

.rank-title {
    color: #9299ad;
    font-size: 14px;
    margin-bottom: 10px;
}

.rank-name {
    font-size: 32px;
    font-weight: bold;
}

.rank-sub {
    color: #7f879c;
    margin-top: 7px;
}

.stats {
    max-width: 850px;
    margin: auto;

    display: grid;
    grid-template-columns: repeat(4, 1fr);

    gap: 15px;

    margin-bottom: 20px;
}

.stat {
    padding: 25px;

    text-align: center;

    border-radius: 18px;

    background: rgba(20,23,35,0.85);

    border: 1px solid #252b3d;
}

.stat-icon {
    font-size: 27px;
    margin-bottom: 12px;
}

.stat-title {
    color: #858ca0;
    font-size: 13px;
    margin-bottom: 8px;
}

.stat-value {
    font-size: 22px;
    font-weight: bold;
}

.matches {
    max-width: 850px;
    margin: auto;

    background: rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;

    padding: 30px;
}

.matches h2 {
    margin-bottom: 20px;
}

.match {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px;

    background: rgba(255,255,255,0.03);

    border-radius: 14px;

    margin-bottom: 10px;
}

.match:last-child {
    margin-bottom: 0;
}

.match-left {
    display: flex;
    align-items: center;
    gap: 15px;
}

.result-win {
    color: #70e09b;
    font-weight: bold;
}

.result-lose {
    color: #ff7272;
    font-weight: bold;
}

.match-map {
    color: #dce0ec;
}

.match-info {
    color: #747c91;
    font-size: 13px;
}

.connect-box {
    max-width: 850px;
    margin: 20px auto 0;

    padding: 25px;

    text-align: center;

    background: rgba(99,102,241,0.08);

    border: 1px solid rgba(124,131,255,0.2);

    border-radius: 18px;
}

.connect-box p {
    color: #9299ad;
    line-height: 1.7;
    margin-bottom: 18px;
}

.page-box {
    max-width: 850px;
    margin: auto;

    padding: 35px;

    background: rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;

    line-height: 1.8;
}

.page-box h1 {
    margin-bottom: 20px;
}

.page-box h2 {
    margin-top: 20px;
    margin-bottom: 8px;
}

.page-box p {
    color: #aeb4c7;
}

.login-card {
    max-width: 650px;
    margin: 50px auto;

    padding: 40px;

    text-align: center;

    background: rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;
}

.login-card p {
    color: #9299ad;
    line-height: 1.8;
}

.notice {
    margin-top: 25px;

    padding: 20px;

    border-radius: 15px;

    background: rgba(99,102,241,0.08);

    border: 1px solid rgba(124,131,255,0.2);

    color: #b7bdd0;

    line-height: 1.7;
}

footer {
    margin-top: 80px;

    border-top: 1px solid #1e2230;

    text-align: center;

    padding: 35px;

    color: #62697b;

    font-size: 13px;
}

footer a {
    color: #858ca0;
    margin: 0 8px;
}

@media(max-width: 750px) {

    .nav-menu {
        display: none;
    }

    .stats {
        grid-template-columns: 1fr 1fr;
    }

    .match {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }

    .header h1 {
        font-size: 35px;
    }

}

</style>
"""


NAV = """
<nav class="navbar">

    <a class="logo" href="/">
        N<span>O</span>VA
    </a>

    <div class="nav-menu">

        <a href="/">
            홈
        </a>

        <a href="/valorant">
            VALORANT
        </a>

        <a href="/terms">
            이용약관
        </a>

        <a href="/privacy">
            개인정보
        </a>

    </div>

</nav>
"""


FOOTER = """
<footer>

    <strong>NOVA</strong>

    <br><br>

    함께 만들어가는 서버 🤖

    <br><br>

    <a href="/terms">
        이용약관
    </a>

    |

    <a href="/privacy">
        개인정보
    </a>

</footer>
"""


# =========================================================
# 홈페이지
# =========================================================

@app.route("/")
def home():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA</title>

{STYLE}

</head>

<body>

{NAV}

<section class="container">

    <div class="header">

        <div class="header-icon">
            🤖
        </div>

        <h1>
            Meet <span style="color:#7c83ff;">NOVA</span>
        </h1>

        <p>
            Discord와 VALORANT를 위한
            NOVA의 다양한 기능을 만나보세요.
        </p>

        <br>

        <a
            class="button primary"
            href="/valorant"
        >
            🎮 VALORANT 전적 보기
        </a>

    </div>

</section>

{FOOTER}

</body>

</html>
"""


# =========================================================
# VALORANT
# =========================================================

@app.route("/valorant")
def valorant():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • VALORANT</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="header">

        <div class="header-icon">
            🎮
        </div>

        <h1>
            VALORANT 전적
        </h1>

        <p>
            NOVA 전적 시스템
        </p>

    </div>

    <div class="profile">

        <div class="avatar">
            🎮
        </div>

        <div>

            <h2>
                NOVA 사용자
            </h2>

            <p>
                Riot 계정 연결 후 전적을 확인할 수 있습니다.
            </p>

        </div>

    </div>

    <div class="rank-card">

        <div class="rank-title">
            🏆 현재 티어
        </div>

        <div class="rank-name">
            준비 중
        </div>

        <div class="rank-sub">
            Riot 계정 연결 후 표시됩니다.
        </div>

    </div>

    <div class="stats">

        <div class="stat">

            <div class="stat-icon">
                📊
            </div>

            <div class="stat-title">
                승률
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>

        <div class="stat">

            <div class="stat-icon">
                ⚔️
            </div>

            <div class="stat-title">
                K/D
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>

        <div class="stat">

            <div class="stat-icon">
                🏆
            </div>

            <div class="stat-title">
                승리
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>

        <div class="stat">

            <div class="stat-icon">
                🎮
            </div>

            <div class="stat-title">
                경기
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>

    </div>

    <div class="matches">

        <h2>
            ⚔️ 최근 경기
        </h2>

        <div class="match">

            <div class="match-left">

                <span class="result-win">
                    WIN
                </span>

                <span class="match-map">
                    최근 경기
                </span>

            </div>

            <span class="match-info">
                준비 중
            </span>

        </div>

        <div class="match">

            <div class="match-left">

                <span class="result-lose">
                    LOSS
                </span>

                <span class="match-map">
                    최근 경기
                </span>

            </div>

            <span class="match-info">
                준비 중
            </span>

        </div>

    </div>

    <div class="connect-box">

        <p>
            자신의 VALORANT 데이터를 확인하려면
            공식 Riot 계정 인증과 데이터 공유 동의가 필요합니다.
        </p>

        <a
            class="button primary"
            href="/connect"
        >
            🔗 Riot 계정 연결
        </a>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================================================
# Riot 연결 안내
# =========================================================

@app.route("/connect")
def connect():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • Riot 연결</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="login-card">

        <div class="header-icon">
            🔗
        </div>

        <h1>
            Riot 계정 연결
        </h1>

        <br>

        <p>
            실제 서비스에서는 Riot의 공식 로그인 절차를 통해
            사용자가 직접 계정을 연결하게 됩니다.
        </p>

        <br>

        <p>
            현재는 NOVA의 계정 연결 흐름을 확인하기 위한
            테스트 화면입니다.
        </p>

        <br><br>

        <a
            class="button primary"
            href="/connected"
        >
            연결 계속하기
        </a>

        <br><br>

        <a
            class="button secondary"
            href="/valorant"
        >
            돌아가기
        </a>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================================================
# 연결 완료 테스트
# =========================================================

@app.route("/connected")
def connected():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 연결 완료</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="login-card">

        <div class="header-icon">
            ✅
        </div>

        <h1>
            연결 테스트 완료
        </h1>

        <br>

        <p>
            NOVA의 계정 연결 흐름이
            정상적으로 작동했습니다.
        </p>

        <div class="notice">

            현재는 테스트 환경입니다.

            <br><br>

            실제 Riot 인증은
            RSO 승인을 받은 이후 연결합니다.

        </div>

        <br><br>

        <a
            class="button primary"
            href="/valorant"
        >
            🎮 전적 페이지로 돌아가기
        </a>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================================================
# 이용약관
# =========================================================

@app.route("/terms")
def terms():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 이용약관</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="page-box">

        <h1>
            📜 이용약관
        </h1>

        <h2>
            제1조 목적
        </h2>

        <p>
            본 페이지는 NOVA 서비스의
            이용약관 안내를 위한 페이지입니다.
        </p>

        <h2>
            제2조 서비스
        </h2>

        <p>
            NOVA는 Discord 서버 관리 및
            VALORANT 관련 정보 제공 기능을
            개발하고 있습니다.
        </p>

        <h2>
            제3조 이용자
        </h2>

        <p>
            이용자는 관련 법령 및 각 서비스의
            이용정책을 준수하여야 합니다.
        </p>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================================================
# 개인정보
# =========================================================

@app.route("/privacy")
def privacy():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 개인정보</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="page-box">

        <h1>
            🔐 개인정보처리방침
        </h1>

        <h2>
            1. 개인정보 수집
        </h2>

        <p>
            실제 서비스에서 수집하는 정보와
            처리 방식은 서비스 출시 전에
            정확하게 명시할 예정입니다.
        </p>

        <h2>
            2. 이용 목적
        </h2>

        <p>
            서비스 제공 및 계정 연결,
            게임 관련 기능 제공을 위해
            필요한 범위에서 정보를 처리합니다.
        </p>

        <h2>
            3. 정보 보호
        </h2>

        <p>
            이용자의 정보가 안전하게 처리될 수 있도록
            적절한 보안 조치를 적용할 예정입니다.
        </p>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================================================
# Discord NOVA 봇
# =========================================================

intents = discord.Intents.default()


class NOVA(commands.Bot):

    def __init__(self):

        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):

        server = discord.Object(id=SERVER_ID)

        self.tree.copy_global_to(guild=server)

        await self.tree.sync(guild=server)

        print("✅ 서버 전용 명령어 동기화 완료!")


bot = NOVA()


# =========================================================
# 메인 메뉴 버튼
# =========================================================

class MainMenu(discord.ui.View):

    @discord.ui.button(
        label="서버 안내",
        emoji="📚",
        style=discord.ButtonStyle.primary
    )
    async def server_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="📚 NOVA 서버 안내",
            description=(
                "NOVA에 오신 것을 환영합니다! 🤖\n\n"
                "게임과 친목을 함께 즐길 수 있는 서버입니다.\n"
                "아래 내용을 확인하고 서버를 이용해주세요."
            ),
            color=0x5865F2
        )

        embed.add_field(
            name="🔞 이용 연령",
            value=(
                "• **만 14세 이상** 이용 가능합니다.\n"
                "• 연령 기준에 맞지 않는 경우 이용이 제한될 수 있습니다."
            ),
            inline=False
        )

        embed.add_field(
            name="📌 서버 이용",
            value=(
                "• 서로 존중하며 대화해주세요.\n"
                "• 욕설 및 과도한 분쟁은 자제해주세요.\n"
                "• 다른 이용자에게 불쾌감을 주는 행동은 금지됩니다.\n"
                "• 서버 규칙을 꼭 확인해주세요."
            ),
            inline=False
        )

        embed.add_field(
            name="🎮 주요 게임",
            value=(
                "• VALORANT\n"
                "• Minecraft\n"
                "• 기타 종합게임"
            ),
            inline=True
        )

        embed.add_field(
            name="🆘 문의",
            value=(
                "서버 이용 중 문제가 발생했다면\n"
                "운영진에게 문의해주세요."
            ),
            inline=True
        )

        embed.set_footer(
            text="NOVA • 함께 만들어가는 서버 🤖"
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

    @discord.ui.button(
        label="유저 정보",
        emoji="👤",
        style=discord.ButtonStyle.secondary
    )
    async def user_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        user = interaction.user

        await interaction.response.send_message(
            f"👤 **유저 정보**\n\n"
            f"닉네임: {user.display_name}\n"
            f"아이디: {user.id}",
            ephemeral=True
        )

    @discord.ui.button(
        label="게임 기능",
        emoji="🎮",
        style=discord.ButtonStyle.success
    )
    async def game_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_message(
            "🎮 **게임 기능**\n\n"
            "VALORANT 관련 기능을 준비하고 있어요!",
            ephemeral=True
        )

    @discord.ui.button(
        label="서버 설정",
        emoji="⚙️",
        style=discord.ButtonStyle.danger
    )
    async def server_settings(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:

            await interaction.response.send_message(
                "❌ 관리자만 사용할 수 있는 기능입니다.",
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            "⚙️ **서버 설정**\n\n"
            "관리자 전용 기능을 준비하고 있어요!",
            ephemeral=True
        )


# =========================================================
# /메뉴
# =========================================================

@bot.tree.command(
    name="메뉴",
    description="NOVA 메인 메뉴를 엽니다."
)
async def menu(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🤖 NOVA",
        description=(
            "안녕하세요! **NOVA**입니다.\n\n"
            "아래 메뉴에서 원하는 기능을 선택해주세요."
        ),
        color=0x5865F2
    )

    embed.add_field(
        name="📚 서버 안내",
        value="서버 이용 방법을 확인해요.",
        inline=True
    )

    embed.add_field(
        name="👤 유저 정보",
        value="내 디스코드 정보를 확인해요.",
        inline=True
    )

    embed.add_field(
        name="🎮 게임 기능",
        value="VALORANT 관련 기능을 이용해요.",
        inline=True
    )

    embed.add_field(
        name="⚙️ 서버 설정",
        value="서버 관리 기능이에요.",
        inline=True
    )

    embed.set_footer(
        text="NOVA • 함께 만들어가는 서버"
    )

    await interaction.response.send_message(
        embed=embed,
        view=MainMenu()
    )


# =========================================================
# /공지
# =========================================================

@bot.tree.command(
    name="공지",
    description="사진과 함께 예쁜 공지를 작성합니다."
)
@app_commands.describe(
    제목="공지 제목을 입력해주세요.",
    내용="공지 내용을 입력해주세요.",
    사진="공지에 넣을 사진을 첨부해주세요."
)
@app_commands.default_permissions(
    administrator=True
)
async def notice(
    interaction: discord.Interaction,
    제목: str,
    내용: str,
    사진: discord.Attachment = None
):

    embed = discord.Embed(
        title="📢 NOVA 서버 공지",
        description=f"## ✨ {제목}\n\n{내용}",
        color=0x5865F2,
        timestamp=discord.utils.utcnow()
    )

    if 사진:

        embed.set_image(
            url=사진.url
        )

    embed.set_author(
        name=interaction.user.display_name,
        icon_url=interaction.user.display_avatar.url
    )

    embed.add_field(
        name="📌 NOVA 안내",
        value="서버 이용에 참고해주세요!",
        inline=False
    )

    embed.add_field(
        name="👤 작성자",
        value=interaction.user.mention,
        inline=True
    )

    embed.add_field(
        name="📅 작성일",
        value=f"<t:{int(discord.utils.utcnow().timestamp())}:D>",
        inline=True
    )

    embed.set_footer(
        text="NOVA • 함께 만들어가는 서버 🤖"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /전적
# =========================================================

@bot.tree.command(
    name="전적",
    description="VALORANT 전적을 조회합니다."
)
@app_commands.describe(
    닉네임="VALORANT 닉네임을 입력해주세요.",
    태그="VALORANT 태그를 입력해주세요."
)
async def valorant_stats(
    interaction: discord.Interaction,
    닉네임: str,
    태그: str
):

    embed = discord.Embed(
        title="🎮 VALORANT 전적",
        description=(
            f"**{닉네임}#{태그}**\n\n"
            "⏳ 현재 전적 조회 시스템을 준비하고 있습니다."
        ),
        color=0x5865F2
    )

    embed.add_field(
        name="🏆 현재 티어",
        value="준비 중",
        inline=True
    )

    embed.add_field(
        name="📊 승률",
        value="준비 중",
        inline=True
    )

    embed.add_field(
        name="⚔️ 최근 경기",
        value="준비 중",
        inline=True
    )

    embed.set_footer(
        text="NOVA • VALORANT"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# Discord 봇 실행
# =========================================================

def run_bot():

    if not TOKEN:

        print("❌ DISCORD_TOKEN이 설정되지 않았습니다.")

        return

    try:

        bot.run(TOKEN)

    except Exception as e:

        print(f"❌ Discord 봇 실행 오류: {e}")


# =========================================================
# Render 시작
# =========================================================

if __name__ == "__main__":

    bot_thread = threading.Thread(
        target=run_bot,
        daemon=True
    )

    bot_thread.start()

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
