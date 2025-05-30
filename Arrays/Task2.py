heros=['spider man','thor','hulk','iron man','captain america']

print("The length of the list is : ",len(heros))

heros.append("black panther")

print("The updated list is : ",heros)

heros.remove(heros[5])
print("List after removing Black panther : ",heros)
    
heros.insert(3,"Black Panther")
print("List after inserting Black panther after hulk: ",heros)

heros[1:3]=["Dr.Strange"]
print("List after inserting Dr Strange inplace of  thor and hulk : ",heros)

heros.sort()
print(f"The sorted final list of heros is : ",heros)