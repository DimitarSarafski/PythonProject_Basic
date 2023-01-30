#input
day_off = int(input())

#logic and outputs

time_off_play = day_off * 127
time_work = 365 - day_off
time_work_play = time_work * 63

time_play_combine = time_off_play + time_work_play

if time_play_combine <= 30000:
    time_in_minutes = 30000 - time_play_combine
    hours = int(time_in_minutes / 60)
    minutes = time_in_minutes - (hours * 60)
    print("Tom sleeps well ")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    time_in_minutes = time_play_combine - 30000
    hours = int(time_in_minutes / 60)
    minutes = time_in_minutes - (hours * 60)
    print("Tom will run away ")
    print(f"{hours} hours and {minutes} minutes more for play")

