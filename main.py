import logging
import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
import datetime
import sqlite3



connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# Intents ----------------------------------------------
intents = disnake.Intents.all()

# Bot Prefix & Intents Enable --------------------------
client = commands.Bot(command_prefix='!', intents=intents, test_guilds=[948245926290538506], help_command=None)


# Ping Command -----------------------------------------
@client.command(description="Pong!")
async def ping(ctx):
    await ctx.send(f"🏓 Pong! ``{round(client.latency * 1000)}ms``")

# Help Command ----------------------------------------
@client.command(description="A basic help command.")
async def help(ctx):
    embed = disnake.Embed(title="Protech - Help Guide")
    embed.add_field(name="In case of something is not properly working, please make sure to:",
                    value="- Have a channel named ``protech-logs``\n- Make sure a Bot has an ``administrator`` Permission\n- Make sure that the Bot Role ``@Protech`` is high enough to work properly",
                    inline=False)
    embed.add_field(name="Bot Information",
                    value=f"[Commands List](https://sites.google.com/view/discord-protech/commands)\n- Default Prefix: ``p!``\n- Default Help Command: ``p!help``\n- Bot Guilds: ``{len(client.guilds):,}``\n- Bot Users: ``{len(client.users):,}``",
                    inline=False)
    embed.add_field(name="Help & Support",
                    value=f"[Support Server](https://discord.gg/asggArXm86)",
                    inline=False)
    embed.add_field(name="Documentation",
                    value=f"[Terms of Service](https://docs.google.com/document/d/1fwFVi3AnKgq53_AOmA_WMcjLG79kQbLlSdxvW6qkMTk/edit?usp=sharing)\n[Privacy Policy](https://docs.google.com/document/d/1HwTK3NCDc4KpfuKI3CtMLn_Wbo1s20Hbor0UMpoCc1k/edit?usp=sharing)",
                    inline=False)
    embed.add_field(name="Get Protech",
                    value=f"[Add Protech to Your Server](https://discord.com/api/oauth2/authorize?client_id=881996813371072552&permissions=8&scope=bot%20applications.commands)",
                    inline=False)
    await ctx.send(embed=embed)

# Kick Command ----------------------------------------
@client.command(description="Kicks a member")
@commands.has_permissions(kick_members=True)

async def kick(ctx: commands.Context, member: disnake.Member = None, *, reason = None):
    guildId = ctx.message.guild.id
    guild = client.get_guild(guildId)
    embed= disnake.Embed(
        color=disnake.Color.blue(), title="**Notification**", description=f"You have been **kicked** from **``{guild.name}``** (ID:{guildId}) for **``{reason}``**")
    embed.timestamp = datetime.datetime.utcnow()
    
    if member == None:
         await ctx.send("You have to specify an user!")
         print('no user')
         return
    if member == ctx.message.author or member == None:
        await ctx.send("You cannot kick yourself!")
        print('yourself')
        return
    if reason == None:
        await ctx.send("You have to specify a reason!")
        print('no reason')
        return
    
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"{member} is succesfully kicked!")
    await member.send(embed=embed)
    channel = disnake.utils.get(ctx.guild.channels, name="protech-logs")
    await channel.send(f"{member} has been **kicked** by {ctx.author} for a reason: **{reason}**")
    serverId = ctx.message.guild.id
    
@client.command(description="Sets up the bot. ")
@commands.has_permissions(administrator=True)
async def setup(ctx, mode: str):
    guildId = ctx.message.guild.id
    guild = client.get_guild(guildId) 
    print(guildId)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    if mode == 'logging':
        print('yes')
        logging_embed = disnake.Embed(color = disnake.Color.blue(),title = '**Logging setup**', description = 'Enter the ID of your logging channel.')
        await ctx.send(embed=logging_embed)
        logging_id = ctx.message.content
        ctx.send('Done, set logging ID. ')
        name = 'a' + str(guildId)
        #cursor.execute(f"CREATE TABLE {name} (id INTEGER)")
        cursor.execute(f"INSERT INTO {name} VALUES({logging_id}) ")
        print(cursor.fetchall())
        print(logging_id)
    
    

client.run('')