from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

# É uma entidade específica que implementa o movimento (ou a falta dele).

class Background(Entity):
    def __init__(self, name: str, position):
        super().__init__(name, position)

    def move (self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH