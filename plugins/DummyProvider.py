from .MenuProvider import MenuProvider


class DummyProvider(MenuProvider):
    def __init__(self, num_suggestions: int):
        super().__init__(num_suggestions)
        self.name = 'GarryGe'
        self.menu = [
            {
                'title': '炸鱼',
                'img': 'http://garry.fish',
                'url': 'http://garry.fish'
            },
            {
                'title': '炸猪排',
                'img': 'http://garry.pork',
                'url': 'http://garry.pork'
            }
        ]
