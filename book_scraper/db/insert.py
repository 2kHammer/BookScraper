from pymongo.errors import BulkWriteError, DuplicateKeyError

def check_reader_in_db(id, db):
    reader_collection = db['readers']
    entry = reader_collection.find_one({'_id': id})
    if entry:
        return True
    else:
        return False

def insert_reader(reader, db):
    reader_collection = db["readers"]
    reader_dic = reader.__dict__
    reader_dic["_id"] = reader_dic.pop("id")
    reader_dic["books"]= [rd.mongo_dict() for rd in reader_dic["books"]]
    db_id = -1
    if not reader_collection.find_one({'_id': reader_dic["_id"]}):
        #already in db
        result = reader_collection.insert_one(reader_dic)
        db_id = result.inserted_id
    else:
        #not in db
        result = reader_collection.replace_one({"_id": reader_dic["_id"]}, reader_dic,upsert=True)
        db_id = result.upserted_id
    # add logging
    return db_id





def insert_books(books, db):
    book_collection = db["books"]
    books_dic = [b.__dict__ for b in books]
    amount_books = len(books_dic)
    for b_d in books_dic:
        b_d["_id"] = b_d.pop("id")

    amount_inserted = 0
    amount_already_inserted = 0
    try:
        # add better logging
        result = book_collection.insert_many(books_dic, ordered=False)
        amount_inserted = len(result.inserted_ids)
        amount_already_inserted = 0
    except BulkWriteError as bwe:
        # if the error occurs, result ist None -> find better solution
        #print(str(len(bwe.details["writeErrors"])) + " books should already be in db")
        amount_already_inserted = len(bwe.details["writeErrors"])
        amount_inserted = amount_books - amount_already_inserted
    return amount_inserted, amount_already_inserted

        
