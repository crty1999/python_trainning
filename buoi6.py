#Bai1

friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

#a
print(f"Length of {friends} is {len(friends)}")

#b
first = friends[0]
mid   = friends[1]
last  = friends[-1]

print("First value:\n", first)
print("Mid value:\n", mid)
print("Last value:\n", last)

print(type(first))
print(type(mid))
print(type(last))

#c
friend_name = input("Nhập vào tên người bạn\t: ")
gender      = input("Nhập vào giới tính\t: ")

friend_tuple = (friend_name, gender)

friends.append(friend_tuple)

print(friends)

#Bai2

set_name = set()

#a

set_name.add('Anna')

#b
set_name.update(('Kenny', 'Jen', 'Danny'))

#c
print(set_name)
print(len(set_name))

#d
set_name.remove('Jen')

#e
set_name.clear()
print(set_name)
