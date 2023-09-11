guests = ['michael jordan', 'kobe bryant', 'emma stone', 'whitney houston', 'chris evans']
print(guests)
cannot_attend = 'chris evans'
guests.remove(cannot_attend)
print(cannot_attend.title() + "is out of town and cannot make it.")
guests.append('travis kelce')
message_1 = guests[0].title() + ", you are invited to a dinner party tonight."
print(message_1)
print(guests[1].title() + ", please accept this invitation to my dinner party tonight at seven.")
message_2 = "Hello " + guests[2].title() + "! You're invited to a dinner party at my place tonight!"
print(message_2)
print("Good morning, " + guests[3].title() + ". Would you like to attend a dinner party at my house tonight?")
message_3 = "I think the last person to invite to the dinner party is " + guests[4].title() + "."
print(message_3)
print("Hey everyone! I ordered a larger table and will be inviting more people. Any suggestions?")
guests.insert(0, 'audrey hepburn')
guests.insert(3, 'kerry walsh')
guests.insert(7, 'ghandi')
message_1 = guests[0].title() + ", you are invited to a dinner party tonight."
print(message_1)
print(guests[1].title() + ", please accept this invitation to my dinner party tonight at seven.")
message_2 = "Hello " + guests[2].title() + "! You're invited to a dinner party at my place tonight!"
print(message_2)
print("Good morning, " + guests[3].title() + ". Would you like to attend a dinner party at my house tonight?")
message_3 = "I think the last person to invite to the dinner party is " + guests[4].title() + "."
print(message_3)
print("Hello, " + guests[5].title() + ", please accept this invitation to my dinner party tonight.")
print(guests[6].title() + ", you are cordially invited to my dinner party this evening.")
print(guests[7].title() + ", you are cordially invited to my dinner party this evening.")
print("Hello everyone! My table has been delayed and I can only invite two people tonight. Aplogies.")
popped_ghandi = guests.pop()
print("Hey, " + popped_ghandi.title() + ", unfortunately I had less room than I thought for tonight and have to uninvite you to dinner. My apologies")
popped_travis = guests.pop()
print("Hey, " + popped_travis.title() + ", unfortunately I don't have enough space for you tonight and have to reschedule. So sorry.")
popped_whitney = guests.pop()
print("Howdy, " + popped_whitney.title() + ". So sorry, I have to reduce my number of guests for tonight. Can we reschedule?")
popped_emma = guests.pop()
print("Hello " + popped_emma.title() + ". I apologize. I have to cut the number of people at dinner tonight and will need to reschedule with you.")
popped_kerry = guests.pop()
print("Hi " + popped_kerry.title() + ". We will need to reschedule since I do not have as much room as I thought.")
popped_kobe = guests.pop()
print("Hi " + popped_kobe.title() + ". We will need to reschedule for another night as I had to reduce my number of guests tonight.")
print(guests[0].title() + ". We are still on for tonight, just us three.")
print(guests[1].title() + ". We are still on for tonight, just us three.")
del guests[0]
del guests[0]
print(guests)
