import json

# load the data from the JSON file
with open('books.json') as f:
    data = json.load(f)

# unique_country=set()
# # unique_author=[]

# for book in data:
#     unique_country.add(book['country'])

# print(unique_country)


countries = [book['country'] for book in data]

country_counts = {}
for country in countries:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

unique_countries = [country for country in country_counts if country_counts[country] == 1]
print(unique_countries)