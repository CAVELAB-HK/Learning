from base_62 import base_62_encoder
from generate_url import generate_random_url
from supabase_ import insert_url_mapping

print("starting URL generation")
print("==========================================")
counter = 1
for _ in range(100): 
    url = generate_random_url(base_url="https://random.com/")
    short_code = base_62_encoder(counter)
    shortened_url = "https://cavelab.com/" + base_62_encoder(counter)
    
    print(f"Inserting {counter}: {short_code} → {url[:50]}...")
    insert_url_mapping(short_code, url, shortened_url)
    counter += 1

print("Done!")




