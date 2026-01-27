print("If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace per mile?, and what is your MPH?")
kilometers = 10
minutes = 42
seconds = 42
## converting to miles
miles = kilometers / 1.61


## converting and combining the two
timeSeconds = (minutes*60) + seconds 

## Finding how long to run 1 mile in min and sec
secondsPerMile = timeSeconds / miles

milesPerMinute = secondsPerMile//60
milesPerSecond = secondsPerMile%60

## Finding the mph
mph = 3600/secondsPerMile

print((int(milesPerMinute)) , "Minutes and" , (int(milesPerSecond)) , "Seconds per mile.")
print(round(mph, 1) , "mph")
print("mph is rounded, same with seconds to appear better.")

