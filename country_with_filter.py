import json

def filter_by_country(books):
    output = {}
    for book in books:
        country = book['country']
        author = book['author']
        title = book['title']
        language = book['language']

        output.setdefault(country,{})

        if author not in output[country]:
            output[country][author] = {
                'title': [],
                'languagea': []
            }

        output[country][author]['title'].append(title)
        output[country][author]['languagea'].append(language)

    return output

with open('books.json') as f:
    data = json.load(f)

filtered_data = filter(lambda book: book['country'] == 'England', data)

output = filter_by_country(filtered_data)

print(output)
