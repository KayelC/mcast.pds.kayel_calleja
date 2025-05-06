length=56
width=34.56
shape='rectangle'

print(length)
print(width)
print(shape)

area=length*width
perimeter=2*length+width

print(area)
print(perimeter)

area_int = length * int(width)

print(type(area) == type(area_int))

msg = "".join(['The area of the ', shape, ' is ', str(area_int), 'cm2'])
print(msg)

print ('The unit of measurement is ' + msg[-3:-1])