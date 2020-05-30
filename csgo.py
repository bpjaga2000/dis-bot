import discord
import json
import http.server as server
from discord.ext import commands
import typing
#server
PORT = 5000
URL = "127.0.0.1"

#bot
TOKEN ='NzE0MzY2ODA0MTg0NTMwOTQ1.Xsto-A.JCKBUK7MFM29I6KIV5WsPxIaGmU'
C_PREFIX='.'
GObot = commands.Bot(command_prefix=C_PREFIX,case_insensitive=True)
stid_uid ={'76561198063022490':'bpj4#5006'}
teams={}


a=json.dumps({"allmembers":
    {'76561198063022490': {'name': 'NIP forest NOCCO', 'observer_slot': 1, 'team': 'CT'},
     '76561198953556885': {'clan': 'FURIAǃ', 'name': 'テイテイ ♡', 'observer_slot': 2, 'team': 'CT'},
     '76561198082650349': {'name': 'seek', 'observer_slot': 3, 'team': 'CT'},
     '76561198047288291': {'name': 'ingridfavret', 'observer_slot': 4, 'team': 'CT'},
     '76561198275299924': {'name': 'MAMAU FLITO CON SAL', 'observer_slot': 6, 'team': 'T'},
     '76561198387963444': {'name': 'Valdir Pudim', 'observer_slot': 7, 'team': 'T'},
     '76561198165594275': {'name': 'noiZ', 'observer_slot': 8, 'team': 'T'},
     '76561198086689743': {'name': 'Sapo Cabeludo', 'observer_slot': 9, 'team': 'T'},
     '76561198381282393': {'name': '*R', 'observer_slot': 5, 'team': 'CT'},
     '76561199051590648': {'name': '𝐃𝐞𝐚𝐍', 'observer_slot': 0, 'team': 'T'}}
              })

print(json.loads(a))
b=json.loads(a)['allmembers']
guild=None

@GObot.command()
async def link(ctx,message):
    stid_uid[message]=str(ctx.message.author)
    print(stid_uid)

@GObot.command()
async def join(ctx,member: typing.Optional[discord.Member]):
    guild=ctx.message.guild
    id=None
    for i in stid_uid:
        if stid_uid[i] ==str(ctx.message.author):
            id=i
    teams[str(ctx.message.author)]=b[id]['team']
    print(teams)
    for channel in ctx.message.guild.voice_channels:
        if channel.name == teams[str(ctx.message.author)]:
            await (ctx.message.guild.get_member(ctx.message.author.id)).move_to(channel)

class handler(server.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

    def do_POST(self):
        pass
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode("utf-8")
        b=json.loads(body)['allplayers']
        print(b)
        for i in b:
            print(i)
            if i in stid_uid:
                print(True)

httpd = server.HTTPServer((URL, PORT), handler)
httpd.serve_forever()
GObot.run(TOKEN)