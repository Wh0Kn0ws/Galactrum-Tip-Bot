import discord
import asyncio
import requests
import simplejson as json

i = 0
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!sleep'):
		await client.send_message(message.channel, "You're not my dad!")
	elif message.content.startswith('!train'):
		await client.send_message(message.channel, "Choo Choo!!")
	elif message.content.startswith('!netcoin'):
		await client.send_message(message.channel, "ⓃⒺⓉⒸⓄⒾⓃ""""
♪:eight_pointed_black_star:♪•.¸¸¸.•¨¨•.¸¸¸.••♪:eight_pointed_black_star:♪¸.•¨¨•.¸¸¸.••♪:eight_pointed_black_star:♪• ♪:eight_pointed_black_star:♪ ░N░E░T░C░O░I░N░:eight_pointed_black_star:░R░O░C░K░S░!░!░♪:eight_pointed_black_star:♪ •♪:eight_pointed_black_star:♪•.¸¸¸.•¨¨•.¸¸¸.••♪¸.•¨¨•.¸¸¸.••♪:eight_pointed_black_star:♪•*
:Netcoin:""""""""")
	elif message.content.startswith('!wallet'):
		port =  "11311"
		getbalance = rpcdat('getbalance',[],port)
		print(getbalance)
		await client.send_message(message.channel, str(getbalance)+" NET")
	elif message.content.startswith('!balance'):
		print(message.author)
		author = message.author
		await start_get_user_bal(message, author)
	elif message.content.startswith('!git'):
		await client.send_message(message.channel, "Git: https://github.com/Aareon/Discord-Netcoin-Bot")

@client.event
async def start_get_user_bal(message, author):
	global i, db_get
	with open('snekdb', 'r+') as db:
		db_get = db.read()
		db.close()
	db_get = db_get.splitlines()
	print(db_get)
	try:
		if str(author) in db_get[i]:
			db_get = db_get[i].split("/")
			print(db_get[1])
			await client.send_message(message.channel, str(db_get[1])+" NET")
			db_get = ""
			return
		else:
			i +=1
			await start_get_user_bal(message, author)
	except IndexError as err:
		print(err)
		await client.send_message(message.channel, "Attempting to add new user to db...")
		add_user(author)

def add_user(author):
	with open('snekdb','a') as f:
		f.write(str(author)+"/0.0000000\n")
		print("Writing: "+str(author)+"/0.0000000")
		f.close()

def rpcdat(method,params,port):
	rpcdata = json.dumps({
		"jsonrpc": 1.0,
		"id":"rpctest",
		"method": str(method),
		"params": params,
		"port": port
		})
	req = requests.get('http://0.0.0.0:'+port, data=rpcdata, auth=('user', 'pass'), timeout=8)
	return req.json()['result']

client.run('token')