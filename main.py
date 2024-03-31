import time

my_time = int(input("Enter the time in seconds: "))

if my_time <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    for i in range(my_time, 0, -1):
        seconds = i % 60
        minutes = (i // 60) % 60
        hours = (i // 3600) % 24
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("Time's up!")
