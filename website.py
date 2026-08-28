```python
import os
import threading

from flask import Flask, render_template_string

import discord
from discord.ext import commands


# =========================================================
# NOVA - VALORANT TIER VERIFICATION PROTOTYPE
# Riot Games API 심사용 프로토타입
# =========================================================

app = Flask(__name__)


# =========================================================
# NOVA 웹사이트
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

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
                sans-serif;

            background:
                linear-gradient(
                    135deg,
                    #0b0b12 0%,
                    #11111d 50%,
                    #171725 100%
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
            padding: 30px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 28px;
            font-weight: 800;
            letter-spacing: 3px;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #a8a8b8;
            font-size: 14px;
        }

        .dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #43d17a;
            box-shadow: 0 0 10px #43d17a;
        }

        .hero {
            text-align: center;
            padding: 90px 20px 70px;
        }

        .badge {
            display: inline-block;
            padding: 8px 16px;
            border: 1px solid #333345;
            border-radius: 999px;
            color: #b7b7c9;
            font-size: 13px;
            margin-bottom: 25px;
            background: rgba(255,255,255,0.03);
        }

        h1 {
            font-size: clamp(42px, 7vw, 76px);
            line-height: 1.05;
            margin-bottom: 25px;
            font-weight: 900;
        }

        .highlight {
            color: #ff4655;
        }

        .description {
            max-width: 700px;
            margin: 0 auto;
            color: #aaaabc;
            font-size: 18px;
            line-height: 1.8;
        }

        .cards {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(250px, 1fr));

            gap: 20px;
            margin-bottom: 80px;
        }

        .card {
            background: rgba(255,255,255,0.04);
            border: 1px solid #292939;
            border-radius: 18px;
            padding: 30px;
            transition: 0.2s ease;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: #444458;
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
            color: #9999aa;
            line-height: 1.7;
            font-size: 14px;
        }

        .notice {
            background: rgba(255,70,85,0.06);
            border: 1px solid rgba(255,70,85,0.25);
            border-radius: 18px;
            padding: 30px;
            margin-bottom: 60px;
        }

        .notice h2 {
            margin-bottom: 12px;
        }

        .notice p {
            color: #aaaabc;
            line-height: 1.8;
            font-size: 14px;
        }

        footer {
            border-top: 1px solid #252532;
            padding: 30px 0;
            color: #777789;
            font-size: 13px;
            text-align: center;
        }

        @media (max-width: 600px) {
            header {
                padding: 20px 0;
            }

            .hero {
                padding-top: 60px;
            }

            .description {
                font-size: 15px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <header>
        <div class="logo">NOVA</div>

        <div class="status">
            <span class="dot"></span>
            서비스 정상 운영
        </div>
    </header>


    <section class="hero">

        <div class="badge">
            VALORANT COMMUNITY SERVICE
        </div>

        <h1>
            NOVA와 함께하는<br>
            <span class="highlight">VALORANT 티어 인증</span>
        </h1>

        <p class="description">
            NOVA는 VALORANT 플레이어의 게임 정보를 확인하고
            Discord 커뮤니티에서 보다 편리하게 티어를 인증할 수 있도록
            개발 중인 커뮤니티 서비스입니다.
        </p>

    </section>


    <section class="cards">

        <div class="card">
            <div class="icon">🏆</div>

            <h2>티어 인증</h2>

            <p>
                플레이어의 VALORANT 경쟁전 정보를 확인하여
                Discord 서버에서 본인의 티어를 인증할 수 있도록
                지원하는 기능을 제공합니다.
            </p>
        </div>


        <div class="card">
            <div class="icon">🎮</div>

            <h2>VALORANT 연동</h2>

            <p>
                Riot Games에서 제공하는 공식 API를 활용하여
                플레이어의 게임 정보를 조회하는 것을 목표로 합니다.
            </p>
        </div>


        <div class="card">
            <div class="icon">💬</div>

            <h2>Discord 커뮤니티</h2>

            <p>
                NOVA Discord 서버와 연동하여
                커뮤니티 구성원이 보다 편리하게
                게임 정보를 확인할 수 있도록 지원합니다.
            </p>
        </div>

    </section>


    <section class="notice">

        <h2>서비스 안내</h2>

        <p>
            본 웹사이트는 NOVA Discord 커뮤니티에서 사용할
            VALORANT 티어 인증 기능을 검증하기 위한
            프로토타입입니다.
            <br><br>

            실제 서비스에서는 Riot Games의 공식 개발자 정책과
            VALORANT API 이용 정책을 준수하며,
            필요한 API 권한이 승인된 경우에만 관련 기능을
            제공할 예정입니다.
        </p>

    </section>


    <footer>
        NOVA VALORANT COMMUNITY · Riot Games API 활용 프로토타입
    </footer>

</div>

</body>
</html>
"""


# =========================================================
# Flask
# =========================================================

@app.route("/")
def home():
    return render_template_string(HTML)


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
    print(f"NOVA Bot 로그인 완료: {bot.user}")


# =========================================================
# Flask 서버 실행
# =========================================================

def run_web():
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )


# =========================================================
# 프로그램 시작
# =========================================================

if __name__ == "__main__":

    web_thread = threading.Thread(
        target=run_web,
        daemon=True
    )

    web_thread.start()

    token = os.environ.get("DISCORD_TOKEN")

    if not token:
        print("DISCORD_TOKEN 환경변수가 없습니다.")
    else:
        bot.run(token)
```
