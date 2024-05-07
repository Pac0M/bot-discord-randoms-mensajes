
# Discord Bot

![Captura de pantalla (178)](https://github.com/Pac0M/bot-discord-randoms-mensajes/assets/119814973/9e54d436-a933-451a-9e8f-e04ea4c98c42)
![Captura de pantalla (177)](https://github.com/Pac0M/bot-discord-randoms-mensajes/assets/119814973/a2e3c617-96b1-469b-9b72-51b01a3dd098)

Este es un bot de Discord sencillo escrito en Python utilizando la librería `discord.py` y `discord_easy_commands`. El bot envía mensajes aleatorios a un canal específico cada cierto tiempo.

## Funcionalidades

- Envía mensajes aleatorios a un canal específico.
- Cambia su estado de actividad cada vez que se conecta.

## Requisitos

- Python 3.6 o superior
- `discord.py` y `discord_easy_commands` (se instalan con `pip install discord.py discord_easy_commands`)

## Configuración

Antes de ejecutar el bot, es necesario configurar las variables de entorno `TOKEN` y `CHANNEL_ID`. Para obtener un token creando una aplicación en [el portal de desarrolladores de Discord](https://discord.com/developers/applications) y generando un token para tu bot. El `CHANNEL_ID` es el ID del canal al que queres que el bot envíe mensajes.


`TOKEN=""`
`CHANNEL_ID=""`


## Uso

Ejecuta el script `bot.py` para iniciar el bot. Asegúrate de que el bot esté invitado a tu servidor de Discord y tenga permisos suficientes para enviar mensajes en el canal especificado.


