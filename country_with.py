import json

# load the data from the JSON file
with open('books.json') as f:
    data = json.load(f)

# create an empty dictionary to store the output
output = {}

# loop through each book in the data
for book in data:
    country = book['country']
    author = book['author']
    # name = book.get('author', {}).get('name')
    title = book['title']
    language = book['language']

    # create the nested dictionary if it does not exist
    if country not in output:
        output[country] = {}

    if author not in output[country]:
        output[country][author] = {
            # 'name': name,
            'title': [],
            'languagea': []
        }

    # append the book title and language to the nested dictionary
    output[country][author]['title'].append(title)
    output[country][author]['languagea'].append(language)

# print the output
print(output)
