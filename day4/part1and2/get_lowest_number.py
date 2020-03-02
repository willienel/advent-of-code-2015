import hashlib
import os


def get_lowest_number(secret_key, hash_start_match="00000"):

    counter = 0

    combined_hash = hashlib.md5(f"{secret_key}{counter}".encode('utf-8')).hexdigest()

    while not combined_hash.startswith(hash_start_match):
        counter += 1
        combined_hash = hashlib.md5(f"{secret_key}{counter}".encode('utf-8')).hexdigest()

    return counter


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), '../input.txt')) as input_file:
        d = input_file.readline()

    print(get_lowest_number(d, "00000"))

    print(get_lowest_number(d, "000000"))
