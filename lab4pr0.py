#Interactive data management system
#Writtn by Sam Traylor, February 18th

majors = {'Harry':'Computer Science', 'Hermione':'Mathematics', 'Ron':'English'} #initialize dict

def look_up(d):
    '''Takes user-inputted name and if it's in the dict, will print string of the
       Associated major. If not found, will print "Not found."

       Arguments:
       d -- dict object containing pairs with strings for name (key) and major (value)'''
    
    inpt = input('Enter a name: ')
    
    if inpt in d.keys(): #if the name is in the dict
        print(d[inpt] + '\n')  #print corresponding major  
    else:
        print('Not found.\n') #if not in dict, print 'Not found.'
        
def add(d):
    '''Takes user-inputted name and major strings, and adds as new dict entry if the
       entry doesn't already exists. If it does exist, it prints, 'A person with this
       name already exists in the system.'
       
       Arguments:
       d -- dict object containing pairs with strings for name (key) and major (value)'''
    
    name = input('Enter a name: ')
    major= input('Enter a major: ')
    
    if (name in d.keys()): #if name exists in dict
        print('A person with this name already exists in the system.\n')  
    else:   #if it's a new entry
        d[name] = major #creates new key/major pair based on input
        print(' ')

def change(d):
    '''Takes user-inputted string called name and if it exists in the dict, asks for
       a major (string form) to change the key's value to. If it doesn't exist already, program prints,
       'That name is not found.'
       
       Arguments:
       d -- dict object containing pairs with strings for name (key) and major (value)'''
    
    name = input('Enter a name: ')

    if name not in d.keys(): #if no key with the specified name is found
        print('That name is not found.\n')
    else:  #if there is a key for the entered name
        major = input('Enter the new major: ') #take input for new major
        d[name] = major  #change value to inputted major at the location where key = name
        print(' ')

def delete(d):
    '''Takes user-inputted name and if it exists in the dict, removes the entry.
       If it doesn't exist in the dictionary, program prints, 'That name is not
       found.'
       
       Arguments:
       d -- dict object containing pairs with strings for name (key) and major (value)'''

    name = input('Enter a name: ')

    if name in d.keys(): #if name exists in dict
        del d[name]     #delete that entry
        print(' ')
    else:               #if it doesn't exist in the dict
        print('That name is not found.\n') 
        
def display(d):
    '''Displays all the entries in the dictionary with print() statements, one
       name/major pair per line.

       Arguments:
       d -- dict object containing pairs with strings for name (key) and major (value)'''

    for name, major in d.items(): #iterate thru all items
        print(name + ' is a wizard in ' + major) #print name/major pair
    print(' ')
    
def get_menu_choice():
    '''Displays to user all of the possible chocies (functions) that the program is
       capable of (look up, add, change, delete, quit). Each choice is designated a
       number and user is asked to enter a number corresponding with the desired choice.
       User will be repeatedly asked to enter a choice until a valid choice is entered.
       If user enters '6', the program will quit instead of execution one of the 5 functions.'''
    
    print('Majors of College Students')
    print('---------------------------')
    print('1. Look up a student\'s major')
    print('2. Add a new student')
    print('3. Change a major')
    print('4. Delete a student')
    print('5. Display all students')
    print('6. Quit the program')
    print()
    pick = int(input('Enter your choice: ')) #set choice to what user chooses

    while pick > 6: #if invalid keep asking for input until valid # (less than 6) entered
        pick = int(input('Enter a valid choice: '))
        
    return pick #once loop is satisfied (meaning a valid num is entered) choice is returned
        

majors = {}
choice = 0

while choice != 6:

    choice = get_menu_choice()

    if choice == 1:
        look_up(majors)
    elif choice == 2:
        add(majors)
    elif choice == 3:
        change(majors)
    elif choice == 4:
        delete(majors)
    elif choice == 5:
        display(majors)

    
