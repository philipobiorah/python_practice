import time
currentTime = time.time() # Get curent time

#Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
print(f" total {totalSeconds}")

#Get the current second
currentSecond = totalSeconds% 60
print(f"currentSecond: {currentSecond}")

#Obtain the total minutes
totalMinutes = totalSeconds // 60
print(f"totalMiuntes: {totalMinutes}")

#obtain current minute 
currentMinute =  totalMinutes %  60
print(f"Current Minute: {currentMinute}")

#Obtain the total number of hours
totalHours = totalMinutes // 60
print(f"Total Hours: {totalHours}")

#Obtain the current hour
currenthour =  totalHours % 24
print(f"Total Hours: {currenthour}")



#Display resutls 
print("Current time is", currenthour, ":",
      currentMinute, ":", currentSecond, "GMT")