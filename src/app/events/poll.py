async def run_event(params):
  sent_message = await params['channel'].send(params['message'])
  await sent_message.add_reaction(params['emoji'])
