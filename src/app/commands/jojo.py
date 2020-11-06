from random import randint

def respond() -> str:
  responses = [
    'It was me, Kermit Bot!',
    'KONO DIO DA',
    'Goodbye, JoJo!',
    'ROOO DOOO ROOO RAAA DAAA',
    'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ' +
      'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ' +
      'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ' +
      'ORA ORA ORA ORA ORA ORA ORA ORA',
    'WRRRRYYYYY',
    'Daga kotowaru!',
    'I can even lift this rock?',
    'How many slices of bread have you eaten?',
    'NOROI NOROI ZA WARUDO WA SAIKYO NO STANDO DA'
  ]
  return responses[randint(0, len(responses) - 1)]
