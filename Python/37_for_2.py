#example of for loop on tuple 
#findout sum and average of all values in tuple
tupel =(10,15,20,7,45,90,11,125)
sum=0

for item in tupel:
    print(item,end=' ')
    sum = sum + 1

average = sum / len(tupel)
print(f"sum{sum}, average =",round(average,2))
