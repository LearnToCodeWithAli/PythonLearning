

# CLI where we're ordering cakes from a cake shop
# Command line interface

# ask customer to choose a cake
# confirm cake selection - if yes, add to order. if no, return to menu
# checkout
# ask for delivery address
# charge customer for the cake

#sarah

class CakeShop:

    def __init__(self):
        self.cakes = {"chocolate": 10,
                      "confetti": 8,
                      "tres leches": 1000,
                      "strawberry shortcake": 9,
                      "oreo": 7.5}
        self.delivery_address = ""
        self.order = []

    def choose_cake(self):
        print("\nWelcome to Sarah's CakeShop!\n")

        for index, (cake, cost) in enumerate(self.cakes.items(), 1):
            print(f"{index}. {cake} - ${cost}")

        selection = int(input("\nWhich cake would you like to purchase? Type 0 to view cart! ")) - 1

        if selection == -1:
            self.view_cart()
        else:
            self.add_to_order(list(self.cakes)[selection])

    def add_to_order(self, cake):
        option = input(f"Would you like to purchase {cake}? Y/N ").upper()

        match option:
            case "Y":
                self.order.append(cake)
            case "N":
                pass

        self.choose_cake()

    def choose_delivery_address(self):
        # todo add code for delivery address
        pass

    def bake_cake(self):
        # todo add code here
        ...

    def print_receipt(self):
        total = 0

        for each in self.order:
            print(f"{each} - ${each}")
            total += self.cakes[each]

        print(f"Total: ${total}")

    def checkout(self):
        self.print_receipt()
        print("Complete purchase? ")

        #todo complete purchase

    def view_cart(self):
        self.print_receipt()
        selection = input("\nWhat would you like to do? \nP - Purchase \nM -Main Menu \n")

        match selection:
            case "P":
                self.checkout()
            case "M":
                self.choose_cake()


cake_shop = CakeShop()
cake_shop.choose_cake()























