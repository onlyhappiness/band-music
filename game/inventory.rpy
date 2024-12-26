init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money=10):
                self.money = money
                self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else: 
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
            if item in self.items:
                return True
            else: 
                return False


label inventory:

    python:
        inventory = Inventory()
        spaghetti = Item("Spaghetti", 3)
        olives = Item("Olives", 4)
        chocolate = Item("Chocolate", 11)

    "Oh, look! I found ten coins!"

    $ inventory.earn(10)

    $ current_money = inventory.money

    "Now I have %(current_money)d coins."

    "My stomach growls loudly."

    if inventory.buy(chocolate):
        "Mmm, chocolate. I'll save that for later... "
    else:
        "I don't have enough money to buy chocolate."

    "Suddenly, I'm hungry"

    jump preshop
    jump shop2

    if inventory.has_item(chocolate):
        "Good thinf I bought that chocolate earlier."
    else:
        "If only I had some chocolate..."

label preshop: 
    $ spaghetticost = spaghetti.cost
    $ olivescost = olives.cost
    $ chocolatecost = chocolate.cost

label shop2:
    menu shop:
        c "I go into the store"

        "Buy spaghetti for %(spaghetticost)d coins.":
            if inventory.buy(spaghetti):
                "Hey, those are uncooked. I can't eat those yet!"
                jump game_continues

        "Buy olives for %(olivescost)d coins.":
            if inventory.buy(olives):
                "I hate olives."
                "And they cost more than the spaghetti."
                "But at least I don't have to cook them... "
                jump game_continues

        "Buy chocolate for %(chocolatecost)d coins.":
            if inventory.buy(chocolate):
                "Mmmm, dark semi-sweet chocolate! My favorite!"
                jump game_continues

        "Buy nothing.":
            jump game_continues         

label fallthrough:
    c "Not enough money..."
    jump shop2

label game_continues:
    "And so I left the store."
    $ current_money = inventory.money
    "I have %(current_money)d left"
