#The problem presents a challenge to reverse the vowels in a given string s. Vowels include the characters 'a', 'e', 'i', 'o', and 'u', and they can be in both lowercase and uppercase. The goal is to reverse the order of only the vowels in the string without altering the position of the other characters. For instance, given the string "hello", the function should return "holle" since the vowels 'e' and 'o' have been reversed in their positions.

#The intuition behind the solution is to use the two-pointer technique. One pointer (i) starts at the beginning of the string, while the other pointer (j) starts at the end. The pointers move towards each other, and when they each find a vowel, those vowels are swapped. The process continues until the two pointers meet or pass one another, which would mean all vowels have been considered.

#Convert the string to a list: Strings in Python are immutable, which means they cannot be changed after they are created. To efficiently swap elements, the string s is converted into a list of characters, cs = list(s).

#Convert the string to a list: Strings in Python are immutable, which means they cannot be changed after they are created. To efficiently swap elements, the string s is converted into a list of characters, cs = list(s).Initialize two pointers: We declare two pointers i and j. Pointer i is initialized to the start of the list (0), and pointer j is set to the end of the list (len(s) - 1).Create a set of vowels: To facilitate the quick lookup, we create a string vowels, which contains all the lowercase and uppercase vowels ("aeiouAEIOU").

def reverse_vowels(s:str):
    vowels = "aeiouAEIOU"
    cl = list(s) #character list that is converting the string to list
    i, j = 0, len(s)-1 #i = left pointer and j = right pointer

    while i < j:
        while i < j and cl[i] not in vowels:
            i += 1
        while i < j and cl[j] not in vowels:
            j -= 1
        if i < j:
            cl[i], cl[j] = cl[j], cl[i]
            i += 1
            j -= 1
    return "".join(cl)

x = input()
result = reverse_vowels(x)
print(result)

