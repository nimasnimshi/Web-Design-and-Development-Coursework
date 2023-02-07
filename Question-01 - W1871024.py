
count_progress=0
count_module_trailer=0
count_exclude=0
count_module_retriever=0
result="null"


def range_check(input_1):  # function for check the range
    if input_1 <= 120 and input_1 >= 0 and input_1 % 20 == 0:
        boolean_1 = True

    else:
        print("Out of range.")
        boolean_1 = False
        return boolean_1


while True:
    boolean_2 = False
    while boolean_2 == False:
     
        boolean_range = False
        while boolean_range == False:
            try:
                PassCR=int(input("\nPlease enter your credits at pass: "))
                boolean_range = range_check(PassCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                DeferCR=int(input("Please enter your credits at Defer: "))
                boolean_range = range_check(DeferCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                FailCR=int(input("Please enter your credits at fail: "))
                boolean_range = range_check(FailCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False
        
        totalOfCredits=PassCR+DeferCR+FailCR
        if totalOfCredits==120:  # Total calculated by the sum of 3 credit types
            boolean_2 = True
            
        else:
            print("Total incorrect")
            boolean_2 = False

    if PassCR == 120:
        print("Progress")
        count_progress+=1

    elif PassCR == 100:
        print("Progress(module trailer)")
        count_module_trailer+=1

    elif FailCR >= 80:
        print("Exclude")
        count_exclude+=1

    else:
        print("Module retriever")
        count_module_retriever+=1
    

    result = count_progress + count_module_trailer + count_exclude + count_module_retriever
    choice=input('\nWould you like to enter another set of data?\nEnter "y" for yes or "q" to quit and view result: ')
    
    if choice == "q":
        break  # break used for stop the programme
    else:
        continue

#Horizontal Histogram    
print("-----------------------------------------------------------")
print("Horizontal Histogram\n") 
print(f'Progress  {count_progress} : {count_progress*"*"}')     
print(f'Trailer  {count_module_trailer} : {count_module_trailer*"*"}')
print(f'Retriever {count_module_retriever} : {count_module_retriever*"*"}')
print(f'Exclude   {count_exclude} : {count_exclude*"*"}')
print(f'\n{count_progress+count_module_trailer+count_exclude+count_module_retriever} outcomes in total ')
print("-----------------------------------------------------------")
