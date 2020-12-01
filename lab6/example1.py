email="ceng113@example.com"
email=email.lower()
user=input("please enter the e-mail:")
user=user.lower()
newuser=user.split("@")
beforeat,afterat=newuser[0],newuser[1]
x=str(newuser[0])
x.replace(".","")
lastuser=x+str(afterat)
if lastuser==email:
  print("True email!")
else:
  print("Wrong email!")






