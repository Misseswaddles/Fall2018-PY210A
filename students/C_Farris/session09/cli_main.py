#!/usr/bin/env Python3

########
#Created by: Carol Farris
#Date: 12/11/18
#Purpose: Remake Mailroom in OO fashion
#CLi_main is to store all the UI and print statements
#Progress:  

########

import sys
import os
from textwrap import dedent

from OO_Mailroom import Donor, DonorCollection


def thank_you():
    """Returns a user selected Donor thank you letter for either
       the sum of the donations or their last donation."""
    getPerson = get_donor()
    donation = get_new_Donation(getPerson)
    print(assemble_thank_you(getPerson, donation))#oritional thank you printed to console. 


def get_donor():
    """Prompts user to provide donor name and returns name if found or adds to collection"""
    donor = ''
    while dc.donor_in_dictionary(donor) == False:   #note, take out dictionary in the definition in teh DC collection
        donor = input('\nPlease enter the donors first and last name,  '
                      'type List to get donor list or 1 to exit ==>')
        donor = donor.strip().lower().title()

        if donor == str(1):
            exit_out()

        if donor == 'List':
            print(dc.list_donors())

        #edit.    
        if dc.donor_in_dictionary(donor):
            dc.addDonor(donor, Donor(donor))
            return donor

        if not donor == 1 and not donor == "List":
            print("\n>>>>>Donor specified not found in collection.<<<<<<<\n")
            repeat = input(("Do you wish to add person? Type: Y\nPress any other key to retry: "))
            repeat = repeat.strip().lower().title()

            if repeat == 'Y':
                dc.addDonor(donor, Donor(donor))
                return donor


def get_new_Donation(getPerson):
    """
    Asks user to specify donation amount and will error out if 
    User specifies other than a float amount.
    :Param: none
    returns: donation retrieved from user
    """
    getDonation = ''
    while not type(getDonation) is float:
        try:
            getDonation = float(input("Please enter donation amount: "))
            dc.add_donor_donation(getPerson,getDonation)
            print("New donation of ", getDonation, " was added to "+ getPerson +"\'s file.")
        except ValueError:
                print('Sorry, that isn\'t a valid dollar amount. Please retry')
    return getDonation




def assemble_thank_you(getPerson, donation):
        return dedent(
        '''\tDear {},
        Thank you for your generous donation of ${} to our cause.
        
        Sincerely,
        The Team'''.format(getPerson, donation))


def make_report():
    """returns report generated by donor collection """
    report = dc.create_report()
    printReport(report)


def printReport(report): # Put almost all in Donor Collection.
    """
    prints report made by make_report
    :param (name): sorted list in ascending order that
                   contains required information
                   for each donor
    :return: It prints, neet to put into a return statement####
    """
    Header = ['Donor Name', 'Total Donation', 'Number Donations', 'Average Donation']
    print("\n{:20} {:<15} {:>5} {:<25}".format(Header[0], Header[1], Header[2], Header[3]))
    for donor in report:
        print('{:<20}'.format(donor[1]), '{:<15,}'.format(donor[0]),
              '{:>5}'.format(donor[2]), '{:>25,}'.format(donor[3]))    


def all_donors():
    print("you selected to send thank you to all donors")
    print("first call list, for each key, print the thank you.")
    dc.save_all_thank_yous()
    print("finished all donors")


def exit_out():
    """
    produces a clean exit from the program
    """
    print("Exiting program...\n")
    sys.exit()


def main():
    """Prompts user for action selection and directs to the relevant action."""
    print("Welcome to the Mailroom!")
    answer = ""
    while answer != '1' or '2' or '3' or '4':
        try:
            print("\n\nPlease select from the following:\n")
            print("(1) - Exit\n" +
                  "(2) - Create a Report\n" +
                  "(3) - Thank you letter\n" +
                  "(4) - send thank you letters to all donors\n")
            answer = input(' ==> ')
            answer = answer.strip()
            answer = answer[0:1].lower()
            user_choices.get(answer)()
        except TypeError:
            retry()


def retry():
    """
    will prompt user to retry selection to make it valid
    :param: none
    :return: none
    """
    print("\n\n\n##########_ERROR_##############")
    print("Please use the actual choices!")
    print("###############################\n\n\n")
    return None


if __name__ == '__main__':
    donor_mock = [Donor("William Gates III", [653772.32, 12.17]),
                Donor("Jeff Bezos", [877.33]),
                Donor("Paul Allen", [663.23, 43.87, 1.32]),
                Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                Donor("John Galt", [25.00, 9038.01, 0.01])]

    user_choices = {'3': thank_you,
                    '2': make_report,
                    '1': exit_out,
                    '4': all_donors}

    dc = DonorCollection(donor_mock)
    main()