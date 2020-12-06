items=list(map(int, input("please enter items of your list seperated by space:").split()))
setOfListe=set(items)
newListe=[]
for element in setOfListe:
  newListe.append(element)
  newListe.sort(reverse=True)
print(newListe)
#I had to use map because 009 was reading as less than 09 and I couldn't find any better solution for now#