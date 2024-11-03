import json
a = open('data.json')
data = json.load(a)

print ('''
1. Train Bot
2. Talk with Bot
3. Exit        
       
''')

while True:
    input_awal = input("Select Menu : ")
    if input_awal == "1":
        while True:
            x = input ("User\t: ")
            if x == "keluar":
                break
            else:
                y = input ("Bot\t: ")
                data[x] = y
                b = open('data.json', "w")
                json.dump(data,b)
                b.close()
    elif input_awal =="2":
        while True:
            x = input("User\t: ")
            if x == 'keluar':
                break
            if x in data:
                print(f'Bot\t: {data[x]}')
            else:
                print("Bot\t: Itu kata yang baru")
    elif input_awal =="3":
           break 
           
    else:
        
        pass            
