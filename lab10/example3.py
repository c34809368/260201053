def sum_of_nested_list(a_list):
  if a_list==[]:
    return 0
  else:
    if isinstance(a_list[0],list):
      return sum_of_nested_list(a_list[0]) + sum_of_nested_list(a_list[1:])
    else:
      return a_list[0] + sum_of_nested_list(a_list[1:])


a_list=[[2,3,4],1,[3,2,[2,7]],7,8,9]
print(sum_of_nested_list(a_list))
