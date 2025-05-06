details = ['Kayel', 19, ['Boxing', 'Karate', 'Meditation']]

print ('My age is' + str(details[1]))

print (str(details[2][-1]))

details.append("kayel.calleja.j96411@mcast.edu.mt")
print (details)

details[2].append('Marksmanship')
print (details[2])

details_copy = []

for item in details:
    details_copy.append(item)
print(details_copy)

details_copy.pop()

print (details_copy)

print ("I have " + str(len(details_copy[2])) + " hobbies")

details_copy.sort

print (details_copy)

# Q.13 Teacher's Answer 
details_copy.sort(key=str)
