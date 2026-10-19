states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

areas = [162968, 83743, 78438, 94163, 135192, 3702, 196024, 44212, 55673, 79716, 191791, 38863, 308252, 307713, 22327, 22429, 21081, 16579, 155707, 50362, 342239, 7096, 130058, 112077, 10486, 240928, 53483, 88752]

for states, areas in zip(states,areas):
    print(states,"has Areas ",areas)