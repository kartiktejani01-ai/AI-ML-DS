#default argument function
def getSecond(hours,minutes=0,seconds=0):
    print(f"Hours:{hours}, Minutes:{minutes}, Seconds:{seconds}")
    totalSeconds = (hours*60*60) + (minutes*60) + seconds
    return totalSeconds

result = getSecond(10,9,0)
print(f"Total Seconds = {result}")
result = getSecond(10,3)
print(f"Total Seconds = {result}")
result = getSecond(10)
print(f"Total Seconds = {result}")