N = int(input("Enter a number: "))
L = []
for i in range(N):
    P = input("Enter a word: ")
    L.append(P)
def alphabetize():
    L.sort()
    print(*L)
alphabetize()  
