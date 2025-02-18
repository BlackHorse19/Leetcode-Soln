#In this code base we try to deal with interchanging the vowels position or we can say interchange the vowel position.
#And add the 2 words as well to return a string.
def merge(word1, word2):
    result =[]
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        
        i += 1
    return ''.join(result)
    
x = str(input())
y = str(input())

word = merge(x,y)
print(word)
