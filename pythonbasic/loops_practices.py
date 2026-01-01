#example
for i in range (10):
    print(i)

#tables from loop4
choice = input("Enter your choice (press q to quit): ")

while choice != "q" :
    num = int (input("Enter the number : "))


    for i in range (1,11):
        #string formatting "f"
        print(f"{num} x {i} = {num*i}")
    choice = input("if you want to continue press any character exect (q)")