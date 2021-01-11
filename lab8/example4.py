def binary_to_dec(binary_num):
  decimal=0
  for digit in str(binary_num):
    decimal=decimal*2 + int(digit)
  return decimal

binary_num=int(input("please enter a binary number:"))
decimal=binary_to_dec(binary_num)
print(decimal)