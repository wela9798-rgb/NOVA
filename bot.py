import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 1541335745753653248
WEBSITE_URL = "https://nova-fo0d.onrender.com"

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN 환경변수가 설정되어 있지 않습니다.")


intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================================================
# 티어 설정
# =========================================================

TIERS = {
    "아이언": "⚙️",
    "브론즈": "🥉",
    "실버": "🥈",
    "골드": "🥇",
    "플래티넘": "💠",
    "다이아몬드": "💎",
    "초월자": "🟢",
    "불멸": "🔥",
    "레디언트": "👑"
}


# =========================================================
# 역할 찾기
# =========================================================

def find_tier_role(guild, tier_name):

    for role in guild.roles:

        if tier_name in role.name:
            return role

    return None


def find_old_tier_roles(member):

    roles = []

    for role in member.roles:

        for tier_name in TIERS:

            if tier_name in role.name:
                roles.append(role)
                break

    return roles


# =========================================================
# 티어 선택
# =========================================================

class TierSelect(discord.ui.Select):

    def __init__(self):

        options = []

        for tier, emoji in TIERS.items():

            options.append(
                discord.SelectOption(
                    label=tier,
                    description=f"{tier} 역할을 테스트합니다.",
                    emoji=emoji,
                    value=tier
                )
            )

        super().__init__(
            placeholder="티어를 선택하세요.",
            options=options,
            min_values=1,
            max_values=1
        )


    async def callback(self, interaction):

        tier = self.values[0]

        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message(
                "❌ 서버에서만 사용할 수 있습니다.",
                ephemeral=True
            )
            return


        # 선택한 역할 찾기

        role = find_tier_role(
            guild,
            tier
        )


        if role is None:

            await interaction.response.send_message(
                f"❌ `{tier}` 역할을 찾을 수 없습니다.",
                ephemeral=True
            )

            return


        # 봇 역할보다 높은 역할인지 확인

        if guild.me and role >= guild.me.top_role:

            await interaction.response.send_message(
                (
                    "❌ 이 역할을 지급할 수 없습니다.\n\n"
                    "서버 설정 → 역할에서\n"
                    "**NOVA 봇 역할을 티어 역할보다 위로** 올려주세요."
                ),
                ephemeral=True
            )

            return


        try:

            # 기존 티어 역할 제거

            old_roles = find_old_tier_roles(
                interaction.user
            )

            if old_roles:

                await interaction.user.remove_roles(
                    *old_roles,
                    reason="NOVA 티어 역할 변경"
                )


            # 새로운 역할 지급

            await interaction.user.add_roles(
                role,
                reason="NOVA 티어 테스트"
            )


        except discord.Forbidden:

            await interaction.response.send_message(
                "❌ 봇에게 역할 관리 권한이 없습니다.",
                ephemeral=True
            )

            return


        embed = discord.Embed(
            title="✅ 티어 역할 지급 완료",
            description=(
                f"{TIERS[tier]} **{tier}**\n\n"
                f"`{role.name}` 역할이 지급되었습니다."
            ),
            color=discord.Color.blurple()
        )

        embed.set_footer(
            text="NOVA Tier Verification Prototype"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


# =========================================================
# 티어 View
# =========================================================

class TierView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=120)

        self.add_item(
            TierSelect()
        )


# =========================================================
# READY
# =========================================================

@bot.event
async def on_ready():

    print("========================================")
    print("NOVA Bot Online")
    print(f"Bot : {bot.user}")
    print("========================================")

    try:

        guild = discord.Object(
            id=GUILD_ID
        )

        synced = await bot.tree.sync(
            guild=guild
        )

        print(
            f"서버 전용 명령어 동기화 완료! ({len(synced)}개)"
        )

        for command in synced:

            print(
                f" - /{command.name}"
            )

    except Exception as e:

        print("명령어 동기화 오류:")
        print(e)


# =========================================================
# /티어인증
# =========================================================

@bot.tree.command(
    name="티어인증",
    description="NOVA VALORANT 티어 인증",
    guild=discord.Object(id=GUILD_ID)
)
async def tier_verify(interaction):

    embed = discord.Embed(
        title="NOVA | VALORANT 티어 인증",
        description=(
            "Riot 계정 인증을 시작하려면\n"
            "아래 버튼을 눌러주세요."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🔐 인증 방식",
        value="Riot Sign On (RSO)",
        inline=False
    )

    view = discord.ui.View()

    view.add_item(
        discord.ui.Button(
            label="Riot 계정 인증하기",
            style=discord.ButtonStyle.link,
            url=f"{WEBSITE_URL}/riot-login"
        )
    )

    await interaction.response.send_message(
        embed=embed,
        view=view,
        ephemeral=True
    )


# =========================================================
# /티어테스트
# =========================================================

@bot.tree.command(
    name="티어테스트",
    description="티어 역할 자동 지급 테스트",
    guild=discord.Object(id=GUILD_ID)
)
async def tier_test(interaction):

    embed = discord.Embed(
        title="🎮 NOVA | 티어 역할 테스트",
        description=(
            "아래에서 티어를 선택해주세요.\n\n"
            "선택한 티어의 Discord 역할이 자동으로 지급됩니다."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="⚠️ 테스트 기능",
        value=(
            "Riot API 승인 전 테스트 기능입니다.\n"
            "실제 Riot 티어를 조회하지 않습니다."
        ),
        inline=False
    )

    await interaction.response.send_message(
        embed=embed,
        view=TierView(),
        ephemeral=True
    )


# =========================================================
# /노바
# =========================================================

@bot.tree.command(
    name="노바",
    description="NOVA 봇 정보",
    guild=discord.Object(id=GUILD_ID)
)
async def nova(interaction):

    embed = discord.Embed(
        title="🌌 NOVA",
        description=(
            "한국 VALORANT 커뮤니티 NOVA 전용 봇입니다."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 티어 인증",
        value="/티어인증",
        inline=True
    )

    embed.add_field(
        name="🧪 티어 테스트",
        value="/티어테스트",
        inline=True
    )

    embed.add_field(
        name="🌐 사이트",
        value=WEBSITE_URL,
        inline=False
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /사이트
# =========================================================

@bot.tree.command(
    name="사이트",
    description="NOVA 인증 사이트",
    guild=discord.Object(id=GUILD_ID)
)
async def site(interaction):

    view = discord.ui.View()

    view.add_item(
        discord.ui.Button(
            label="NOVA 인증 사이트",
            style=discord.ButtonStyle.link,
            url=WEBSITE_URL
        )
    )

    await interaction.response.send_message(
        "🌐 **NOVA 인증 사이트**",
        view=view,
        ephemeral=True
    )


# =========================================================
# /도움말
# =========================================================

@bot.tree.command(
    name="도움말",
    description="NOVA 봇 도움말",
    guild=discord.Object(id=GUILD_ID)
)
async def help_command(interaction):

    embed = discord.Embed(
        title="🌌 NOVA Bot",
        description="사용 가능한 명령어입니다.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 /티어인증",
        value="VALORANT 티어 인증",
        inline=False
    )

    embed.add_field(
        name="🧪 /티어테스트",
        value="티어 역할 지급 테스트",
        inline=False
    )

    embed.add_field(
        name="🌐 /사이트",
        value="NOVA 사이트",
        inline=False
    )

    embed.add_field(
        name="ℹ️ /노바",
        value="NOVA 봇 정보",
        inline=False
    )

    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )


# =========================================================
# 실행
# =========================================================

bot.run(TOKEN)

