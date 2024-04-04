import discord
import discord.ext.commands
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="vole-", intents=intents)


@bot.command(name="do_something")
async def do_something(ctx: discord.ext.commands.context.Context):
    print(f"Got message from {ctx.author}")
    await ctx.send("Done something")


""" 
vole-start_hangman -> hra sa nastartuje, bot vyberie tajne slovo
vole-guess_letter a -> bot sa pokusi zistit ci tajne slovo obsahuje dane pismenko
vole-guess_word word -> bot sa pokusi zistit ci je uhadnute slovo
"""

secret_word = ""
guessed_letters = ""
lives = 0

words = ["apple", "banana", "car", "mountain", "ocean", "python", "java"]


@bot.command(name="start_hangman")
async def start_hangman(ctx: discord.ext.commands.context.Context):
    global secret_word
    global guessed_letters
    global lives
    global words

    random_index = random.randint(0, len(words))
    secret_word = words[random_index]
    print(f"Secret word is: {secret_word}")

    guessed_letters = "~" * len(secret_word)
    lives = 3
    await ctx.send("Started game of hangman")


@bot.command(name="guess_letter")
async def guess_letter(ctx: discord.ext.commands.context.Context, letter: str):
    global secret_word
    global guessed_letters
    global lives

    if lives <= 0:
        await ctx.send("Game over")
        return

    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                l_guessed_word = list(guessed_letters)
                l_guessed_word[i] = secret_word[i]
                guessed_letters = "".join(l_guessed_word)
        if "~" not in guessed_letters:
            await ctx.send("You won")
        else:
            await ctx.send(f"You guessed: {guessed_letters}")
    else:
        lives -= 1
        await ctx.send(f"Wrong, you got {lives} left")


@bot.command(name="guess_word")
async def guess_word(ctx: discord.ext.commands.context.Context, word: str): ...


bot.run("")
