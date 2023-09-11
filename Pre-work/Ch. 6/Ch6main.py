my_dict = {    
    'soccer': ['Manchester City', 'Bayern Munich', 'Seattle Sounders'],
    'formula one': {'driver':'andretti'},
    'football': {'nfl': ['seahawks', 'packers', 'NOT THE PATRIOTS ANYONE BUT TOM BRADY'],
                 'college': ['Clemson', 'UCLA', 'ANYONE BUT ALABAMA']}
}
print(isinstance(my_dict['football']['college'],list))



# my_dict['new key'] = 'Alphonse'
# my_dict[2] = 'cheesy bread' 

# print(my_dict)

# x = my_dict.get(3)
# print(x)

# for key, value in my_dict.items():
#     print(f'The key is {key}')
#     print(f'And this is the value:{value}')

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)
