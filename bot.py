import os
import discord
from discord.ext import commands


# =========================================================
# NOVA DISCORD BOT
# VALORANT TIER VERIFICATION PROTOTYPE
# =========================================================


# =========================================================
# 환경변수
# =========================================================

TOKEN = os.getenv("DISCORD_TOKEN")

# NOVA Discord 서버 ID
GUILD_ID = 1541335745753653248

# NOVA 사이트
WEBSITE_URL = "https://nova-fo0d.onrender.com"


# =========================================================
# TOKEN 확인
# =========================================================

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN 환경변수가 설정되어 있지 않습니다."
    )


# =========================================================
# Discord Intents
# =========================================================

intents = discord.Intents.default()

intents.guilds = True
intents.members = True


# =========================================================
# Bot
# =========================================================

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================================================
# 티어 역할 설정
# =========================================================

TIER_ROLES = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Diamond",
    "Ascendant",
    "Immortal",
    "Radiant"
]


# =========================================================
# 티어 선택 메뉴
# =========================================================

class TierSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(
                label="Bronze",
                description="브론즈 티어 역할을 테스트합니다.",
                emoji="🥉"
            ),

            discord.SelectOption(
                label="Silver",
                description="실버 티어 역할을 테스트합니다.",
                emoji="🥈"
            ),

            discord.SelectOption(
                label="Gold",
                description="골드 티어 역할을 테스트합니다.",
                emoji="🥇"
            ),

            discord.SelectOption(
                label="Platinum",
                description="플래티넘 티어 역할을 테스트합니다.",
                emoji="💠"
            ),

            discord.SelectOption(
                label="Diamond",
                description="다이아몬드 티어 역할을 테스트합니다.",
                emoji="💎"
            ),

            discord.SelectOption(
                label="Ascendant",
                description="어센던트 티어 역할을 테스트합니다.",
                emoji="🟢"
            ),

            discord.SelectOption(
                label="Immortal",
                description="불멸 티어 역할을 테스트합니다.",
                emoji="🔥"
            ),

            discord.SelectOption(
                label="Radiant",
                description="레디언트 티어 역할을 테스트합니다.",
                emoji="👑"
            )
        ]

        super().__init__(
            placeholder="인증할 티어를 선택하세요.",
            min_values=1,
            max_values=1,
            options=options
        )


    async def callback(
        self,
        interaction: discord.Interaction
    ):

        selected_tier = self.values[0]

        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message(
                "❌ 서버에서만 사용할 수 있습니다.",
                ephemeral=True
            )
            return


        # -------------------------------------------------
        # 선택한 역할 찾기
        # -------------------------------------------------

        selected_role = discord.utils.get(
            guild.roles,
            name=selected_tier
        )


        if selected_role is None:

            await interaction.response.send_message(
                (
                    f"❌ `{selected_tier}` 역할을 찾을 수 없습니다.\n\n"
                    f"서버에 `{selected_tier}` 역할을 만들어주세요."
                ),
                ephemeral=True
            )

            return


        # -------------------------------------------------
        # 봇 역할 위치 확인
        # -------------------------------------------------

        bot_member = guild.me

        if bot_member is None:

            await interaction.response.send_message(
                "❌ 봇 정보를 확인할 수 없습니다.",
                ephemeral=True
            )

            return


        if selected_role >= bot_member.top_role:

            await interaction.response.send_message(
                (
                    "❌ 이 역할을 지급할 수 없습니다.\n\n"
                    "Discord 서버 설정에서 **NOVA 봇 역할을 "
                    "티어 역할보다 위로** 올려주세요."
                ),
                ephemeral=True
            )

            return


        # -------------------------------------------------
        # 기존 티어 역할 제거
        # -------------------------------------------------

        roles_to_remove = []

        for tier_name in TIER_ROLES:

            role = discord.utils.get(
                guild.roles,
                name=tier_name
            )

            if role is not None and role in interaction.user.roles:
                roles_to_remove.append(role)


        try:

            if roles_to_remove:

                await interaction.user.remove_roles(
                    *roles_to_remove,
                    reason="NOVA 티어 역할 자동 변경"
                )


            # -------------------------------------------------
            # 새로운 티어 역할 지급
            # -------------------------------------------------

            await interaction.user.add_roles(
                selected_role,
                reason="NOVA 티어 역할 자동 지급"
            )


        except discord.Forbidden:

            await interaction.response.send_message(
                (
                    "❌ 역할을 지급할 권한이 없습니다.\n\n"
                    "NOVA 봇의 역할을 티어 역할보다 위로 올려주세요."
                ),
                ephemeral=True
            )

            return


        except Exception as e:

            print("Role Assignment Error:")
            print(e)

            await interaction.response.send_message(
                "❌ 역할 지급 중 오류가 발생했습니다.",
                ephemeral=True
            )

            return


        # -------------------------------------------------
        # 완료 메시지
        # -------------------------------------------------

        embed = discord.Embed(
            title="✅ NOVA 티어 역할 지급 완료",
            description=(
                f"현재 선택된 테스트 티어는\n\n"
                f"## {selected_tier}\n\n"
                f"역할이 자동으로 지급되었습니다."
            ),
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="⚠️ 테스트 기능",
            value=(
                "현재는 Riot API 승인 전이므로 "
                "실제 VALORANT 티어를 확인한 결과가 아닙니다."
            ),
            inline=False
        )

        embed.set_footer(
            text="NOVA Tier Verification Prototype"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


# =========================================================
# 티어 선택 View
# =========================================================

class TierView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=120)

        self.add_item(
            TierSelect()
        )


