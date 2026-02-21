from code.Background import Background
from code.Const import WIN_WIDTH, WIND_HEIGHT


# É o "balcão de pedidos". O Level pede "Level1Bg" e a fábrica se vira para montar o pacote de 7 imagens.
class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case _:
                return None  # Isso satisfaz o aviso do editor