import datetime
import os
import time


def timenow():
    data = datetime.datetime.now()
    time = data.time()
    data = f'{data.day}/{data.month}/{data.year}'
    return data

def petchy():
    print()
    print("██████╗ ███████╗████████╗ ██████╗██╗  ██╗██╗   ██╗        ██╗  ██╗ ██████╗ ████████╗███████╗██╗")
    print("██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗ ██╔╝        ██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║")
    print("██████╔╝█████╗     ██║   ██║     ███████║ ╚████╔╝         ███████║██║   ██║   ██║   █████╗  ██║     ")
    print("██╔═══╝ ██╔══╝     ██║   ██║     ██╔══██║  ╚██╔╝          ██╔══██║██║   ██║   ██║   ██╔══╝  ██║     ")
    print("██║     ███████╗   ██║   ╚██████╗██║  ██║   ██║           ██║  ██║╚██████╔╝   ██║   ███████╗███████╗")
    print("╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝           ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝")
    print("")
    print("-- THIS PROGRAM MAKE BY PHESTSUWAPHAT THONGSUK --".center(100))

def home():
    print("╔"+"="*100+"╗")
    print("║"+" "*100+"║")
    print("║%s%s"%("Petchy Hotel".center(100),"║"))
    print("║"+" "*100+"║")
    print("╚"+"="*100+"╝")
    print()
    print("%35s %30s %s"%("[1] - Register","","[2] - Room Info"))
    print()
    print("%36s %29s %s"%(" [3] - Check In ","","[4] - Record"))
    print()
    print("%37s %28s %s"%("[5] - Check Out ","","[E] - Exit"))
    print("")
    print("="*100)

def back():
    back = input("Enter any key to back to menu ....")

def template(name_menu):
    print("╔"+"="*100+"╗")
    print("║"+" "*100+"║")
    print("║%s%s"%(name_menu.center(100),"║"))
    print("║"+" "*100+"║")
    print("╚"+"="*100+"╝")
    print()

def register():
    os.system('cls')
    template('Register Menu')

    first_name = input(">>>> Enter fisrt name : ").capitalize().strip()
    if not first_name.isalpha():
        print("Sorry, you can only enter your first name., you can ")
        back()
        return
    last_name = input(">>>> Enter last name : ").capitalize().strip()
    if not last_name.isalpha():
        print("Sorry, you can only enter your last name., you can ")
        back()
        return

    print("Are you sure to use thisname "+'"'+first_name+" "+last_name+'"')
    confirm = input('>>>> Confirm or not ?? ( Y - Yes / N - No ) : ').upper()
    while confirm != 'Y' :

        if confirm == 'N' :
            print('Sorry, you can try again..')
            back()
            os.system('cls')
            return
        print("\nSorry, you can choose only 'Y' or 'N'")
        print("Are you sure to use this name "+'"'+first_name+" "+last_name+'"')
        confirm = input('>>>> Confirm or not ?? ( Y - Yes / N - No ) : ').upper()

    try : 
        age = int(input(">>>> Enter your age : "))
        if age < 18 :
            print("Sorry, You under 18 year old can't use it...")
            time.sleep(2)
            os.system('cls')
            return

    except:
        print("Sorry, you only need to enter your age with number.")
        back()
        os.system('cls')
        return
    date = timenow()
    idcard = input(">>>> Enter your ID card : ").upper()
    have = []
    with open('data.txt','a+') as file :
        pass
    with open('data.txt','r') as file :
        data = file.read().splitlines()
        for i in data :
            line = i .split()
            have.append(line[4])
    if idcard in have :
        print('This Id card already have...')
        back()
        os.system('cls')
        return
    else :
        if idcard.isnumeric() and len(idcard) == 13 :

            with open('data.txt','a+') as file :
                with open('data.txt','r') as file1 :
                    data = file1.read()
                    if data == '' :
                        with open('data.txt','w') as empty :
                            empty.write('%s %s %s %s %s'%(first_name,last_name,age,date,idcard))
                    else :    
                        for i in data :
                            line = i.split()
 
                            if idcard in line :
                                print('Sorry This ID is already register in this Hotel..')
                                back()
                                os.system('cls')
  
                            else :
                                with open('data.txt','w') as not_empty :
                                    not_empty.write('%s\n%s %s %s %s %s'%(data,first_name,last_name,age,date,idcard))
            print("="*40+"++","   SUCCESS   ",'++'+"="*40)
            time.sleep(1)
        else :
            print("Invalid ID card.. You must have 13 digits!.")
            time.sleep(2)
            os.system('cls')

def room_info():
    os.system('cls')
    print("╔"+"="*122+"╗")
    print("║"+" "*122+"║")
    print("║%s%s"%("Rule and Room Info".center(122),"║"))
    print("║"+" "*122+"║")
    print("╚"+"="*122+"╝")
    print("\nWelcome to Petchy Hotel\nChildren under the age of 18 are not allowed to use the service.")
    print("You can only use it for 1 night. If not checked out the staff will unlock the room key and take your belongings out of the hotel.")
    print("\n%-35s %-35s %-35s %s"%("Class A","Class B","Class C","Class D"))
    print()
    print("%-35s %-35s %-35s %s"%("- Two bed","- Two bed","- One bed","- One bed"))
    print("%-35s %-35s %-35s %s"%("- Daily Cleaning","- Free wifi","- Free wifi","- Free wifi"))
    print("%-35s %-35s %-35s "%("- Free wifi","- Balcony","- Balcony"))
    print("%-35s %-35s %-35s "%("- Balcony","- Free breakfast","- Free breakfast"))
    print("%-35s  "%("- Jacuzzi"))
    print("%-35s  "%("- Free breakfast"))
    print()
    print("%-35s %-35s %-35s %-35s"%("Price 20,000 BAHT","Price 5,000 BAHT","Price 2,000 BAHT","Price 750 BAHT"))
    print()
    room = []
    for i in ['A','B','C','D']:
        with open(i+'.txt','r') as file:
            data = file.read()
            room.append(data)
    print("     left %-30s left %-30s left %-30s left %s "%(room[0],room[1],room[2],room[3]))
    print()

