months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Arp": "April",
    "Ma": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}  # they stored as key and value and can be access by key
# print(months.get("Momo harai", "Not in the dictionary"))# to get the the key and print it if the key is not in the dictionary then it we can give any message we want like : Not in the dictionary
# print(months["Mar"])# we are asking value by giving key
# print(months.items())
# print(months.keys())# prints the keys 
# print(months.values())to print the values 
# months.update({"name": "Momo"})#it is added as new key and value | because the key does and exit and so it creates the key called name and give it value :Momo
months.update({"Jan": "Ahahah"})
# months.pop("Jan")#remove it from the dictionary 
print(months)
