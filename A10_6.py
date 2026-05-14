def check_position(pos):
        first = 'abcdefgh'
        second = '12345678'
        if pos[0] in first and pos[1] in second and len(pos) == 2:
            return True
        else:
            return False
while True:
    user = input("Enter a legal chess coordinate: ")
    if check_position(user) == True:
        print(True)
        break
 
    
