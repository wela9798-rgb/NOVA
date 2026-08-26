from flask import Flask

app = Flask(__name__)


STYLE = """
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background:
        radial-gradient(
            circle at 50% 0%,
            #292f70 0%,
            #0b0d14 45%,
            #07080c 100%
        );

    color: white;
    font-family: Arial, "Noto Sans KR", sans-serif;
    min-height: 100vh;
}

a {
    text-decoration: none;
}

.navbar {
    width: 100%;
    padding: 25px 7%;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    color: white;
    font-size: 25px;
    font-weight: 900;
}

.logo span {
    color: #7c83ff;
}

.nav-menu {
    display: flex;
    gap: 28px;
}

.nav-menu a {
    color: #aeb4c7;
    font-size: 14px;
}

.nav-menu a:hover {
    color: white;
}

.container {
    max-width: 1100px;
    margin: auto;
    padding: 60px 25px;
}

.back {
    color: #9299ad;
    display: inline-block;
    margin-bottom: 30px;
}

.header {
    text-align: center;
    margin-bottom: 45px;
}

.header-icon {
    font-size: 55px;
    margin-bottom: 15px;
}

.header h1 {
    font-size: 45px;
    margin-bottom: 12px;
}

.header p {
    color: #9299ad;
}

.profile {
    max-width: 850px;
    margin: auto;

    display: flex;
    align-items: center;
    gap: 20px;

    padding: 30px;

    background: rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;

    margin-bottom: 20px;
}

.avatar {
    width: 70px;
    height: 70px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #9b7cff
        );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 32px;
}

.profile h2 {
    margin-bottom: 6px;
}

.profile p {
    color: #7f879c;
    font-size: 14px;
}

.rank-card {
    max-width: 850px;
    margin: auto;

    padding: 30px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(99,102,241,0.18),
            rgba(20,23,35,0.95)
        );

    border: 1px solid #303653;

    margin-bottom: 20px;
}

.rank-title {
    color: #9299ad;
    font-size: 14px;
    margin-bottom: 10px;
}

.rank-name {
    font-size: 32px;
    font-weight: bold;
}

.rank-sub {
    color: #7f879c;
    margin-top: 7px;
}

.stats {
    max-width: 850px;
    margin: auto;

    display: grid;
    grid-template-columns:
        repeat(4, 1fr);

    gap: 15px;

    margin-bottom: 20px;
}

.stat {
    padding: 25px;

    text-align: center;

    border-radius: 18px;

    background:
        rgba(20,23,35,0.85);

    border: 1px solid #252b3d;
}

.stat-icon {
    font-size: 27px;
    margin-bottom: 12px;
}

.stat-title {
    color: #858ca0;
    font-size: 13px;
    margin-bottom: 8px;
}

.stat-value {
    font-size: 22px;
    font-weight: bold;
}

.matches {
    max-width: 850px;
    margin: auto;

    background:
        rgba(20,23,35,0.9);

    border: 1px solid #2a3044;

    border-radius: 22px;

    padding: 30px;
}

.matches h2 {
    margin-bottom: 20px;
}

.match {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px;

    background:
        rgba(255,255,255,0.03);

    border-radius: 14px;

    margin-bottom: 10px;
}

.match:last-child {
    margin-bottom: 0;
}

.match-left {
    display: flex;
    align-items: center;
    gap: 15px;
}

.result-win {
    color: #70e09b;
    font-weight: bold;
}

.result-lose {
    color: #ff7272;
    font-weight: bold;
}

.match-map {
    color: #dce0ec;
}

.match-info {
    color: #747c91;
    font-size: 13px;
}

.connect-box {
    max-width: 850px;
    margin: 20px auto 0;

    padding: 25px;

    text-align: center;

    background:
        rgba(99,102,241,0.08);

    border:
        1px solid rgba(124,131,255,0.2);

    border-radius: 18px;
}

.connect-box p {
    color: #9299ad;
    line-height: 1.7;
    margin-bottom: 18px;
}

.button {
    display: inline-block;

    padding: 13px 22px;

    border-radius: 11px;

    font-weight: bold;
}

.primary {
    background: #6366f1;
    color: white;
}

.secondary {
    background: rgba(255,255,255,0.05);
    color: #d8dbea;

    border: 1px solid #303548;
}

footer {
    margin-top: 80px;

    border-top: 1px solid #1e2230;

    text-align: center;

    padding: 35px;

    color: #62697b;

    font-size: 13px;
}

footer a {
    color: #858ca0;
    margin: 0 8px;
}

@media(max-width: 750px) {

    .nav-menu {
        display: none;
    }

    .stats {
        grid-template-columns: 1fr 1fr;
    }

    .match {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
}

</style>
"""


