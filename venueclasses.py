from sqlitedict import SqliteDict

class Venue:
  def __init__(self, id, name, date, tables, persons):
    self.id = id
    self.name = name
    self.date = date
    self.tables = tables
    self.persons = persons

def save(key, value, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value # Using dict[key] to store
            mydict.commit() # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)
 
def load(key, cache_file="cache.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key] # No need to use commit(), since we are only loading data!
        return value
    except Exception as ex:
        print("Error during loading data:", ex)