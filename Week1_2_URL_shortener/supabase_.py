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
    
    try: 
        response = supabase.table("url_shortener_and_click_analysis").insert(row_to_be_inserted).execute()
        return response.data
    except Exception as error:
        print(f"{error}")

def edit_url_mapping(short_code, original_url, shortened_url):
    row_to_be_edited = {"short_code": short_code, 
                          "original_url": original_url, 
                          "shortened_url": shortened_url}
    
    response = (
    supabase.table("url_shortener_and_click_analysis")
    .update(row_to_be_edited)
    .eq("short_code", short_code)
    .execute()
)
    
    try:
        return response.data
    except Exception as error:
        print(f"{error}")


def get_original_url(short_code):

    response = (
        supabase.table("url_shortener_and_click_analysis")
        .select("original_url")
        .eq("short_code", short_code)
        .limit(1)
        .single()
        .execute()
    )

    try: 
        return response.data
    except Exception as error: 
        print(f"{error}")


def increment_click_count(short_code):
    response = (
        supabase.table("url_shortener_and_click_analysis")
        .select("click_count")
        .eq("short_code", short_code)
        .single()
        .execute()
    )
    
    try:
        current_count = response.data["click_count"]
        
        update_response = (
            supabase.table("url_shortener_and_click_analysis")
            .update({"click_count": current_count + 1})
            .eq("short_code", short_code)
            .execute()
        )
        
        return update_response.data
    except Exception as error:
        print(f"Error: {error}")
        return None

