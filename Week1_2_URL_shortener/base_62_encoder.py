def base_62_encoder(url): 
    url_spliter = list(url.split("/"))
    url_spliter = url_spliter.pop(2)
    url_spliter = url_spliter.pop(1)
    url_spliter = url_spliter.pop(0)
    return url_spliter

print(base_62_encoder("https://www.something.com/random"))