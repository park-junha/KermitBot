from app.app import KermitClient
from dotenv import load_dotenv
import os

if __name__ == '__main__':
  load_dotenv()
  env = {
    'token': os.getenv('TOKEN'),
    'guild': os.getenv('GUILD'),
    'announcements': os.getenv('ANNOUNCEMENTS')
  }
  client = KermitClient()
  client.set_env(env)
  client.run(env['token'])
