item=input("please enter items of your list seperated by space:")
liste=item.split()
setOfListe=set(liste)
newListe=[]
for element in setOfListe:
  newListe.append(element)
  newListe.sort(reverse=True)
print(newListe)