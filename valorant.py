from flask import Flask

app = Flask(__name__)


@app.route("/")
def valorant():

    return """
<!DOCTYPE html>
<html lang="ko">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>NOVA • VALORANT</title>


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
            #292f70,
            #0b0d14 45%,
            #07080c
        );

    color: white;

    font-family:
        Arial,
        "Noto Sans KR",
        sans-serif;

    min-height: 100vh;

}


.container {

    max-width: 950px;

    margin: auto;

    padding:
        80px 25px;

}


.back {

    color: #8f96ad;

    text-decoration: none;

    font-size: 14px;

}


.back:hover {

    color: white;

}


.header {

    text-align: center;

    margin:
        70px 0 45px;

}


.header .icon {

    font-size: 60px;

    margin-bottom: 20px;

}


.header h1 {

    font-size: 45px;

    margin-bottom: 12px;

}


.header p {

    color: #9299ad;

}


.login-card {

    max-width: 600px;

    margin: auto;

    padding: 45px;

    border-radius: 25px;

    background:
        rgba(20,23,35,0.9);

    border:
        1px solid #2a3044;

    text-align: center;

    box-shadow:
        0 25px 80px
        rgba(0,0,0,0.35);

}


.login-card h2 {

    margin-bottom: 15px;

}


.login-card p {

    color: #8f96a9;

    line-height: 1.7;

}


.riot-button {

    display: inline-block;

    margin-top: 30px;

    padding:
        15px 30px;

    border-radius: 12px;

    background: #d63845;

    color: white;

    text-decoration: none;

    font-weight: bold;

}


.riot-button:hover {

    background: #ee4653;

}


.notice {

    margin-top: 25px;

    padding: 15px;

    border-radius: 12px;

    background:
        rgba(255,255,255,0.04);

    color: #777f94;

    font-size: 13px;

}


.stats {

    margin-top: 40px;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 15px;

}


.stat {

    padding: 25px;

    border-radius: 18px;

    background:
        rgba(20,23,35,0.8);

    border:
        1px solid #252b3d;

    text-align: center;

}


.stat .emoji {

    font-size: 28px;

    margin-bottom: 12px;

}


.stat h3 {

    font-size: 14px;

    color: #858ca0;

    margin-bottom: 8px;

}


.stat strong {

    font-size: 20px;

}


footer {

    text-align: center;

    color: #555c70;

    margin-top: 80px;

    font-size: 13px;

}


@media(max-width: 700px) {

    .stats {

        grid-template-columns:
            1fr;

    }


    .header h1 {

        font-size: 35px;

    }

}

</style>

</head>


<body>


<div class="container">


    <a
        class="back"
        href="http://127.0.0.1:5000"
    >
        ← NOVA 홈으로
    </a>


    <div class="header">

        <div class="icon">
            🎮
        </div>

        <h1>
            VALORANT
        </h1>

        <p>
            NOVA에서 VALORANT 전적을 확인하세요.
        </p>

    </div>


    <div class="login-card">

        <h2>
            🔗 Riot 계정 연결
        </h2>

        <p>

            Riot 계정을 연결하면
            자신의 VALORANT 경기 기록과
            통계를 확인할 수 있도록 준비하고 있습니다.

        </p>


        <a
            class="riot-button"
            href="#"
        >
            RIOT 계정 연결하기
        </a>


        <div class="notice">

            현재 Riot 공식 인증 연동을 준비 중입니다.
            <br>
            지금은 테스트 화면입니다.

        </div>

    </div>


    <div class="stats">


        <div class="stat">

            <div class="emoji">
                🏆
            </div>

            <h3>
                현재 티어
            </h3>

            <strong>
                준비 중
            </strong>

        </div>


        <div class="stat">

            <div class="emoji">
                📊
            </div>

            <h3>
                승률
            </h3>

            <strong>
                준비 중
            </strong>

        </div>


        <div class="stat">

            <div class="emoji">
                ⚔️
            </div>

            <h3>
                최근 경기
            </h3>

            <strong>
                준비 중
            </strong>

        </div>


    </div>


    <footer>

        NOVA • VALORANT

    </footer>


</div>


</body>

</html>
"""


if __name__ == "__main__":

    app.run(
        port=5001,
        debug=True
    )