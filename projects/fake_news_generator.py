import random
import time
import datetime

# list of subjects
people_type=["Teacher","Politician","Scientist","Influencer","Hacker","Grandmother","College student",
             "Gym trainer","Barber","Alien tourist","Angry chef","Lazy programmer","Detective","Farmer","Delivery boy"]

weird_character=["Time traveler","Invisible man","Talking dog","Zombie accountant","AI robot","Ninja cat",
                 "Flying buffalo","Pirate monkey","Singing dinosaur","Angry ghost"]

things=["Refrigerator","Laptop","Smartwatch","Ceiling fan","Washing machine","Auto-rickshaw","Traffic signal","Drone","Toothbrush"]

# list of actions
people_act=["accidentally launched","secretly stole","married","danced with","challenged","roasted","hacked","chased","adopted","escaped from",
            "started teaching","became CEO of","sold","painted","disappeared with","fought against","opened a startup for","live-streamed","banned","invented"]

weird_act=["started a war with","discovered","transformed into","got trapped inside","broke the internet using",
              "started farming on","built a rocket from","replaced teachers with","trained monkeys to use","created a black hole using"]

things_act=["trained an AI to predict","hacked the school Wi-Fi using","uploaded consciousness into",
          "turned into NFT","automated","accidentally deleted"]

# list of objects
people_obj=["shopping mall","railway station","Mars","classroom","wedding hall","metro","temple",
       "cricket stadium","secret lab","underwater city"]

weird_obj=["laptop","banana","drone","refrigerator","goldfish","scooter","Wi-Fi router"
            ,"exam paper","robot vacuum cleaner"]

things_obj=["Instagram account","crypto wallet","gaming PC","Chat app","meme page","online exam portal","dating app"]

styles=["BREAKING","SHOCKING","EXCLUSIVE","VIRAL","TRENDING"]

locations=["Bengaluru metro","Hyderabad hostel","Mumbai local train",
          "engineering college canteen","village bus stop"]

history=[]


def heading(sub):
    if sub==1:
        sub=random.choice(people_type)
        act=random.choice(people_act)
        obj=random.choice(people_obj)
    elif sub==2:
        sub=random.choice(weird_character)
        act=random.choice(weird_act)
        obj=random.choice(weird_obj)
    elif sub==3:
        sub=random.choice(things)
        act=random.choice(things_act)
        obj=random.choice(weird_obj)
    else:
        all_subject = people_type + weird_character + things
        all_actions = people_act + weird_act + things_act
        all_objects = people_obj + weird_obj + things_obj
        sub=random.choice(all_subject)
        act=random.choice(all_actions)
        obj=random.choice(all_objects)
    style=random.choice(styles)
    location=random.choice(locations)
    headline=f"{style} - {location}\n {sub} {act} {obj}"
    return headline

# loop
while True:
    print("\n\n===fake news heading generator===")
    print("1:generate a joke")
    print("2:exit!\n")

    try:
        choice=int(input("enter your choice: "))

        if choice==1:
            print("select any subject (or) category")
            print("1:people")
            print("2:weird")
            print("3:machines")
            sub=int(input("enter your choice: "))

            print("\nGenerating headline.....\n")
            time.sleep(2)
            line=heading(sub)
            history.append(line)
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"[{current_time}] {line}")


        elif choice==2:
            if len(history)>0:
                save=input("Do You Want To Save Generated Headlineds(yes/no)?")
                
                if save.lower()=="yes":
                    filename=input("enter the filename: ")
                    with open(filename + ".txt","a") as file:
                        for line in history:
                            file.write(f"{current_time} {line} \n")
                    print(f"file saved as :{filename}.txt")
            print("goodbye")
            break
        else:
            print("invalid choice!!")
    except(TypeError,ValueError):
        print("enter only numbers.")
        print("select from the options")