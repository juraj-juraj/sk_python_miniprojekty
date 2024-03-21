# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    print(f"Dostal spravu od: {message.author.name} a obsah spravy: {message.content}")

    # Tato podmienka kontroluje ci sprava ide zo servera
    if isinstance(message.channel, discord.channel.TextChannel):
        print(f"Sprava z kanalu {message.channel.name}")
        if message.channel.name == "15":

            # Bot odpovie hello na Prikaz say_hello
            if message.content.startswith("say_hello"):
                await message.channel.send("Hello!")

            # Ak napisem do kanalu $write me, zasle mi sukromnu spravu I am <bot name> nice to meet you
            if message.content.startswith("$write_me"):
                await message.author.send(f"I am {client.user}, nice to meet you")

            # Tato funkcionalita zatial nefunguje, ale mala by zaslat spravu vsetkym clenom kanalu
            if message.content.startswith("$write_all"):
                members = message.channel.members
                for member in members:
                    if member == client.user:
                        continue
                    print(f"posielam spravu: {member.name}")
                    await member.send(f"This is from {message.author.name}")

    # tato podmienka kontroluje ci sprava ide zo sikromnych sprav
    elif isinstance(message.channel, discord.channel.DMChannel):
        if message.content == "Help me":
            await message.author.send(f"Help yourself {message.author.name}")


# Sem vlozte svoj token bota
client.run(token="")
