# example of for loop on string 
#count words, letters 
line = "the easylearn academy 105, eva surbhi opp waghawadi road, bhavnagar - 36001"

words = 1
count = 0

for letter in line:
    #print(letter)
    if letter == " ":
        words = words+1
        count += 1
    print(f"no of {words} and Letter of no {count}")

#count symbols 
#count digits