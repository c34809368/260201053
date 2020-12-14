def sumliste(liste):
  sumnums=0
  for i in liste:
    sumnums+=i
  result=sumnums**2
  return(result)

liste=[12, -7, 5, -89.4, 3, 27, 56, 57.3]
resultLast=sumliste(liste)
print(resultLast)