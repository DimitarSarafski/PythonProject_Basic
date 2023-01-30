line_of_numbers = int(input())
left_sum = 0
right_sum = 0


for index in range(line_of_numbers * 2 ):
    left_sum = left_sum + int(input())
    right_sum = right_sum + int(index())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")