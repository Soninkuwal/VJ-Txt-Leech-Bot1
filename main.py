import os
import re
import sys
import json
import time
import aiohttp
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper
import datetime
import ffmpeg
import logging

from yt_dlp import YoutubeDL
import yt_dlp as youtube_dl
from pytube import YouTube
from aiohttp import web

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types import messages_and_media, InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    "bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    editable = await m.reply_text(
        f"𝐇𝐞𝐥𝐥𝐨 ❤️\n\n ▂▃▅▇█▓▒░ ❤️  SONIC KUWAL SSC BOT 🌈™ ❤️ ░▒▓█▇▅▃▂ \n\n❈ I Am A Bot For Download Links From Your **.TXT** File And Then Upload That File Om Telegram So Basically\n\n If You Want To Use Me First Send Me ⟰ \n /txt Command And Then Follow Few Steps..\n\n I working link ALL APP TXT WORKING NOT WORKING YOUTUBE LINK. \n\n YOUTUBE LINK WORKING SOON POSSIBLE....\n\n more apps add SOON update contact me :- <a href='https://telegram.me/SONICKUWALSSCBOT'>❖ ꧁༺ ❤️ 𝓚𝓐𝓝𝓗𝓐𝓘𝓨𝓐 𝓛𝓐𝓛 𝓜𝓔𝓔𝓝𝓐 𝓚𝓤𝓦𝓐𝓛 💕 ༻꧂ ❖ ™</a>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✜ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜",
                        url=f"https://t.me/SONICKUWALUPDATEKANHA",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✜◆ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 ◆✜", url="https://t.me/SONICKUWALSSCBOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋", url="https://t.me/SONICKUWALSSCBOT"
                    )
                ],
            ]
        ),
    )


@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


# Handle /txt command
@bot.on_message(filters.command(["txt"]))
async def upload(bot: Client, m: Message):
    user_id = m.from_user.id
    # Use asyncio to handle the user interaction concurrently
    asyncio.create_task(handle_txt_upload(bot, m, user_id))


