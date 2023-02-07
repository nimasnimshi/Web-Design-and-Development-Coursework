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

b = []
c = []
d = []
e = []

full_data = []

while True:
    boolean_2 = False
    while boolean_2 == False:
        a = []
        t = []
        
        boolean_range = False
        while boolean_range == False:
            try:
                PassCR=int(input("\nPlease enter your credits at pass: "))
                a.append(PassCR)
                t.append(PassCR)
                boolean_range = range_check(PassCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                DeferCR=int(input("Please enter your credits at Defer: "))
                a.append(DeferCR)
                t.append(DeferCR)
                boolean_range = range_check(DeferCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                FailCR=int(input("Please enter your credits at fail: "))
                a.append(FailCR)
                t.append(FailCR)
                boolean_range = range_check(FailCR)

            except ValueError:
                print("Integer required.")
                boolean_range = False
        
        totalOfCredits=PassCR+DeferCR+FailCR
        if totalOfCredits==120:  
            boolean_2 = True
            
        else:
            print("Total incorrect")
            boolean_2 = False

    if PassCR == 120:
        print("Progress")
        b.append("Progress - {a},{b},{c}".format(a = a[0], b = a[1],c = a[2]))
        text = "Progress - {a},{b},{c}\n".format(a = t[0], b = t[1],c = t[2])
        count_progress+=1

    elif PassCR == 100:
        print("Progress(module trailer)")
        c.append("Progress(module trailer) - {a},{b},{c}".format(a = a[0], b = a[1],c = a[2]))
        text = "Progress(module trailer) - {a},{b},{c}\n".format(a = t[0], b = t[1],c = t[2])
        count_module_trailer+=1

    elif FailCR >= 80:
        print("Exclude")
        e.append("Exclude - {a},{b},{c}".format(a = a[0], b = a[1],c = a[2]))
        text = "Exclude - {a},{b},{c}\n".format(a = t[0], b = t[1],c = t[2])
        count_exclude+=1

    else:
        print("Module retriever")
        d.append("Module retriever - {a},{b},{c}".format(a = a[0], b = a[1],c = a[2]))
        text = "Module retriever - {a},{b},{c}\n".format(a = t[0], b = t[1],c = t[2])
        count_module_retriever+=1
    full_data.append(text)

    result = count_progress + count_module_trailer + count_exclude + count_module_retriever
    choice=input('\nWould you like to enter another set of data?\nEnter "y" for yes or "q" to quit and view result: ')
    
    if choice == "q":
        break  # break used for stop the programme
    else:
        continue
    
print("-----------------------------------------------------------")
print("Horizontal Histogram\n")                                        #Horizontal Histogram
print(f'Progress  {count_progress} : {count_progress*"*"}')     
print(f'Trailer   {count_module_trailer} : {count_module_trailer*"*"}')
print(f'Retriever {count_module_retriever} : {count_module_retriever*"*"}')
print(f'Exclude   {count_exclude} : {count_exclude*"*"}')
print(f'\n{count_progress+count_module_trailer+count_exclude+count_module_retriever} outcomes in total ')
print("-----------------------------------------------------------")


vert_histogram = max(count_progress, count_module_trailer, count_module_retriever, count_exclude)  # 0 to max is the range
print("Vertical Histogram\n")
print("Progress Trailing Retriever  Excluded")
for count in range(0, vert_histogram):

    if count_progress > 0:  # I used for loop for vertical histogram.

        print("   *", end="         ")
        count_progress -= 1  
    else:
        print("   ", end="          ")

    if count_module_trailer > 0:
        print("*", end="        ")
        count_module_trailer -= 1
    else:
        print("", end="         ")

    if count_module_retriever > 0:
        print("*", end="          ")
        count_module_retriever -= 1
    else:
        print("", end="           ")

    if count_exclude > 0:
        print("*", end="\n")
        count_exclude -= 1
    else:
        print("", end="\n")
print("-----------------------------------------------------------")
print("List\n")    
print(*b, sep = "\n")
print(*c, sep = "\n")
print(*d, sep = "\n")
print(*e, sep = "\n")
print("-----------------------------------------------------------")

file1 = open("myfile.txt", "w")
file1.writelines(full_data)
file1.close()
print("Data from the text file\n")
file1 = open("myfile.txt", "r")
data = file1.read()
print(data)
file1.close()


   
