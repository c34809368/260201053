import time
def timer(t):
  if t==0:
    print("alarm!!")
  else:
    for _ in range(t):
      print(t)
      time.sleep(5)
      t=t-1
      return(timer(t))
t=int(input("enter an integer:")) 
timer(t)