async def handle_txt_upload(bot: Client, m: Message, user_id: int):
    editable = await m.reply_text('Send a TXT file. **\n\nDeveloper** : 🅑🅞🅣 🅜🅐🅓🅔 🅑🅨  LOVER 💖 BOY  content: @SONICKUWALSSCBOT **')
    input_message: Message = await bot.listen(editable.chat.id)  # Capture the message object

    if not input_message or not input_message.document:
        await editable.edit("Invalid input. Please send a TXT file.")
        return
        
    x = await input_message.download()
    await input_message.delete(True)



    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except Exception as e:
        await m.reply_text(f"**Invalid file input.**\nError: {str(e)}")
        os.remove(x)
        return

    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit(
        "**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality"
    )
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080"
        else:
            res = "UN"
    except Exception:
        res = "UN"

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == "Robin":
        MR = highlighter
    else:
        MR = raw_text3

    await editable.edit(
        "Now send the Thumb url/nEg » https://graph.org/file/61cc479c28b7ed60b4bc9-ca29dd2be7cf33e737.jpg \n Or if don't want thumbnail send = no"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):
            try:
                V = links[i][1].replace("file/d/", "uc?export=download&id=").replace(
                    "www.youtube-nocookie.com/embed", "youtu.be"
                ).replace("www.youtube.com/live", "youtu.be").replace(
                    "www.youtube.com/embed", "youtu.be"
                ).replace(
                    "youtube.com/embed/", "youtube.com/watch?v="
                ).replace(
                    "?modestbranding=1", ""
                ).replace(
                    "/view?usp=sharing", ""
                ).replace(
                    "d3nzo6itypaz07", "d26g5bnklkwsh4"
                ).replace(
                    "dn6x93wafba93", "d26g5bnklkwsh4"
                ).replace(
                    "d2tiz86clzieqa", "d26g5bnklkwsh4"
                ).replace(
                    "vod.teachx.in", "d3igdi2k1ohuql.cloudfront.net"
                ).replace(
                    "downloadappx.appx.co.in", "d33g7sdvsfd029.cloudfront.net"
                ).replace(
                    "mpd", "m3u8"
                )
                url = "https://" + V

                name1 = (
                    links[i][0]
                    .replace("\t", "")
                    .replace(":", "")
                    .replace("/", "")
                    .replace("+", "")
                    .replace("#", "")
                    .replace("|", "")
                    .replace("@", "")
                    .replace("*", "")
                    .replace(".", "")
                    .replace("https", "")
                    .replace("http", "")
                    .strip()
                )

                # Shorten filename
                name = f"{str(count).zfill(3)}) {name1[:40]}"  # Truncate filename
                name = re.sub(r"[^\w\s-]", "", name, flags=re.UNICODE)  # Remove special chars
                name = name.strip()
                output_filename = f"@SONICKUWALSSCBOT {name}.pdf"

                ytf = (
                    f"bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]/best[height<={raw_text2}]"
                    if "youtube" in url
                    else f"bestvideo[height<={raw_text2}]+bestaudio/b/best"
                )

                cmd = (
                    f'yt-dlp -o "{name}.%(ext)s" -f "{ytf}" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                    if "acecwply" in url
                    else None
                )

                ydl_opts = {
                    "outtmpl": output_filename,  # Use output_filename here
                    "fragment_retries": 25,
                    "retries": 25,
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "referer": "https://cwmediabkt99.crwilladmin.com",  # Setting a referer
                    "add_header": [
                        "Referer:https://cwmediabkt99.crwilladmin.com",
                    ],  # Setting a referer
                }

                if "visionias" in url:
                    async with ClientSession() as session:
                        try:
                            async with session.get(
                                url,
                                headers={
                                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                    "Accept-Language": "en-US,en;q=0.9",
                                    "Cache-Control": "no-cache",
                                    "Connection": "keep-alive",
                                    "Pragma": "no-cache",
                                    "Referer": "http://www.visionias.in/",
                                    "Sec-Fetch-Dest": "iframe",
                                    "Sec-Fetch-Mode": "navigate",
                                    "Sec-Fetch-Site": "cross-site",
                                    "Upgrade-Insecure-Requests": "1",
                                    "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                                    "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
                                    "sec-ch-ua-mobile": "?1",
                                    "sec-ch-ua-platform": '"Android"',
                                },
                            ) as resp:
                                text = await resp.text()
                                url = re.search(
                                    r"(https://.*?playlist.m3u8.*?)\"", text
                                ).group(1)
                                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
                        except Exception as e:
                            logger.error(f"Visionias download error: {e}")
                            await m.reply_text(f"Visionias download error: {e}")
                            continue  # Skip to the next link

                elif "classplusapp" in url:
                    headers = {
                        "Host": "api.classplusapp.com",
                        "x-access-token": "eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9",
                        "user-agent": "Mobile-Android",
                        "app-version": "1.4.37.1",
                        "api-version": "18",
                        "device-id": "5d0d17ac8b3c9f51",
                        "device-details": "2848b866799971ca_2848b8667a33216c_SDK-30",
                        "accept-encoding": "gzip, deflate",
                    }

                    params = (("url", f"{url}"),)
                    try:
                        response = requests.get(
                            "https://api.classplusapp.com/cams/uploader/video/jw-signed-url",
                            headers=headers,
                            params=params,
                        )
                        url = response.json()["url"]
                        cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
                    except Exception as e:
                        logger.error(f"Classplus download error: {e}")
                        await m.reply_text(f"Classplus download error: {e}")
                        continue

                elif any(
                    domain in url
                    for domain in [
                        "tencdn.classplusapp",
                        "media-cdn-alisg.classplusapp.com",
                        "media-cdn.classplusapp",
                    ]
                ):
                    headers = {
                        "Host": "api.classplusapp.com",
                        "x-access-token": "eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9",
                        "user-agent": "Mobile-Android",
                        "app-version": "1.4.37.1",
                        "api-version": "18",
                        "device-id": "5d0d17ac8b3c9f51",
                        "device-details": "2848b866799971ca_2848b8667a33216c_SDK-30",
                        "accept-encoding": "gzip",
                    }
                    params = (("url", f"{url}"),)
                    try:
                        response = requests.get(
                            "https://api.classplusapp.com/cams/uploader/video/jw-signed-url",
                            headers=headers,
                            params=params,
                        )
                        url = response.json()["url"]
                        cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
                    except Exception as e:
                        logger.error(f"Classplus CDN download error: {e}")
                        await m.reply_text(f"Classplus CDN download error: {e}")
                        continue

                elif "/master.mpd" in url:
                    id = url.split("/")[-2]
                    url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

                elif "/utkarshapp.mpd" in url:
                    id = url.split("/")[-2]
                    url = "https://apps-s3-prod.utkarshapp.com/" + id + "/utkarshapp.com"
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

                elif "madxapi" in url:
                    id = url.split("/")[-2]
                    url = (
                        "https://madxapi-d0cbf6ac738c.herokuapp.com/"
                        + id
                        + "/master.m3u8?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzgzMjk2NTIuNTAyLCJkYXRhIjp7Il9pZCI6IjY2NTM1YmIxNGE1YjZhN2NiM2EwMzAzYiIsInVzZXJuYW1lIjoiOTUwODYwNTI1OSIsImZpcnN0TmFtZSI6IkFiaGlzaGVrIiwibGFzdE5hbWUiOiJUaGFrdXIiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJhYmhpc2hlazcyNTQ4NUBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3Mzc3MjQ4NTJ9.mRWT-khhl7Y-cxRdgaoX4mdXRegaU0KbTX9wxhuw0oQ"
                    )
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

                elif "edge.api.brightcove.com" in url:
                    bcov = "bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg"
                    url = url.split("bcov_auth")[0] + bcov
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

                if (
                    "instagram.com" in url
                    and "/reel/" in url
                    or "/p/" in url
                    or "/tv/" in url
                ):
                    # cmd = f'yt-dlp --cookies "{INSTAGRAM_COOKIES_PATH}" -o "{name}.mp4" "{url}"' #Needs cookies
                    cmd = f'yt-dlp  -o "{name}.mp4" "{url}"'  # Trying without cookies (might work)

                if "jw-prod" in url:
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

                if "embed" in url:
                    ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
                    cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

                # Default yt-dlp command
                if not cmd:
                    cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

                try:
                    if "drive" in url:
                        try:
                            ka = await helper.download(url, name)
                            file_size = os.path.getsize(ka)
                            file_size_mb = file_size / (1024 * 1024)  # Convert to MB
                            cc1 = f'**[📁] Pdf_ID:❤️ @SONICKUWALSSCBOT ❤️** `{str(count).zfill(3)}. {name}{MR} [@SONICKUWALSSCBOT].pdf`\n**File Size:** `{file_size_mb:.2f} MB`\n\n**𝔹ᴀᴛᴄʜ** » `{raw_text0}`\n\n**𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 ➤ https://sonickuwalssc.blogspot.com/ **'

                            copy = await bot.send_document(
                                chat_id=m.chat.id, document=ka, caption=cc1
                            )
                            count += 1
                            os.remove(ka)
                            time.sleep(1)
                        except FloodWait as e:
                            await m.reply_text(str(e))
                            time.sleep(e.x)
                            continue

                    elif ".pdf" in url:
                        try:
                            # Use yt-dlp with explicit options
                            with YoutubeDL(ydl_opts) as ydl:
                                try:
                                    ydl.download([url])
                                    file_size = os.path.getsize(output_filename)
                                    file_size_mb = file_size / (1024 * 1024)

                                    cc1 = f'**[📁] Pdf_ID:❤️ @SONICKUWALSSCBOT ❤️** `{str(count).zfill(3)}. {name}{MR} [@SONICKUWALSSCBOT].pdf`\n**File Size:** `{file_size_mb:.2f} MB`\n\n**𝔹ᴀᴛᴄʜ** » `{raw_text0}`\n\n**𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 ➤ https://sonickuwalssc.blogspot.com/ **'

                                    try:
                                        await bot.send_document(
                                            chat_id=m.chat.id, document=output_filename, caption=cc1
                                        )
                                    except Exception as e:
                                        logger.error(f"Telegram upload error: {e}")
                                        await m.reply_text(f"Telegram upload error: {str(e)}")
                                    finally:
                                        count += 1
                                        os.remove(output_filename)

                                except Exception as e:
                                    logger.error(f"yt-dlp download failed: {str(e)}")
                                    await m.reply_text(f"yt-dlp download failed: {str(e)}")
                                    continue

                        except FloodWait as e:
                            await m.reply_text(str(e))
                            time.sleep(e.x)
                            continue

                    else:
                        try:
                            Show = (
                                f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n"
                                f"**📝Name »** `{name}`\n❄Quality » `{res}`\n\n**🔗URL »** `{url}`"
                            )
                            prog = await m.reply_text(Show)

                            # Download the video using helper function
                            filename = await helper.download_video(url, cmd, name)

                            if filename:
                                # Get video information using ffprobe
                                try:
                                    probe = ffmpeg.probe(filename)
                                    duration_seconds = float(probe["format"]["duration"])
                                    duration = time.strftime("%H:%M:%S", time.gmtime(duration_seconds))
                                    file_size = os.path.getsize(filename)
                                    file_size_mb = file_size / (1024 * 1024)

                                    cc = f'**[📽️] Vid_ID:❤️ @SONICKUWALSSCBOT ❤️** `{str(count).zfill(3)}. {name}{MR} [@SONICKUWALSSCBOT].mkv`\n' f"**File Size:** `{file_size_mb:.2f} MB`\n" f"**Quality:** `{res}`\n" f"**Duration:** `{duration}`\n" f"**𝔹ᴀᴛᴄʜ** » `{raw_text0}`\n\n" f"**𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 ➤ https://sonickuwalssc.blogspot.com/ **"
                                except Exception as e:
                                    cc = f'**[📽️] Vid_ID:❤️ @SONICKUWALSSCBOT ❤️** `{str(count).zfill(3)}. {name}{MR} [@SONICKUWALSSCBOT].mkv`\n' f"**File Size:** `N/A`\n" f"**Quality:** `{res}`\n" f"**Duration:** `N/A`\n" f"**𝔹ᴀᴛᴄʜ** » `{raw_text0}`\n\n" f"**𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐁𝐘 ➤ https://sonickuwalssc.blogspot.com/ **"
                                    print(f"Error getting video info: {e}")

                                await prog.delete(True)
                                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                                count += 1
                                time.sleep(1)
                            else:
                                await prog.edit("Failed to download video.")

                        except Exception as e:
                            await m.reply_text(
                                f"**Downloading Interrupted **\n{str(e)}\n**Name** » `{name}`\n**Link** » `{url}`"
                            )
                            continue

                except Exception as e:
                    await m.reply_text(f"An error occurred: {str(e)}")
                    continue  # Continue to the next link even if one fails

    except Exception as e:
        await m.reply_text(f"An error occurred: {str(e)}")
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()