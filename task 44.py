user_name = input()
vowels = ['a', 'e', 'i', 'o', 'u', ]
vowel_count = 0
count = 0
while count < len(user_name):
    if user_name[count] in vowels:
        vowel_count += 1
    count += 1
print("there are", vowel_count, ' vowel in your name', user_name)