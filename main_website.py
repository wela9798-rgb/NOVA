from flask import Flask

app = Flask(**name**)

DISCORD_URL = "https://discord.gg/gHfjAj96r"

@app.route("/")
def home():
return """ <!DOCTYPE html> <html lang="ko"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>NOVA</title> <style>
body {
margin: 0;
background: #08080f;
color: white;
font-family: Arial, sans-serif;
text-align: center;
}

```
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 100px 20px;
        }

        h1 {
            font-size: 80px;
            letter-spacing: 10px;
            margin-bottom: 20px;
        }

        p {
            color: #b8b8c8;
            font-size: 20px;
            line-height: 1.7;
        }

        .buttons {
            margin-top: 40px;
        }

        a {
            display: inline-block;
            margin: 10px;
            padding: 16px 28px;
            border-radius: 14px;
            text-decoration: none;
            color: white;
            font-weight: bold;
            background: #665cff;
        }

        a.secondary {
            background: #191925;
            border: 1px solid #303044;
        }
    </style>
</head>

<body>

    <div class="container">

        <h1>NOVA</h1>

        <p>
            한국 VALORANT 커뮤니티 NOVA
        </p>

        <p>
            VALORANT 티어 인증과<br>
            다양한 커뮤니티 기능을 제공합니다.
        </p>

        <div class="buttons">

            <a href="https://discord.gg/gHfjAj96r"
               target="_blank">
                NOVA Discord 입장
            </a>

            <a class="secondary"
               href="https://nova-fo0d.onrender.com/riot-login">
                티어 인증
            </a>

        </div>

    </div>

</body>
</html>
"""
```

if **name** == "**main**":
app.run(
host="0.0.0.0",
port=10000
)
