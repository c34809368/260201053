books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict={}
for i in range(len(books)):
  key=books[i]
  chars=len(key)
  unique=len(set(key))
  value=chars,unique
  book_dict[key]=value

print(book_dict)

#continue 
for book in books:
  chars,unique=book_dict[book]
  book_dict[book]=chars,unique,((chars+unique)/2)

print(book_dict)


