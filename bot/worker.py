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


from .FastTelethon import download_file, upload_file
from .funcn import *


async def stats(e):
    try:
        wah = e.pattern_match.group(1).decode("UTF-8")
        wh = decode(wah)
        out, dl, id = wh.split(";")
        ot = hbs(int(Path(out).stat().st_size))
        ov = hbs(int(Path(dl).stat().st_size))
        ans = f"Downloaded:-\n<b>☞ {ov}</b>\n\nCompressing:-\n<b>☞ {ot}</b>"
        await e.answer(ans, cache_time=0, alert=True)
    except Exception as er:
        LOGS.info(er)
        await e.answer("Someting Went Wrong 🤔\nResend Media", cache_time=0, alert=True)

encode_channel_id = "-1001592627525"
filz_channel_id = -1001592627525
status_channel_id = -1001667460631
async def encod(event):
    try:
        if not event.is_channel:
            return
        event.sender
        if str(event.sender_id) in encode_channel_id:
            return
        if not event.media:
            return
        if hasattr(event.media, "document"):
            if not event.media.document.mime_type.startswith(
                ("video", "application/octet-stream")
            ):
                return
        else:
            return
        try:
            oc = event.fwd_from.from_id.user_id
            occ = (await event.client.get_me()).id
            if oc == occ:
                return await event.reply("`This Video File is already Compressed 😑😑.`")
        except BaseException:
            pass
        xxx = await event.reply("`Downloading...`")
        s = dt.now()
        ttt = time.time()
        dir = f"downloads/"
        try:
            if hasattr(event.media, "document"):
                file = event.media.document
                filename = event.file.name
                if not filename:
                    filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                dl = dir + filename
                with open(dl, "wb") as f:
                    ok = await download_file(
                        client=event.client,
                        location=file,
                        out=f,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                xxx,
                                ttt,
                                "Downloading",
                            )
                        ),
                    )
            else:
                dl = await event.client.download_media(
                    event.media,
                    dir,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, xxx, ttt, "Downloading")
                    ),
                )
        except Exception as er:
            WORKING.clear()
            LOGS.info(er)
            return os.remove(dl)
        es = dt.now()
        kk = dl.split("/")[-1]        
        hh = kk
        hh = hh.replace("[SubsPlease]", " ")
        gg = hh
        gg = gg.replace("SubsPlease", " ")
        ss = gg
        ss = ss.replace("_", " ")          
        jj = ss
        jj = jj.replace("1080p", "480p x264")
        mm = ' '.join(jj.split()[:-1])
        rr = f"encode"
        bb = f"{mm}.mkv"                       
        out = f"{rr}/{bb}"
        thum = "thumb.jpg"
        dtime = ts(int((es - s).seconds) * 1000)
        e = xxx
        hehe = f"{out};{dl};0"
        wah = code(hehe)
        nn = await e.client.send_message(status_channel_id,
            mm,
                    buttons=[
                [Button.inline("Sᴛᴀᴛᴜs 📊", data=f"stats{wah}")],
                [Button.inline("Cᴀɴᴄᴇʟ 🗑️", data=f"skip{wah}")],
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
                await e.edit(str(er) + "\n**ERROR** \nContact : \nOwner : @ANIMEXTLIVE")
                WORKING.clear()
                os.remove(dl)
                return os.remove(out)
        except BaseException:
            pass
        ees = dt.now()
        ttt = time.time()
        nnn = await nn.edit("🚀`Uploading...`", 
                    buttons=[Button.inline("Cᴀɴᴄᴇʟ 🗑️", data=f"skip{wah}")],
            )
        with open(out, "rb") as f:
            ok = await upload_file(
                client=e.client,
                file=f,
                name=out,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, nnn, ttt, "uploading..")
                ),
            )
        ds = await e.client.send_file(
             filz_channel_id, file=ok, caption=mm.replace("AD", "[AD](https://t.me/animedirectoryy)"), force_document=True, thumb=thum
        )
        await nnn.edit(mm + " Encoded Successfully✅",                   
                       buttons=[]
                      )
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
            f"☞ 💿Original Size : {hbs(org)}\n☞ 📀Compressed Size : {hbs(com)}\n☞ Compressed Percentage : {per}\n\nℹ️Mediainfo: [Ⓑ]({a1})//[Ⓐ]({a2})\n\nDownloaded📥 in {x}\nCompressed in {xx}\nUploaded📤 in {xxx}",
            link_preview=False,
        )
        os.remove(dl)
        os.remove(out)
        WORKING.clear()
    except BaseException as er:
        LOGS.info(er)
        WORKING.clear()
