# Using encode() method for creating hash table
import hashlib

class hashTable: 
    def __init__(self, url, size): 
        self.url = url
        self.size = size
    
    def hash_index(self, key): 
        key_index = key.encode('utf-8')
        hasher = 
    

