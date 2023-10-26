set1=set() 
print("initial empty:", set1) 
set1.add("red") 
print("after entering 1 element:", set1) 
set1.update(["yellow", "blue"]) 
print("after updating more element:", set1) 
if "red" in set1: 
    set1.remove("red") 
print("after removing (red) element:", set1) 
print(set1) 
for item in set1: 
    print(item) 
print("item count:", len(set1)) 
isempty=len(set1)==0 
set1=set(["red", "yellow"]) 
set2=set(["blue", "yellow"]) 
set3=set1 & set2 
set4=set1 | set2 
set5=set1 - set3 
set6=set1 ^ set2 
issubset=set1 <= set2 
issuperset=set1 >= set2 
set7=set1.copy() 
set7.remove("red") 
set8=set1.copy() 
set8.clear() 
print("original set:", set1) 
print("original set:", set2) 
print("intersection set1 & set2:", set3) 
print("union set1 | set2:", set4) 
print("set difference(set1 - set3):", set5) 
print("symmetric difference(set1 ^ set3):", set6) 