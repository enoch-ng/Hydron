# Hydron
A better Discord bot for Warframe notifications.

## Getting the bot on your server
You can invite my instance of the bot to your server here: (link)

## Getting started

## Advanced functionality

## Running your own instance

Dependencies:
* Python >=3.5
* discord.py

Get Python here: https://www.python.org/downloads/

For more information on installing discord.py, go here: https://github.com/Rapptz/discord.py

To use this bot, you need to create a file named "settings.json" in the data/ folder. You can also find an example settings file there.

In order to obtain a token, create a new bot user here: https://discordapp.com/developers/applications/me

In order to obtain a Steam user API key, go here: https://steamcommunity.com/dev/apikey

The complete list of options is as follows:
```
{
	"token": String that will be the bot's token
	"prefix": String representing the command prefix, defaults to ;
	"owner": String representing your Discord user ID
}
```

Only `token` is required. The bot will attempt to determine its owner automatically if `owner` is not provided.

## Bugs, feature requests, and development updates
To report a bug or offer a suggestion, feel free to open an issue on this repository or join our Discord server here: https://discord.gg/KFmrB4E

## Todo
* Interactive setup
* Sorties
* Invasions
* Acolytes
