print(''' 
 
 ,--._______,-. 
       ,','  ,    .  ,_`-. 
      / /  ,' , _` ``. |  )       `-.. 
     (,';'""`/ '"`-._ ` \/ ______    \\ 
       : ,o.-`- ,o.  )\` -'      `---.)) 
       : , d8b ^-.   '|   `.      `    `. 
       |/ __:_     `. |  ,  `       `    \ 
       | ( ,-.`-.    ;'  ;   `       :    ; 
       | |  ,   `.      /     ;      :    \ 
       ;-'`:::._,`.__),'             :     ; 
      / ,  `-   `--                  ;     | 
     /  \                   `       ,      | 
    (    `     :              :    ,\      | 
     \   `.    :     :        :  ,'  \    : 
      \    `|-- `     \ ,'    ,-'     :-.-'; 
      :     |`--.______;     |        :    : 
       :    /           |    |         |   \ 
       |    ;           ;    ;        /     ; 
     _/--' |   -hrr-   :`-- /         \_:_:_| 
   ,',','  |           |___ \ 
   `^._,--'           / , , .) 
                      `-._,-' ''')
                      


print("Welcome to dog vaccination")
print("Know about proper vaccination time for dogs")

puppy = 6
dog = 12
name =  input("Enter your dog/puppy name: ")

choice=input('Know about dog vaccination when to get one for your dog/puppy! Would you like to continue? Type "yes" or "no": ')

if choice == "yes":
    breed=input('What is your dog: puppy or dog? Type "puppy" or "dog": ')
    if breed == "puppy":
        print("You need to vaccinate your puppy between 6-8 weeks")
        age = int(input("What is your puppy age in weeks: Type 6 or 10: "))
        if age < 10:
            print("You need to get your puppy first vaccination")
        elif age > 10:
            print("You need to get your Dog second vaccination")
    elif breed == "dog":
        print("You need to vaacinate your dog in at 12 months")
        age = int(input("What is your dog age in months? Type 13 or 14 or 16 or 18: "))
        if age == 13:
            print("Your dog is adult and uptonow there should be 3-4 vaccinations should be done")
            print("After 12 months your dog will get its first rabies vaccination")
        elif age > 14:
            print("Along with vaccination get your dog its second rabies vaccination")
else:
    print("You exited the programm")
    
    

date = input("Please enter your dog/puppy vaccination date (e.g., DD/MM/YYYY): ")
owner = input("Enter owner name of dog/puppy: ")
print("Thank you for using vaccination tool :) ")
print("------VACCINATION CARD------")
print(f"Dog name: {name}")
print(f"Age: {age} months/weeks")
print(f"Breed: {breed}")
print(f"Vaccination date: {date}")
print(f"Owner of dog/puppy: {owner}")
print("******Thank you******")