import discord
import os
from dotenv import load_dotenv

def main():
  client = discord.Client()

  @client.event
  async def on_ready():
    print(f'KONO {client.user} DA!')

  client.run(ENV['TOKEN'])

if __name__ == '__main__':
  load_dotenv()
  ENV = {}
  ENV['TOKEN'] = os.getenv('DISCORD_TOKEN')
  main()
