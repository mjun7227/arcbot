import discord
from discord.ext import commands
import os
import Bot_Data
import random

bot =commands.Bot(command_prefix='대립이 ') 


@bot.event 
async def on_ready():
    print("파괴된 탑에서 깨어나게 된 그녀가 첫 번째로 본 것은 공중에서 희미하게 흩날리고 있던 유리 조각들이었으며, 조각들은 곧 하얀 세상으로 그녀를 인도하였다.")        
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(activity=discord.Game(name="대립이 [명령어]"))

    
@bot.command(name="ping")
async def ping(ctx):
    latancy = bot.latency
    await ctx.send(f"핑 {round(latancy*1000)}") 

@bot.command(pass_contxt=True,aliases=["주오르히","conflict","컨플"])
async def sing_conflict(ctx):
    await ctx.send(Bot_Data.Songs_meme["Conflict"])

@bot.command(pass_contxt=True,aliases=["이어진","crossover","크로스오버"])
async def sing_crossover(ctx):
        await ctx.send(Bot_Data.Songs_meme["crossover"])

@bot.command(name="선곡")
async def choose(ctx, levelnpack:str):
    Song=random.choice(Bot_Data.Songs_by_Level[levelnpack])
    if Song in Bot_Data.Ssongs.keys():
        await ctx.send(Bot_Data.Ssongs[Song])
    else:
        await ctx.send(Song)

@choose.error
async def choose_error(ctx,error):
    if error.param.name =="levelnpack":
        await ctx.send(random.choice(Bot_Data.Songs_by_Level[random.choice(list(Bot_Data.Songs_by_Level.keys()))]))
    else:
        await ctx.send("잘 모르겠어요....\n명령어 ex) 대립이 선곡 [레벨]")

@bot.command(pass_context=True,name="arc")
async def pro_arcaea(ctx):
    await ctx.send("♚♚아☆르☆케☆아♚♚가입시$$전원 히카리☜☜타이리츠100%증정※ ♜레드아크♜\
무료증정￥ 특정조건 §§대폭풍§§★재규어★겨울 에토 루나 획득기회@@@ 즉시이동https://arcaea.lowiro.com/ko")

@bot.command(pass_contxt=True,aliases=["도움말","도움"])
async def _help(ctx):
    embed=discord.Embed(
        colour = discord.Colour.dark_blue()
    )
    embed.set_author(name="대립이 명령어 모음")
    for i in Bot_Data.BotCommands.keys():
        embed.add_field(name=i,value=Bot_Data.BotCommands[i],inline=False)
    await ctx.send(embed=embed)
@bot.command(name="패치노트")   
async def send_patch(ctx):
    author=ctx.message.author
    embed=discord.Embed(
        colour = discord.Colour.dark_blue()
    )
    embed.set_author(name="패치노트")
    for i in Bot_Data.patchnote.keys():
        embed.add_field(name=i,value=Bot_Data.patchnote[i],inline=False)
    await ctx.send(author,embed=embed)

@bot.command(pass_contxt=True,aliases=["안녕","하위","어서오고"])
async def hello(ctx):
    await ctx.send(f"만나서 반가워요. {ctx.author.mention}님")

@bot.command(pass_contxt=True,aliases=["빅스비"])
async def nexne(ctx):
    await ctx.send("누나ㅏㅏㅏ 나주거ㅓㅓㅓㅓㅓㅓ")
    print(ctx.message.content) 

        

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("잘 모르겠어요...\n명령어 목록 호출) 대립이 도움말")
    else:
        return
    print(error)




bot.run(os.environ["token"])
