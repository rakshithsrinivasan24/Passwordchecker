# L = ['Batman', 'Spiderman', 'Avengers', 'Iron Man']
# L.append('Superman')
# L.insert(2, 'Game of Thrones')

# for i in L:
#     print (i)

# L = ['Will', 'Arya', 'Jack', 'Syon', 'Neil']
# L[0] = 'Bijan'
# L.insert(3, 'Bohan')
# L.append('Nihaal')
# L.sort()
# print (L)
# L2 = L[::]
# print (L2)

# X = "Hello, how are you?"
# y = X.split()
# z = list(X)
# print (z)

# x = ['03', '02', '2024']
# y = "/".join(x)
# print(y)

x = "apple"
L = []
while True:
    y = input("Guess the password: ")
    if y == x:
        print("Access Granted")
        print("Wrong passwords tried", L)
        break
    else:
        print("Access Denied")
        L.append(y)
