courses = ["History", "Math", "Physics", "Compsci"]
print(courses)
print(len(courses))
print(courses[0])

# length of a list os [TotalLength - 1]

print(courses[-1]) 	# To print the last item.
print(courses[0:3]) 	# First index is inclusive and last index is not.
print(courses[2:]) 	# Start from 2nd index all the way to end.

courses.append("Art")
courses.insert(0,"Bio")

courses2 = ["English", "Tamil"]
courses.insert(0, courses2) 		# [['English', 'Tamil'], 'Bio', 'History', 'Math', 'Physics', 'Compsci', 'Art']

print(courses)
courses.remove(["English", "Tamil"])

courses.extend(courses2)		# ['Bio', 'History', 'Math', 'Physics', 'Compsci', 'Art', 'English', 'Tamil'] 
print(courses)

courses.remove("English")
print(courses)

x = courses.pop()			# pop will remove the last item in the list and returns the value.
print(x)
print(sorted(courses))			# sorted() will return only the sorted version.
print(courses)
courses.sort()				# courses.sort() will modify the original object.
print(courses)
courses.sort(reverse=True)		# to reverse sort.
print(courses)

print(courses.index("Bio"))		# this will return the index of the element.
print("Bio" in courses)			# this will return True / False
