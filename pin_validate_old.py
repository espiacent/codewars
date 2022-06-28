def validate(pin):
  try:
    int(pin)
  except:
    return False
  if "-" in pin:
    return False
  elif " " in pin:
    return False
  elif "+" in pin:
    return False
  elif len(pin) == 4 or len(pin) == 6:
    return True
  else:
    return False

print(validate('098989'))