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
                background: #0f1117;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 100px 20px;
            }

            h1 {
                font-size: 48px;
                margin-bottom: 10px;
            }

            p {
                color: #aaa;
                font-size: 18px;
            }

            .button {
                display: inline-block;
                margin-top: 30px;
                padding: 14px 28px;
                background: #5865F2;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <h1>🌌 NOVA</h1>
        <p>VALORANT Community</p>
        <p>한국 발로란트 커뮤니티 NOVA</p>

        <a class="button"
           href="https://discord.gg/gHfjAj96r">
            NOVA Discord 서버 입장
        </a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
