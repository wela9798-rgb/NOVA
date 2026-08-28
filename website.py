import os
import threading

from flask import Flask, render_template_string
import discord
from discord.ext import commands

# =========================================================

# NOVA - VALORANT TIER VERIFICATION PROTOTYPE

# Riot Games API 심사용 프로토타입

# =========================================================

app = Flask(**name**)

# =========================================================

# NOVA 홈페이지

# =========================================================

HTML = """

<!DOCTYPE html>

<html lang="ko">

<head>

```
<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>NOVA | VALORANT 티어 인증</title>

<style>

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            "Noto Sans KR",
            sans-serif;

        background:
            radial-gradient(
                circle at top,
                #191927 0%,
                #0b0b12 55%,
                #07070c 100%
            );

        color: #ffffff;
        min-height: 100vh;
    }

    .container {
        width: 90%;
        max-width: 1100px;
        margin: 0 auto;
    }

    header {
        height: 80px;

        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .logo {
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 4px;
    }

    .status {
        display: flex;
        align-items: center;
        gap: 8px;

        color: #a9a9b8;
        font-size: 13px;
    }

    .status-dot {
        width: 8px;
        height: 8px;

        border-radius: 50%;

        background: #45d483;
        box-shadow: 0 0 12px #45d483;
    }

    .hero {
        text-align: center;

        padding: 100px 20px 80px;
    }

    .badge {
        display: inline-block;

        padding: 8px 16px;
        margin-bottom: 25px;

        border: 1px solid #30303f;
        border-radius: 999px;

        background: rgba(255,255,255,0.04);

        color: #b8b8c8;

        font-size: 12px;
        letter-spacing: 1px;
    }

    h1 {
        font-size: clamp(42px, 7vw, 78px);

        font-weight: 900;
        line-height: 1.08;

        margin-bottom: 28px;
    }

    .red {
        color: #ff4655;
    }

    .hero-text {
        max-width: 720px;

        margin: 0 auto;

        color: #a7a7b7;

        font-size: 17px;
        line-height: 1.8;
    }

    .cards {
        display: grid;

        grid-template-columns:
            repeat(
                auto-fit,
                minmax(250px, 1fr)
            );

        gap: 20px;

        margin-bottom: 70px;
    }

    .card {
        padding: 30px;

        background:
            rgba(255,255,255,0.035);

        border: 1px solid #292936;
        border-radius: 18px;

        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }

    .card:hover {
        transform: translateY(-4px);

        border-color: #414152;
    }

    .icon {
        font-size: 30px;

        margin-bottom: 18px;
    }

    .card h2 {
        font-size: 20px;

        margin-bottom: 12px;
    }

    .card p {
        color: #9696a7;

        font-size: 14px;
        line-height: 1.8;
    }

    .verification {
        margin-bottom: 30px;

        padding: 35px;

        background:
            linear-gradient(
                135deg,
                rgba(255,70,85,0.08),
                rgba(255,255,255,0.025)
            );

        border:
            1px solid rgba(255,70,85,0.25);

        border-radius: 20px;
    }

    .verification h2 {
        font-size: 22px;

        margin-bottom: 15px;
    }

    .verification p {
        color: #a6a6b5;

        line-height: 1.8;
        font-size: 14px;
    }

    .steps {
        display: grid;

        gap: 12px;

        margin-top: 22px;
    }

    .step {
        display: flex;
        align-items: center;

        gap: 14px;

        padding: 15px;

        background:
            rgba(0,0,0,0.2);

        border-radius: 12px;

        color: #bdbdca;

        font-size: 14px;
    }

    .number {
        width: 28px;
        height: 28px;

        display: flex;
        align-items: center;
        justify-content: center;

        flex-shrink: 0;

        border-radius: 50%;

        background: #ff4655;

        color: #ffffff;

        font-weight: 800;
        font-size: 12px;
    }

    .notice {
        margin-bottom: 70px;

        padding: 30px;

        border: 1px solid #292936;
        border-radius: 18px;

        background:
            rgba(255,255,255,0.025);
    }

    .notice h2 {
        font-size: 20px;

        margin-bottom: 14px;
    }

    .notice p {
        color: #9696a7;

        font-size: 13px;
        line-height: 1.9;
    }

    footer {
        padding: 30px 0;

        border-top:
            1px solid #242430;

        text-align: center;

        color: #666676;

        font-size: 12px;
        line-height: 1.8;
    }

    @media (max-width: 600px) {

        header {
            height: 70px;
        }

        .logo {
            font-size: 23px;
        }

        .hero {
            padding-top: 65px;
        }

        .hero-text {
            font-size: 15px;
        }

        .verification,
        .notice {
            padding: 25px;
        }

    }

</style>
```

</head>

<body>

<div class="container">

```
<header>

    <div class="logo">
        NOVA
    </div>


    <div class="status">

        <span class="status-dot"></span>

        서비스 정상 운영

    </div>

</header>


<section class="hero">


    <div class="badge">
        VALORANT COMMUNITY SERVICE
    </div>


    <h1>

        NOVA와 함께하는<br>

        <span class="red">
            VALORANT 티어 인증
        </span>

    </h1>


    <p class="hero-text">

        NOVA는 VALORANT 플레이어가
        자신의 게임 정보를 확인하고
        Discord 커뮤니티에서 티어를
        인증할 수 있도록 지원하기 위해
        개발 중인 커뮤니티 서비스입니다.

    </p>


</section>


<section class="cards">


    <div class="card">


        <div class="icon">
            🏆
        </div>


        <h2>
            티어 인증
        </h2>


        <p>

            플레이어의 VALORANT 경쟁전 정보를
            확인하고 Discord 서버에서 본인의
            현재 티어를 인증할 수 있도록
            지원합니다.

        </p>


    </div>


    <div class="card">


        <div class="icon">
            🎮
        </div>


        <h2>
            VALORANT 연동
        </h2>


        <p>

            Riot Games에서 제공하는 공식 API를
            활용하여 플레이어의 게임 정보를
            조회하는 기능을 구현하는 것을
            목표로 합니다.

        </p>


    </div>


    <div class="card">


        <div class="icon">
            💬
        </div>


        <h2>
            Discord 연동
        </h2>


        <p>

            NOVA Discord 커뮤니티와 연동하여
            인증된 플레이어의 티어 정보를
            커뮤니티에서 편리하게 확인할 수
            있도록 합니다.

        </p>


    </div>


</section>


<section class="verification">


    <h2>
        티어 인증 절차
    </h2>


    <p>

        실제 서비스에서는 Riot Games의
        공식 인증 및 API 이용 절차를 기반으로
        플레이어의 게임 정보를 확인할 예정입니다.

    </p>


    <div class="steps">


        <div class="step">

            <span class="number">
                1
            </span>

            Riot 계정 인증

        </div>


        <div class="step">

            <span class="number">
                2
            </span>

            VALORANT 플레이어 정보 확인

        </div>


        <div class="step">

            <span class="number">
                3
            </span>

            경쟁전 티어 정보 확인

        </div>


        <div class="step">

            <span class="number">
                4
            </span>

            Discord 서버에서 티어 인증

        </div>


    </div>


</section>


<section class="notice">


    <h2>
        Riot Games API 이용 안내
    </h2>


    <p>

        본 웹사이트는 NOVA Discord 커뮤니티에서
        사용할 VALORANT 티어 인증 기능을
        검증하기 위한 프로토타입입니다.

        <br><br>

        현재 단계에서는 Riot Games API의
        실제 Production 이용 승인을 전제로
        기능을 설계하고 있습니다.

        <br><br>

        필요한 권한이 승인된 경우
        Riot Games의 공식 API 정책과
        개발자 약관을 준수하여 서비스를
        운영할 예정입니다.

        <br><br>

        플레이어의 정보는 서비스 기능에
        필요한 범위에서만 사용하며,
        불필요한 개인정보를 수집하거나
        저장하지 않는 것을 원칙으로 합니다.

    </p>


</section>


<footer>

    NOVA VALORANT COMMUNITY

    <br>

    VALORANT 티어 인증 프로토타입

</footer>
```

</div>

</body>

</html>
"""

# =========================================================

# Flask Web Server

# =========================================================

@app.route("/")
def home():

```
return render_template_string(HTML)
```

# =========================================================

# Discord Bot

# =========================================================

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(
command_prefix="!",
intents=intents
)

@bot.event
async def on_ready():

```
print(
    f"NOVA Bot 로그인 완료: {bot.user}"
)
```

# =========================================================

# Flask 실행

# =========================================================

def run_web():

```
port = int(
    os.environ.get(
        "PORT",
        10000
    )
)


app.run(
    host="0.0.0.0",
    port=port
)
```

# =========================================================

# 프로그램 시작

# =========================================================

if **name** == "**main**":

```
web_thread = threading.Thread(
    target=run_web,
    daemon=True
)


web_thread.start()


token = os.environ.get(
    "DISCORD_TOKEN"
)


if not token:

    print(
        "DISCORD_TOKEN 환경변수가 없습니다."
    )

else:

    bot.run(token)
```
