import json

def read_log():
   #option 1
   # file = open("app.log")
   # print(file.readline())
   # file.close()

    #option 2
    with open("app.log","r") as file:
        return file.readlines()

def analyse_log(lines):
    log_counts ={
        "INFO": 0,
        "WARNING":0,
        "ERROR":0,
        "CRITICAL":0
    }
    for i in lines:
        if "INFO"  in i:
            log_counts.update({"INFO": log_counts["INFO"]+1})
        elif "WARNING" in i:
            log_counts.update({"WARNING": log_counts["WARNING"]+1})
        elif "ERROR" in i:
             log_counts.update({"ERROR": log_counts["ERROR"]+1})
        elif "CRITICAL" in i:
            log_counts.update({"CRITICAL": log_counts["CRITICAL"]+1})
        else:
            continue
    return log_counts 


def write_json(counts):
    with open("output.json","w+") as json_file:
        json.dump(counts,json_file)






lines = read_log()
counts = analyse_log(lines)
write_json(counts)




