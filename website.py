import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

RIOT_API_KEY = os.getenv("RIOT_API_KEY", "")

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NOVA 티어 인증</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, "Noto Sans KR", sans-serif;
            background:
                radial-gradient(circle at top left, #1e293b 0%, transparent 35%),
                radial-gradient(circle at bottom right, #312e81 0%, transparent 35%),
                #080b12;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px 15px;
        }

        .container {
            width: 100%;
            max-width: 650px;
        }

        .logo {
            text-align: center;
            margin-bottom: 25px;
        }

        .logo h1 {
            margin: 0;
            font-size: 48px;
            letter-spacing: 8px;
            font-weight: 900;
        }

        .logo p {
            margin-top: 10px;
            color: #9ca3af;
            font-size: 15px;
        }

        .card {
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.45);
            backdrop-filter: blur(10px);
        }

        .title {
            font-size: 25px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .description {
            color: #9ca3af;
            line-height: 1.6;
            margin-bottom: 28px;
        }

        label {
            display: block;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #d1d5db;
        }

        input, select {
            width: 100%;
            padding: 14px 15px;
            margin-bottom: 18px;
            border: 1px solid #374151;
            border-radius: 10px;
            background: #111827;
            color: white;
            font-size: 15px;
            outline: none;
        }

        input:focus, select:focus {
            border-color: #6366f1;
        }

        .riot-id {
            display: grid;
            grid-template-columns: 1fr 120px;
            gap: 10px;
        }

        button {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            font-size: 16px;
            font-weight: 800;
            cursor: pointer;
            transition: 0.2s;
        }

        button:hover {
            transform: translateY(-1px);
            opacity: 0.95;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            border-radius: 14px;
            background: #0f172a;
            border: 1px solid #334155;
        }

        .result.success {
            border-color: #22c55e;
        }

        .result.warning {
            border-color: #f59e0b;
        }

        .result.error {
            border-color: #ef4444;
        }

        .rank {
            font-size: 30px;
            font-weight: 900;
            margin: 10px 0;
        }

        .small {
            color: #94a3b8;
            font-size: 13px;
            line-height: 1.6;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 25px;
        }

        .feature {
            padding: 15px 10px;
            text-align: center;
            background: #111827;
            border-radius: 12px;
            color: #cbd5e1;
            font-size: 13px;
        }

        .feature strong {
            display: block;
            color: white;
            margin-bottom: 5px;
        }

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 12px;
            margin-top: 20px;
            line-height: 1.6;
        }

        @media (max-width: 550px) {
            .card {
                padding: 25px 20px;
            }

            .logo h1 {
                font-size: 38px;
            }

            .features {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <div class="logo">
        <h1>NOVA</h1>
        <p>VALORANT COMMUNITY</p>
    </div>

    <div class="card">

        <div class="title">발로란트 티어 인증</div>

        <div class="description">
            NOVA 서버에서 사용할 발로란트 티어 인증 페이지입니다.<br>
            라이엇 게임 계정 정보를 이용하여 플레이어 정보를 확인합니다.
        </div>

        <form method="POST">

            <label>라이엇 ID</label>

            <div class="riot-id">
                <input
                    type="text"
                    name="game_name"
                    placeholder="게임 이름"
                    required
                >

                <input
                    type="text"
                    name="tag_line"
                    placeholder="태그"
                    required
                >
            </div>

            <label>지역</label>

            <select name="region">
                <option value="kr">대한민국</option>
                <option value="na">북미</option>
                <option value="eu">유럽</option>
                <option value="ap">아시아 태평양</option>
            </select>

            <button type="submit">
                티어 인증 시작
            </button>

        </form>

        {% if result %}

        <div class="result {{ result_type }}">

            <strong>{{ result_title }}</strong>

            {% if rank %}
                <div class="rank">{{ rank }}</div>
            {% endif %}

            <div class="small">
                {{ result }}
            </div>

        </div>

        {% endif %}

        <div class="features">

            <div class="feature">
                <strong>Riot ID</strong>
                계정 확인
            </div>

            <div class="feature">
                <strong>VALORANT</strong>
                플레이어 정보
            </div>

            <div class="feature">
                <strong>NOVA</strong>
                서버 인증
            </div>

        </div>

    </div>

    <div class="footer">
        NOVA는 Riot Games와 별개의 커뮤니티입니다.<br>
        Riot Games 및 VALORANT 관련 상표와 콘텐츠의 권리는 해당 권리자에게 있습니다.
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    result_title = None
    result_type = "warning"
    rank = None

    if request.method == "POST":

        game_name = request.form.get("game_name", "").strip()
        tag_line = request.form.get("tag_line", "").strip()
        region = request.form.get("region", "kr")

        if not game_name or not tag_line:

            result_title = "입력 확인"
            result = "라이엇 ID와 태그를 모두 입력해주세요."
            result_type = "error"

        elif not RIOT_API_KEY:

            result_title = "티어 인증 프로토타입"
            result = (
                "현재 NOVA 티어 인증 시스템은 Riot Games API 연동을 위한 "
                "프로토타입으로 구성되어 있습니다. "
                "Riot API 인증 키가 서버 환경변수에 설정되면 실제 API 연동을 진행할 수 있습니다."
            )
            result_type = "warning"

        else:

            result_title = "인증 요청 접수"
            result = (
                f"{game_name}#{tag_line} 계정의 "
                f"VALORANT 정보를 확인하도록 요청했습니다. "
                f"선택 지역: {region.upper()}"
            )
            result_type = "success"

    return render_template_string(
        HTML,
        result=result,
        result_title=result_title,
        result_type=result_type,
        rank=rank
    )


@app.route("/health")
def health():
    return "NOVA OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
