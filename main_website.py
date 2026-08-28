from flask import Flask

app = Flask(__name__)


# ========================================
# NOVA 메인 홈페이지
# ========================================

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
            body {
                margin: 0;
                background: #0f1117;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 100px 20px;
            }

            h1 {
                font-size: 56px;
                margin-bottom: 10px;
            }

            .subtitle {
                color: #aaa;
                font-size: 20px;
                margin-bottom: 40px;
            }

            .button {
                display: inline-block;
                padding: 15px 30px;
                margin: 10px;
                background: #5865F2;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }

            .button:hover {
                opacity: 0.85;
            }

            .card {
                margin-top: 50px;
                padding: 30px;
                background: #181b24;
                border-radius: 15px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🌌 NOVA</h1>

            <div class="subtitle">
                한국 VALORANT 커뮤니티
            </div>

            <div>
                <a class="button"
                   href="https://discord.gg/gHfjAj96r">
                    💬 NOVA Discord
                </a>

                <a class="button"
                   href="/tier">
                    🏆 티어 인증
                </a>
            </div>

            <div class="card">

                <h2>🎮 NOVA Tier Verification</h2>

                <p>
                    VALORANT 티어 인증을 진행할 수 있습니다.
                </p>

                <p>
                    Riot Production API 승인 후
                    실제 Riot 계정 티어가 연결됩니다.
                </p>

            </div>

        </div>

    </body>
    </html>
    """


# ========================================
# 티어 인증 페이지
# ========================================

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

            body {
                margin: 0;
                background: #0f1117;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 80px 20px;
            }

            .card {
                background: #181b24;
                padding: 40px;
                border-radius: 18px;
            }

            h1 {
                margin-bottom: 10px;
            }

            .rank {
                font-size: 35px;
                margin: 30px 0;
            }

            .test {
                color: #aaa;
                font-size: 14px;
            }

            .button {
                display: inline-block;
                margin-top: 30px;
                padding: 14px 28px;
                background: #5865F2;
                color: white;
                text-decoration: none;
                border-radius: 10px;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <div class="card">

                <h1>🌌 NOVA</h1>

                <h2>VALORANT Community Tier Verification</h2>

                <hr>

                <h2>인증 완료</h2>

                <div class="rank">
                    🥉 Bronze 3
                </div>

                <p class="test">
                    테스트 티어
                </p>

                <p>
                    현재 표시되는 티어는 테스트 데이터입니다.
                </p>

                <p>
                    실제 Riot 계정 및 실제 경쟁전 티어는
                    Riot Production API 승인 후 연결됩니다.
                </p>

                <a class="button"
                   href="/">
                    처음으로 돌아가기
                </a>

            </div>

        </div>

    </body>

    </html>
    """


# ========================================
# Render 실행
# ========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
