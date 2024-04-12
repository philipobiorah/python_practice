import time
currentTime = time.time() # Get curent time

#Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)
print(f" total {totalSeconds}")

#Get the current second
currentSecond = totalSeconds% 60
print(currentSecond)

