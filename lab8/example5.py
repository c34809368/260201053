def password_checker(password):
  level=0
  if (len(password)<8) or (" " in password):
    print("It is not valid")
    return level
  else:
    for char in password:
      if char.isdigit():
        level+=1
        break
    for char in password:
      if char.isalpha():
        level+=1
        break
    for char in password:
      if not char.isnumeric() and not char.isdigit() and char!=" ":
        level+=1
        break
  return level


def main():
  password=input("please enter a password:")
  level=password_checker(password)
  print("Security level of the entered password is:", level)

main()