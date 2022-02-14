hours = 7 # number of hours spent driving
kilometres = 440 # number of kilometers travelled
kmh = kilometres/hours # speed calculated by dividing distance by time
kmh = round(kmh,2) # round speed to 2 decimals

seconds = hours * 60 * 60 # number of seconds calculated by multiplying hours by 60 minutes and then by 60 seconds
metres = kilometres * 1000 # number of metres calculated by multiplying kilometres by 1000
msec = round(metres/seconds) # metres per second calculated by dividing distance by time and then rounded to the nearest integer

print("Your speed is ", kmh, " km/h or ", msec, " m/sec")