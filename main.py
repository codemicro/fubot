import discord
import json
import urllib.parse
import sys
import requests
import random
import datetime

CONF = json.load(open("config.json"))
bot = discord.Bot(intents=discord.Intents.all())


def translate_string(en_txt: str) -> str:
    # source: https://web.archive.org/web/20220101090143/https://danpetrov.xyz/programming/2021/12/30/telegram-google-translate.html
    uri = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl="
        + "en"  # for future abi looking at this wondering what the fuck is going on: this is the source language
        + "&tl="
        + "pl"  # this is the target language
        + "&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&kc=7&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&q="
    )
    uri += urllib.parse.quote_plus(en_txt)  # this is normal url encoding
    res = requests.get(uri)
    j = res.json()
    return j[0][0][0]  # lol


def get_max_prob() -> int:
    end = int((datetime.date.today() + datetime.timedelta(days=1)).strftime("%s"))
    remaining = end - int((datetime.datetime.utcnow()).strftime("%s"))
    return (int(90*(remaining/5184000))) + 10


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.event
async def on_message(msg):
    if not((td := datetime.date.today()).day == 1 and td.month == 4):
        return

    if msg.author.id == bot.user.id:
        return

    if random.randint(1, get_max_prob()) != 2:
        return

    try:
        await msg.reply(translate_string(msg.content))
    except Exception as e:
        # :(
        print("Error: " + e, file=sys.stderr)


if __name__ == "__main__":
    bot.run(CONF.get("token"))
