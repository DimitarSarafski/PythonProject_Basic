hour_of_the_exam = int(input())
minutes_of_the_exam = int(input())

hour_of_the_arr = int(input())
minutes_of_the_arr = int(input())

exam_tine_in_minutes = (hour_of_the_exam * 60) + minutes_of_the_exam
arr_time_in_minutes = (hour_of_the_arr * 60) + minutes_of_the_arr

time_diff = exam_tine_in_minutes - arr_time_in_minutes

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_diff)
result = ""
if(minutes >= 60):
    hours = minutes// 60
    minutes = minutes % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes> 0:
    result = f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)