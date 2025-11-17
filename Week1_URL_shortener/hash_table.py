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
    
    # def close_addressing(self, hash_element_index, url): 
    
def main(): 
    hash_table = hashTable(100)
    final_table = []

    for _ in range(100): 
        url = generate_random_url(base_url="https://random.com/")
        url_dict = generate_random_url_dict(url)
        actual_url = list(url_dict.keys())[0]  
        actual_content = list(url_dict.values())[0]

        hash_array_index_number = hash_table.generate_hash_array_index_number(actual_url, 100)
        final_table = hash_table.open_addressing(hash_array_index_number, actual_url, actual_content)

    df = pd.DataFrame(final_table)
    df.to_csv("Week1_URL_shortener/list_of_url.csv", index=False)


if __name__ == "__main__": 
    main()  
