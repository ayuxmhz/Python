# friends = ["Zoro", "Sanji", "Luffy", "Brook", "Nico", "Nami"]
# friends[3] = "Boa"
# friends[4] = "Nico Robin"
# print(friends[2:4:1])
# print(friends[4], "is hottest")
friends = ["Zoro", "Sanji", "Luffy", "Brook", "Nico", "Nami"]
Lucky_numbers = [1, 7, 8, 20, 21, 99]
# friends.extend(Lucky_numbers) # This add the lucky numbers with the friends lists / combine two different list/with different data types in one
friends.append(
    "Boa Hancock"
)  # Boa hancock added at the list total values in list 7 / index 6
# friends.append("Boa Hancock"[6])# this print the "n" because it "n" is in  the 6th index of the sentence
friends.insert(
    6, "Orihime"
)  # this add value to the index we give , Right now given index is 6 so now the orihime gonna be in the 6th index and the all the value after the 6 gonna move index up
# friends[7] = "hinata" # this replace the 7 index value with the new one which is Orihime
print(friends)
# print(Lucky_numbers)
# friends.remove("Brook")# It's gonna remove the brook from  the list
# friends.clear()# it removes all the elements from the list
# friends.pop()#removes the last element from the list
# print(friends.index("Nico"))#checks the element is in the list or not
# print(friends.count("Zoro"))# checks how many time the element has come in the list
# friends.sort()#this put the elements of the list in the alphabet order 
# friends.reverse()#it just reverse the list elements 
# frnds=friends.copy()#it copies
# print(friends)
print(frnds)
