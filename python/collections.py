alist = [10,20,30,40,50]

alist.append(5)
alist.append(6)
alist.append(7)
print(alist)

alist.remove(50)
alist.pop(2)
print(alist)
alist.sort()
print(alist)

dog = "dog"
dogs = dog * 3
print(dogs)

empty = [0] * 10
empty[0] = 10

empty = []
for val in alist:
    if val >= 7 and val <= 20:
        empty.append(val)
print(empty)

# Comprehension
squares = []
for i in range(1,10):
    squares.append(i*i)

print(squares)
squares_copy = squares
# squares[0] = 9000
print(squares)
squares_copy = [value for value in squares if value > 9]
squares[0] = 9000
print(squares_copy)

evens_num = [i for i in range(2,101) if i % 2 == 0]
print(evens_num)

# Sets

aset = {1,2,700,5,6,100} # does not keep the order that you give it
print(aset)

dups = [1,2,2,3,3,6,6,7,7,1]
no_dups = set(dups)
print(no_dups)
# no_dups[0] = 100 doesn't work
no_dups.add(4) # hw2
print(no_dups)

#Dictionaries

fav_foods = {"kathleen" : "pizza", "george" : "lobster", "nick" : "pasta bolognese", "kai" : "alfredo"}

kai_ff = fav_foods["kai"]
print(kai_ff)
print(fav_foods)

# kim_ff = fav_foods["kim"] #key error 
if "kim" in fav_foods:
    print(fav_foods["kim"])
else:
    fav_foods["kim"] = "cereal"

for key in fav_foods:
    print(key, "fav food is", fav_foods[key])

for key, value in fav_foods.items(): #don't use unless you need the value
    print(key, "fav food is", fav_foods[key])

