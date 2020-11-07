async def run_event(params):
  message_draft: str = params['message'] + '\n'
  for option in params['options']:
    message_draft += '\n- ' + str(option['emoji']) + ' ' + option['name']

  sent_message = await params['channel'].send(message_draft)

  for option in params['options']:
    await sent_message.add_reaction(option['emoji'])

  return message_draft
