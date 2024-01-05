import time

# time.sleep(3)   # this means that our system will sleep for 3 seconds
# print("TIME'S UP")


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds= x%60 
    minutes= int(x/60)%60
    hours = int(x/3600)         # WE have excluded %24 as we dont have any days in our display so there is no limit on number of hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")