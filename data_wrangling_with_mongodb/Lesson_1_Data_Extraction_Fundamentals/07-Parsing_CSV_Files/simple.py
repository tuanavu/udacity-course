# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    
    with open(datafile, "rb") as f:
        # read first header line
        header = f.readline().split(",")
        # read next 10 lines
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            # empty dict
            entry = dict()

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter+=1
                
    return data

def parse_csv(datafile):
    """ Parse file using csv module
    """
    data = []
    n = 0
    with open(datafile, "r") as f:
        r = csv.DictReader(f)
        for line in r:
            data.append(line)

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)

    d2 = parse_csv(datafile)

    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    assert d2[0] == firstline
    assert d2[9] == tenthline

if __name__ == "__main__":
    # datafile = os.path.join(DATADIR, DATAFILE)
    # parse_file(datafile)    
    test()