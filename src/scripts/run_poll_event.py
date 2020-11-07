# This script opens a bot connection, runs the 'poll' event, then closes
# the connection as soon as it finishes.

from app.app import KermitClient
from dotenv import load_dotenv
import os
import asyncio

async def main():
  load_dotenv()
  env = {
    'token': os.getenv('TOKEN'),
    'guild': os.getenv('GUILD'),
    'announcements': os.getenv('ANNOUNCEMENTS'),
    'event_onstart': {
      'event_name': 'poll_games',
      'close_after': True
    }
  }
  client = KermitClient()
  client.set_env(env)
  print('starting client...')
  await client.start(env['token'])
  print('done!')
  return

if __name__ == '__main__':
  asyncio.run(main())
