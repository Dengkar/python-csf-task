user_name = input()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for name in vowels:
    if name in user_name:
        count += 1
        break
if count > 0:
    print("True")
else:
    print("False")

