from passlib.hash import sha256_crypt


def generate_pword_hash(pword):
    return sha256_crypt.hash(pword)


def verify_pword_hash(pword, hash):
    return sha256_crypt.verify(pword, hash)
