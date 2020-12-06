books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict=dict()
for i in range(len(books)):
  key=books[i]
  chars=len(key)
  unique=len(set(key))
  value=chars,unique
  book_dict[key]=value

print(book_dict)



