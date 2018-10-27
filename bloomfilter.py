import sys  # For capturing command line arguments
import hashlib  # For using hash functions


class BloomFilter:

    # Creates the bloom filters with the size of bad password list and number of hash functions
    def __init__(self, size, hash_num):
        self.bit_array = list([False] * size)
        self.size = size
        self.number_hashes = hash_num

    # Function to add bad passwords to the filters
    def add(self, item):
        hash_function = ['sha512', 'sha384', 'sha256', 'sha224', 'md5']
        for i in range(self.number_hashes):
            hasher = getattr(hashlib, hash_function[i])  # Select hash function
            hashed = int(hasher(item.encode('utf-8')).hexdigest(), 16) % self.size  # Hash and divide by size
            self.bit_array[hashed] = True
        return self

    # Function to check if given password is possibly in the filter or definitely not not in the filter
    def contains(self, item):
        in_filter = True
        hash_function = ['sha512', 'sha384', 'sha256', 'sha224', 'md5']
        for i in range(self.number_hashes):
            hasher = getattr(hashlib, hash_function[i])
            hashed = int(hasher(item.encode('utf-8')).hexdigest(), 16) % self.size
            if not self.bit_array[hashed]:
                in_filter = False
        return in_filter


# Function to parse input and bad password list
def parser(any_file):
    parsed = []
    file = open(any_file)
    for line in file:
        parsed.append(line.strip())
    file.close()
    return parsed


# Function to write to output3.txt and output5.txt
def write_output(bloom_filter, input_pws, output_file):
    file = open(output_file, 'w')  # Open file
    for pw in input_pws:
        if bloom_filter.contains(pw):
            file.write('maybe\n')
        else:
            file.write('no\n')
    file.close()  # Close file


# Everything is done within main and the BloomFilter class :) !
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

    # Send the input passwords to be tested against the bloom filters and then written to output files
    print("Comparing input passwords with the Bloom Filters!")
    write_output(bloom_filter3, input_list, out3)
    write_output(bloom_filter5, input_list, out5)
    print("Check output3.txt and output5.txt for results!")


main()
