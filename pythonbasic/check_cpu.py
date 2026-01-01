import psutil

def check_cpu():
    cpu_treshod = int(input("Enter the cpu treshod : "))

    current_cpu = psutil.cpu_percent(interval=1) #this comes from library of psutil
    print("cpu current %",current_cpu)

    if cpu_treshod > current_cpu :
        print("cpu is in safe state")

    else :
        print("sent cpu alert email ")


check_cpu()

