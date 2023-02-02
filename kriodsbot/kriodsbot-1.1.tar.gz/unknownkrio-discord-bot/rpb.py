class RayaPraim:
    def __init__(self):
        # coding=UTF-8
        from ast import Try
        from email import message
        from email.base64mime import body_encode
        import datetime
        import datetime
        import os
        import os
        import discord
        from discord.ext.commands import has_permissions
        from discord.ext import commands
        import asyncio
        from asyncio import sleep
        from asyncio import sleep
        import smtplib as smtp
        from email.mime.text import MIMEText
        from email.header import Header

        def prompt(prompt):
            return input(prompt).strip()

        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        token = "OTg4NjgzNzE0OTc0MzE4NjMy.GLy_rD.Vtwc1spZPV1CaxYZxXCzSkWBPvbj9v4WxLs5uA"
        help_command = commands.DefaultHelpCommand(
            no_category = 'Команды:'
        )
        client = commands.Bot(command_prefix='+', intents = intents, help_command = help_command) # инициализируем бота с вашим префиксом

        @client.event
        async def on_ready():
            await client.change_presence(status=discord.Status.online, activity=discord.Game("+help | Python"))
            print("Succesful")
        #
        @client.event
        async def on_message(message: discord.Message):
            time=datetime.datetime.now(tz=None)
            if message.guild is None and not message.author.bot:
                print(f"[{time}] {message.author} пишет вам: {message.content}")
                user = await client.fetch_user(810914294437773352)
                embed = discord.Embed(
                title = 'Вам пришло сообщение',
                color = discord.Colour.blue(),
                description = f'{message.author} пишет вам: {message.content}'
                )
                embed.set_author(name=f'{time}')
                await user.send(embed=embed)
            await client.process_commands(message)
        #
        @client.command(help='Отправить личное сообщение')
        async def личка(ctx, anon:str, user_to_dm: discord.Member, message: discord.Message):
            if anon==False:

                embed = discord.Embed(
                title = 'Вам пришло сообщение',
                color = discord.Colour.blue(),
                description = f'{message.author} пишет вам: {message.content}'
                )
                embed.set_author(name=f'{time}')
                await user_to_dm.send(embed)
            elif anon==True:
                embed = discord.Embed(
                title = 'Вам пришло анонимное сообщение',
                color = discord.Colour.purple(),
                description = f'ANONYMOUS пишет вам: {message.content}'
                )
                await ctx.message.delete()
        #спам
        @client.command(help = 'Спамит введённое сообщение. +spam <кол-во раз>, <сообщ>')
        async def спам(ctx, num: int, *, message):
            for _ in range(num):
                await ctx.send(message)
        # Отправка почты
        @client.command(pass_context=True, help = 'Отправит электронное письмо. Использование: email <адрес эл.почты> <тема> <текст>', category = 'main')
        async def письмо(ctx, to, subject, *, text):
            await ctx.message.delete()

            login = 'raiyapraim@ya.ru'
            password = 'rzmcabrnrpntimgo'

            try:
                login = 'raiyapraim@yandex.ru'
                password = 'rzmcabrnrpntimgo'

                mime = MIMEText(text, 'plain', 'utf-8')
                mime['From'] = 'raiyapraim@yandex.ru'

                server = smtp.SMTP('smtp.yandex.ru', 587)

                server.starttls()
                server.login(login, password)
                mime['Subject'] = Header(subject, 'utf-8')

                server.sendmail(login, to, mime.as_string())

                #Эмбеды
                embedyes = discord.Embed(
                    title = "Успешно",
                    color = discord.Colour.green()
                )

                embedyes.set_author(name='Письмо')
                embedyes.add_field(name='Отправлено с raiyapraim@yandex.ru', value="```\n{Всё отправилось!}\n```")
                await ctx.send(embed=embedyes)
            except:
                embedn = discord.Embed(
                    title = 'Неуспешно',
                    color = discord.Colour.red()
                )

                embedn.set_image(url='https://flyclipart.com/thumb2/red-cross-mark-clipart-227244.png')
                embedn.set_author(name='Письмо')
                embedn.add_field(name='Не удалось отправить сообщение')
                await ctx.send(embed=embedn)
            

        #
        @client.command(pass_context=True, help = 'Очистить сообщения')
        @has_permissions(manage_messages = True)
        async def очистить(ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            print(f'Команда "очистить" была использована {ctx.author.name}')
        #
        @client.command( pass_context = True, help = 'Выгнать пользователя' )
        @has_permissions( kick_members = True )
        async def кик( ctx, member: discord.Member, *, reason = 'Лох' ):
            try:
                await member.kick( reason = reason )
                await ctx.message.delete()
                print(f'Команда kick была использована {member}')
                embedyes = discord.Embed(
                title = 'Успешно',
                color = discord.Colour.green(),
                description = f'{member} был кикнут по причине: {reason}'
                )
                embedyes.set_author(name='Кик')
                await ctx.send(embed=embedyes)

            except:
                embedn = discord.Embed(
                title = 'Неуспешно',
                color = discord.Colour.red(),
                description = f'Не удалось кикнуть {member}'
                )
                embedn.set_author(name='Кик')
                await ctx.send(embed=embedn)
        #
        @client.command(pass_context = True, help = 'Пингануть пользователя. ping <пользователь> <кол-во>')
        async def пинг(ctx, member: discord.Member, count: int):
            print(f'Команда ping была использована {ctx.author.name} на {member}')
            for _ in range(count):
                await ctx.send(member)
        #

        @client.command( pass_context = True, help = 'Забанить пользователя' )
        @has_permissions( ban_members = True )

        async def бан( ctx, member: discord.Member, *, reason = None ):
            await member.ban( reason = reason )
            await ctx.message.delete()
            await ctx.send( f'{ member.mention } был забанен по причине: {reason}')
            print( f'{ member.mention } был забанен пользователем {ctx.author.name}')
        #
        @client.command()
        async def занят(ctx, help='Перевод в режим Занят. Доступен только создателю бота'):
            if str(ctx.message.author) == "??????#7270":
                await client.change_presence(status=discord.Status.dnd, activity=discord.Game("+help | Python"))
            else:
                embed = discord.Embed(
                    title = "Неудача",
                    color = discord.Colour.red()
                )

                embed.set_author(name='Перевод в режим Занят')
                embed.add_field(name='Вы не создатель бота')
                await ctx.send(embed=embed)
        #
        @client.command()
        async def онлайн(ctx, help='Перевод в режим Онлайн. Доступен только создателю бота'):
            if str(ctx.message.author) == "??????#7270":
                await client.change_presence(status=discord.Status.online, activity=discord.Game("+help | Python"))
            else:
                embed = discord.Embed(
                    title = "Неудача",
                    color = discord.Colour.red()
                )

                embed.set_author(name='Перевод в режим Онлайн')
                embed.add_field(name='Вы не создатель бота')
                await ctx.send(embed=embed)
        #
        @client.command()
        async def техработы(ctx, help='Доступен только создателю бота'):
            if str(ctx.message.author) == "??????#7270":
                await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Технические работы"))
            else:
                embed = discord.Embed(
                    title = "Неудача",
                    color = discord.Colour.red()
                )

                embed.set_author(name='Перевод в режим Тех.Работы')
                await ctx.send(embed=embed)
        #
        @client.command(help = 'Разбанить пользователя')
        @has_permissions(ban_members=True)
        async def разбанить(ctx, member: discord.Member, reason):
            await unban(member, reason=None)
            await ctx.send(f'{member} был разбанен по причине {reason}')

        #
        @client.command( pass_context = True, help = 'Заглушить пользователя' )
        @has_permissions( manage_messages = True )
        async def заглушить(ctx, user: discord.Member, time: int, reason):
            minutes=time*60
            await user.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=minutes), reason=reason)
            embedy = discord.Embed(
                title = "Получилось",
                color = discord.Colour.green()
            )

            embedy.set_author(name='Заглушить пользователя')
            await ctx.send(embed=embedy)
        #
        @client.command(help = 'Повторит сообщение. s <текст>')
        @has_permissions( manage_messages=True )
        async def повтори(ctx, *, arg):
            try:
                await ctx.message.delete()
                await ctx.send(arg)
            except:
                await ctx.send('У тебя нет прав')
            print(f'Команда say была использована {ctx.author.name}')

        #Команды закончились

        client.run(token)
