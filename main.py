from telethon import *
import time
import subprocess
from PIL import Image
import os
from googletrans import Translator

api_id = 16245046
api_hash = "b5a4cc89f1abd9c9e62c54548da4d2d2"

teleco = TelegramClient("Teleco", api_id=api_id, api_hash=api_hash)

@teleco.on(events.NewMessage(outgoing=True, pattern=r".hi"))
async def hi(event):
	chat = await event.get_chat()
	await teleco.delete_messages(chat, event.message)
	await teleco.send_message(chat, "**🦚 ʜɪ, ᴛᴇʟᴇᴄᴏ ᴜsᴇʀʙᴏᴛ ʜᴇʀᴇ 🦄...**")

@teleco.on(events.NewMessage(outgoing=True, pattern=r".alive"))
async def alive(event):
	chat = await event.get_chat()
	user = await teleco.get_me()
	await teleco.delete_messages(chat, event.message)
	uptime = int(time.time()) - teleco.start_time
	cap = f"""
**ʜɪ {user.first_name} 🦚 !**

**ɪ ᴀᴍ ᴀʟɪᴠᴇ 🎉!!!**

**ᴜᴘᴛɪᴍᴇ 🦄: {uptime} sᴇᴄᴏɴᴅs**
	"""
	await teleco.send_file(chat.id, file="teleco.jpg", caption=cap)

@teleco.on(events.NewMessage(outgoing=True, pattern=r".ping"))
async def ping(event):
	chat = await event.get_chat()
	await teleco.delete_messages(chat, event.message)
	ping_result = subprocess.run(["ping", "-c", "4", "www.google.com"], capture_output=True, text=True)
	ping_output = ping_result.stdout
	ping_time = parse_ping_output(ping_output)
	ping_text = ping_time.replace("=", "")
	await event.respond(f"ᴘᴏɴɢ : {ping_text} ᴍs")

def parse_ping_output(ping_output) :
	try:
		lines = ping_output.splitlines()
		for line in lines:
			if "time" in line:
				time_parts = line.split("time")[1].split(" ")[0]
				return time_parts
		return "N/A"
	except Exception as e:
		print(f"Error while parsing the ping {e}")
		return "N/A"

@teleco.on(events.NewMessage(outgoing=True, pattern=r'.kang'))
async def kang(event):
	if event.is_reply:
		replied_msg = await event.get_reply_message()
		me = await teleco.get_me()
		pack = 1
		emoji = "⚡"
		nickname = f"@{me.username}'s ᴘᴀᴄᴋ {pack} 🔥"
		packname = f"Teleco_463842_{pack}"
		stcker = await replied_msg.download_media()
		if stcker.endswith((".jpg", ".jpeg", ".png")):
			file = "sticker.png"
			c = Image.open(stcker)
			c = c.resize((512, 512))
			c.save(file, optimize=True, quality=10)
			os.remove(stcker)
		elif stcker and stcker.endswith(".webp"):
			file = "sticker.png"
			c = Image.open(stcker)
			c = c.resize((512, 512))
			c.save(file)
			os.remove(stcker)
		else:
			return await teleco.edit_message(event.message, "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")
		x = await teleco.edit_message(event.message, "**ᴘʀᴏᴄᴇssɪɴɢ...**")
		cmd = "/newpack"
		async with teleco.conversation('@Stickers') as conv:
			await conv.send_message("/addsticker")
			await conv.get_response()
			await teleco.send_read_acknowledge(conv.chat_id)
			await conv.send_message(packname)
			xx = await conv.get_response()
			await teleco.send_read_acknowledge(conv.chat_id)
			if xx.text == "Invalid set selected.":
				await x.edit("**ᴍᴀᴋɪɴɢ ɴᴇᴡ ᴘᴀᴄᴋ.**")
				await conv.send_message(cmd)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message(nickname)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_file(file, force_document=True)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message(emoji)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message("/publish")
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message("/skip")
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message(packname)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await x.edit(f"sᴛɪᴄᴋᴇʀ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ɴᴇᴡ ᴘᴀᴄᴋ.\n[ʜᴇʀᴇ](https://t.me/addstickers/{packname})", parse_mode="md")
			else:
				await conv.send_file(file, force_document=True)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message(emoji)
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await conv.send_message("/done")
				await conv.get_response()
				await teleco.send_read_acknowledge(conv.chat_id)
				await x.edit(f"sᴛɪᴄᴋᴇʀ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ɴᴇᴡ ᴘᴀᴄᴋ.\n[ʜᴇʀᴇ](https://t.me/addstickers/{packname})", parse_mode="md")
	else:
		return await teleco.edit_message(event.message, "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")

@teleco.on(events.NewMessage(outgoing=True, pattern=r'.q'))
async def quote(event):
	chat = await event.get_chat()
	replied_msg = await event.get_reply_message()
	await teleco.edit_message(event.message, "**ᴘʀᴏᴄᴇssɪɴɢ...**")
	x = await replied_msg.forward_to('@MTF_QuotLy_bot')
	async with teleco.conversation('@MTF_QuotLy_bot') as conv:
		xx = await conv.get_response(x.id)
		await teleco.send_read_acknowledge(conv.chat_id)
		await teleco.delete_messages(chat, event.message)
		await teleco.send_message(chat, xx)

translator = Translator()
@teleco.on(events.NewMessage(outgoing=True, pattern=r'.tr'))
async def translate_command(event):
	try:
		if event.is_reply:
			replied_message = await event.get_reply_message()
			text_to_translate = replied_message.text
		else:
			_, *text = event.raw_text.split(' ')
			text_to_translate = ' '.join(text).strip()
		if '-' in text_to_translate:
			text_parts = text_to_translate.split('-')
			tex_to_translate = text_parts[0].strip()
			target_lang = text_parts[1].strip()
		else:
			target_lang = 'en'
		
		translated_text = translator.translate(text_to_translate, dest=target_lang).text
		chat = await event.get_chat()
		await teleco.delete_messages(chat, event.message)
		await event.reply(f"ᴛʀᴀɴsʟᴀᴛᴇᴅ ({target_lang}) : \n{translated_text}")
	except ValueError:
		await event.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴀɴᴅ ᴛᴀʀɢᴇᴛᴛᴇᴅ ʟᴀɴɢᴜᴀɢᴇ ᴀғᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ, ᴇ.ɢ. `.tr ¿hola, cómo estás? -en`")
	except Exception as e:
		await event.reply(f"ᴇʀʀᴏʀ : {e}")

teleco.start_time = int(time.time())

teleco.start()
teleco.run_until_disconnected()