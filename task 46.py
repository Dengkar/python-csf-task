user_name = int(input())
factorial = 1
while user_name > 0:
    factorial *= user_name
    user_name -= 1
print(factorial)