from discord import Client
from app.commands import jojo, gamers, copy_message
from app.events import poll

class KermitClient(Client):
  def __init__(self, *args, **kwargs):
    super(KermitClient, self).__init__(*args, **kwargs)
    self.copy_flip = False

  # TODO (junha-park): rework this and integrate into __init__ perhaps
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

  async def run_function(self, run_command, message, *args):
    self.LogClient(message)
    response: str = run_command(*args)
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

#   ### TODO (junha-park): remove this before merging PR
#   for emoji in self.env_guild.emojis:
#     print(emoji.id, emoji.name)
#   ###

    if self.local_env['event_onstart'] != None:
      event_name: str = self.local_env['event_onstart']['event_name']
      await self.run_event(event_name)
      print(f'bot completed running event: {event_name}')
      if self.local_env['event_onstart']['close_after'] == True:
        print('closing bot connection...')
        await self.close()
        print('bot connection closed!')
      return

  def toggle_copy_flip(self) -> str:
    self.copy_flip = not self.copy_flip
    return f'toggled copy_flip to: {self.copy_flip}'

  async def on_message(self, message):
    # Ignore messages from the bot itself to avoid getting stuck in a loop
    if message.author == self.user:
      return

    if message.content == '$jojo':
      await self.run_function(jojo.respond, message)
    if message.content == '$togglecopyflip':
      await self.run_function(self.toggle_copy_flip, message)
    if message.content.lower() == 'gamers':
      await self.run_function(gamers.respond, message)

    if message.author.display_name == 'Kermit Black' and \
      self.copy_flip == True:
      await self.run_function(copy_message.respond, message, \
        message.content)

  def get_static_message_params(self, message):
    params = {
      'channel': self.announcements,
      'message': message,
      'react_only': True,
      'options': []
    }
    return params

  # TODO: replace with db call
  def TEMPORARY_get_poll_game_params(self):
    params = {
      'channel': self.announcements,
      'message': 'What games would you guys like to play tonight? ' + \
        'Feel free to vote for more than one!',
      'react_only': False,
      'options': [
        {
          'name': 'skribbl.io',
          'emoji_id': 768260649779200070
        },
        {
          'name': 'Jackbox',
          'emoji_id': 768246281100853258
        },
        {
          'name': 'Among Us',
          'emoji_id': 756211678579785863
        }
      ]
    }

    # Add custom emojis to params
    for option in params['options']:
      option['emoji'] = self.get_emoji(option['emoji_id'])

    return params

  # TODO: replace with db call
  def TEMPORARY_get_poll_gametime_params(self):
    params = {
      'channel': self.announcements,
      'message': 'What times work best for you this weekend? Select all ' +
        'that apply (all Pacific Time PM):',
      'react_only': True,
      'options': [
        {
          'name': '5:00PM PST',
          'emoji': '\U0001F554'
        },
        {
          'name': '5:30PM PST',
          'emoji': '\U0001F560'
        },
        {
          'name': '6:00PM PST',
          'emoji': '\U0001F555'
        },
        {
          'name': '6:30PM PST',
          'emoji': '\U0001F561'
        },
        {
          'name': '7:00PM PST',
          'emoji': '\U0001F556'
        },
        {
          'name': '7:30PM PST',
          'emoji': '\U0001F562'
        },
        {
          'name': '8:00PM PST',
          'emoji': '\U0001F557'
        },
        {
          'name': '8:30PM PST',
          'emoji': '\U0001F563'
        },
        {
          'name': '9:00PM PST',
          'emoji': '\U0001F558'
        },
        {
          'name': '9:30PM PST',
          'emoji': '\U0001F564'
        },
        {
          'name': '10:00PM PST',
          'emoji': '\U0001F559'
        },
        {
          'name': '10:30PM PST',
          'emoji': '\U0001F565'
        },
        {
          'name': '11:00PM PST',
          'emoji': '\U0001F55A'
        },
        {
          'name': '11:30PM PST',
          'emoji': '\U0001F566'
        }
      ]
    }
    return params

  async def run_event(self, event: str):
    message: str = ''

    if event == 'poll_games':
      # TODO: replace the following line with db call
      params = self.TEMPORARY_get_poll_game_params()
      self.LogServer(await poll.run_event(params))
      return
    if event == 'poll_gametime':
      # TODO: replace the following line with db call
      params = self.TEMPORARY_get_poll_gametime_params()
      self.LogServer(await poll.run_event(params))
      return
    if event == 'static_message':
      params = self.get_static_message_params(
        self.local_env['event_onstart']['message'])
      self.LogServer(await poll.run_event(params))
      return

    error: str = 'Unknown event ' + event + ' was passed to ' \
      + 'KermitClient.run_event'
    print(f'FATAL: {error}')
    raise Exception(error)
