# Creates a csv file for raffle tickets
# Sort output file by item column in excel after running
# For items under 100 entries copy and paste names into wheeldecide
# For items over 100 entries use random number generator to decide winner



import csv

def main():
    # Create a dictionary to store the raffle tickets
    raffle_tickets = {}

    # Get the file name
    inputfilename = input('What would you like the file to be called: ')
    
    # Open the csv file to write to
    with open(inputfilename, 'w', newline='') as csvfile:
        # Create a csv writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Create a loop to collect raffle tickets
        while True:
            # Ask the user for their name
            name = input('What is your name? ')

            # Ask the user for the item they are entering for
            item = input('What are you entering for? ')

            # Ask the user for the number of tickets they are entering
            tickets = input('How many tickets are you entering? ')

            # Create a loop to collect the raffle tickets
            for i in range(int(tickets)):
                # Create a unique ID for each ticket
                ticket_id = str(i)

                # Add the ticket to the dictionary
                raffle_tickets[ticket_id] = [name, item]

                # Write the ticket to the csv file
                csvwriter.writerow([ticket_id, name, item])

            # Ask the user if they are done entering tickets
            done = input('Are you done entering tickets? (y/n) ')

            # If the user is done, break the loop
            if done == 'y':
                break
            
        # Print the raffle tickets
        #print(raffle_tickets)

main()