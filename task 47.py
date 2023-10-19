user_name = int(input())
factorial = 1
for i in range(1, user_name+1):
    factorial *= user_name
    user_name -= 1
print(factorial)