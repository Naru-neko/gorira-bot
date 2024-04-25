import discord
import os
from dotenv import load_dotenv
from discord.commands import Option
from datetime import datetime, timezone


class AfkView(discord.ui.View): 
    def __init__(self, timeout=None):
        super().__init__(timeout=timeout)

    async def gen_afking(self, nickname, reason):
        embed = discord.Embed(title=nickname+' さんが離席中', description='理由：'+ reason)
        return embed

    async def send_afk_log(self, nickname, reason, channels):
        embed_log = discord.Embed(title=nickname+' さんが離席', description='理由：'+ reason, timestamp=datetime.now(timezone.utc))
        for channel in channels:
            if channel.name in channel_name:
                await channel.send(embed=embed_log)
                
    async def gen_error(self):
        embed = discord.Embed(title=':no_entry:既に離席中です:no_entry:', description='先に別の離席を完了させて下さい')
        return embed

    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='toilet',emoji='🚽')
    async def toilet(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = 'お手洗い:toilet:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='bath',emoji='🛀')
    async def bath(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = 'お風呂:bath:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='meal',emoji='🍚')
    async def meal(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = 'ご飯:rice:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='telephone',emoji='☎')
    async def telephone(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = '電話:telephone:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='toothbrush',emoji='🦷')
    async def toothbrush(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = '歯磨き:toothbrush:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='parent',emoji='👨')
    async def parent(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = '親フラ:man:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='thinking',emoji='💭')
    async def thinking(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = '考え事:thought_balloon:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))
        
    @discord.ui.button(style=discord.ButtonStyle.primary, custom_id='others',emoji='❓')
    async def others(self, button: discord.ui.Button, interaction: discord.Interaction):
        reason = 'その他:question:'
        if interaction.user.display_name in afk_user:
            await interaction.response.send_message(embed=await self.gen_error(), ephemeral=True)
            return
        else:
            afk_user.append(interaction.user.display_name)
            await self.send_afk_log(interaction.user.display_name, reason, interaction.guild.text_channels)
            await interaction.response.send_message(embed=await self.gen_afking(interaction.user.display_name, reason), 
                                                    view=CompView(timeout=None))

class CompView(discord.ui.View): 
    def __init__(self, timeout=None):
        super().__init__(timeout=timeout)
        
    async def send_back_log(self, nickname, channels):
        embed_log = discord.Embed(title=nickname+' さんが戻りました', timestamp=datetime.now(timezone.utc))
        for channel in channels:
            if channel.name in channel_name:
                await channel.send(embed=embed_log)
                
    @discord.ui.button(label='完了' ,style=discord.ButtonStyle.primary, custom_id='complete', emoji='✅')
    async def comp(self, button: discord.ui.Button, interaction: discord.Interaction):
        afk_user.remove(interaction.user.display_name)
        await self.send_back_log(interaction.user.display_name, interaction.guild.text_channels)
        await interaction.message.delete()


load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')

channel_name = 'bot'

afk_user = []

bot = discord.Bot(
        intents=discord.Intents.all(),
        activity=discord.Activity(type=discord.ActivityType.custom, state='有能ゴリラです'),
)


@bot.event
async def on_ready():
    print("Bot Booted.")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return


@bot.command(name="afk", description="離席報告用メッセージを投稿します")
async def afk(ctx: discord.ApplicationContext):
    embed = discord.Embed(title='離席報告',
                          description='''
[:toilet: お手洗い]　[:bath: お風呂]
[:rice: ご飯]　[:telephone: 電話]
[:tooth: 歯磨き]　[:man: 親フラ]
[:thought_balloon: 考え事]　[:question: その他]
'''
)
    view = AfkView(timeout=None)
    await ctx.interaction.response.send_message(embed=embed,
                                                view=view,
                                                )

'''
@bot.command(name="cmdtest", description="for debug")
async def test(ctx: discord.ApplicationContext):
    await ctx.respond(':toilet:')
'''
    
# BOT起動
bot.run(TOKEN)
