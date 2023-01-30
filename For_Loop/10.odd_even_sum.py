line_of_numbers = int(input())
left_sum = 0
right_sum = 0

for index in range(line_of_numbers):
    current_number = int(input())
    if index % 2 == 0:
        left_sum = left_sum + current_number
    else:
        right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f"Yes")
    print(f"Sum = {left_sum}")
else:
    print("No")
    print(f"Diff = {abs(right_sum - left_sum)}")