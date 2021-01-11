def get_reversed(liste):
  if len(liste)==0:
    return []
  else:
    return get_reversed(liste[1:])+[liste[0]]
    
liste=[1,2,3]
print(get_reversed(liste))