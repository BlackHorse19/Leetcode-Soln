vowel = ["a","e","i","o","u"]
word = input("Enter your word:" )
count = 0

for character in word:
    if character in vowel:
        count += 1
print("No. of vowels", count)

countc = 0
for character in word:
    if character not in vowel:
        countc +=1
print("No. of consonants", countc)
