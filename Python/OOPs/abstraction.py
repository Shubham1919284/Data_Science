class CoffeeMachine:

    # These methods represent the internal working.
    # Users are not expected to call them directly.
    def _heat_water(self):
        print("Heating water...")

    def _add_coffee(self):
        print("Adding coffee powder...")

    def _pour_coffee(self):
        print("Pouring coffee into the cup...")

    # This is the method exposed to the user.
    # It hides all the internal complexity.
    def make_coffee(self):
        self._heat_water()
        self._add_coffee()
        self._pour_coffee()
        print("☕ Coffee is ready!")


# Create an object
machine = CoffeeMachine()

# User only needs to call this one method.
machine.make_coffee()