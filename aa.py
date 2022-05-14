import discord
from discord.ext import commands

TOKEN = 'OTc0Njk4NDg0OTAzMDg0MDky.GUr7t-.BBPJqBVRCVI_QCxpnzRvxq0B5hAL7ObB8dQW-k'
bot = commands.Bot(command_prefix='$')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

bot.run(TOKEN)
