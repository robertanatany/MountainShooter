class Entity (ABC):
    def __init__(self, name: str,  position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset' + name + '.png')
        self.position = position

    def move (self, ):
        pass

