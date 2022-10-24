# Discord bots
In this repository you can find different Discord bots developed using python with the library discord.py. For more info about the discord.py library please check more info in the following link https://discordpy.readthedocs.io/en/stable/index.html#getting-started . You might need to install the python libraries dependancies according to each of the scripts. 

## Prerequisites
Check the python script you want to use for developing your bot and install the python libraries it contains. Notice that these scripts use a .env file that you will need to create named .env (the same) so you can put there your discord app token, althought it is not neccesary it is a good practice if you would like to share your code instead of hardcoding your token in the scripts. 

.env example content:
token = 'yourdiscordapptokenhere'

## Welcome Bot
welcomebot.py 

This discord bot send a random message when a new member joins the server. In the code you wil find that there is an array wich contains the different messages you would like to send, amend that according to your needs. The list of messages can be big or smaill, it is up to you, the function get_random_message() will return a randome message within the messages list. Notice that you will need to set the serverid and channelid (you can find those parameters at the beggining of the script) in wich you want to send the message. 

<img src='https://github.com/adrianrodriguez-io/discord-bots/blob/main/images/welcomebot.png'></img>

## Reply bot
replybot.py

This bot will reply with a Hello! message everytime a member send a $hello message. 
