import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions

# Intents ----------------------------------------------
intents = disnake.Intents.all()

# Bot Prefix & Intents Enable --------------------------
client = commands.Bot(command_prefix='p!', intents=intents, test_guilds=[948245926290538506], help_command=None)

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
async def kick(ctx: commands.Context, member: disnake.Member, *, reason):

    message = f"You have been kicked from **{ctx.guild.name}** for **{reason}**!"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"{member} is succesfully kicked!")
    channel = disnake.utils.get(ctx.guild.channels, name="protech-logs")
    await channel.send(f"{member} has been **kicked** by {ctx.author} for a reason: **{reason}**")
    serverId = ctx.message.guild.id
    await ctx.send(embed= disnake.Embed(title="Notification", description=f"You have been kicked from {serverId}")
