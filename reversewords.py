#In this problem, we are presented with a string s that consists of words separated by spaces.
#Our objective is to reverse the order of these words and return the resulting string with the words placed in opposite order from that of the input.
#A word is defined as a sequence of non-space characters, meaning that punctuation and letters are considered part of a word but spaces are not. 
#Additionally, the given string s could have leading or trailing spaces and could also contain multiple spaces between words.

def reverseWords(s):
    
    words = s.split()
    rw = reversed(words)

    return ' '.join(rw)

x = str(input()) #input your words or sentences with spaces
y = reverseWords(x)
print(y)
