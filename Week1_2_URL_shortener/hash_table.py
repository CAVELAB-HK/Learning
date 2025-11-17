# Using encode() method for creating hash table
import hashlib
import pandas as pd
from generate_url import generate_random_url, generate_random_url_dict

class hashTable: 
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def generate_hash_array_index_number(self, url, size): 
        url = url.encode('utf-8')
        key = hashlib.sha3_256(url).hexdigest()
        hash_element_index = int(key, 16) % size
        return hash_element_index
    
    def open_addressing(self, hash_element_index, url, url_content): 
        for _ in range(len(self.table)): 
            index = (hash_element_index + _) % self.size
            if self.table[index] == None: 
                self.table[index] = {"url": url, "url_content": url_content}
                break
            else: 
                continue
        return self.table
    
    def closed_addressing(self, hash_element_index, url, url_content): 
        if self.table[hash_element_index] != None:
            self.table[hash_element_index].append({"url": url, "url_content": url_content})
        else: 
            self.table[hash_element_index] = [{"url": url, "url_content": url_content}]
        return self.table
    
def main(): 
    hash_table_open = hashTable(100)
    hash_table_closed = hashTable(100)

    for _ in range(100): 
        url = generate_random_url(base_url="https://random.com/")
        url_dict = generate_random_url_dict(url)
        actual_url = list(url_dict.keys())[0]  
        actual_content = list(url_dict.values())[0]

        hash_array_index_number_open = hash_table_open.generate_hash_array_index_number(actual_url, 100)
        hash_array_index_number_closed = hash_table_closed.generate_hash_array_index_number(actual_url, 100)
        
        final_table_open = hash_table_open.open_addressing(hash_array_index_number_open, actual_url, actual_content)
        final_table_closed = hash_table_closed.closed_addressing(hash_array_index_number_closed, actual_url, actual_content)

    print("url hash table open addressing method: \n")
    print("=========================================================================")
    for i, slot in enumerate(final_table_open): 
        if slot is not None:
            print(f"Index {i}: 1 URL")
            print(f"  - {slot['url']}")
            
    print("=========================================================================")
    print("\n url hash table closed addressing method: \n")
    for i, slot in enumerate(final_table_closed):
        if slot is not None and len(slot) > 0:
            print(f"Index {i}: {len(slot)} URLs")
            for item in slot:
                print(f"  - {item['url']}")

if __name__ == "__main__": 
    main()  