NAV = """
<nav class="navbar">

    <a class="logo" href="/">
        N<span>O</span>VA
    </a>

    <div class="nav-menu">

        <a href="/">
            홈
        </a>

        <a href="/valorant">
            VALORANT
        </a>

        <a href="/terms">
            이용약관
        </a>

        <a href="/privacy">
            개인정보
        </a>

    </div>

</nav>
"""


FOOTER = """
<footer>

    <strong>NOVA</strong>

    <br><br>

    함께 만들어가는 서버 🤖

    <br><br>

    <a href="/terms">
        이용약관
    </a>

    |

    <a href="/privacy">
        개인정보
    </a>

</footer>
"""


# =========================
# 홈페이지
# =========================

@app.route("/")
def home():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA</title>

{STYLE}

</head>

<body>

{NAV}

<section class="container">

    <div class="header">

        <div class="header-icon">
            🤖
        </div>

        <h1>
            Meet <span style="color:#7c83ff;">NOVA</span>
        </h1>

        <p>
            Discord와 VALORANT를 위한
            NOVA의 다양한 기능을 만나보세요.
        </p>

        <br>

        <a
            class="button primary"
            href="/valorant"
        >
            🎮 VALORANT 전적 보기
        </a>

    </div>

</section>

{FOOTER}

</body>

</html>
"""


# =========================
# VALORANT 전적
# =========================

@app.route("/valorant")
def valorant():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • VALORANT</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <a class="back" href="/">
        ← NOVA 홈으로
    </a>


    <div class="header">

        <div class="header-icon">
            🎮
        </div>

        <h1>
            VALORANT 전적
        </h1>

        <p>
            NOVA 전적 시스템 미리보기
        </p>

    </div>


    <!-- 프로필 -->

    <div class="profile">

        <div class="avatar">
            🎮
        </div>

        <div>

            <h2>
                플래시맞은토끼
            </h2>

            <p>
                실력키우자
            </p>

        </div>

    </div>


    <!-- 티어 -->

    <div class="rank-card">

        <div class="rank-title">
            🏆 현재 티어
        </div>

        <div class="rank-name">
            준비 중
        </div>

        <div class="rank-sub">
            Riot 계정 연결 후 표시됩니다.
        </div>

    </div>


    <!-- 통계 -->

    <div class="stats">


        <div class="stat">

            <div class="stat-icon">
                📊
            </div>

            <div class="stat-title">
                승률
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>


        <div class="stat">

            <div class="stat-icon">
                ⚔️
            </div>

            <div class="stat-title">
                K/D
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>


        <div class="stat">

            <div class="stat-icon">
                🏆
            </div>

            <div class="stat-title">
                승리
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>


        <div class="stat">

            <div class="stat-icon">
                🎮
            </div>

            <div class="stat-title">
                경기
            </div>

            <div class="stat-value">
                준비 중
            </div>

        </div>


    </div>


    <!-- 최근 경기 -->

    <div class="matches">

        <h2>
            ⚔️ 최근 경기
        </h2>


        <div class="match">

            <div class="match-left">

                <span class="result-win">
                    WIN
                </span>

                <span class="match-map">
                    최근 경기
                </span>

            </div>

            <span class="match-info">
                준비 중
            </span>

        </div>


        <div class="match">

            <div class="match-left">

                <span class="result-lose">
                    LOSS
                </span>

                <span class="match-map">
                    최근 경기
                </span>

            </div>

            <span class="match-info">
                준비 중
            </span>

        </div>


        <div class="match">

            <div class="match-left">

                <span class="result-win">
                    WIN
                </span>

                <span class="match-map">
                    최근 경기
                </span>

            </div>

            <span class="match-info">
                준비 중
            </span>

        </div>

    </div>


    <!-- Riot 연결 -->

    <div class="connect-box">

        <p>

            자신의 VALORANT 데이터를 확인하려면
            공식 Riot 계정 인증과 데이터 공유
            동의가 필요합니다.

        </p>

        <a
            class="button primary"
            href="/connect"
        >
            🔗 Riot 계정 연결

        </a>

    </div>


</div>

{FOOTER}

</body>

</html>
"""


