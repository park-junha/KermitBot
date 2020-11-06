import discord
import os
from dotenv import load_dotenv

def LOG_C(message):
  print(f'client ({message.author}) sent: {message.content}')

def LOG_S(client, response):
  print(f'server ({client.user}) sent: {response}')

class KermitClient(discord.Client):
  async def on_ready(self):
    print(f'bot connected: {client.user}')
    for guild in client.guilds:
      if guild.name == ENV['GUILD']:
        print(f'bot found discord guild: {guild.name}')

  async def on_message(self, message):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == client.user:
      return

    if message.content == '$konobotda':
      LOG_C(message)
      response = 'It was me, Kermit Bot!'
      await message.channel.send(response)
      LOG_S(client, response)

if __name__ == '__main__':
  load_dotenv()
  ENV = {
    'TOKEN': os.getenv('TOKEN'),
    'GUILD': os.getenv('GUILD'),
  }
  client = KermitClient()
  client.run(ENV['TOKEN'])
