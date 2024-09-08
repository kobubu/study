location = {
'Red Square': 'Russia',
'Swallow Nest': 'Russia',
'Niagara Falls': 'USA',
'Grand Canyon': 'USA',
'Louvre': 'France',
'Hermitage': 'Russia'
}
for ind, value in location.items():
    if value != 'Russia':
        location[ind] = 'Unavailable'
print(location)
#{'Red Square': 'Russia', 'Swallow Nest': 'Russia',
#'Niagara Falls': 'Unavailable', 'Grand Canyon': 'Unavailable', 'Louvre': 'Unavailable', 'Hermitage': 'Russia'}
