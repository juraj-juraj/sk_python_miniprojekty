# bot.py
import discord
import os

from dotenv import load_dotenv

load_dotenv("token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

import discord.ext.commands
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    print(f"Message from {message.author}: {message.content}")
    if isinstance(message.channel, discord.channel.TextChannel):
        if message.channel.name == "15":
            print("Replying")
            await bot.process_commands(message)


@bot.command(help="This command does something")
async def do_something(ctx: discord.ext.commands.context.Context):
    print(f"Message from {ctx.author}: {ctx.message.content}")
    await ctx.send("I did something!")


@bot.command(name="write_to", help="Write to member")
async def write_to(
    ctx: discord.ext.commands.context.Context, member: discord.Member, *args
):
    print(f"Message from {ctx.author}: {ctx.message.content}")
    print(f"{args = }")
    await member.send("Hello!")


guessing_word = ""
guessed_word = ""
failed_tries = 0

dictionary = ["apple", "banana", "car", "mountain", "ocean", "python", "java"]


@bot.command(name="start_hangman", help="Starts a hangman game")
async def start_hangman(ctx: discord.ext.commands.context.Context):
    global guessing_word
    global guessed_word
    global failed_tries
    guessing_word = dictionary[random.randint(0, len(dictionary) - 1)]
    print(f"guessing_word: {guessing_word}")
    guessed_word = "$" * len(guessing_word)
    failed_tries = 0
    await ctx.send("Hangman game started!")


@bot.command(name="guess_letter", help="Guess a letter")
async def guess_letter(ctx: discord.ext.commands.context.Context, letter: str):
    global guessing_word
    global guessed_word
    global failed_tries
    if len(letter) != 1:
        await ctx.send("Please guess only one letter!")
        return

    if letter in guessing_word:
        for i in range(len(guessing_word)):
            if guessing_word[i] == letter:
                l_guessed_word = list(guessed_word)
                l_guessed_word[i] = letter
                guessed_word = "".join(l_guessed_word)
        print(f"guessed_word: {guessed_word}")
        await ctx.send(f"Correct! {guessed_word}")

    else:
        failed_tries += 1
        await ctx.send(f"Incorrect! {guessed_word}")
        if failed_tries == 6:
            await ctx.send(f"Game over! The word was {guessing_word}")
            guessing_word = ""
            guessed_word = ""
            failed_tries = 0


@bot.command(name="guess_word", help="Guess the word")
async def guess_word(ctx: discord.ext.commands.context.Context, word: str):
    global guessing_word
    global guessed_word
    global failed_tries
    if word == guessing_word:
        await ctx.send(f"Correct! The word was {guessing_word}")
        guessing_word = ""
        guessed_word = ""
        failed_tries = 0
    else:
        failed_tries += 1
        await ctx.send(f"Incorrect! {guessed_word}")
        if failed_tries == 6:
            await ctx.send(f"Game over! The word was {guessing_word}")
            guessing_word = ""
            guessed_word = ""
            failed_tries = 0


#### Notepad implementation


class UserNotepad:
    def __init__(self, user_name):
        self.user = user_name
        self.notes: list[str] = []

    def add_note(self, note: str):
        self.notes.append(note)

    def list_notes(self) -> str:
        notes = [f"{idx}: {note}" for idx, note in enumerate(self.notes)]
        return "\n".join(notes)

    def delete_note_idx(self, idx: int) -> bool:
        if idx not in range(len(self.notes)):
            return False
        self.notes.pop(idx)
        return True


Notepads: dict[int, UserNotepad] = {}


@bot.command(name="add_to_notepad", help="Add to personal notepad at the end")
async def add_to_notepad(ctx: discord.ext.commands.context.Context, *args):
    note = " ".join(args)
    print(f"Add to notepad: {note}")
    if ctx.author.id not in Notepads:
        notepad = UserNotepad(ctx.author.name)
        notepad.add_note(note)
        Notepads[ctx.author.id] = notepad
    else:
        Notepads[ctx.author.id].add_note(note)
    await ctx.send("Note succesfully added to personal notepad")


@bot.command(name="list_notes")
async def list_notes(ctx: discord.ext.commands.context.Context):
    if ctx.author.id in Notepads:
        await ctx.send(Notepads[ctx.author.id].list_notes())
    else:
        await ctx.send(f"User {ctx.author.name} doesnt have notepad created")


@bot.command(name="delete_note_id")
async def delete_note_id(ctx: discord.ext.commands.context.Context, id: str):
    if ctx.author.id in Notepads:
        Notepads[ctx.author.id].delete_note_idx(int(id))
        await ctx.send("Deleted note")
    else:
        await ctx.send("User has no personal notepad")


bot.run(TOKEN)
