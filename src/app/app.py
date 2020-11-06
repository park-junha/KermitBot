from discord import Client
from app.commands import jojo, gamers

class KermitClient(Client):
  def set_env(self, env):
    self.local_env = {
      'guild': env['guild']
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
        print(f'bot found discord guild: {guild.name}')

  async def on_message(self, message: str):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == self.user:
      return

    if message.content == '$jojo':
      await self.run_function(jojo.respond, message)

    if message.content.lower() == '$gamers':
      await self.run_function(gamers.respond, message)
