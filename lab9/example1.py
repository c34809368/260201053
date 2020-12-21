def harmonic_sum(num):
  if num==1:
    return 1
  else:
    return harmonic_sum(num-1) + (1/num)

num=int(input("Enter a number:"))
print(harmonic_sum(num))  
  