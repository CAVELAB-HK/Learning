import secrets

def generate_random_url(base_url="https://random.com/"):
    token = secrets.token_urlsafe()
    url = f"{base_url}{token}"
    return url

def generate_random_url_dict(url): 
    content = secrets.token_urlsafe()
    return {url: content}



