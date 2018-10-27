import sys  # For capturing command line arguments
import hashlib  # For using hash functions


class BloomFilter:

    # Creates the bloom filters with the size of bad password list and number of hash functions
    def __init__(self, size, hash_num):
        self.bit_array = list([False] * size)
        self.size = size
        self.number_hashes = hash_num









def main():
    # Assign command line arguments to variables
    out3 = sys.argv[6]
    out5 = sys.argv[7]
    bad_pws = sys.argv[2]
    input_file = sys.argv[4]

    # Send PW files to parser to get back as lists
    bad_list = parser(bad_pws)
    input_list = parser(input_file)


main()
