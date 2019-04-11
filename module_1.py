# Module 1 - Functions Associated w/ Script1


def get_clean_file_utf8(original_file):
    # Python throws an error when trying to read text.
    # This code creates a new file and ignores any characters that can't be read.
    
    # Create New File
    new_file= open('train_clean.txt', 'w')

    with open(original_file, 'rb') as f:
        lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
        for line in lines:
            new_file.write(line)
        new_file.close()



