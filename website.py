```python
import os
from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# =========================================================
# NOVA - VALORANT TIER VERIFICATION PROTOTYPE
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA | VALORANT Tier Verification</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b0f19;
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .container {
            width: 90%;
            max-width: 520px;
            background: #121827;
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 15px 50px rgba(0,0,0,.45);
        }

        .logo {
            font-size: 42px;
            font-weight: 800;
            letter-spacing: 5px;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #9ca3af;
            margin-bottom: 35px;
        }

        .button {
            display: block;
            width: 100%;
            padding: 15px;
            border: 0;
            border-radius: 12px;
            background: #5865f2;
            color: white;
            text-decoration: none;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        .button:hover {
            opacity: .9;
        }

        .status {
            margin-top: 25px;
            padding: 15px;
            border-radius: 12px;
            background: #1b2335;
            color: #d1d5db;
        }

        .rank {
            font-size: 30px;
            font-weight: bold;
            margin: 15px 0;
        }

        .small {
            color: #9ca3af;
            font-size: 13px;
            margin-top: 20px;
        }
    </style>
</head>

<body>

<div class="container">

    <div class="logo">NOVA</div>

    <div class="subtitle">
        VALORANT Community Tier Verification
    </div>

    {% if page == "home" %}

        <p>
            Riot 계정을 인증하고<br>
            NOVA 서버에서 VALORANT 티어를 인증해보세요.
        </p>

        <br>

        <a class="button" href="/riot-login">
            Riot 계정 인증하기
        </a>

        <div class="small">
            테스트 프로토타입 · Riot RSO 연동 준비 중
        </div>

    {% elif page == "login" %}

        <h2>Riot 계정 인증</h2>

        <div class="status">
            현재 Riot Production API 심사 중입니다.
            <br><br>
            이 화면은 RSO 연동 전 테스트 화면입니다.
        </div>

        <br>

        <a class="button" href="/verify">
            테스트 인증 진행
        </a>

    {% elif page == "verify" %}

        <h2>인증 완료</h2>

        <div class="status">
            Riot 계정 인증 테스트가 완료되었습니다.
        </div>

        <div class="rank">
            🥉 Bronze 3
        </div>

        <p>
            테스트 플레이어
        </p>

        <div class="small">
            실제 티어 정보는 Riot API 승인 후 표시됩니다.
        </div>

    {% endif %}

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, page="home")


@app.route("/riot-login")
def riot_login():
    return render_template_string(HTML, page="login")


@app.route("/verify")
def verify():
    return render_template_string(HTML, page="verify")


# =========================================================
# Render 실행
# =========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
```
