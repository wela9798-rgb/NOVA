import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA | VALORANT 인증</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, "Noto Sans KR", sans-serif;
            background:
                radial-gradient(circle at top left, #22243d 0%, transparent 35%),
                radial-gradient(circle at bottom right, #351f36 0%, transparent 35%),
                #0b0c12;
            color: #ffffff;
            min-height: 100vh;
        }

        .container {
            width: min(1050px, 92%);
            margin: 0 auto;
        }

        nav {
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-size: 26px;
            font-weight: 900;
            letter-spacing: 4px;
        }

        .badge {
            padding: 8px 14px;
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 999px;
            color: #bfc2d9;
            font-size: 13px;
        }

        .hero {
            padding: 75px 0 40px;
            text-align: center;
        }

        .hero h1 {
            margin: 0;
            font-size: clamp(42px, 7vw, 76px);
            letter-spacing: -3px;
        }

        .hero h1 span {
            color: #ff4655;
        }

        .hero p {
            max-width: 650px;
            margin: 24px auto 0;
            color: #aeb1c4;
            line-height: 1.8;
            font-size: 16px;
        }

        .card {
            max-width: 650px;
            margin: 35px auto;
            padding: 34px;
            background: rgba(22, 23, 33, 0.92);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 22px;
            box-shadow: 0 25px 80px rgba(0,0,0,0.35);
        }

        .card h2 {
            margin-top: 0;
            margin-bottom: 10px;
        }

        .card-description {
            color: #9da0b4;
            line-height: 1.7;
            font-size: 14px;
            margin-bottom: 25px;
        }

        .riot-button {
            width: 100%;
            border: 0;
            border-radius: 12px;
            padding: 16px;
            background: #ff4655;
            color: white;
            font-size: 16px;
            font-weight: 800;
            cursor: pointer;
            transition: 0.2s;
        }

        .riot-button:hover {
            transform: translateY(-2px);
            filter: brightness(1.08);
        }

        .flow {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 25px;
        }

        .step {
            padding: 20px;
            border-radius: 16px;
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.06);
        }

        .step-number {
            display: inline-flex;
            width: 30px;
            height: 30px;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #ff4655;
            font-weight: 800;
            margin-bottom: 12px;
        }

        .step h3 {
            font-size: 15px;
            margin: 5px 0;
        }

        .step p {
            color: #8f92a5;
            font-size: 13px;
            line-height: 1.6;
            margin: 0;
        }

        .notice {
            margin-top: 25px;
            padding: 17px;
            border-radius: 12px;
            background: rgba(255,255,255,0.035);
            color: #9da0b4;
            font-size: 12px;
            line-height: 1.7;
        }

        footer {
            padding: 60px 0 35px;
            text-align: center;
            color: #676a7a;
            font-size: 12px;
        }

        .result {
            text-align: center;
        }

        .verified {
            display: inline-block;
            padding: 7px 13px;
            border-radius: 999px;
            background: rgba(60, 200, 130, 0.12);
            color: #67d99d;
            font-size: 13px;
            margin-bottom: 15px;
        }

        .rank-box {
            margin-top: 20px;
            padding: 25px;
            border-radius: 17px;
            background: rgba(255,255,255,0.035);
        }

        .rank {
            font-size: 34px;
            font-weight: 900;
            margin-top: 8px;
        }

        .back {
            display: inline-block;
            margin-top: 20px;
            color: #aeb1c4;
            text-decoration: none;
            font-size: 13px;
        }

        @media (max-width: 700px) {
            .flow {
                grid-template-columns: 1fr;
            }

            .card {
                padding: 25px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <nav>
        <div class="logo">NOVA</div>
        <div class="badge">VALORANT COMMUNITY</div>
    </nav>

    {% if verified %}

    <section class="hero">
        <h1>인증 <span>완료</span></h1>
        <p>
            Riot 계정 인증 흐름이 완료된 것으로 표시되는
            NOVA 심사용 프로토타입 화면입니다.
        </p>
    </section>

    <div class="card result">

        <div class="verified">
            ✓ Riot 계정 인증 완료
        </div>

        <h2>VALORANT 티어 인증</h2>

        <div class="rank-box">
            <div>현재 경쟁전 티어</div>
            <div class="rank">GOLD 2</div>
        </div>

        <div class="notice">
            이 화면의 티어 정보는 심사용 프로토타입을 위한
            예시 데이터입니다. 실제 플레이어 데이터는
            Riot Sign On(RSO) 인증 및 승인된 API 접근을 통해
            사용자의 동의 후 표시됩니다.
        </div>

        <a class="back" href="/">← 처음으로 돌아가기</a>

    </div>

    {% else %}

    <section class="hero">

        <h1>NOVA <span>VERIFY</span></h1>

        <p>
            VALORANT 플레이어가 자신의 Riot 계정을 연결하고
            경쟁전 티어를 인증할 수 있도록 설계된
            NOVA의 계정 인증 프로토타입입니다.
        </p>

    </section>

    <div class="card">

        <h2>VALORANT 티어 인증</h2>

        <div class="card-description">
            Riot 계정을 안전하게 연결하여 본인의 VALORANT
            계정 정보를 인증하는 흐름입니다.
            계정 연결 과정에서는 Riot Sign On을 통한
            사용자 동의가 필요합니다.
        </div>

        <form action="/verify" method="get">
            <button class="riot-button" type="submit">
                Riot 계정으로 인증하기
            </button>
        </form>

        <div class="flow">

            <div class="step">
                <div class="step-number">1</div>
                <h3>Riot 계정 연결</h3>
                <p>
                    사용자가 Riot Sign On을 통해
                    자신의 계정을 연결합니다.
                </p>
            </div>

            <div class="step">
                <div class="step-number">2</div>
                <h3>사용자 동의</h3>
                <p>
                    계정 데이터 공유에 대한
                    사용자의 동의를 확인합니다.
                </p>
            </div>

            <div class="step">
                <div class="step-number">3</div>
                <h3>티어 인증</h3>
                <p>
                    승인된 API와 인증 정보를 이용하여
                    본인의 VALORANT 정보를 확인합니다.
                </p>
            </div>

        </div>

        <div class="notice">
            <strong>개인정보 및 데이터 공유 안내</strong><br>
            NOVA는 사용자가 직접 계정을 연결하고 데이터 공유에
            동의한 경우에만 해당 플레이어의 정보를 표시하는 것을
            목표로 합니다. 현재 페이지는 RSO 연동 전 단계의
            심사용 프로토타입입니다.
        </div>

    </div>

    {% endif %}

    <footer>
        NOVA · VALORANT Community Service<br>
        This is an independent community project and is not endorsed by Riot Games.
    </footer>

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        verified=False
    )


@app.route("/verify")
def verify():
    return render_template_string(
        HTML,
        verified=True
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
