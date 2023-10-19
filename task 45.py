user_name = input()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
vowel_count = 0
for char in user_name:
    if char in vowels:
        vowel_count += 1
print("there are ",vowel_count, "vowels in your name", user_name)