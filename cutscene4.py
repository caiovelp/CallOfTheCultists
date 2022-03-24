from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene4():
    def __init__(self, janela):
        self.janela = janela

        #region Backgrounds e mapas
        self.background2 = GameImage("images/backgrounds/background2.jpg")
        #endregion

        #region Personagens
        self.detetive = Sprite("images/personagens/detetive/0.png")
        self.detetive.x = 300 - self.detetive.width
        self.detetive.y = 540 - self.detetive.height

        self.japones = Sprite("images/personagens/japones/0.png")
        self.japones.x = 200 - self.japones.width
        self.japones.y = 545 - self.japones.height
        #endregion

        #region Boarmen
        self.boarmen = Sprite("images/personagens/boarmen/boizaodepe.png")
        self.boarmen.x = 1200 - self.boarmen.width
        self.boarmen.y = 540 - self.boarmen.height
        #endregion

        #region Dialogo
        self.fundo_dialogo = Sprite("images/dialogo/fundo.png")
        self.fundo_dialogo.y = 500

        self.detetive_face = Sprite("images/dialogo/detetive_face.png")
        self.detetive_face.y = 520
        self.detetive_face.x = 100

        self.japones_face = Sprite("images/dialogo/japones_face.png")
        self.japones_face.y = 520
        self.japones_face.x = 1100

        self.boarmen_face = Sprite("images/dialogo/boizao.png")
        self.boarmen_face.y = 520
        self.boarmen_face.x = 1100
        #endregion

        #region Indices
        self.cronometoIndice = 0
        self.corridaIndice = 0

        self.velocidade_camera = -1

        self.contador_dialogo4 = 0

        self.state_bonecos = "nada"

        self.velocidade_movimento = 0.3
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

    def cena(self):
        self.detetive.draw()
        self.japones.draw()
        self.boarmen.draw()
        self.dialogo()

    def dialogo(self):
        self.contador_dialogo4 += gamestates.vel_cena

        if (1 < self.contador_dialogo4 < 5):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("Que criatura é essa?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)

        if (5 < self.contador_dialogo4 < 10):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Nunca vi nada desse tipo, cuidado Patrick!",
                                  x=self.japones_face.x - 800, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)

        if (10 < self.contador_dialogo4 < 15):
            self.fundo_dialogo.draw()
            self.boarmen_face.draw()
            self.janela.draw_text("ROOOOOOOOOAAAAAR!",
                                  x=self.boarmen_face.x - 900, y=620, size=60, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)

        if (self.contador_dialogo4 > 15):
            gamestates.GameState = 6

    def toca_musica(self):
        if gamestates.GameState == 5:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def run(self):
        #draw
        self.background2.draw()

        self.cena()

        self.toca_musica()