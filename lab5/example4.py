password="abc123"
user=input("please enter the password:")
while True:
  if user == password:
    print("Welcome!")
    break
  elif user=="help":
    print("a")
    break
  else:
    print("Wrong!")
    break


