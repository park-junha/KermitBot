# TODO: get rid of this file eventually

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
      'event_name': 'poll',
      'close_after': True
    }
  }
  client = KermitClient()
  client.set_env(env)
  print('Starting client...')
  await client.start(env['token'])
# print('Running poll event...')
# await client.run_event('poll')
# print('Closing client...')
# await client.close()
  print('Done!')
  return

if __name__ == '__main__':
  asyncio.run(main())
