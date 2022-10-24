# discord bots
In this repository you can find different Discord bots developed using python with the library discord.py. For more info about the discord.py library please check more info in the following link https://discordpy.readthedocs.io/en/stable/index.html#getting-started . You might need to install the python libraries dependancies according to each of the scripts.  

## Welcome Bot
welcomebot.py 

This discord bot send a random message when a new member joins the server. In the code you wil find that there is an array wich contains the different messages you would like to send, amend that according to your needs. The list of messages can be big or smaill, it is up to you, the function get_random_message() will return a randome message within the messages list. Notice that you will need to set the serverid and channelid (you can find those parameters at the beggining of the script) in wich you want to send the message

## Reply bot
replybot.py

This bot will reply with a Hello! message everytime a member send a $hello message. 
