def get_rec_evens(liste):
  count=0
  if len(liste)==0:
    return 0
  else:
    for item in liste:
      if item%2==0:
        count+=1
        liste.remove(item)
        return get_rec_evens(liste)
      else:
        continue
  return count

liste=[1,2,3,4,5,6]
print(get_rec_evens(liste))