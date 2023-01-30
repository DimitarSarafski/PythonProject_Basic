world_record_seconds = float(input())
word_record_metres = float(input())
time_seconds = float(input())

time = word_record_metres * time_seconds
resistence = int((word_record_metres / 15)) * 12.5
total_time = time + resistence

if world_record_seconds <= total_time:
    need_second = total_time - world_record_seconds
    print(f"No, he failed! He was {need_second:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
