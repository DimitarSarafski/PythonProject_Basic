from math import ceil
#inputs
serial = input()
episode_time = int(input())
break_time = int(input())

#logic

lunch_time = round(break_time * 1/8)
relax_time = round(break_time * 1/4)
time_left = break_time - lunch_time - relax_time
if time_left >= episode_time:
    time_for_episode = time_left - episode_time
    print(f"You have enough time to watch {serial} and left with {time_for_episode} minutes free time.")
else:
    time_for_episode = episode_time - time_left
    print(f"You don't have enough time to watch {serial}, you need {time_for_episode} more minutes.")
