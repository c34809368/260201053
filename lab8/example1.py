def sumliste(liste):
  sumnums=0
  for i in liste:
    sumnums+=i
  return(sumnums)

liste=[12, -7, 5, -89.4, 3, 27, 56, 57.3]
summation=sumliste(liste)
print(round(summation,1))