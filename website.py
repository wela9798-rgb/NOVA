import os
import threading

from flask import Flask, render_template_string
import discord
from discord.ext import commands


# =========================================================
# NOVA - VALORANT TIER VERIFICATION PROTOTYPE
# Riot Production API 심사용 프로토타입
# =========================================================


app = Flask(__name__)


# =========================================================
# 기본 홈페이지
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>NOVA | VALORANT Rank Verification</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family:
                Arial,
                Helvetica,
                sans-serif;

            background:
                linear-gradient(
                    135deg,
                    #0b0d12 0%,
                    #111827 50%,
                    #080a0f 100%
                );

            color: #ffffff;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px 70px;
        }

        .top {
            text-align: center;
            margin-bottom: 45px;
        }

        .logo {
            font-size: 48px;
            font-weight: 900;
            letter-spacing: 8px;
            margin-bottom: 8px;
        }

        .subtitle {
            color: #a7adbb;
            font-size: 16px;
        }

        .prototype {
            display: inline-block;
            margin-top: 18px;
            padding: 7px 14px;
            border-radius: 20px;

            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);

            color: #ffcc66;
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .card {
            background: rgba(18, 22, 31, 0.94);

            border: 1px solid
                rgba(255,255,255,0.08);

            border-radius: 20px;

            padding: 32px;

            box-shadow:
                0 20px 60px
                rgba(0,0,0,0.35);

            margin-bottom: 25px;
        }

        .card h1 {
            margin-top: 0;
            font-size: 28px;
        }

        .card h2 {
            font-size: 20px;
            margin-top: 0;
        }

        .card p {
            color: #b8bfcc;
            line-height: 1.7;
        }

        .button {
            display: inline-block;

            margin-top: 20px;

            padding: 15px 25px;

            border-radius: 10px;

            background: #ffffff;
            color: #111111;

            text-decoration: none;

            font-weight: 800;

            transition:
                transform 0.15s,
                opacity 0.15s;
        }

        .button:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }

        .steps {
            display: grid;

            grid-template-columns:
                repeat(5, 1fr);

            gap: 12px;

            margin-top: 25px;
        }

        .step {
            padding: 20px 12px;

            border-radius: 14px;

            background:
                rgba(255,255,255,0.04);

            border:
                1px solid
                rgba(255,255,255,0.07);

            text-align: center;
        }

        .number {
            width: 35px;
            height: 35px;

            margin:
                0 auto 12px;

            border-radius: 50%;

            display: flex;

            align-items: center;
            justify-content: center;

            background: #ffffff;
            color: #111111;

            font-weight: 900;
        }

        .step-title {
            font-size: 13px;
            font-weight: bold;
        }

        .step-description {
            margin-top: 7px;

            color: #8f98a8;

            font-size: 11px;

            line-height: 1.5;
        }

        .verification {
            margin-top: 25px;

            padding: 22px;

            border-radius: 15px;

            background:
                rgba(255,255,255,0.035);

            border:
                1px solid
                rgba(255,255,255,0.08);
        }

        .verification-title {
            font-weight: 800;
            margin-bottom: 10px;
        }

        .status {
            display: inline-block;

            padding: 7px 12px;

            border-radius: 20px;

            background:
                rgba(255,255,255,0.08);

            color: #d7dce5;

            font-size: 12px;

            font-weight: bold;
        }

        .demo {
            margin-top: 18px;

            padding: 18px;

            border-radius: 12px;

            background:
                rgba(255, 204, 102, 0.06);

            border:
                1px solid
                rgba(255, 204, 102, 0.18);
        }

        .demo strong {
            color: #ffcc66;
        }

        .rank {
            margin-top: 15px;

            font-size: 28px;

            font-weight: 900;
        }

        .small {
            font-size: 12px;
            color: #7f8795;
        }

        .footer {
            text-align: center;

            margin-top: 45px;

            color: #737b89;

            font-size: 12px;

            line-height: 1.7;
        }

        .links {
            margin-top: 15px;
        }

        .links a {
            color: #bfc6d3;
            text-decoration: none;
            margin: 0 8px;
        }

        .links a:hover {
            text-decoration: underline;
        }


        @media (max-width: 800px) {

            .steps {
                grid-template-columns:
                    repeat(2, 1fr);
            }

        }


        @media (max-width: 500px) {

            .container {
                padding:
                    25px 15px 50px;
            }

            .logo {
                font-size: 36px;
            }

            .card {
                padding: 22px;
            }

            .steps {
                grid-template-columns:
                    1fr;
            }

        }

    </style>
