from .MenuProvider import MenuProvider


class DummyProvider(MenuProvider):
    def __init__(self, num_suggestions: int):
        super().__init__(num_suggestions)
        self.name = 'Garry'
        self.menu = [{
            'title': 'Fry Fish',
            'img': 'http://garry.fish',
            'url': 'http://garry.fish'
        },
                     {
                         'title': 'Fry Pork',
                         'img': 'http://garry.pork',
                         'url': 'http://garry.pork'
                     }]
