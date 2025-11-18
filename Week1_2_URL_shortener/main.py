from base_62 import base_62_encoder
from generate_url import generate_random_url
from hash_table import hashTable
import random
import base64
import pandas as pd

item_number = random.randint(1, 100)
print(item_number)

with open("Week1_2_URL_shortener/hash_table.py") as hash_table_file:
	exec(hash_table_file.read())
	
hash_table_open = hashTable(item_number)

# secrets.token_urlsafe() uses URL-safe base64
# different from regular base64
# therefore use base64.urlsafe_b64decode() instead
# just a remark, but we won't use it here

counter = 1
for _ in range(item_number): 
    url = generate_random_url(base_url="https://random.com/")
    shortened_url = "https://cavelab.com/" + base_62_encoder(counter)
    index_in_hash_table = base_62_encoder(counter)
    counter += 1
    
    hash_index = hash_table_open.generate_hash_array_index_number(index_in_hash_table, item_number)
    open_addressed_hash_table = hash_table_open.open_addressing(hash_index, url, shortened_url, 100)

# For reference 
'''
df = pd.DataFrame(open_addressed_hash_table)
df.to_csv("Week1_2_URL_shortener/test.csv", index=False)
'''  




