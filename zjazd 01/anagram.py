#sprawdz czy podane slowo jest anagramem

word = input("Podaj slowo: ")

no_of_iterations = len(word)//2

for i in range(no_of_iterations):
    if word[i] != word[-1 -i]:
        print("nook")

if word.replace(' ', '').lower() == word[::-1].replace(' ', '').lower():
    print("To jest anagram")
else:
    print("To nie jest anagram")