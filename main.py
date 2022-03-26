#Hier zeige ich dir heute wie man seinen ersten Discord Python bot mit pycord erstellt.
#Alles was nicht hier in dieser Date zu finden ist, findest du in den anderen Ordnern
#Als erst nutzt du diesen Befehl in der Konsole "pip install py-cord"
#Du musst natürlich auch einen Bot im Discord Developer Portal erstellen


#Erster Schritt
#Importier alle Dinge die du benötigst
import discord
from discord.ext import commands
import os


#Als zweiten Schritt legen wir das Prefix fest und geben an welche Intens wir benötigen
bot = commands.Bot(commands.when_mentioned_or("!")  #Hier gibst du dein Wunsch Prefix an
                   ,intents=discord.Intents.all())  #Hier gibst du an welche Intens du möchtest -> Hier in diesem Beispiel alle
bot.remove_command("help")  #Hiermit entfernst du den Standart Help Command von Discord


#Als nächstest machen wir ein Event was reagiert wenn der Bot online ist.
@bot.event
async def on_ready():

    #Hiermit Geben wir dem bot einen Status deiner Wahl
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, #Hier kannst du den Type angeben den du möchtest (watching, playing oder listening)
                             name=f"Spielt mit {bot.user.name}"),   #Hier kannst du deinen Wunschstatus angeben
                             status=discord.Status.online)  #Hier kannst du angeben ob der Bot online, abwesend, dnd oder offline ist


#Zu guter Letzte siehst du hier, wie man Ordner laden kann.
for filename in os.listdir('./Beispiele'):   #hier gibst du an wie der ordner heißen soll.
    if filename.endswith('.py'):    #Hier checkst du ob es eine python Datei ist
        bot.load_extension(f'Beispiele.{filename[:-3]}') #Und hiermit lädst du den Ordner

bot.run("token")    #Hiermit wird der bot gesartet. "token" ersetzt du mit dem Bot Token.

# Wenn du das alles gemacht hast, ist dein Bot online und er hat einen Status
