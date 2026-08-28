from flask import Flask

app = Flask(__name__)


# =========================================================
# NOVA 메인 홈페이지
# =========================================================

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA | VALORANT Community</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background:
                radial-gradient(circle at top, #252b4a 0%, #0f1117 45%);
            color: white;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 100px 20px;
            text-align: center;
        }

        .logo {
            font-size: 72px;
            font-weight: 900;
            letter-spacing: 4px;
        }

        .subtitle {
            color: #aeb3c2;
            font-size: 20px;
            margin-top: 10px;
            margin-bottom: 50px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .button {
            display: inline-block;
            padding: 15px 28px;
            background: #5865F2;
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-weight: bold;
            transition: 0.2s;
        }

        .button:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }

        .button.secondary {
            background: #242733;
        }

        .card {
            margin-top: 60px;
            padding: 35px;
            background: rgba(24, 27, 36, 0.9);
            border: 1px solid #2d3140;
            border-radius: 20px;
        }

        .card h2 {
            margin-top: 0;
        }

        .card p {
            color: #aeb3c2;
            line-height: 1.7;
        }

        .status {
            display: inline-block;
            margin-top: 15px;
            padding: 8px 15px;
            border-radius: 20px;
            background: #17351f;
            color: #72e28b;
            font-size: 14px;
        }

        footer {
            margin-top: 70px;
            color: #666b78;
            font-size: 13px;
        }
    </style>
</head>

<body>

<div class="container">

    <div class="logo">🌌 NOVA</div>

    <div class="subtitle">
        한국 VALORANT 커뮤니티
    </div>

    <div class="buttons">

        <a class="button"
           href="https://discord.gg/gHfjAj96r"
           target="_blank">
            💬 NOVA Discord
        </a>

        <a class="button secondary"
           href="/tier">
            🏆 티어 인증
        </a>

    </div>


    <div class="card">

        <h2>🎮 NOVA Tier Verification</h2>

        <p>
            NOVA는 VALORANT 플레이어의 티어 인증 기능을
            제공하기 위한 시스템을 개발하고 있습니다.
        </p>

        <p>
            현재 페이지는 Riot API Production Key 심사를 위한
            프로토타입으로 운영되고 있습니다.
        </p>

        <span class="status">
            ● Prototype Online
        </span>

    </div>


    <footer>
        NOVA VALORANT Community
    </footer>

</div>

</body>
</html>
"""


# =========================================================
# 티어 인증 페이지
# =========================================================

@app.route("/tier")
def tier():
    return """
<!DOCTYPE html>
<html lang="ko">

<head>

    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>NOVA | 티어 인증</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background:
                radial-gradient(circle at top, #252b4a 0%, #0f1117 50%);
            color: white;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 650px;
            margin: 0 auto;
            padding: 70px 20px;
        }

        .card {
            background: rgba(24, 27, 36, 0.95);
            border: 1px solid #2d3140;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
        }

        .logo {
            font-size: 45px;
            font-weight: 900;
        }

        .description {
            color: #aeb3c2;
            line-height: 1.7;
        }

        .rank-box {
            margin: 35px 0;
            padding: 30px;
            background: #10131b;
            border-radius: 15px;
        }

        .rank-label {
            color: #8f95a5;
            font-size: 14px;
        }

        .rank {
            font-size: 42px;
            font-weight: bold;
            margin-top: 10px;
        }

        .test {
            display: inline-block;
            margin-top: 10px;
            padding: 6px 12px;
            border-radius: 15px;
            background: #30333f;
            color: #aeb3c2;
            font-size: 12px;
        }

        .notice {
            margin-top: 25px;
            padding: 18px;
            background: #1c1f29;
            border-radius: 12px;
            color: #aeb3c2;
            font-size: 14px;
            line-height: 1.6;
        }

        .button {
            display: inline-block;
            margin-top: 30px;
            padding: 14px 26px;
            background: #5865F2;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
        }

        .button:hover {
            opacity: 0.85;
        }

    </style>

</head>

<body>

<div class="container">

    <div class="card">

        <div class="logo">
            🌌 NOVA
        </div>

        <h2>
            VALORANT 티어 인증
        </h2>

        <p class="description">
            NOVA Discord에서 사용할 수 있는
            VALORANT 티어 인증 시스템입니다.
        </p>


        <div class="rank-box">

            <div class="rank-label">
                현재 인증 티어
            </div>

            <div class="rank">
                🥉 Bronze 3
            </div>

            <span class="test">
                TEST DATA
            </span>

        </div>


        <div class="notice">

            현재 표시되는 티어는
            <b>테스트 데이터</b>입니다.

            <br><br>

            Riot Production API 승인 이후
            실제 Riot 계정의 VALORANT 경쟁전 티어를
            조회하고 인증하는 기능으로 연결할 예정입니다.

        </div>


        <a class="button"
           href="https://discord.gg/gHfjAj96r"
           target="_blank">
            💬 NOVA Discord 입장
        </a>

        <br>

        <a class="button"
           href="/">
            ← 홈페이지로 돌아가기
        </a>

    </div>

</div>

</body>
</html>
"""


# =========================================================
# Render 실행
# =========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )

