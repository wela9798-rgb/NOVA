```python
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NOVA | VALORANT Community</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background:
        radial-gradient(circle at top, #202040 0%, #0b0b16 45%, #050509 100%);
    color: white;
    min-height: 100vh;
}

.container {
    width: min(1100px, 92%);
    margin: auto;
}

nav {
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: 4px;
}

.nav-button {
    text-decoration: none;
    color: white;
    padding: 12px 20px;
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 12px;
    background: rgba(255,255,255,.06);
}

.hero {
    text-align: center;
    padding: 100px 0 80px;
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(120,100,255,.15);
    border: 1px solid rgba(120,100,255,.3);
    color: #b9adff;
    font-size: 14px;
    margin-bottom: 24px;
}

h1 {
    font-size: clamp(48px, 8vw, 88px);
    margin: 0;
    letter-spacing: 8px;
}

.hero p {
    color: #b8b8c8;
    font-size: 19px;
    line-height: 1.7;
    max-width: 650px;
    margin: 25px auto 35px;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
}

.button {
    text-decoration: none;
    color: white;
    padding: 15px 28px;
    border-radius: 14px;
    font-weight: bold;
    background: #665cff;
}

.button.secondary {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.15);
}

.features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    padding-bottom: 80px;
}

.card {
    padding: 28px;
    border-radius: 20px;
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,255,255,.09);
}

.icon {
    font-size: 32px;
}

.card h2 {
    margin-bottom: 10px;
}

.card p {
    color: #aaaabb;
    line-height: 1.6;
}

footer {
    text-align: center;
    padding: 30px;
    color: #777788;
    border-top: 1px solid rgba(255,255,255,.08);
}

@media (max-width: 800px) {

    .features {
        grid-template-columns: 1fr;
    }

    .hero {
        padding-top: 70px;
    }

}

</style>

</head>

<body>

<div class="container">

<nav>

<div class="logo">
NOVA
</div>

<a
class="nav-button"
href="https://discord.gg/DpDuPK7b4
target="_blank">
Discord
</a>

</nav>


<section class="hero">

<div class="badge">
KOREAN VALORANT COMMUNITY
</div>

<h1>NOVA</h1>

<p>
VALORANT를 좋아하는 사람들이 함께하는
한국 커뮤니티입니다.<br>
친목부터 파티 모집, 내전, 티어 인증까지
NOVA에서 함께하세요.
</p>

<div class="buttons">

<a
class="button"
href="https://discord.gg/여기에초대코드"
target="_blank">
NOVA Discord 입장
</a>

<a
class="button secondary"
href="https://nova-fo0d.onrender.com/riot-login">
티어 인증
</a>

</div>

</section>


<section class="features">

<div class="card">

<div class="icon">🎮</div>

<h2>VALORANT Community</h2>

<p>
VALORANT를 함께 즐기고
파티를 모집하며 새로운 사람들과
게임을 즐길 수 있는 커뮤니티입니다.
</p>

</div>


<div class="card">

<div class="icon">🏆</div>

<h2>Tier Verification</h2>

<p>
Riot 계정 인증을 통해
VALORANT 경쟁전 티어를 인증하는
시스템을 준비하고 있습니다.
</p>

</div>


<div class="card">

<div class="icon">🤖</div>

<h2>NOVA Bot</h2>

<p>
NOVA Discord 서버에서
티어 인증과 다양한 커뮤니티 기능을
지원하는 전용 봇입니다.
</p>

</div>

</section>

</div>


<footer>

NOVA Community · VALORANT

</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
```
