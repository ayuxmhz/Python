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
# print(months.get("Momo harai", "Not in the dictionary"))
# print(months["Mar"])
# print(months.items())
months.update({"name": "Momo"})
months.update({"Jan": "January", "Name": "Nami"})
months.pop("Jan")
print(months)
