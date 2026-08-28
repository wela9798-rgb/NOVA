```python
import os
from flask import Flask, render_template_string, redirect, url_for

# =========================================================
# NOVA
# VALORANT TIER VERIFICATION PROTOTYPE
# =========================================================

app = Flask(__name__)


# =========================================================
# 공통 HTML
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>{{ title }} | NOVA</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;

            display: flex;
            align-items: center;
            justify-content: center;

            font-family:
                Arial,
                "Noto Sans KR",
                sans-serif;

            background:
                radial-gradient(
                    circle at top,
                    #1b2340 0%,
                    #0b0f19 45%,
                    #070a11 100%
                );

            color: white;
        }

        .container {
            width: 92%;
            max-width: 560px;

            padding: 45px 35px;

            background: rgba(18, 24, 39, 0.96);

            border: 1px solid rgba(255,255,255,0.08);

            border-radius: 24px;

            text-align: center;

            box-shadow:
                0 25px 70px rgba(0,0,0,0.5);
        }

        .logo {
            font-size: 48px;
            font-weight: 900;
            letter-spacing: 8px;

            margin-bottom: 8px;
        }

        .tagline {
            color: #9ca3af;
            font-size: 15px;

            margin-bottom: 35px;
        }

        h2 {
            margin-top: 0;
            margin-bottom: 15px;
        }

        p {
            color: #c7cbd4;
            line-height: 1.7;
        }

        .button {
            display: block;

            width: 100%;

            padding: 16px 20px;

            margin-top: 25px;

            border-radius: 13px;

            background: #5865f2;

            color: white;

            text-decoration: none;

            font-size: 16px;
            font-weight: 700;

            transition: 0.2s;
        }

        .button:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }

        .secondary {
            background: #252c3d;
        }

        .box {
            margin-top: 25px;

            padding: 18px;

            background: #1b2335;

            border-radius: 14px;

            color: #cbd5e1;

            line-height: 1.7;
        }

        .rank {
            margin-top: 25px;

            font-size: 34px;

            font-weight: 900;
        }

        .badge {
            display: inline-block;

            padding: 7px 13px;

            margin-top: 10px;

            border-radius: 999px;

            background: #252c3d;

            color: #cbd5e1;

            font-size: 13px;
        }

        .footer {
            margin-top: 28px;

            color: #6b7280;

            font-size: 12px;
        }

    </style>

</head>


<body>

<div class="container">

    <div class="logo">
        NOVA
    </div>

    <div class="tagline">
        VALORANT Community Tier Verification
    </div>


    {% if page == "home" %}

        <h2>
            VALORANT 티어 인증
        </h2>

        <p>
            NOVA 커뮤니티에서<br>
            자신의 VALORANT 경쟁전 티어를 인증할 수 있습니다.
        </p>

        <a
            class="button"
            href="/riot-login"
        >
            Riot 계정 인증하기
        </a>


        <div class="footer">
            NOVA Tier Verification Prototype
        </div>


    {% elif page == "login" %}

        <h2>
            Riot 계정 인증
        </h2>

        <p>
            NOVA에서 VALORANT 티어 인증을 진행합니다.
        </p>

        <div class="box">

            🔐 Riot Sign On (RSO)

            <br><br>

            현재 NOVA는 Riot Production API 심사 중입니다.

            <br>

            아래 버튼은
            <strong>테스트 인증</strong>을 위한 버튼입니다.

        </div>


        <a
            class="button"
            href="/verify"
        >
            테스트 인증 진행
        </a>


        <a
            class="button secondary"
            href="/"
        >
            돌아가기
        </a>


    {% elif page == "verify" %}

        <h2>
            인증 완료
        </h2>


        <div class="box">

            ✅ Riot 계정 인증 테스트 완료

        </div>


        <div class="rank">
            🥉 Bronze 3
        </div>


        <div class="badge">
            테스트 티어
        </div>


        <p>
            현재 표시되는 티어는 테스트 데이터입니다.
        </p>


        <div class="box">

            실제 Riot 계정 및 실제 경쟁전 티어는
            Riot Production API 승인 후 연결됩니다.

        </div>


        <a
            class="button"
            href="/"
        >
            처음으로 돌아가기
        </a>


    {% endif %}

</div>

</body>

</html>
"""


# =========================================================
# 메인 페이지
# =========================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        page="home",
        title="VALORANT Tier Verification"
    )


# =========================================================
# Riot 로그인 페이지
# =========================================================

@app.route("/riot-login")
def riot_login():

    return render_template_string(
        HTML,
        page="login",
        title="Riot Account Verification"
    )


# =========================================================
# 테스트 인증
# =========================================================

@app.route("/verify")
def verify():

    return render_template_string(
        HTML,
        page="verify",
        title="Verification Complete"
    )


# =========================================================
# Health Check
# =========================================================

@app.route("/health")
def health():

    return {
        "status": "ok",
        "service": "NOVA",
        "riot_api": "pending_review"
    }


# =========================================================
# 실행
# =========================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
```
