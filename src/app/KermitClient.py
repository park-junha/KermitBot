from discord import Client
from random import randint

class KermitClient(Client):
  def set_env(self, env):
    self.local_env = {
      'guild': env['guild']
    }

  def LogClient(self, message):
    print(f'client ({message.author}) sent: {message.content}')

  def LogServer(self, response):
    print(f'server ({self.user}) sent: {response}')

  async def on_ready(self):
    print(f'bot connected: {self.user}')
    for guild in self.guilds:
      if guild.name == self.local_env['guild']:
        print(f'bot found discord guild: {guild.name}')

  async def on_message(self, message):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == self.user:
      return

    if message.content == '$jojo':
      self.LogClient(message)

      responses = [
        'It was me, Kermit Bot!',
        'KONO DIO DA',
        'Goodbye, JoJo!',
        'ROOO DOOO ROOO RAAA DAAA',
        'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA',
        'WRRRRYYYYY',
        'Daga kotowaru!',
        'I can even lift this rock?',
        'How many slices of bread have you eaten?',
        'NOROI NOROI ZA WARUDO WA SAIKYO NO STANDO DA'
      ]
      response = responses[randint(0, len(responses) - 1)]
      await message.channel.send(response)
      self.LogServer(response)
