
#1
tupl_list = ("cars", "machines", "houses", "garage", "garden")
tupl_list2 = ("mango", "orange", "guava", "kiwi", "melon")

print(tupl_list)


#2

print("A tuple as similar to list are used to store one or multiple items in a single variable")

#3
print("The 4th element in the tuple is: ", tupl_list[3], "The 4th elementfrom the end of the tuple is: ", tupl_list[-4])

#4
if "lake" in tupl_list:
    print("Lake is in the tupul")
else:
    print("Lake is not in the tuple")

#5
print(len(tupl_list))

#6
print("A list is used to store multiple items in a list")

#7
print(tupl_list[2])


#8
print(tupl_list + tupl_list2)

#9

x =list(tupl_list)
x[1] = "yam"
y = tuple(x)
print(y)


#10

print("A dictionary is a collection that is ordered and changable and does not allow duplicate items")

#11
dict_ = {"brand":"Ford", "model":"Mustang", "year":1964}

dict_["year"] = 1299
print(dict_)





