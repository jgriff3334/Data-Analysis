parks=['black canyon', 'acadia', 'glacier', 'yellowstone', 'isle royale', 'redwood', 'zion', 'grand canyon', 'yosemite']
print(parks[0])
print(parks[1])
print(parks[2].upper())
print(parks[3].title())
print(parks[4].title())
print(parks[5])
print(parks[6].upper())
print(parks[7].upper())
print(parks[8].title())
print(parks[-1].title())
print(parks[-2].upper())
print(parks[-3].title())
print(parks[-4].upper())
print(parks[-5].title())
print(parks[-6].upper())
print(parks[-7].title())
print(parks[-8].upper())
print(parks[-9].title())
message="I would like to travel to all the national parks. The first one I will visit is " + parks[4].title() + "."
print(message)
parks.append('crater lake')
print(parks)
del parks[9]
print(parks)
parks.insert(9, 'crater lake')
print(parks)
popped_parks = parks.pop()
print("I have already visited " + popped_parks.title() + ".")
print(parks)
too_far = 'glacier'
parks.remove(too_far)
print(parks)
print("\nI think " + too_far + " national park is too far to visit right now.")

