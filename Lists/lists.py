fruits = ["peaches", "pears", "apples"]
years = [2, "1998", 2.5, 987, "1994"]

print(fruits, years)

#adds the item orange to the list
fruits.append("oranges")
print(fruits)

#adds all items in list years to the list of fruits
fruits.extend(years)
print(fruits)

#removes the item orange from the list
fruits.remove("oranges")
print(fruits)

#removes item at index position 1.  Index starts at 0
fruits.pop(1)
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.sort()
print(fruits)