def roomadd(clases,check_id,price):
    
    with open(clases+".txt") as file :
        data =  file.read()
        amt = int(data)
        if amt == 0 :
            print('room not avaliable!')
            back()
            return
        amt -= 1 
        
        with open(clases+".txt","w") as file :
            file.write('%s'%(amt)) 
        with open('data.txt','r') as rd :
            data = rd.read().splitlines()
            for i in data :
                line = i.split()
                if check_id in line :
                    name = line[0]
                    sur  = line[1]
                    date = line[3]
                    fullname = line[0]+" "+line[1]
            with open('record.txt','a+') as file :
                file.write('%-15s %-27s %-17s %-23s %s\n'%(date,fullname,clases,price,"Check-IN"))
            with open('whereyou.txt','a+') as file :
                file.write('%s %s\n'%(check_id,clases))
        print("---- SUCESS ----")
        back()

def check_in():
    os.system('cls')
    template('Check In menu')
    with open('data.txt','a+') as file :
        pass
    check_id = input('Enter your ID : ').strip()
    id_list = []
    
    with open('data.txt') as file : 
        data = file.read().splitlines()
        for i in data :
            line = i.split()
            id_list.append(line[4])

        if check_id in id_list :
            os.system('cls')
            template("Select Your class")
            print("[A] - 20,000 BAHT\n[B] - 5,000 BAHT\n[C] - 2,000 BAHT\n[D] - 750 BAHT")
            print("="*100)
            choose = input(">>>> Enter your class :").upper()
            
            if choose == "A":
                roomadd("A",check_id,"20,000 BAHT")
                
            elif choose == "B" :
                roomadd("B",check_id,"5,000 BAHT")      
                
            elif choose == "C" :
                roomadd("C",check_id,"2,500 BAHT")
                
            elif choose == "D" :
                roomadd("D",check_id,"750 BAHT")
    
            else:
                print("Sorry, Invalid menu please try again...")
                back()
                os.system('cls')
                return

            os.system('cls')
        
        else :
            print("Invalid Id card")
            back()
            os.system('cls')

def out_come(clases,check_id):
    with open(clases+".txt") as file :
        data =  file.read()
        amt = int(data)
        if amt >= 10 :
            print("You did't check In in the room")
            back()
            return
    
        amt += 1 
        with open(clases+".txt","w") as file :
            file.write('%s'%(amt)) 
        with open('data.txt','r') as rd :
            data = rd.read().splitlines()
            for i in data :
                line = i.split()
                if check_id in line :
                    name = line[0]
                    sur  = line[1]
                    date = line[3]
                    fullname = name+" "+sur
                    
            with open('record.txt','a+') as file :
                file.write('%-15s %-27s %-17s %-23s %s\n'%(date,fullname,clases,"------","Check-OUT"))
            with open('whereyou.txt','a+') as file :
                file.write('%s %s\n'%(check_id,clases))
        print("Thank you for using the service".center(100))
        print("---- Check Out Completee ----".center(100))

def remove_room(id,type): #" type"
    check = id+type
    cache = []
    with open("whereyou.txt",'r') as read :
            data = read.read().splitlines()
            if check in data :
                for i in data :
                    cache.append(i)
                     
                cache.remove(check)
                
            for i in cache :
                write = i
               
                with open('whereyou.txt','w') as file:
                     for i in range(len(cache)):
                        file.write("%s\n"%(cache[i]))
            
def check_out():
    new = []

    id = input(">>>> Enter your ID : ").strip()
    
    with open('whereyou.txt','a+') as file:
        pass
    with open("whereyou.txt","r") as file :
        data = file.read().splitlines()
        if id+" A" in data :
            remove_room(id,' A')
            out_come("A",id)
        elif id+" B" in data :
            remove_room(id,' B')
            out_come("B",id)
        elif id+" C" in data :      
            remove_room(id," C")
            out_come("C",id)
        elif id+" D" in data : 
            remove_room(id," D")
            out_come("D",id)
        else :
            print("Sorry, you entered incorrectly...")
            back()
            return

def record():
    with open('record.txt') as rec :
        template('Record Menu')
        data = rec.read().splitlines()
        print('%-20s %-20s %-20s %-20s %s'%("Date","Name","Class","Price","Check IN/OUT"))
        print("="*102)
        print()
        for i in data :
            print(i)      

def main():
    try:
        for i in ['A','B','C','D']:
            a = open(f'%s.txt'%i,'r')
            a.close()
        
    except:
        for i in ['A','B','C','D']:
            a = open(f'%s.txt'%i,'w')
            a.write('10')
            a.close()

    petchy() 
    time.sleep(2)
    os.system('cls')
    home()
    
    menu = input(">>>> Enter a menu : ").upper()
    os.system('cls')

    while menu != 'E' :
        if menu == "1" :
            register()
            os.system('cls')
        elif menu == "2" :
            room_info()
            back()
            os.system('cls')
        elif menu == "3" :
            check_in()
            os.system('cls')
        elif menu == '4' :
            try :
                record()
            except:
                template('Record Menu')
                print("You don't have record")
            back()
            os.system('cls')
        elif menu == "5" :
            template("Check Out Menu")
            check_out()
            os.system('cls')
            
        else :
            print("Invalid menu !!!")
            
        home()
        menu = input(">>>> Enter a menu : ").upper()
        os.system('cls')

main()