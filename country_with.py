import json

with open('books.json') as f:
    data = json.load(f)

output = {}

for book in data:
    country = book['country']
    author = book['author']
    # name = book.get('author', {}).get('name')
    title = book['title']
    language = book['language']

    output.setdefault(country,{})

    # if country not in output:
    #     output[country] = {}

    if author not in output[country]:
        output[country][author] = {
            # 'name': name,
            'title': [],
            'languagea': []
        }

    output[country][author]['title'].append(title)
    output[country][author]['languagea'].append(language)

# print the output
print(output)

# output ={
#     'Nepal':{
#     'devkota':[1,2,3,4]
#     }
# }
# print(output['Nepal']['devkota'])