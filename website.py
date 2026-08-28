import os

from flask import Flask, render_template_string


app = Flask("nova")


HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA - VALORANT 티어 인증</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, "Noto Sans KR", sans-serif;
            background: #0b0b12;
            color: white;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
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
            letter-spacing: 5px;
        }

        .status {
            color: #aaaabb;
            font-size: 13px;
        }

        .hero {
            text-align: center;
            padding: 110px 20px 90px;
        }

        .badge {
            display: inline-block;
            padding: 8px 16px;
            border: 1px solid #30303d;
            border-radius: 30px;
            color: #aaaabb;
            font-size: 12px;
            margin-bottom: 25px;
        }

        h1 {
            font-size: clamp(42px, 7vw, 78px);
            line-height: 1.1;
            margin-bottom: 30px;
        }

        .red {
            color: #ff4655;
        }

        .hero-text {
            max-width: 720px;
            margin: auto;
            color: #a5a5b5;
            line-height: 1.9;
            font-size: 17px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 60px;
        }

        .card {
            padding: 30px;
            background: #12121b;
            border: 1px solid #292936;
            border-radius: 18px;
        }

        .icon {
            font-size: 30px;
            margin-bottom: 18px;
        }

        .card h2 {
            margin-bottom: 12px;
            font-size: 20px;
        }

        .card p {
            color: #9696a7;
            line-height: 1.8;
            font-size: 14px;
        }

        .verification {
            padding: 35px;
            margin-bottom: 30px;
            background: #12121b;
            border: 1px solid #3d2025;
            border-radius: 20px;
        }

        .verification h2 {
            margin-bottom: 15px;
        }

        .verification p {
            color: #a6a6b5;
            line-height: 1.8;
            font-size: 14px;
        }

        .steps {
            margin-top: 25px;
            display: grid;
            gap: 12px;
        }

        .step {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 15px;
            background: #0d0d14;
            border-radius: 12px;
            color: #c0c0cc;
            font-size: 14px;
        }

        .number {
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #ff4655;
            font-size: 12px;
            font-weight: bold;
        }

        .notice {
            padding: 30px;
            margin-bottom: 70px;
            background: #12121b;
            border: 1px solid #292936;
            border-radius: 18px;
        }

        .notice h2 {
            margin-bottom: 15px;
        }

        .notice p {
            color: #9696a7;
            line-height: 1.9;
            font-size: 13px;
        }

        footer {
            padding: 30px 0;
            border-top: 1px solid #242430;
            text-align: center;
            color: #666676;
            font-size: 12px;
            line-height: 1.8;
        }

    </style>
</head>

<body>

<div class="container">

    <header>

        <div class="logo">
            NOVA
        </div>

        <div class="status">
            ● 서비스 정상 운영
        </div>

    </header>


    <section class="hero">

        <div class="badge">
            VALORANT COMMUNITY SERVICE
        </div>

        <h1>
            NOVA와 함께하는<br>
            <span class="red">VALORANT 티어 인증</span>
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
                확인하고 Discord 서버에서
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

                Riot Games에서 제공하는
                공식 API를 활용하여
                플레이어의 게임 정보를
                조회하는 기능을 구현합니다.

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
                편리하게 확인할 수 있도록 합니다.

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
            Production 이용 승인을 전제로
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

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


port = int(os.environ.get("PORT", "10000"))

app.run(
    host="0.0.0.0",
    port=port
)
