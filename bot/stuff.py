#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from .funcn import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"ℍ𝕚 `{event.sender.first_name}`, \nDEPLOYED ON VPS FOR [ANIMEXT]( https://t.me/joinchat/RSJAb24o_OoFJu83 ).",
        buttons=[
            [Button.inline("ℍ𝕖𝕝𝕡", data="ihelp")],
            [
                Button.url("👥𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=" https://t.me/joinchat/RSJAb24o_OoFJu83 "),
                Button.url("🌟𝗢𝗪𝗡𝗘𝗥", url="https://t.me/sidd_2005"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**ENCODER**\n\n+PRIVATE"
    )


async def ihelp(event):
    await event.edit(
        "**ENCODER**\n\n+PRIVATE",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"`{event.sender.first_name}`, \nWORKING",
        buttons=[
            [Button.inline("ℍ𝕖𝕝𝕡", data="ihelp")],
            [
                Button.url("𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=" https://t.me/joinchat/RSJAb24o_OoFJu83 "),
                Button.url("👨‍💻𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥", url="https://t.me/sidd_2005"),
            ],
        ],
    )
