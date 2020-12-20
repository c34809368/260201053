def is_prime(number):
  count=0
  isPrime=False
  for i in range(1,number+1):
    if number%i==0:
      count+=1
  if count==2:
    isPrime=True
  return(isPrime)

def print_primes_between(num1,num2):
  for i in range(num1,num2+1):
    if is_prime(i)==True:
      print(i)

def main():
  num1=int(input("enter the first number:"))
  num2=int(input("enter the second number:"))
  print("Prime numbers between",num1,"and",num2,"are:")
  print_primes_between(num1,num2)

main()