fibo = [0, 1]

n = int(input("Enter till when you want fibonacci: "))

for i in range(2 , n):
    num = fibo[i - 1] + fibo[i - 2]
    fibo.append(num)

print(f"fibonacci till {n} is ",fibo)
