def extract_features(url):

    return [
        len(url),                 # url_length
        1 if url.startswith("http") else 0,  # valid_url
        url.count("@"),           # at_symbol
        0,                        # sensitive_words_count
        len(url.split("/")) if "/" in url else 0,  # path_length
        1 if url.startswith("https") else 0,       # isHttps
        url.count("."),           # nb_dots
        url.count("-"),           # nb_hyphens
        url.count("&"),           # nb_and
        url.lower().count("or"),  # nb_or
        url.count("www"),         # nb_www
        url.count(".com"),        # nb_com
        url.count("_")            # nb_underscore
    ]