word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
len1 = len(word1)
len2 = len(word2)

def compare_string():
    if len1 > len2 + 1:
        difference = len1 - len2
        print(f"{word1} has {difference} more characters than {word2}.")
        
    if len2 > len1 + 1:
        difference = len2 - len1
        print(f"{word2} has {difference} more characters than {word1}.")
    
    if len1 > len2:
        difference = len1 - len2
        print(f"{word1} has {difference} more character than {word2}.")
    if len2 > len1:
        difference = len2 - len1
        print(f"{word2} has {difference} more character than {word1}.")
    elif len2 == len1:
        print("Both names have the same number of characters.")
compare_string()  
