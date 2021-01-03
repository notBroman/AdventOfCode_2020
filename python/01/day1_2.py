# Day 1 advent of code Roman Berger
# find numbers that add to 2020 and multiply them                               
                                                                                   
def read_file(fileName):                                                        

    myFile = open(fileName, 'r')                                                
    a = myFile.read().splitlines()                                              
    myFile.close()                                                              

    for i in range(len(a)):
        a[i] = int(a[i])                                                        

    return a                                                                    

def find_pair(myList):                                                          
    for i in range(len(myList)-1):                                              

        for j in range(len(myList)-i):                                          

            for k in range(len(myList)):

                if(myList[i] + myList[i+j] + myList[k] == 2020):                                
                    return myList[i] * myList[i+j] * myList[k]
                else:                                                               
                    pass                                                            

def main_program():                                                             

    name = '/home/broman/dev/_projects/adventOfCOde/01/day1_1.txt'              
    print(find_pair(read_file(name)))                                           

main_program()                                                                  
                
