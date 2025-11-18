import hashlib

class hashTable: 
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def generate_hash_array_index_number(self, url, size): 
        url = url.encode('utf-8')
        key = hashlib.sha3_256(url).hexdigest()
        hash_element_index = int(key, 16) % size
        return hash_element_index
    
    def open_addressing(self, hash_element_index, url, shortened_url, click_count): 
        for _ in range(len(self.table)): 
            index = (hash_element_index + _) % self.size
            if self.table[index] == None: 
                self.table[index] = {"url": url, "shortened_url": shortened_url, "click_count": click_count}
                break
            else: 
                continue
        return self.table
    
    def closed_addressing(self, hash_element_index, url, shortened_url, click_count): 
        if self.table[hash_element_index] != None:
            self.table[hash_element_index].append({"url": url, "shortened_url": shortened_url, "click_count": click_count})
        else: 
            self.table[hash_element_index] = [{"url": url, "shortened_url": shortened_url, "click_count": click_count}]
        return self.table

# For checking
'''
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
'''