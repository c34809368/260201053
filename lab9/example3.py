def get_rec_evens(liste):
  count=0
  if len(liste)==0:
    return 0
  else:
    for item in liste:
      if item%2==0:
        count+=1
        liste.remove(item)
        get_rec_evens(liste)
      else:
        continue
  return count

print(get_rec_evens([1,2,3,4,5,6]))