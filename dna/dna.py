import csv
import sys

#reader will help us get the columns
#dictreader will help us get the str values

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) !=3:
        print("Incorrect command-line argument")
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)

        headers = reader.fieldnames #can loop through to get the headers of the csv file

        # TODO: Read DNA sequence file into a variable
        with open(sys.argv[2], "r") as sequence:
            sequence_reader = sequence.read()

            # TODO: Find longest match of each STR in DNA sequence
            sequence_count = {}
            for header in headers[1:]:
                    dna_count = longest_match(sequence_reader, header)
                    sequence_count[header] = str(dna_count)

            # TODO: Check database for matching profiles
            count=0
            for row in reader:
                for header in headers[1:]:
                    if row[header] == sequence_count[header]:
                        count+=1
                        if count==len(headers[1:]):
                            print(row["name"])
                            return
                count=0
            print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
