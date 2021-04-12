all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors (item):
    return item["sexy"]

def generate_li (value):
    return f'<li>{value["label"]}</li>'

colorsSexy=list(filter(filter_colors , all_colors))
listaColors=''
listaColors=list(map(generate_li , colorsSexy))

print(listaColors)
#<li>Red</li><li>Orange</li><li>Pink</li><li>Violet</li>
#'<li>Red</li>', '<li>Orange</li>', '<li>Pink</li>', '<li>Violet</li>']