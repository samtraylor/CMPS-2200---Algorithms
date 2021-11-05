#written by Sam Traylor on Feb 4, 2019. Purpose of program is to verify several
#requirements for a user-entered password

space = False
caps = False
lowerc = False
num = False
symbols = False
q = 0

while q == 0:
    passwd = input("Please enter a password: ")
    
    for k in passwd:
        if k == " ":   #tests for spaces
            space = True
            
    if (len(passwd) >= 8) and (len(passwd) <= 20) and (space == False):

        for i in passwd:
         
            for x in range(65, 91):
                if ord(i) == x:
                    caps = True
                    #print('caps', caps)

            for y in range(97, 123):
                if ord(i) == y:
                    lowerc = True
                    #print('lowerc', lowerc)

            for z in range(0,10):
                if i == str(z):
                    num = True
                    #print('num', num)

            for g in range(33, 48):
                if ord(i) == g:
                    symbols = True
                    #Print('symbols',symbols)

            for h in range(58, 65):
                if ord(i) == h:
                    symbols = True
                    #print('symbols',symbols)

            for p in range(91, 97):
                if ord(i) == p:
                    symbols = True
                    #print('symbols',symbols)

        if caps == True and lowerc == True and num == True and symbols == True:
            print('Password accepted')
            q = 1
        
        
        
            

        
                
        
    
