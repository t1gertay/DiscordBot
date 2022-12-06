import hikari
import lightbulb

bot = lightbulb.BotApp(intents=hikari.Intents.ALL, token='MTA0ODMyODA2MjA1MzQwNDY3Mg.GOh-xc.O98q0IUrIbXx2blRqfMRhp3mxF4wCjyxcpOnyg')

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')

bot.load_extensions_from('./extensions')
bot.run()