# =========================
# Riot 연결 안내
# =========================

@app.route("/connect")
def connect():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • Riot 연결</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="login-card">

        <div class="header-icon">
            🔗
        </div>

        <h1>
            Riot 계정 연결
        </h1>

        <p>

            실제 서비스에서는 Riot의 공식
            로그인 절차를 통해 사용자가 직접
            계정을 연결하게 됩니다.

        </p>

        <br>

        <p>

            현재는 NOVA의 사용자 흐름을
            확인하기 위한 테스트 화면입니다.

        </p>


        <br><br>

        <a
            class="button primary"
            href="/connected"
        >
            연결 계속하기
        </a>


        <br><br>

        <a
            class="button secondary"
            href="/valorant"
        >
            돌아가기
        </a>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================
# 연결 완료 테스트
# =========================

@app.route("/connected")
def connected():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 연결 완료</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="login-card">

        <div class="header-icon">
            ✅
        </div>

        <h1>
            연결 테스트 완료
        </h1>

        <p>

            NOVA의 계정 연결 흐름이
            정상적으로 작동했습니다.

        </p>

        <div class="notice">

            현재는 테스트 환경입니다.

            <br><br>

            실제 Riot 인증은
            RSO 승인을 받은 이후 연결합니다.

        </div>

        <br><br>

        <a
            class="button primary"
            href="/valorant"
        >
            🎮 전적 페이지로 돌아가기
        </a>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================
# 이용약관
# =========================

@app.route("/terms")
def terms():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 이용약관</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="page-box">

        <h1>
            📜 이용약관
        </h1>

        <br>

        <h2>
            제1조 목적
        </h2>

        <p>
            본 페이지는 NOVA 서비스의
            이용약관 안내를 위한 페이지입니다.
        </p>

        <br>

        <h2>
            제2조 서비스
        </h2>

        <p>
            NOVA는 Discord 서버 관리 및
            VALORANT 관련 정보 제공 기능을
            개발하고 있습니다.
        </p>

        <br>

        <h2>
            제3조 이용자
        </h2>

        <p>
            이용자는 관련 법령 및 각 서비스의
            이용정책을 준수하여야 합니다.
        </p>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================
# 개인정보
# =========================

@app.route("/privacy")
def privacy():

    return f"""
<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>NOVA • 개인정보</title>

{STYLE}

</head>

<body>

{NAV}

<div class="container">

    <div class="page-box">

        <h1>
            🔐 개인정보처리방침
        </h1>

        <br>

        <h2>
            1. 개인정보 수집
        </h2>

        <p>
            실제 서비스에서 수집하는 정보와
            처리 방식은 서비스 출시 전에
            정확하게 명시할 예정입니다.
        </p>

        <br>

        <h2>
            2. 이용 목적
        </h2>

        <p>
            서비스 제공 및 계정 연결,
            게임 관련 기능 제공을 위해
            필요한 범위에서 정보를 처리합니다.
        </p>

        <br>

        <h2>
            3. 정보 보호
        </h2>

        <p>
            이용자의 정보가 안전하게
            처리될 수 있도록 적절한
            보안 조치를 적용할 예정입니다.
        </p>

    </div>

</div>

{FOOTER}

</body>

</html>
"""


# =========================
# 실행
# =========================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

      

      
