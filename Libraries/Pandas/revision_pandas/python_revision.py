d = {"name":"Yashasvi"}
print(d)
#var[key]=value
d["city"] = "Pune"
print(d)
#var[key]
print(d["name"])
#var.pop(key)
d.pop("name")
print(d)
#for loop
d = {1:1,2:4,3:9,4:16,5:25}
for i,j in d.items():
    print(j)