</head>


<body>

<div class="container">

    <div class="top">

        <div class="logo">
            NOVA
        </div>

        <div class="subtitle">
            VALORANT Community Rank Verification
        </div>

        <div class="prototype">
            PRODUCTION APPLICATION PROTOTYPE
        </div>

    </div>


    <!-- =====================================================
         INTRODUCTION
         ===================================================== -->

    <div class="card">

        <h1>
            VALORANT Rank Verification
        </h1>

        <p>
            NOVA provides a community rank verification
            system for VALORANT players.
        </p>

        <p>
            Members can link their Riot Account through
            Riot Sign On (RSO), verify their VALORANT
            competitive rank, and use the verified result
            within the NOVA Discord community.
        </p>

        <a
            class="button"
            href="/verify"
        >
            Start Rank Verification
        </a>

    </div>


    <!-- =====================================================
         USER FLOW
         ===================================================== -->

    <div class="card">

        <h2>
            Verification Flow
        </h2>

        <p>
            The following flow demonstrates how a NOVA
            member will verify their VALORANT rank.
        </p>


        <div class="steps">


            <div class="step">

                <div class="number">
                    1
                </div>

                <div class="step-title">
                    Start
                </div>

                <div class="step-description">
                    Begin the NOVA rank verification process.
                </div>

            </div>


            <div class="step">

                <div class="number">
                    2
                </div>

                <div class="step-title">
                    Riot Sign On
                </div>

                <div class="step-description">
                    User opts in and securely links their Riot Account.
                </div>

            </div>


            <div class="step">

                <div class="number">
                    3
                </div>

                <div class="step-title">
                    Account
                </div>

                <div class="step-description">
                    The authenticated Riot account is identified.
                </div>

            </div>


            <div class="step">

                <div class="number">
                    4
                </div>

                <div class="step-title">
                    Rank
                </div>

                <div class="step-description">
                    VALORANT competitive rank is retrieved.
                </div>

            </div>


            <div class="step">

                <div class="number">
                    5
                </div>

                <div class="step-title">
                    Discord
                </div>

                <div class="step-description">
                    Verified rank can be associated with a Discord role.
                </div>

            </div>


        </div>

    </div>


    <!-- =====================================================
         DEMO RESULT
         ===================================================== -->

    <div class="card">

        <h2>
            Verification Result
        </h2>

        <div class="verification">

            <div class="verification-title">
                Riot Account
            </div>

            <span class="status">
                DEMO ACCOUNT
            </span>

            <div class="rank">
                Gold 2
            </div>

            <p class="small">
                Example verification result for the prototype.
            </p>

        </div>


        <div class="demo">

            <strong>
                Prototype Notice
            </strong>

            <p>
                This page currently uses demonstration data.
                Live Riot Account authentication and player
                data will only be enabled after the NOVA
                application receives the required Riot
                production approval and RSO access.
            </p>

        </div>

    </div>


    <!-- =====================================================
         RSO EXPLANATION
         ===================================================== -->

    <div class="card">

        <h2>
            Riot Account Privacy & Opt-in
        </h2>

        <p>
            NOVA will require users to explicitly opt in
            to Riot Account data sharing through Riot Sign On.
        </p>

        <p>
            NOVA will not ask users for their Riot Account
            password. Authentication will be handled through
            Riot's official authentication flow.
        </p>

        <p>
            Users who do not authorize account linking will
            not have their Riot player information displayed
            through this verification system.
        </p>

    </div>


    <!-- =====================================================
         PRIVACY
         ===================================================== -->

    <div class="card">

        <h2>
            Data Usage
        </h2>

        <p>
            The purpose of the verification system is to
            confirm a member's VALORANT competitive rank
            for use within the NOVA community.
        </p>

        <p>
            The system is not intended to provide gameplay
            advantages, scouting functionality, or an
            alternative ranking system.
        </p>

        <p>
            NOVA does not calculate MMR or ELO and does not
            attempt to replace VALORANT's official ranking
            system.
        </p>

    </div>


    <!-- =====================================================
         FOOTER
         ===================================================== -->

    <div class="footer">

        <div>
            NOVA is an independent community project.
        </div>

        <div>
            This project is not endorsed by or affiliated
            with Riot Games.
        </div>

        <div class="links">

            <a href="/privacy">
                Privacy
            </a>

            <a href="/terms">
                Terms
            </a>

            <a href="/about">
                About NOVA
            </a>

        </div>

    </div>

