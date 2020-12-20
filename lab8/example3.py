import random

def get_rand_list(b,e,N):
  randomList=random.sample(range(b,e),N)
  return(randomList)

def get_overlap(list1,list2):
  list3=list()
  for i in list1:
    if i in list2:
      list3.append[i]
  return(list3)

def main():
  list1=get_rand_list(0,10,5)
  list2=get_rand_list(0,10,5)
  print("First list:\n",list1)
  print("Second list:\n",list2)
  list3=get_overlap(list1,list2)
  print("Intersection list of these two lists:",list3)
  
main()

