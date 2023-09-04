import couchdb

# Connect to CouchDB server
server = couchdb.Server('http://localhost:5984')

# Create or access a database
db_name = 'UserBank'
if db_name in server:
    db = server[db_name]
else:
    db = server.create(db_name)

# Create a document
doc_data = {
    'name': 'Ben Carlson',
    'email': 'johndoe@bencarlson.com',
    'age': 30
}

# Insert the document into the database
doc_id, doc_rev = db.save(doc_data)

# Retrieve a document by its ID
retrieved_doc = db[doc_id]
print("Retrieved Document:")
print(retrieved_doc)

# Update a document
retrieved_doc['age'] = 31
db.save(retrieved_doc)

# Retrieve the updated document
updated_doc = db[doc_id]
print("Updated Document:")
print(updated_doc)

# Delete a document
db.delete(updated_doc)
print("Document Deleted")