</div>

</body>
</html>
"""


# =========================================================
# 인증 페이지
# =========================================================

VERIFY_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA | Verify Rank</title>

<style>

body {
    margin: 0;
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #0b0d12;

    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;
}

.box {
    width: 90%;
    max-width: 600px;

    padding: 40px;

    border-radius: 20px;

    background: #12161f;

    border: 1px solid
        rgba(255,255,255,0.08);

    text-align: center;
}

h1 {
    margin-top: 0;
}

p {
    color: #aeb6c4;
    line-height: 1.7;
}

.demo-button {
    display: inline-block;

    margin-top: 20px;

    padding: 14px 22px;

    border-radius: 10px;

    background: white;
    color: #111;

    font-weight: bold;
}

.notice {
    margin-top: 25px;

    padding: 18px;

    border-radius: 12px;

    background:
        rgba(255,204,102,0.06);

    border:
        1px solid
        rgba(255,204,102,0.18);

    text-align: left;
}

.notice strong {
    color: #ffcc66;
}

a {
    color: #cbd1dc;
    text-decoration: none;
}

</style>

</head>


<body>

<div class="box">

    <h1>
        Connect Riot Account
    </h1>

    <p>
        To verify your VALORANT rank, NOVA will
        use Riot Sign On (RSO) to allow you to
        securely authorize access to your Riot
        Account information.
    </p>


    <div class="notice">

        <strong>
            Prototype Mode
        </strong>

        <p>
            RSO access is not enabled in this prototype.
            The button below represents the planned
            Riot Sign On step for the final application.
        </p>

    </div>


    <div class="demo-button">
        Continue with Riot Sign On
    </div>


    <p style="margin-top:30px;">

        <a href="/">
            ← Back to NOVA
        </a>

    </p>

</div>

</body>

</html>
"""


# =========================================================
# Privacy Policy
# =========================================================

PRIVACY_HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA | Privacy</title>

<style>

body {
    background: #0b0d12;
    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    margin: 0;
}

.container {
    max-width: 850px;

    margin: auto;

    padding: 50px 20px;
}

.card {
    background: #12161f;

    border-radius: 18px;

    padding: 35px;
}

p {
    color: #adb5c3;

    line-height: 1.8;
}

a {
    color: white;
}

</style>

</head>


<body>

<div class="container">

<div class="card">

<h1>
NOVA Privacy Policy
</h1>

<p>
NOVA is a community project for VALORANT players.
</p>

<p>
The planned rank verification system will use Riot
Sign On (RSO) so that users can explicitly authorize
Riot Account data sharing.
</p>

<p>
NOVA will only use authorized information for the
purpose of verifying a member's VALORANT competitive
rank within the NOVA community.
</p>

<p>
NOVA will not request or store Riot Account passwords.
</p>

<p>
Users may choose not to link their Riot Account.
</p>

<p>
This prototype does not currently perform live Riot
Account authentication.
</p>

<p>
<a href="/">
← Back to NOVA
</a>
</p>