# =========================================================
# Bot 시작
# =========================================================

@bot.event
async def on_ready():

    print("----------------------------------------")
    print("NOVA Bot Online")
    print(f"Bot Name : {bot.user}")
    print(f"Bot ID   : {bot.user.id}")
    print("----------------------------------------")

    try:

        guild = discord.Object(
            id=GUILD_ID
        )

        # NOVA 서버에 Slash Command 동기화
        synced = await bot.tree.sync(
            guild=guild
        )

        print(
            f"Slash Commands Synced : {len(synced)}"
        )

        for command in synced:

            print(
                f" - /{command.name}"
            )

    except Exception as e:

        print("Slash Command Sync Error:")
        print(e)


# =========================================================
# /티어인증
# =========================================================

@bot.tree.command(
    name="티어인증",
    description="NOVA에서 VALORANT 티어 인증을 진행합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def tier_verify(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="NOVA  |  VALORANT 티어 인증",
        description=(
            "NOVA 서버에서 VALORANT 티어를 인증하려면\n"
            "아래 **Riot 계정 인증하기** 버튼을 눌러주세요."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🔐 인증 방식",
        value="Riot Sign On (RSO)",
        inline=False
    )

    embed.add_field(
        name="🎮 게임",
        value="VALORANT",
        inline=True
    )

    embed.add_field(
        name="🛡️ 개인정보",
        value=(
            "Riot 계정 인증 과정에서 사용자의 동의가 필요합니다."
        ),
        inline=True
    )

    embed.set_footer(
        text="NOVA Tier Verification"
    )


    # -----------------------------------------------------
    # Riot 인증 버튼
    # -----------------------------------------------------

    view = discord.ui.View()

    button = discord.ui.Button(
        label="Riot 계정 인증하기",
        style=discord.ButtonStyle.link,
        url=f"{WEBSITE_URL}/riot-login"
    )

    view.add_item(button)


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
    description="NOVA 티어 역할 자동 지급을 테스트합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def tier_test(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🎮 NOVA | 티어 역할 테스트",
        description=(
            "아래 메뉴에서 티어를 선택해주세요.\n\n"
            "선택한 티어 역할이 자동으로 지급됩니다."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="⚠️ 주의",
        value=(
            "이 기능은 Riot API 승인 전 테스트용입니다.\n"
            "실제 VALORANT 티어를 조회하는 기능이 아닙니다."
        ),
        inline=False
    )

    embed.set_footer(
        text="NOVA Tier Verification Prototype"
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
    description="NOVA 봇 정보를 확인합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def nova_info(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🌌 NOVA",
        description=(
            "한국 VALORANT 커뮤니티 NOVA의 전용 봇입니다.\n\n"
            "VALORANT 티어 인증 및 커뮤니티 기능을 제공합니다."
        ),
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 게임",
        value="VALORANT",
        inline=True
    )

    embed.add_field(
        name="🔐 티어 인증",
        value="/티어인증",
        inline=True
    )

    embed.add_field(
        name="🧪 역할 테스트",
        value="/티어테스트",
        inline=True
    )

    embed.add_field(
        name="🌐 Website",
        value=WEBSITE_URL,
        inline=False
    )

    embed.set_footer(
        text="NOVA Community"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================================================
# /사이트
# =========================================================

@bot.tree.command(
    name="사이트",
    description="NOVA 인증 사이트 링크를 표시합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def website(
    interaction: discord.Interaction
):

    view = discord.ui.View()

    button = discord.ui.Button(
        label="NOVA 인증 사이트",
        style=discord.ButtonStyle.link,
        url=WEBSITE_URL
    )

    view.add_item(button)

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
    description="NOVA 봇의 명령어를 확인합니다.",
    guild=discord.Object(id=GUILD_ID)
)
async def help_command(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="🌌 NOVA Bot",
        description="사용 가능한 명령어입니다.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎮 /티어인증",
        value="VALORANT 티어 인증을 시작합니다.",
        inline=False
    )

    embed.add_field(
        name="🧪 /티어테스트",
        value="티어 역할 자동 지급을 테스트합니다.",
        inline=False
    )

    embed.add_field(
        name="🌐 /사이트",
        value="NOVA 인증 사이트를 확인합니다.",
        inline=False
    )

    embed.add_field(
        name="ℹ️ /노바",
        value="NOVA 봇 정보를 확인합니다.",
        inline=False
    )

    embed.add_field(
        name="❓ /도움말",
        value="명령어 목록을 확인합니다.",
        inline=False
    )

    embed.set_footer(
        text="NOVA Community"
    )

    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )


# =========================================================
# 봇 실행
# =========================================================

bot.run(TOKEN)

