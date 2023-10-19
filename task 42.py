user_name = input()
vowels = ['a', 'e', 'i', 'o', 'u']
while any(vowel in user_name for vowel in vowels):
    print('true')
    break
else:
    print("false")



