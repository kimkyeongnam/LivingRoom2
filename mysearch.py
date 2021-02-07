import meilisearch


client = meilisearch.Client("http://127.0.0.1:7700", "apiKey")
index = client.create_index(name='ssr', uid='ssr_uid')  # If your index does not exist
index = client.get_index('ssr_uid')  # If you already created your index

documents = [
    {"id": 123, "title": 'Pride and Prejudice'},
    {"id": 456, "title": 'Le Petit Prince'},
    {"id": 1, "title": 'Alice In Wonderland'},
    {"id": 1344, "title": 'The Hobbit'},
    {"id": 4, "title": 'Harry Potter and the Half-Blood Prince'},
    {"id": 42, "title": 'The Hitchhiker\'s Guide to the Galaxy'}
]

# index.add_documents(documents)  # asynchronous