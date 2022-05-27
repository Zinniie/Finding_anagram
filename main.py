# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    
        str1 = "mender"
        str2 = "remend"
        str1= input ("Enter first string: ")
        str2= input("Enter second string: ")

        if (sorted (str1) ==sorted (str2)):
            
            return True
        else:
            return False

print(find_anagram("mender","remend"))

  

