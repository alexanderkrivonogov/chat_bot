import discord
from discord.ext import commands

intents = discord.Intents.default()  # Создание объекта intents
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    print(author)
    await ctx.send(
        f'Hello, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


bot.run()  # Обращаемся к словарю settings с ключом token, для получения токена
