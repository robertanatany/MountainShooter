import pygame.image

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_YELLOW, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.click_sound = pygame.mixer.Sound('./asset/click.wav')
        self.click_sound.set_volume(0.3)
        self.confirm_sound = pygame.mixer.Sound('./asset/pickup.wav')

        # CARREGAMOS AS FONTES AQUI (Uma única vez)
        # Criamos duas versões: uma bold para o título e uma normal para o resto
        self.font_title = pygame.font.SysFont('lucidasans', 50, bold=True)
        self.font_menu = pygame.font.SysFont('lucidasans', 20, bold=False)


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)



        # 1. PRIMEIRO: Checa eventos (Input)
        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Se clicar no "X"
                    pygame.quit()  # Close Window
                    quit()  # ctrl+alt+l
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # desce o menu
                        self.click_sound.play()
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    elif event.key == pygame.K_UP: # sobe o menu
                        self.click_sound.play()
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    elif event.key == pygame.K_RETURN: # Enter
                        self.confirm_sound.play()
                        pygame.time.delay(150) # Pausa o código por 150ms para o som aparecer
                        return MENU_OPTION[menu_option]


            # 2. SEGUNDO: Desenha (Render)
            self.window.blit(source=self.surf, dest=self.rect)

            # ENCREVENDO O TEXTO
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH/2), 70), True)
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH/2), 120), True)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    # Se for a opção selecionada, desenha em AMARELO
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH/2), 190 + 25 * i))
                else:
                    # Se não for, desenha em BRANCO
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH/2), 190 + 25 * i))

            # 3. TERCEIRO: Mostra tudo de uma vez
            pygame.display.flip()



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, is_title: bool = False):
        # Em vez de SysFont, escolhemos uma das fontes já carregadas
        # 1. Transforma o texto em imagem (Surface)
        # .convert_alpha() acelera o desenho na tela se houver transparência
        if is_title:
            text_surf = self.font_title.render(text, True, text_color).convert_alpha()
        else:
            text_surf = self.font_menu.render(text, True, text_color).convert_alpha()

        # 3. Cria o retângulo posicionado
        text_rect = text_surf.get_rect(center=text_center_pos)

        # 4. Desenha na janela
        self.window.blit(source=text_surf, dest=text_rect)