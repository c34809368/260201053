#BerraAvci-260201053

#file function to read and store data
def file_func(path):
    filename=open(path,encoding="utf-8")
    text=filename.readlines()

    usernames=list()
    passwords=list()
    friendsTemp=list()
    for line in text:
        line=str(line)
        newline=line.split(";")
        newline=list(newline)
        usernames.append(newline[0])
        passwords.append(newline[1])
        friendsTemp.append(newline[2])
    
    friends=list()
    for item in friendsTemp:
        newitems=item.split(",")
        for i in newitems:
          if "\n" in i:

        friends.append(newitems) #to have all users' friends lists in a list
    
    my_dict={"usernames":usernames,"passwords":passwords,"friends":friends}
    return my_dict

#validate usernames
def validate_usernames(new_username,usernames):
    notValid="Username not valid\n"
    validName=False
    containsDigit=0
    containsLetter=0
    if new_username in usernames:
        print(notValid)
    else:
        tempName=new_username.lower()
        if tempName!=new_username:
            print(notValid)
        else:
            for char in new_username:
                if char.isdigit()==True:
                    containsDigit+=1
                elif char.isalpha()==True:
                    containsLetter+=1
        if (containsDigit+containsLetter)==len(new_username) and (containsDigit>0 and containsLetter>0) :
            validName=True
        else:
            validName=False
                    
    return validName

#validate passwords:
def validate_passwords(new_password):
    notValid="Password not valid\n"
    validPassword=False
    containsDigit=0
    containsLetter=0
    if 8>=len(new_password)>=4:
        for char in new_password:
            if char.isdigit()==True:
                containsDigit+=1
            elif char.isalpha()==True:
                containsLetter+=1
            else:
                pass
    else:
        print(notValid)
    if (containsDigit>0 and containsLetter>0):
        validPassword=True
    else:
        pass
    return validPassword

#1_log in
def log_in(username,usernames,passwords):
    log=False
    wrong="Wrong password or username\n"
    checkers=list()
    temp_i=-1
    password=input("Please enter password:\n")
    if username in usernames:
        i=usernames.index(username)
        checkers.append(i)        
        if passwords[i]==password:
            print("Logged in")
            log=True
            checkers.append(log)
        else:
            print(wrong)
            checkers.append(temp_i)
            checkers.append(log)
    else:
        print(wrong)
        checkers.append(temp_i)
        checkers.append(log)
    return checkers

#2_create new user
def create_newUser(new_username,usernames,passwords,friends):
    conditionFor_name=validate_usernames(new_username,usernames)
    if conditionFor_name==True:
        new_password=input("Please enter password:\n")
        conditionFor_password=validate_passwords(new_password)
        if conditionFor_password==True:
            usernames.append(new_username)
            passwords.append(new_password)
            friends.append(list())
        else:
            print("Password not valid\n")
    else:
        print("Username not valid\n")
        
    updated_usernames_passwords_friends={"usernames":usernames,"passwords":passwords,"friends":friends}
    return updated_usernames_passwords_friends

#3_add friend
def add_friend(friends,usernames,checkers):
    if checkers[1]==True:
        friend_name=input("Please enter the name of your new friend:\n")
        if friend_name in usernames:
            i=checkers[0]
            friends[i].insert(0,friend_name)
        else:
            print("Friend not found\n")
    else:
        print("You need to log in first\n")
    if checkers==None:
        print("You need to log in first\n")
    return friends

#4_show my friends
def show_myFriends(friends,checkers):
    if checkers[1]==True:
        i=checkers[0]
        if len(friends[i])>0:
          print(",".join(friends[i]))
        else:
          print("\n")
    else:
        print("You need to log in first\n")

#run all functions
def main():
    items=file_func("users.txt")
    usernames=items.get("usernames")
    passwords=items.get("passwords")
    friends=items.get("friends")
    checkers=[-1,False]
    while True:
        menu_text="1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"
        choice=input(menu_text)
        if choice=="1":
            username=input("Please enter username:\n")
            checkers=log_in(username, usernames, passwords)
        elif choice=="2":
            new_username=input("Please enter username:\n")
            updated_usernames_passwords_friends=create_newUser(new_username, usernames, passwords,friends)
            usernames=updated_usernames_passwords_friends.get("usernames")
            passwords=updated_usernames_passwords_friends.get("passwords")
            friends=updated_usernames_passwords_friends.get("friends")
        elif choice=="3":
            friendsNew=add_friend(friends, usernames, checkers)
            friends==friendsNew
        elif choice=="4":
            show_myFriends(friends, checkers)
        elif choice=="5":
            break
        else:
            print("Invalid option\n")
            
main()

