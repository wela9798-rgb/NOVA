import discord
from discord import app_commands
from discord.ext import commands

SERVER_ID = 1541335745753653248

intents = discord.Intents.default()


class NOVA(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        server = discord.Object(id=SERVER_ID)

        self.tree.copy_global_to(guild=server)
        await self.tree.sync(guild=server)

        print("서버 전용 명령어 동기화 완료!")


bot = NOVA()


# ========================================
# 메인 메뉴
# ========================================

class MainMenu(discord.ui.View):

    @discord.ui.button(
        label="서버 안내",
        emoji="📚",
        style=discord.ButtonStyle.primary
    )
    async def server_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "📚 **서버 안내**\n\n"
            "NOVA 서버에 오신 것을 환영합니다! 🤖\n\n"
            "서버 규칙과 이용 방법을 확인해주세요.",
            ephemeral=True
        )

    @discord.ui.button(
        label="유저 정보",
        emoji="👤",
        style=discord.ButtonStyle.secondary
    )
    async def user_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        user = interaction.user

        await interaction.response.send_message(
            f"👤 **유저 정보**\n\n"
            f"닉네임: {user.display_name}\n"
            f"아이디: {user.id}",
            ephemeral=True
        )

    @discord.ui.button(
        label="게임 기능",
        emoji="🎮",
        style=discord.ButtonStyle.success
    )
    async def game_info(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "🎮 **게임 기능**\n\n"
            "VALORANT 관련 기능을 준비하고 있어요!",
            ephemeral=True
        )

    @discord.ui.button(
        label="서버 설정",
        emoji="⚙️",
        style=discord.ButtonStyle.danger
    )
    async def server_settings(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ 관리자만 사용할 수 있는 기능입니다.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "⚙️ **서버 설정**\n\n"
            "관리자 전용 기능을 준비하고 있어요!",
            ephemeral=True
        )


# ========================================
# /메뉴
# ========================================

@bot.tree.command(
    name="메뉴",
    description="NOVA 메인 메뉴를 엽니다."
)
async def menu(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🤖 NOVA",
        description=(
            "안녕하세요! **NOVA**입니다.\n\n"
            "아래 메뉴에서 원하는 기능을 선택해주세요."
        ),
        color=0x5865F2
    )

    embed.add_field(
        name="📚 서버 안내",
        value="서버 이용 방법을 확인해요.",
        inline=True
    )

    embed.add_field(
        name="👤 유저 정보",
        value="내 디스코드 정보를 확인해요.",
        inline=True
    )

    embed.add_field(
        name="🎮 게임 기능",
        value="VALORANT 관련 기능을 이용해요.",
        inline=True
    )

    embed.add_field(
        name="⚙️ 서버 설정",
        value="서버 관리 기능이에요.",
        inline=True
    )

    embed.set_footer(
        text="NOVA • 함께 만들어가는 서버"
    )

    await interaction.response.send_message(
        embed=embed,
        view=MainMenu()
    )


# ========================================
# /공지
# ========================================

@bot.tree.command(
    name="공지",
    description="사진과 함께 예쁜 공지를 작성합니다."
)
@app_commands.describe(
    제목="공지 제목을 입력해주세요.",
    내용="공지 내용을 입력해주세요.",
    사진="공지에 넣을 사진을 첨부해주세요."
)
@app_commands.default_permissions(administrator=True)
async def notice(
    interaction: discord.Interaction,
    제목: str,
    내용: str,
    사진: discord.Attachment = None
):

    embed = discord.Embed(
        title="📢 NOVA 서버 공지",
        description=f"## ✨ {제목}\n\n{내용}",
        color=0x5865F2,
        timestamp=discord.utils.utcnow()
    )

    if 사진:
        embed.set_image(url=사진.url)

    embed.set_author(
        name=interaction.user.display_name,
        icon_url=interaction.user.display_avatar.url
    )

    embed.add_field(
        name="📌 NOVA 안내",
        value="서버 이용에 참고해주세요!",
        inline=False
    )

    embed.add_field(
        name="👤 작성자",
        value=interaction.user.mention,
        inline=True
    )

    embed.add_field(
        name="📅 작성일",
        value=f"<t:{int(discord.utils.utcnow().timestamp())}:D>",
        inline=True
    )

    embed.set_footer(
        text="NOVA • 함께 만들어가는 서버 🤖"
    )

    await interaction.response.send_message(
        embed=embed
    )


# ========================================
# /전적
# ========================================

@bot.tree.command(
    name="전적",
    description="VALORANT 전적을 조회합니다."
)
@app_commands.describe(
    닉네임="VALORANT 닉네임을 입력해주세요.",
    태그="VALORANT 태그를 입력해주세요."
)
async def valorant_stats(
    interaction: discord.Interaction,
    닉네임: str,
    태그: str
):

    embed = discord.Embed(
        title="🎮 VALORANT 전적",
        description=(
            f"**{닉네임}#{태그}**\n\n"
            "⏳ 현재 전적 조회 시스템을 준비하고 있습니다."
        ),
        color=0x5865F2
    )

    embed.add_field(
        name="🏆 현재 티어",
        value="준비 중",
        inline=True
    )

    embed.add_field(
        name="📊 승률",
        value="준비 중",
        inline=True
    )

    embed.add_field(
        name="⚔️ 최근 경기",
        value="준비 중",
        inline=True
    )

    embed.set_footer(
        text="NOVA • VALORANT"
    )

    await interaction.response.send_message(
        embed=embed
    )


# ========================================
# 봇 시작
# ========================================

bot.run()