</div>

</div>

</body>

</html>
"""


# =========================================================
# Terms
# =========================================================

TERMS_HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA | Terms</title>

<style>

body {
    background: #0b0d12;
    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    margin: 0;
}

.container {
    max-width: 850px;

    margin: auto;

    padding: 50px 20px;
}

.card {
    background: #12161f;

    border-radius: 18px;

    padding: 35px;
}

p {
    color: #adb5c3;

    line-height: 1.8;
}

a {
    color: white;
}

</style>

</head>


<body>

<div class="container">

<div class="card">

<h1>
NOVA Terms
</h1>

<p>
NOVA is an independent community project and is not
endorsed by Riot Games.
</p>

<p>
The planned verification service is intended only
to help members verify their VALORANT competitive
rank within the NOVA community.
</p>

<p>
NOVA does not provide gameplay advantages,
scouting tools, MMR calculations, or ELO calculations.
</p>

<p>
The current website is a prototype and does not
perform live Riot Account authentication.
</p>

<p>
<a href="/">
← Back to NOVA
</a>
</p>

</div>

</div>

</body>

</html>
"""


# =========================================================
# About
# =========================================================

ABOUT_HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA | About</title>

<style>

body {
    background: #0b0d12;
    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    margin: 0;
}

.container {
    max-width: 850px;

    margin: auto;

    padding: 50px 20px;
}

.card {
    background: #12161f;

    border-radius: 18px;

    padding: 35px;
}

p {
    color: #adb5c3;

    line-height: 1.8;
}

a {
    color: white;
}

</style>

</head>


<body>

<div class="container">

<div class="card">

<h1>
About NOVA
</h1>

<p>
NOVA is a VALORANT-focused Discord community.
</p>

<p>
The project aims to provide community tools that
help members connect with other players and maintain
a trustworthy environment.
</p>

<p>
One planned feature is Riot Account-based VALORANT
rank verification using Riot's official authentication
and API systems.
</p>

<p>
This website is currently a prototype demonstrating
the planned user experience.
</p>

<p>
<a href="/">
← Back to NOVA
</a>
</p>

</div>

</div>

</body>

</html>
"""


# =========================================================
# Flask Routes
# =========================================================

@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/verify")
def verify():
    return render_template_string(VERIFY_HTML)


@app.route("/privacy")
def privacy():
    return render_template_string(PRIVACY_HTML)


@app.route("/terms")
def terms():
    return render_template_string(TERMS_HTML)


@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML)


# =========================================================
# Flask 실행
# =========================================================

def run_web():

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


# =========================================================
# Discord Bot 설정
# =========================================================

intents = discord.Intents.default()

intents.message_content = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================================================
# Discord Bot 준비 완료
# =========================================================

@bot.event
async def on_ready():

    print(
        "=========================================="
    )

    print(
        "✅ NOVA 봇 온라인!"
    )

    print(
        f"🤖 봇 이름 : {bot.user}"
    )

    print(
        f"🆔 봇 ID   : {bot.user.id}"
    )

    print(
        f"🏠 서버 수 : {len(bot.guilds)}"
    )

    print(
        "=========================================="
    )


    await bot.change_presence(

        status=discord.Status.online,

        activity=discord.Game(
            name="NOVA | Valorant"
        )

    )


# =========================================================
# Ping 명령어
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
# NOVA 인증 안내 명령어
# =========================================================

@bot.command()
async def tier(ctx):

    await ctx.send(
        "🏆 **NOVA VALORANT 티어 인증**\n\n"
        "현재 Riot API 심사용 프로토타입이 준비되어 있습니다.\n"
        "웹사이트에서 인증 흐름을 확인할 수 있습니다.\n\n"
        "🌐 https://nova-fo0d.onrender.com/verify"
    )


# =========================================================
# Discord Bot 실행
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

        bot.run(
            token
        )

    except Exception as e:

        print(
            f"❌ 봇 실행 중 오류 발생: {e}"
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


    run_bot()
