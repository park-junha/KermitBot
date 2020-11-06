from random import random

def respond() -> str:
  seed: float = random()
  if seed < 0.15:
    return 'FALL DOWN'
  return 'RISE UP'
