# Using encode() method for creating hash table
import hashlib
import secrets

def generate_random_url(base_url = "https://random.com/"):
    token = secrets.token_urlsafe()
    url = f"{base_url}{token}"
    return url

class hashTable: 
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def generate_hash_array_index_number(self, url, size): 
        url = url.encode('utf-8')
        key = hashlib.sha3_256(url).hexdigest()
        hash_element_index = int(key, 16) % size
        return hash_element_index, key
    
    def setting_up_hash_table(self, hash_element_index, key, url): 
        self.table[hash_element_index] = {key: url}
        return self.table

hashTable = hashTable(10)

list_of_urls = []
for i in range(10): 
    url = generate_random_url(base_url = "https://random.com/")
    hash_array_index_number, key = hashTable.generate_hash_array_index_number(url, 10)
    table = hashTable.setting_up_hash_table(hash_array_index_number, key, url)

print(hashTable.table[4])



