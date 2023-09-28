import hashlib

def generateUUIDfromString(uuidfromTitle):

    sha = hashlib.sha256()

    sha.update(uuidfromTitle.encode('utf-8'))

    hash_hex = sha.hexdigest()

    ten_letter_uuid = hash_hex[:10]

    return ten_letter_uuid