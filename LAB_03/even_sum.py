print("--- Using a For Loop ---")
sum_for = 0

# range(1, 51) starts at 1 and stops before 51
for num in range(1, 51):
    if num % 2 == 0:  # Check if the number is even
        sum_for += num

print(f"The sum of even numbers from 1 to 50 is {sum_for}.\n")


print("--- Method 2: Using a While Loop ---")
sum_while = 0
current_num = 1

# Manually from 1 to 50
while current_num <= 50:
    if current_num % 2 == 0:
        sum_while += current_num
    current_num += 1  

print(f"The sum of even numbers from 1 to 50 is {sum_while}.\n")
