password="abc123"
while True:
  user=input("please enter the password:")
  if user == password:
    print("Welcome!")
    break
  elif user=="help":
    print("a")
    continue
  else:
    print("Wrong!")
    continue


