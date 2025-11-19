-- Create database tables

CREATE TABLE url_shortener_and_click_analysis (
    id SERIAL PRIMARY KEY, 
    short_code VARCHAR(20) UNIQUE NOT NULL,  
    shortened_url VARCHAR(200) NOT NULL,   
    original_url TEXT NOT NULL,               
    click_count INT DEFAULT 0, 
    created_at TIMESTAMP DEFAULT NOW()
);
