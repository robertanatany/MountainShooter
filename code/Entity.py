from abc import ABC, abstractmethod, abstractproperty

import pygame

# Entity: Define que tudo no jogo tem imagem, posição e sabe se mover.
# Mas ela sozinha não "existe" (por isso é ABC).

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod # decoretor
    def move (self, ):
        pass

