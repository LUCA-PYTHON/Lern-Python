#Hier zeigen wir dir was du alles in anderen Ordnern zum laden der Ordner benötigst und machen unseren ersten Command.
#Erste Wichtige Info, in externen Ordnern fängt man mit einem command/event immer eine Zeile weiter rechts an bzw. auf der höhe von self.bot = bot.
#Zuerst importieren wir wieder die wichtigsten Dinge

import discord
from discord.ext import commands

#zunächst erstellen wir eine class, das sieht dann so aus:
class name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Dann starten wir hier mit unserem ersten command
    @commands.command()
    async def test(self, ctx):  #Command name und alles was du benötigst. In externen Datein benötigen wir immer self, ctx, ...
        await ctx.send("Erfolreich")    #Was macht der Command am ende? Er senden einen text nachdem man "!test" benutzt hat.

#Hier siehst du ein paar Beispiele zu unterschiedlichen commands:

    #Ban Command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send("Member banned")

    #Add Reaction
    @commands.command()
    async def reaction(self, ctx):
        await ctx.add_reaction("✅")

    #Remove Reaction
    @commands.command()
    async def reaction(self, ctx):
        await ctx.add_reaction("✅")
        await ctx.add_reaction("❌")
        await ctx.remove_reaction("✅")
    
    #Cooldown
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def reaction(self, ctx):
        await ctx.send("Cooldown")

def setup(bot): #Hier machen wir das Setup für die Datei
  bot.add_cog(name(bot))    #Hier benötigen wir den gleichen Name wir oben in der Class
