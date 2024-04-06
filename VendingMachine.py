# Use case: Few drinks item selections with any price (no coin). The customer should be able to insert any notes to buy preferred drinks.
#           The outcome is to release the least amount of notes back to the customer.

class VendingMachine():
    def __init__(self):
        self.notes = [20, 10, 5, 1] # According to Malaysia's vending machine bank notes acceptance
        self.drinks = [
            {
                'drink_name': '100 Plus',
                'cost'      : 3
            },
            {
                'drink_name': 'Milo',
                'cost'      : 4
            },
            {
                'drink_name': 'Redbull',
                'cost'      : 6
            },
            {
                'drink_name': '1664 Blanc',
                'cost'      : 10
            }
        ]
    
    def display_drink_choices(self):
        print('Drinks availability:')
        for index, choice in enumerate(self.drinks):
            print("{}. {} - RM {}".format(index+1, choice['drink_name'], choice['cost']))
        self.validate_drink_selection()

    def calculate_remaining_amount(self, drink, amount_entered):
        remaining_amount = amount_entered - drink['cost']
        print("Your changes of: RM {}, enjoy your {}!".format(str(remaining_amount), drink['drink_name']))

        if remaining_amount:
            # Calculate and return change with using least amount of notes
            change = remaining_amount
            for note in self.notes:
                num_notes = change // note
                if num_notes > 0:
                    print("Return of {} RM {} note(s)".format(str(num_notes), str(note)))
                    change -= num_notes * note
                if change == 0:
                    break
    
    def calculate_note_amount(self, drink):
        note_amount  = 0
        
        while True:
            insert_notes = input("Please insert your notes, enter 'Ok' when done: ")
            if insert_notes.lower() == 'ok':
                # Check if submitted amount is lesser than the cost of the drink
                if note_amount < drink['cost']:
                    print("Insufficient amount! Cost of the drink: RM {} and total amount inserted: RM {}".format(drink['cost'], note_amount))
                else:
                    break
            else:
                try:
                    note = int(insert_notes)
                    if note in self.notes:
                        note_amount += note
                        print("Total amount inserted: RM {}".format(note_amount))
                    else:
                        print("Note invalid, please insert a valid note of {}".format(", ".join(str(denom) for denom in self.notes)))
                except ValueError:
                    print("Invalid input. Please enter a number or 'Ok'.")
        self.calculate_remaining_amount(drink, note_amount)

    def validate_drink_selection(self):
        while True:
            try:
                select_drink = int(input("Please enter the number of the drink to purchase: ")) # Prompt for user input to select drinks

                if select_drink < 1 or select_drink > len(self.drinks):
                    print("Entered number is invalid. Please enter a valid number again.")
                else:
                    break
            except ValueError:
                print("Invalid input, please enter the number of the drink.")
        get_selected_drink = self.drinks[select_drink-1]
        print("Selected drink is: {} - RM {}".format(get_selected_drink['drink_name'], get_selected_drink['cost']))
        self.calculate_note_amount(get_selected_drink)