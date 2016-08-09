import sys

y=0
print("Welcome to the Database!\n")
while(True):
    while y < 3:
        a = input("\nPlease enter your username: ")
        b = len(a)
    
        if b <= 8 and b >= 0:
             c = input("\nPlease enter your password: ")
             break
        else:
            print("\nLogin incorrect. Username must contain no more than 8 alphanumeric characters.\n")
            y = y+1
            continue
    if y==3:
        print("\nGoodbye!")
        break

    d = str(a)+str(':')+str(c)+str('\n')
    
    usersfile = open('users.txt','r').readlines()
    authfile = open('auth.txt','r').readlines()
    
    flag = 0

    if d in usersfile:
        
        print("\nEnter each file name you are trying to access each time prompted. When finished accessing files, press 'Control-D.' at the next prompt.")

        while flag == 0:
            try:
                line = input("\nWhat is the name of the file you are trying to access? ")
                for x in range(0,len(authfile)):
                    p = authfile[x].split(":")
                    if (p[1] == a or p[1] == '') and (p[2] == (str(line)+'\n') or p[2] == '\n'):
                        if p[0] == 'PERMIT':
                            try:
                                u = open(str(line),'r')
                            except IOError:
                                print("\nAccess to file: " + str(line) + " denied.")
                                break
                                
                            w = u.read()
                            print(w) 
                            break
                            
                        else:
                            print("\nAccess to file: " + str(line) + " denied.")
                            break
                    else:
                        if x==len(authfile)-1:
                            print("\nAccess to file: " + str(line) + " denied.")
                        else:
                            continue
               

            except EOFError:
                break
                    
    else:
        print("\nLogin incorrect")
        y = y+1
        continue

    break
 
    
