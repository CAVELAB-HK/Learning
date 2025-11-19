from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_url_mapping(short_code, original_url, shortened_url):
    row_to_be_inserted = {"short_code": short_code, 
                          "original_url": original_url, 
                          "shortened_url": shortened_url}
    
    response = supabase.table("url_shortener_and_click_analysis").insert(row_to_be_inserted).execute()
    
    if response.data: 
        print("Data inserted")
    else: 
        print("Data not inserted")

def get_original_url(short_code):


def increment_click_count(short_code):
