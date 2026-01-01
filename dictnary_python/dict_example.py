info = {
    "name" : "mohammad adnan khan",
    "city" : "gaya",
    "height" : 7,
    "age" : 23
}

print ("i live in", info["city"]) 

info.update({"caste":"khan"})
print (info)

for i,j in info.items():
    print(i,j)