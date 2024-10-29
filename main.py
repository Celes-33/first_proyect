import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_message(message):
    list = ["$Reducir", "$Reutilizar", "$Reciclar", "$Energía", "$Agua", "$Transporte", "$Productos", "$Compostaje", "$Educación", "$Recursos1", "$Recursos2", "$Recursos3", "$RECORDATORIO"]
    plus = ("Estos son los comandos q puedes utilizar para obtener informacion sobre el tema")
    if message.author == bot.user:
        return
    if message.content.startswith('$ayuda'):
        await message.channel.send(plus)
        await message.channel.send(list)
    elif message.content.startswith('$Reducir'):
        await message.channel.send("Compra solo lo necesario y evita productos con mucho empaque.")
    elif message.content.startswith('$Reutilizar'):
        await message.channel.send("Usa bolsas reutilizables, botellas de agua y contenedores de comida.")
    elif message.content.startswith("$Reciclar"):
        await message.channel.send("Separa los residuos reciclables como papel, vidrio, plástico y metal.")
    elif message.content.startswith("$Energía"):
        await message.channel.send("1.Apaga las luces y los electrodomésticos cuando no los estés usando. 2.Usa bombillas de bajo consumo o LED. 3.Aprovecha la luz natural siempre que sea posible.")
    elif message.content.startswith("$Agua"):
        await message.channel.send("1.Cierra el grifo mientras te cepillas los dientes. 2.Toma duchas más cortas. 3.Repara las fugas de agua en casa. ")
    elif message.content.startswith("$Transporte"):
        await message.channel.send("1.Usa la bicicleta, camina o utiliza el transporte público en lugar de conducir. 2.Si necesitas un coche, comparte viajes con amigos o familiares.")
    elif message.content.startswith("$Productos"):
        await message.channel.send("1.Elige productos con certificaciones ecológicas. 2.Compra alimentos locales y de temporada para reducir la huella de carbono.")
    elif message.content.startswith("$Compostaje"):
        await message.channel.send("1.Crea un compost en casa para los restos de comida y residuos orgánicos. 2.El compostaje reduce la cantidad de residuos que van a los vertederos y produce abono natural para las plantas.")
    elif message.content.startswith("$Educación"):
        await message.channel.send("1.Infórmate sobre los problemas ambientales y comparte lo que aprendas con otros. 2.Participa en actividades comunitarias como limpiezas de playas o parques.")
    elif message.content.startswith("$Recursos1"):
        await message.channel.send("Documentales y Libros: Hay muchos documentales y libros sobre el medio ambiente que pueden ofrecerte más información y motivación.")
    elif message.content.startswith("$Recursos2"):
        await message.channel.send("Organizaciones Ambientales: Únete a grupos locales o internacionales que trabajan en la protección del medio ambiente.")
    elif message.content.startswith("$Recursos3"):
        await message.channel.send("Cursos en Línea: Existen cursos gratuitos y de pago sobre sostenibilidad y prácticas ecológicas.")
    elif message.content.startswith("$RECORDATORIO"):
        await message.channel.send("Recuerda que cada pequeño cambio cuenta y que juntos podemos hacer una gran diferencia para proteger nuestro planeta. ¡Buena suerte en tu camino hacia un estilo de vida más ecológico!")
    else:
        await message.channel.send ("Lo siento, no tenemos información sobre eso. Escribe $ayuda si quieres saber la informacion q tenemos") 
 
bot.run("TOKEN")