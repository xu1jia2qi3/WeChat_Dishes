import random


class MenuProvider:
    def __init__(self, num_suggestions: int):
        self.num_suggestions = num_suggestions
        self.name = 'base class'
        self.menu = []
        self._update_menu()

    def get_menu(self):
        k = min(self.num_suggestions, len(self.menu))
        return random.sample(self.menu, k)

    def _update_menu(self):
        return

    def debug_info(self):
        print(self.name)
        print(self.menu)
