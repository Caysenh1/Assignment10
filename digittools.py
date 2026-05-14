def sum_digits(num):
    num = input("Enter a number: ")
    List = []
    pos = 0
    for i in range(len(num)):
        List.append(int(num[pos]))
        pos += 1
    total = (sum(List))
    print(total)
        
