# 🏔️ Mountain Shooter

Um jogo de tiro arcade desenvolvido em Python utilizando a biblioteca **Pygame**. O projeto é acadêmico, desenvolvido na disciplina de Linguagem de Programação Aplicada e foca em conceitos de Programação Orientada a Objetos (POO), manipulação de superfícies, renderização de texto e gerenciamento de trilha sonora.

## 🚀 Funcionalidades

- **Menu Principal**: Interface com carregamento de assets e textos customizados.
- **Trilha Sonora**: Sistema de música de fundo em loop infinito.
- **Gráficos**: Renderização de planos de fundo otimizados com `convert_alpha()`.
- **Game Loop**: Estrutura robusta para controle de eventos e atualização de tela.

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/) - Linguagem base.
* [Pygame](https://www.pygame.org/) - Biblioteca para desenvolvimento de jogos.

## 📁 Estrutura do Projeto

```text
├── asset/              # Imagens e sons (bg.png, fase1.mp3)
├── main.py             # Ponto de entrada (Classe Game)
├── menu.py             # Lógica da interface (Classe Menu)
└── README.md           # Documentação

```

## 🔧 Como Rodar o Projeto

1. **Pré-requisitos**:
Certifique-se de ter o Python instalado. Se não tiver o Pygame, instale via terminal:
```bash
pip install pygame

```


2. **Clonando o repositório**:
```bash
git clone [https://github.com/SEU_USUARIO/mountain-shooter.git](https://github.com/SEU_USUARIO/mountain-shooter.git)

```


3. **Executando o jogo**:
Navegue até a pasta do projeto e execute:
```bash
python main.py

```



## 🧠 Conceitos Aplicados

Neste projeto, explorei técnicas fundamentais de Game Dev:

* **Blitting**: Técnica para desenhar superfícies sobre a tela principal.
* **Rect Manipulation**: Uso de objetos `Rect` para posicionamento preciso de elementos.
* **Event Handling**: Captura de eventos do sistema para fechar o jogo corretamente.
* **Otimização de Assets**: Carregamento de fontes e imagens fora do loop principal para melhor performance.

---

Desenvolvido com 🕹️ por [Roberta Natany]
