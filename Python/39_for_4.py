# example of for loop on dictionary 
india = {
    "Sanju Samson": 3,
    "Abhishek Sharma": 69,
    "Ishan Kishan": 37,
    "Shreyas Iyer": 1,
    "Tilak Varma": 28,
    "Naman Dhir": 10,
    "Nitish Kumar Reddy": 21,
    "Axar Patel": 20,
    "Arshdeep Singh": 11,
    "Prince Yadav": 13,
    "Mayank Yadav": 0
}

'''count = 0
for key in india:
    if india[key] == 0:
        count = count+1
        print("Who Player Scored 0 :",count)
'''
'''sum = 0
for key in india:
    sum = sum + india[key]
    print(sum)'''

'''for key in india:    
    if india[key]>50:
        print(key,india[key])    '''

for key in india:
    if india[key]<10:
        print(key,india[key])