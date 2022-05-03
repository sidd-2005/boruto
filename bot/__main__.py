#    This file is part of the Compressor distribution.
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
# License can be found in
# <https://github.com/1Danish-00/CompressorQueue/blob/main/License> .


from . import *
from .devtools import *

LOGS.info("Starting...")


######## Connect ########


try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########


@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
    await start(e)


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)


######## Callbacks #########


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## Direct ###########


@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


########## AUTO ###########


@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in range(9999999999999999999999999):  # ik very weird way 😅😅
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                e = await bot.send_message(user, "𝐷𝑜𝑤𝑛𝑙𝑜𝑑𝑖𝑛𝑔📥 𝑄𝑢𝑒𝑢𝑒 𝐹𝑖𝑙𝑒𝑠📂")
                dl, file = QUEUE[list(QUEUE.keys())[0]]
                s = dt.now()
                tt = time.time()
                dl = "downloads/" + dl
                with open(dl, "wb") as f:
                    ok = await download_file(
                        client=bot,
                        location=file,
                        out=f,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                e,
                                tt,
                                "𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕚𝕟𝕘📥 𝕥𝕠 𝕄𝕪 𝕊𝕖𝕣𝕧𝕖𝕣🖥️",
                            )
                        ),
                    )
                es = dt.now()
                kk = dl.split("/")[-1]
                hh = kk
                hh = hh.replace("1080p", "720p")
                jj = hh
                jj = jj.replace(kk[-14:], "(EngSub).mkv")
                aa = kk.split(".")[-1]
                rr = "encode"
                bb = kk.replace(f".{aa}", ".mkv")
                bb = bb.replace("SubsPlease", "ANIMEXT")
                bb = bb.replace("_", " ")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "**Pʀᴏᴄᴇssʜɴɢ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ**\nClick Below👇 To Know The Progress.",
                    buttons=[
                        [Button.inline("𝚂𝚝𝚊𝚝𝚜 📊", data=f"stats{wah}")],
                        [Button.inline("𝙲𝚊𝚗𝚌𝚎𝚕 🛑", data=f"skip{wah}")],
                    ],
                )
                cmd = FFMPEG.format(dl, out)
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**ERROR** Contact @animextlive owner")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(e.chat_id, "`Uploading...`")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, "**Uᴘʟᴏᴀᴅʜɴɢ📤 Tᴏ Tᴇʟᴇɢʀᴀᴍ**")
                        ),
                    )
                encode_channel_id = -1001783078830
                ds = await e.client.send_file(
                    encode_channel_id, file=ok, caption=jj.replace("SubsPlease", "ANIMEXT"), force_document=True, thumb=thum
                )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = await ds.rely(
                f"**☞ 💿Original Size : **{hbs(org)}\n**☞ 📀Compressed Size : **{hbs(com)}\n**☞ Compressed Percentage : **{per}\n\n**☞ ℹ️Mediainfo: **[Ⓑ🅔︎]({a1})//[Ⓐ🅕︎]({a2})\n\n__Downloaded📥 in {x}\nCompressed in {xx}__\n__Uploaded📤 in {xxx}__",
                  link_preview=False,
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has started.")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
