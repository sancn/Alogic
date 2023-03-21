import json
con_count=0

# load the data from the JSON file
with open('/home/intern-1/Desktop/sc-python/file_handling/books.json') as f:
    data = json.load(f)

# get user input for the country
country= input("Enter a country: ")

# search for the country in the data
for da in data:
    if da['country'] == country:
    # print all the details for that country
        print(f"Author: {da['author']}")
        print(f"Country: {da['country']}")
        print(f"Image Link: {da['imageLink']}")
        print(f"Language: {da['language']}")
        print(f"Link: {da['link']}")
        print(f"Pages: {da['pages']}")
        print(f"Title: {da['title']}")
        print(f"Year: {da['year']}")
        con_count+=1
print(con_count)


