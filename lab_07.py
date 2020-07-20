from collections import defaultdict


# Return True if the two strings have ne mismatch
def oneMismatch(s1, s2):
    # s1 and s2 have the same length
    if len(s1) != len(s2):
        raise Exception("Error. Strings should have same length".format(s1, s2))
    mm = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: mm += 1
        if mm > 1: return False
    return mm == 1


# Return the mismatch
def getMismatch(s1, s2):
    # s1 and s2 have the same length
    # there is exactly one mismatch
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return min(s1[i], s2[i]) + max(s1[i], s2[i])
    raise Exception("Error. Strings should have one mismatch".format(s1, s2))


if __name__ == '__main__':
    names2lower = False  # Distinguish upper case (usually first letter) or not
    minNameFreq = 10  # name is at least 10 times in PubMed

    d = defaultdict(set)

    # Strings of size 5 must have a 2 mer in common if they differ by max. one character
    # at 6 it is 3, etc.
    l2n = {5: 2, 6: 3, 7: 3, 8: 4, 9: 4}

    # Frequency of names as given in the PubMed name data
    name2freq = defaultdict(int)

    # Read data from file
    i, j = 0, 0
    for line in open("Pubmed.Forename.txt"):
        i += 1
        if i == 1:
            continue  # Ignore head line of file
        # if i>10: break
        # Each line has name and its freq tab delimited
        # Get the first name as name, its length in l, and its frequency as num
        name = line.split("\t")[0].strip()
        if names2lower:
            name = name.lower()
        l = len(name)
        num = int(line.split("\t")[1])
        # If the name has a given frequency (ignore rare names, which may include
        # typos and similar) and the length l is within boundaries, then
        # put name in dictionary d with key l and value is set of names.
        # Also count freq of letters in name
        if num > minNameFreq and 4 < l < 10:
            j += 1
            d[len(name)].add(name)
            name2freq[name] = num

    print("Read %d names and will process %d" % (i, j))

    # Process each length l at a time
    for l in d.keys():
        # Create a dictionary of the nmers in names of length l
        nmer2name = defaultdict(set)
        # For all names of length l
        for name in d[l]:
            # Get all nmers and index the name by the nmer
            for i in range(l - l2n[l]):
                nmer = name[i:i + l2n[l]]
                nmer2name[nmer].add(name)
        # For all nmers
        print("Processing %d nmers of strings of length %d" % (len(nmer2name.keys()), l))
