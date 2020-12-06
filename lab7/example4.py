password=input("please enter a passoword:")
digit=False
up=False
low=False
for char in password:
  if char.isdigit():
    digit=True
  if char.isupper():
    up=True
  if char.islower():
    low=True
if digit== True and up== True and low== True:
  print("It is a valid password.")
else:
  print("It is not a valid password.")