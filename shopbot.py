import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='s!')

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

@bot.command()
async def shop(ctx):
    embed = discord.Embed(
        title = "LT2 Shop!",
        color = discord.Color.green(),
        description = "Everything You Can Get Here:"
    )
    embed.set_footer(text="""To Order These Type: s!buy Discord: [discord username + tag], Roblox: [roblox username], [item]. You can do mutiple Items But Make Sure To Add a , after each item (apart from last item of the order).""")
    embed.add_field(
        name="2015 GIFTS", value="""Firey Gift of Lumber - 5000
Wobbly Gift of Uncertainty - 25000
Poorly Wrapped Gift From Bob - 5500
Happy Red Gift of Fun - 5000""", inline=True)
    embed.add_field(
        name="2016 GIFTS", value="""Sweet Gift - 7000
Happy Blue Gift of Fun - 5000
Jingly Gift of Jingles - 20000
Acceptable Gift From Bob
Wobblier Gift of Less Certainty - 20000""", inline=True)
    embed.add_field(
        name="2017 GIFTS", value="""Joyful Green Gift of High Quality Charm - 5000
The Gift of Great Times - 10000
The Golden Gift of Golden Times - 15000""", inline=True)
    embed.add_field(
        name="2018 GIFTS", value="""Cold And Wet Lumpy Gift From Bob - 5000
Gift of Adventure - 250000
Gingerbread Gift - 10000
Orange Gift of Traffic Control and Corporate Power - 9000
Warm Gift of Love and Safety - 1000""", inline=True)
    embed.add_field(
            name="2019 GIFTS", value="""Joyful Green Gift of High Quality Charm - 5000
    The Gift of Great Times - 10000
    The Golden Gift of Golden Times - 15000""", inline=True)
    embed.add_field(
            name="2020 GIFTS", value="""Spooky Deep Earth Gift - 15000
Gift With Green Candy Cane stripes - 4500""", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def buy(ctx, *, args=None):
    if args != None:
        try:
            target = await bot.fetch_user("714541407846793266")
            await target.send(args)

            await ctx.channel.send("Order Sent!")

        except:
            await ctx.channel.send("Couldn't Send Order. Please Contact legacy#3485.")

    else:
        await ctx.channel.send("A user_id and/or arguments were not included.")

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f"Cleared {amount} messages!")

bot.run("ODI2MTY4NTg3OTQwMDAzOTAx.YGIjdA.qTwgeHiZXmUaCTGvy_lhkO7xhQ0")
