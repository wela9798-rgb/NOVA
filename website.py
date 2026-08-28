import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA - VALORANT Tier Verification</title>

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
                    #25213d 0%,
                    #11101b 45%,
                    #09090f 100%
                );

            color: #ffffff;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1050px;
            margin: 0 auto;
            padding: 30px 20px 60px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0 40px;
        }

        .logo {
            font-size: 30px;
            font-weight: 900;
            letter-spacing: 4px;
        }

        .badge {
            padding: 8px 14px;
            border-radius: 20px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.1);
            color: #cfcfe8;
            font-size: 13px;
        }

        .hero {
            text-align: center;
            padding: 65px 20px 45px;
        }

        .hero h1 {
            font-size: clamp(40px, 7vw, 72px);
            font-weight: 900;
            letter-spacing: -3px;
            margin-bottom: 18px;
        }

        .hero h1 span {
            color: #8f7cff;
        }

        .hero p {
            color: #aaa8bd;
            font-size: 17px;
            line-height: 1.8;
        }

        .card {
            background: rgba(24, 23, 38, 0.92);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 35px;
            box-shadow: 0 25px 70px rgba(0,0,0,0.35);
            backdrop-filter: blur(15px);
        }

        .card-title {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .card-description {
            color: #9d9aad;
            line-height: 1.7;
            margin-bottom: 28px;
        }

        .steps {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }

        .step {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px;
            padding: 20px;
        }

        .step-number {
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #7665ff;
            font-weight: 800;
            margin-bottom: 12px;
        }

        .step h3 {
            font-size: 15px;
            margin-bottom: 7px;
        }

        .step p {
            color: #9290a1;
            font-size: 13px;
            line-height: 1.5;
        }

        .notice {
            background: rgba(118,101,255,0.08);
            border: 1px solid rgba(118,101,255,0.25);
            border-radius: 15px;
            padding: 18px;
            color: #c5c0ff;
            font-size: 13px;
            line-height: 1.7;
            margin-bottom: 25px;
        }

        .button {
            width: 100%;
            border: none;
            border-radius: 14px;
            padding: 17px 20px;
            background: #7665ff;
            color: white;
            font-size: 16px;
            font-weight: 800;
            cursor: pointer;
            transition: 0.2s;
        }

        .button:hover {
            transform: translateY(-2px);
            background: #8575ff;
        }

        .button:active {
            transform: translateY(0);
        }

        .result {
            display: none;
            margin-top: 25px;
        }

        .result.show {
            display: block;
        }

        .success {
            background: rgba(63, 200, 132, 0.08);
            border: 1px solid rgba(63, 200, 132, 0.25);
            border-radius: 15px;
            padding: 17px;
            color: #79e0aa;
            margin-bottom: 20px;
        }

        .profile {
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 18px;
            padding: 25px;
        }

        .profile-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }

        .profile-name {
            font-size: 22px;
            font-weight: 800;
        }

        .verified {
            color: #6ee7a0;
            font-size: 13px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        .stat {
            background: rgba(0,0,0,0.15);
            border-radius: 14px;
            padding: 18px;
        }

        .stat-label {
            color: #858294;
            font-size: 12px;
            margin-bottom: 8px;
        }

        .stat-value {
            font-size: 18px;
            font-weight: 800;
        }

        .tier {
            color: #e7c56b;
        }

        footer {
            text-align: center;
            color: #676575;
            font-size: 12px;
            line-height: 1.7;
            margin-top: 35px;
        }

        @media (max-width: 700px) {
            .steps {
                grid-template-columns: 1fr;
            }

            .stats {
                grid-template-columns: 1fr;
            }

            .card {
                padding: 23px;
            }

            .hero {
                padding-top: 35px;
            }

            header {
                padding-bottom: 20px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <header>
        <div class="logo">NOVA</div>
        <div class="badge">VALORANT TIER VERIFICATION</div>
    </header>

    <section class="hero">
        <h1>NOVA <span>Tier Verify</span></h1>
        <p>
            NOVA 서버에서 사용하는<br>
            VALORANT 티어 인증 시스템 프로토타입
        </p>
    </section>

    <section class="card">

        <div class="card-title">
            티어 인증
        </div>

        <div class="card-description">
            Riot 계정 인증을 통해 본인의 VALORANT 계정을 확인하고
            서버에서 티어 인증을 진행할 수 있습니다.
        </div>

        <div class="steps">

            <div class="step">
                <div class="step-number">1</div>
                <h3>Riot 계정 연결</h3>
                <p>
                    Riot 계정을 안전하게 연결합니다.
                </p>
            </div>

            <div class="step">
                <div class="step-number">2</div>
                <h3>계정 확인</h3>
                <p>
                    연결된 계정 정보를 확인합니다.
                </p>
            </div>

            <div class="step">
                <div class="step-number">3</div>
                <h3>티어 인증</h3>
                <p>
                    확인된 계정의 티어 정보를 표시합니다.
                </p>
            </div>

        </div>

        <div class="notice">
            <strong>데이터 공유 안내</strong><br>
            실제 서비스에서는 Riot Sign On(RSO)을 통해
            사용자가 직접 계정 연결 및 데이터 공유에 동의한 후
            플레이어 정보를 확인합니다.
            현재 페이지는 Riot 심사용 사용자 흐름을 보여주기 위한
            프로토타입입니다.
        </div>

        <button class="button" onclick="verifyAccount()">
            Riot 계정 인증 시작
        </button>

        <div id="result" class="result">

            <div class="success">
                ✓ 계정 인증 프로세스가 완료되었습니다.
            </div>

            <div class="profile">

                <div class="profile-header">

                    <div>
                        <div class="profile-name">
                            NOVA_TestUser#KR1
                        </div>

                        <div class="verified">
                            ✓ 인증된 계정
                        </div>
                    </div>

                </div>

                <div class="stats">

                    <div class="stat">
                        <div class="stat-label">
                            RIOT ID
                        </div>

                        <div class="stat-value">
                            NOVA_TestUser
                        </div>
                    </div>

                    <div class="stat">
                        <div class="stat-label">
                            지역
                        </div>

                        <div class="stat-value">
                            KR
                        </div>
                    </div>

                    <div class="stat">
                        <div class="stat-label">
                            현재 티어
                        </div>

                        <div class="stat-value tier">
                            Gold 2
                        </div>
                    </div>

                </div>

            </div>

        </div>

    </section>

    <footer>
        NOVA Tier Verification Prototype<br>
        This is an unofficial VALORANT community project.
        NOVA is not endorsed by Riot Games.
    </footer>

</div>

<script>
function verifyAccount() {

    const button = document.querySelector(".button");
    const result = document.getElementById("result");

    button.disabled = true;
    button.textContent = "계정 확인 중...";

    setTimeout(function() {

        result.classList.add("show");

        button.textContent = "인증 완료";
        button.disabled = false;

    }, 1200);
}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
