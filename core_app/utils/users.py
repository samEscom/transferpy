import hashlib


def str_to_hash(text_to_hash: str):
    text_to_hash = hashlib.md5(text_to_hash.encode())

    return text_to_hash.hexdigest()
