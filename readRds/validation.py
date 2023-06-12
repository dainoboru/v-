
def nullCheck(searchWords):
  if searchWords is None:
    return False
  return True
  
def numCheck(searchWords):
  sum = 0
  for word in searchWords:
    sum += len(word)
    if sum > 40:
      return False
  return True
  
def searchWordCheck(searchWords):
  
  if not(nullCheck(searchWords)):
    return False
  if not(numCheck(searchWords)):
    return False
  return True

