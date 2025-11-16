# Using encode() method for creating hash table
import hashlib
import pandas as pd
from generate_url import generate_random_url

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


def main(): 
    hash_table = hashTable(100)
    list_of_urls = []

    for i in range(100): 
        url = generate_random_url(base_url="https://random.com/")
        hash_array_index_number, key = hash_table.generate_hash_array_index_number(url, 100)
        table = hash_table.setting_up_hash_table(hash_array_index_number, key, url)
        df = pd.DataFrame(table)
        df.to_csv("list_of_url.csv", index=True)


if __name__ == "__main__": 
    main()  





