from discord import Client
from app.commands import jojo, gamers
from app.events import poll

# TODO: replace with db call
def TEMPORARY_get_poll_params():
  return {
    'message': 'What games would you guys like to play this weekend?',
    'options': [
      {
        'name': 'skribbl.io',
        'emoji_id': 768246281100853258
      },
      {
        'name': 'Among Us',
        'emoji_id': 756211678579785863
      }
    ]
  }

class KermitClient(Client):
  def set_env(self, env):
    self.local_env = {
      'guild': env['guild'],
      'announcements': env['announcements']
    }
    try:
      self.local_env['event_onstart'] = env['event_onstart']
    except KeyError:
      self.local_env['event_onstart'] = None
      print('WARN: env not supplied with event_onstart, skipping')

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
        self.env_guild = guild
        print(f'bot found discord guild: {self.env_guild.name}')
        break
    for text_channel in self.env_guild.text_channels:
      if text_channel.name == self.local_env['announcements']:
        self.announcements = text_channel
        print(f'bot found text channel: {self.announcements.name}')
        break
    if self.local_env['event_onstart'] != None:
      event_name: str = self.local_env['event_onstart']['event_name']
      await self.run_event(event_name)
      print(f'bot completed running event: {event_name}')
      if self.local_env['event_onstart']['close_after'] == True:
        print('closing bot connection...')
        await self.close()
        print('bot connection closed!')
      return

  async def on_message(self, message):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == self.user:
      return

    if message.content == '$jojo':
      await self.run_function(jojo.respond, message)

    if message.content.lower() == 'gamers':
      await self.run_function(gamers.respond, message)

  async def run_event(self, event: str):
    message: str = ''

    if event == 'poll':
      params = TEMPORARY_get_poll_params() # TODO: replace with db call
      # Add announcements channel and emojis to params
      params['channel'] = self.announcements
      for option in params['options']:
        option['emoji'] = self.get_emoji(option['emoji_id'])

      self.LogServer(await poll.run_event(params))
      return

    error: str = 'Unknown event ' + event + ' was passed to ' \
      + 'KermitClient.run_event'
    print(f'FATAL: {error}')
    raise Exception(error)
