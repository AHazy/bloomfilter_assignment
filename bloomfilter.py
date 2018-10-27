import sys  # For capturing command line arguments
import hashlib  # For using hash functions


class BloomFilter:

    # Creates the bloom filters with the size of bad password list and number of hash functions
    def __init__(self, size, hash_num):
        self.bit_array = list([False] * size)
        self.size = size
        self.number_hashes = hash_num


# Function to parse input and bad password list
def parser(any_file):
    parsed = []
    file = open(any_file)
    for line in file:
        parsed.append(line.strip())
    file.close()
    return parsed


def main():
    # Assign command line arguments to variables
    out3 = sys.argv[6]
    out5 = sys.argv[7]
    bad_pws = sys.argv[2]
    input_file = sys.argv[4]

    # Send PW files to parser to get back as lists
    bad_list = parser(bad_pws)
    input_list = parser(input_file)

    # Create two bloom filters
    print("Bloom Filters created!")
    bloom_filter3 = BloomFilter(len(bad_list) * 8, 3)
    bloom_filter5 = BloomFilter(len(bad_list) * 8, 5)

    # Setup the bloom filters by adding the bad passwords
    print("Adding bad passwords to the Bloom Filters!")
    for pw in bad_list:
        bloom_filter3.add(pw)
        bloom_filter5.add(pw)


main()
