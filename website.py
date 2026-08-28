import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NOVA</title>

        <style>
            body {
                margin: 0;
                background: #0b0f19;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }

            .box {
                width: 90%;
                max-width: 500px;
                background: #121827;
                padding: 40px;
                border-radius: 20px;
                text-align: center;
            }

            h1 {
                font-size: 45px;
                letter-spacing: 6px;
            }

            p {
                color: #aaa;
            }

            a {
                display: block;
                margin-top: 25px;
                padding: 15px;
                background: #5865f2;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>NOVA</h1>

            <p>
                VALORANT Community Tier Verification
            </p>

            <a href="/riot-login">
                Riot 계정 인증하기
            </a>
        </div>
    </body>
    </html>
    """


@app.route("/riot-login")
def riot_login():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>NOVA Riot 인증</title>
    </head>

    <body style="
        background:#0b0f19;
        color:white;
        font-family:Arial;
        text-align:center;
        padding-top:100px;
    ">

        <h1>NOVA</h1>

        <h2>Riot 계정 인증</h2>

        <p>
            현재 Riot Production API 심사 중입니다.
        </p>

        <p>
            이 페이지는 RSO 연동 전 테스트 페이지입니다.
        </p>

        <a
            href="/verify"
            style="
                display:inline-block;
                margin-top:20px;
                padding:15px 30px;
                background:#5865f2;
                color:white;
                text-decoration:none;
                border-radius:10px;
            "
        >
            테스트 인증 진행
        </a>

    </body>
    </html>
    """


@app.route("/verify")
def verify():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>NOVA 인증 완료</title>
    </head>

    <body style="
        background:#0b0f19;
        color:white;
        font-family:Arial;
        text-align:center;
        padding-top:100px;
    ">

        <h1>✅ 인증 완료</h1>

        <h2>Bronze 3</h2>

        <p>
            테스트 인증이 완료되었습니다.
        </p>

        <p style="color:#aaa;">
            실제 VALORANT 티어 정보는
            Riot API 승인 후 연결됩니다.
        </p>

    </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
```
