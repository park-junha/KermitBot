from discord import Client
from app.commands import jojo, gamers

class KermitClient(Client):
  def set_env(self, env):
    self.local_env = {
      'guild': env['guild'],
      'announcements': env['announcements']
    }

  def LogClient(self, message: str):
    print(f'client ({message.author}) sent: {message.content}')

  def LogServer(self, response: str):
    print(f'server ({self.user}) sent: {response}')

  async def run_function(self, run_command, message):
    self.LogClient(message)
    response: str = run_command()
    await message.channel.send(response)
    self.LogServer(response)

  async def on_ready(self):
    print(f'bot connected: {self.user}')
    for guild in self.guilds:
      if guild.name == self.local_env['guild']:
        self.guild = guild
        print(f'bot found discord guild: {self.guild.name}')
        break
    for text_channel in self.guild.text_channels:
      if text_channel.name == self.local_env['announcements']:
        self.announcements = text_channel
        print(f'bot found text channel: {self.announcements.name}')
        break
    await self.run_event('test')

  async def on_message(self, message):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == self.user:
      return

    if message.content == '$jojo':
      await self.run_function(jojo.respond, message)

    if message.content.lower() == 'gamers':
      await self.run_function(gamers.respond, message)

  async def run_event(self, event: str):
    if event == 'test':
      response: str = 'I AM ONLINE WRRRYYYY'
      await self.announcements.send(response)
      self.LogServer(response)
      return

    error: str = 'Unknown event ' + event + ' was passed to ' \
      + 'KermitClient.run_event'
    print(f'FATAL: {error}')
    raise Exception(error)
