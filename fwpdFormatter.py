"""
A small tool to change crime codes to a better description for GIS use
"""

import csv

# Dictionary of police codes
codes = {
    '200': 'Arson',
    '13A': 'Aggravated Assault',
    '13B': 'Simple Assault',
    '13C': 'Intimidation',
    '510': 'Bribery',
    '220': 'Burglary/Breaking & Entering',
    '250': 'Counterfeiting/Forgery',
    '290': 'Destruction/Damage/Vandalism of Property',
    '35A': 'Drug/Narcotic Violations',
    '35B': 'Drug Equipment Violations',
    '270': 'Embezzlement',
    '210': 'Extortion/Blackmail',
    '26A': 'False Pretenses/Swindle/Confidence Game',
    '26B': 'Credit Card/Automated Teller Machine Fraud',
    '26C': 'Impersonation',
    '26D': 'Welfare Fraud',
    '26E': 'Wire Fraud',
    '39A': 'Betting/Wagering',
    '39B': 'Operating/Promoting/Assisting Gambling',
    '39C': 'Gambling Equipment Violations',
    '39D': 'Sports Tampering',
    '09A': 'Murder & Nonnegligent Manslaughter',
    '09B': 'Negligent Manslaughter',
    '09C': 'Justifiable Homicide',
    '64A': 'Human Trafficking, Commercial Sex Acts',
    '64B': 'Human trafficking, Involuntary Servitude',
    '100': 'Kidnapping/Abduction',
    '23A': 'Pocket-Picking',
    '23B': 'Purse-Snatching',
    '23C': 'Shoplifting',
    '23D': 'Theft From Building',
    '23E': 'Theft from Coin-Operated Machine or Device',
    '23F': 'Theft From Motor Vehicle',
    '23G': 'Theft of Motor Vehicle Parts or Accessories',
    '23H': 'All Other Larceny',
    '240': 'Motor Vehicle Theft',
    '370': 'Pornography/Obscene Material',
    '40A': 'Prostitution',
    '40B': 'Assisting or Promoting Prostitution',
    '40C': 'Purchasing Prostitution',
    '120': 'Robbery',
    '11A': 'Rape',
    '11B': 'Sodomy',
    '11C': 'Sexual Assault With An Object',
    '11D': 'Fondling',
    '36A': 'Incest',
    '36B': 'Statutory Rape',
    '280': 'Stolen Property Offenses',
    '520': 'Weapon Law Offenses',
    '90A': 'Bad Checks',
    '90B': 'Curfew/Loitering/Vagrancy Violations',
    '90C': 'Disorderly Conduct',
    '90D': 'Driving Under the Influence',
    '90E': 'Drunkenness',
    '90F': 'Family Offenses, Nonviolent',
    '90G': 'Liquor Law Violations',
    '90H': 'Peeping Tom',
    '90I': 'Runaway',
    '90J': 'Trespass of a Real Property',
    '90Z': 'All Other Offenses'
}


def reader(infile):
    """
    Read CSV file and return line by line
    :param infile: the input CSV file downloaded from PD
    :return:
    """
    with open(infile, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            yield row


def writer(line, outfile):
    """
    Write results to CSV
    :return:
    """
    record_number = 1
    with open(outfile, 'w', newline='') as outfile:
        out_line = csv.writer(outfile, delimiter=',')
        print("Writing record {0}".format(record_number))
        out_line.writerow(line)
        record_number += 1


def formatter(line, column):
    """
    Checks "offense" column and returns the formatted description
    :parameter line: dict of line data
    :parameter column: column number where crime code is located
    :return: formatted line for printing
    """
    row_number = 0

    if row_number > 0:
        in_code = line[column]
        print("Code {0} found".format(in_code))


reader(input("in file: "))


def dict_search(searchKey):
    """
    Searches codes dict keys for code and returns the value
    :param searchKey: Key to search for. Should be the UCR code from CSV
    :return: Dict value
    """

    if searchKey in codes:
        value = codes[searchKey]
        print(value)
        return value


def run_formatter():
    """
    Get file locations and run the functions
    :return:
    """
    in_file = input("Enter police record CSV file location: ")
    out_file = input("Enter output CSV file location: ")
    code_column = input("Enter column number of crime code (numbering begins at 0): ")

    for i in reader(in_file):
        value = dict_search(i[code_column])  # Search for dict key for each row
        writer(i, out_file)


if __name__ == '__main__':
    run_formatter()
