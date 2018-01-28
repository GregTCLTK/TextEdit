import sys
import discord
import time

import KEYS

class MyClient(discord.Client):
	async def on_ready(self):
		print("Erfolgreich eingeloggt!")
		print("Der Bot ist auf folgeneden Servern:")
		insguilds = 0
		for guild in client.guilds:
			print("%s - %s" %(guild.name, guild.id))
			insguilds = insguilds + 1
		print("Server: " + str(insguilds))

		#Game Precense
		game = discord.Game(name="-help")
		await client.change_presence(status=discord.Status.online, game=game)

	async def on_message(self, message):
		if message.content.startswith(KEYS.PREFIX):
			invoke = message.content[1:].split(" ")[0]
			args = message.content.split(" ")[1:]
			if invoke == "ping":
				await message.channel.send(content="Pong!")

			if invoke == "clear" and message.author.guild_permissions.administrator == True:

				try:
					ammount = int(args[0])+1 if len(args) > 0 else 1
				except:
					await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="UNGÜLTIGER WERT"))
					return
				async for message in message.channel.history(limit=ammount):
					try:
						await message.delete()
					except discord.error.Forbidden:
						await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="OH es sieht so aus als hättest du keine Permissions um nachrichten zu löschen. Sorry"))
						break

			elif invoke=="clear" or invoke=="message" and message.author.guild_permissions.administrator == False:
				notification = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Diesen Command dürfen leider nur Administratoren nutzen, sorry").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))
				await asyncio.sleep(20)
				await notification.delete()
			if invoke == "help":
				await message.channel.send(content="Ich habe die eine Liste mit allen Commands per DM geschickt. Wenn du nicht bekommen hast überprüfe bitte ob du es aktiviert hast das du Direktnachrichten von Servermitgliedern aktiviert hast. Du findest Hilfe auch auf: https://thebotdev.de/work01.html  https://i.imgur.com/QFtGBSG.png")
				try;
					await message.author.send(embed=discord.Embed(description="***Support***\n**Prefix:**\n-[command]\n**Checkt ob der Bot online ist**\n-ping \nzeigt das der Bot online ist und die nachricht gelsesen hat\n*Nachricht löschen**\n-clear [Anzahl der nachrichten die gelöscht werden sollen]\nLöscht so viele Nachrichten wie nach dem Command angegeben sind\n**Erstellen einer Nachricht**\n-message\nDort ist ein Wizzard der dir dabei helfen wird die nachricht so zu erstellen wie du willst.\n**Bot Info**\n-info\n-----------\nFormatierung der Nachricht: *https://thebotdev.de/Markdown.html*\n"))
				except discord.error.Forbidden:
					await message.channel.send(content="Error! Ich konnte dir leider keine nachricht per DM schicken deswegen ist jetzt hier die Hilfe Liste für dich :)")
					await message.author.send(embed=discord.Embed(description="***Support***\n**Prefix:**\n-[command]\n**Checkt ob der Bot online ist**\n-ping \nzeigt das der Bot online ist und die nachricht gelsesen hat\n*Nachricht löschen**\n-clear [Anzahl der nachrichten die gelöscht werden sollen]\nLöscht so viele Nachrichten wie nach dem Command angegeben sind\n**Erstellen einer Nachricht**\n-message\nDort ist ein Wizzard der dir dabei helfen wird die nachricht so zu erstellen wie du willst.\n**Bot Info**\n-info\n-----------\nFormatierung der Nachricht: *https://thebotdev.de/Markdown.html*\n"))
			if invoke == "info":
				await message.channel.send(embed=discord.Embed(color=discord.Color.purple(), description="**Bot von *BaseChip*\n**Projek:** *TheBotDev*\n**Support:** *[BaseChip's Support Server](https://discord.gg/HD7x2vx)*\n**Bot Invite:** *[INVITE BaseChip's Bot](https://discordapp.com/api/oauth2/authorize?client_id=384757717346025472&permissions=67577856&scope=bot)*\n*Dies ist ein Fork von GitHub von dem Bot von BaseChip*"))
			if invoke == "message" and message.author.guild_permissions.administrator == True:
				setup = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(), description="OK! Das Setup um die nachricht zu erstellen wurde gestartet. Bitte sende nun die Farbe die die Embed Message am Rand haben soll (Grün/Rot/Magenta/Blau/Gold) und mache dir keine Sorgen über die nachricht die während der Installation geschrieben werden ich werde diese spter löschen :)"))

				def checkmsg(m):
					if m.author.id == message.author.id and m.channel.id == message.channel.id:
						return m

				msgwaitfor = await client.wait_for("message", check=checkmsg, timeout=None)
				if msgwaitfor.content != " ":

					if msgwaitfor.content == "grün":
						print("Farbe: Grün")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description="Du hast die Farbe grün ausgewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nachricht grün gefärbt. Bitte gebe jetzt den Text ein der in der nachricht stehen soll!"))
						def checkg(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkg, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))

					elif msgwaitfor.content == "rot":
						print("Color: Red")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Du hast die Farbe rot ausgewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nachricht rot gefärbt. Bitte gebe jetzt den Text ein der in der nachricht stehen soll!"))
						def checkr(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=None, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))




					elif msgwaitfor.content == "blau":
						print("Color: Blue")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description="Du hast die Farbe blau ausgewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nachricht blau gefärbt. Bitte gebe jetzt den Text ein der in der nachricht stehen soll!"))
						def checkb(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkb, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))



					elif msgwaitfor.content == "magenta":
						print("Color: Magenta")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(),description="Du hast die Farbe magenta ausgewählt. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nachricht magenta gefärbt. Bitte gebe jetzt den Text ein der in der nachricht stehen soll!"))

						def checkm(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkm, timeout=None)
						text = await message.channel.send(
							embed=discord.Embed(color=discord.Color.magenta(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))


					elif msgwaitfor.content == "gold":
						print("Color: Gold")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.gold(),description="Du hast die Farbe gold ausgewählt aber eigentlich sieht es eher wie gelb aus. Als Beispiel wie die nachricht später aussehen wird habe ich den Rand dieser Nachricht gold gefärbt. Bitte gebe jetzt den Text ein der in der nachricht stehen soll!"))

						def checkgold(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m

						msg2 = await client.wait_for("message", check=checkgold, timeout=None)
						text = await message.channel.send(
							embed=discord.Embed(color=discord.Color.gold(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh es sieht so aus als müsste ich mich selbs korrigieren. Ich habe gesagt das ich alle nachrichten des Setup's löschen werde aber wie es aussieht habe ich nicht die Permission's dazu die Permission heisst (Nachrichten verwalten)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))

					else:
						idktc = await message.channel.send(content="Sorry aber die Farbe: "+msgwaitfor.content+" kenne ich nicht!")
						await asyncio.sleep(20)
						await idktc.delete()




client= MyClient()
client.run(KEYS.TOKEN)
