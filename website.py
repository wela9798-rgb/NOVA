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

        embed = discord.Embed(
            title="📚 NOVA 서버 안내",
            description=(
                "NOVA에 오신 것을 환영합니다! 🤖\n\n"
                "게임과 친목을 함께 즐길 수 있는 서버입니다.\n"
                "아래 내용을 확인하고 서버를 이용해주세요."
            ),
            color=0x5865F2
        )

        embed.add_field(
            name="🔞 이용 연령",
            value=(
                "• **만 14세 이상** 이용 가능합니다.\n"
                "• 연령 기준에 맞지 않는 경우 이용이 제한될 수 있습니다."
            ),
            inline=False
        )

        embed.add_field(
            name="📌 서버 이용",
            value=(
                "• 서로 존중하며 대화해주세요.\n"
                "• 욕설 및 과도한 분쟁은 자제해주세요.\n"
                "• 다른 이용자에게 불쾌감을 주는 행동은 금지됩니다.\n"
                "• 서버 규칙을 꼭 확인해주세요."
            ),
            inline=False
        )

        embed.add_field(
            name="🎮 주요 게임",
            value=(
                "• VALORANT\n"
                "• Minecraft\n"
                "• 기타 종합게임"
            ),
            inline=True
        )

        embed.add_field(
            name="🆘 문의",
            value=(
                "서버 이용 중 문제가 발생했다면\n"
                "운영진에게 문의해주세요."
            ),
            inline=True
        )

        embed.set_footer(
            text="NOVA • 함께 만들어가는 서버 🤖"
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )
