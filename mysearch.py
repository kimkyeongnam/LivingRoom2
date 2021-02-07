import meilisearch

client = meilisearch.Client('http://127.0.0.1:7700', 'masterKey')

# An index is where the documents are stored.
index = client.index('books')

documents = [
  { 'book_id': 123,  'title': 'Pride and Prejudice' },
  { 'book_id': 456,  'title': 'Le Petit Prince' },
  { 'book_id': 1,    'title': 'Alice In Wonderland' },
  { 'book_id': 1344, 'title': 'The Hobbit' },
  { 'book_id': 4,    'title': 'Harry Potter and the Half-Blood Prince' },
  { 'book_id': 42,   'title': 'The Hitchhiker\'s Guide to the Galaxy' }
]

# If the index 'books' does not exist, MeiliSearch creates it when you first add the documents.
index.add_documents(documents) # => { "updateId": 0 }