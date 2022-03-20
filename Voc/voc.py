import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from os import getenv
load_dotenv()

intents = discord.Intents.default() 
intents.members = True

class Voc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

#    def is_admin_check(ctx):
#        role = discord.utils.get(ctx.bot.get_guild(907734650527571978).roles, name='✔︎')
#        gerants = get(ctx.guild.roles, id = 913205391763066941)     #admin
#        return role in ctx.author.roles


#    def is_admin_check(ctx):
#        return ctx.author.id == 913205391763066941
    
#    def is_admin():
#        return commands.check(is_admin_check)

#    def is_gold_check(ctx):
#        return ctx.author.id == 907753246775455824

#    def is_gold():
#        return commands.check(is_gold_check)

#    def is_gerant_check(ctx):
#        gerant = discord.utils.get(ctx.bot.get_guild(907734650527571978).roles, name='| 𝗚𝗘́𝗥𝗔𝗡𝗧𝗦') 
#        return gerant in ctx.author.roles


    @commands.command()
    @commands.has_any_role(913205391763066941, 955145240262606868)
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.send('Joined !')
        await channel.connect()

    @commands.command()
    @commands.has_any_role(913205391763066941, 955145240262606868)
    async def leave(self, ctx):
        await ctx.send('Leaved !')
        await ctx.voice_client.disconnect()

def setup(bot: commands.Bot):
    bot.add_cog(Voc(bot))