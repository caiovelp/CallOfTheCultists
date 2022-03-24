from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

import gamestates
from gamestates import *

class Cutscene6():
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

        #region Japonês
        self.japones0 = Sprite("images/personagens/japones/0.png")
        self.japones1 = Sprite("images/personagens/japones/1.png")
        self.japones2 = Sprite("images/personagens/japones/2.png")
        self.japones3 = Sprite("images/personagens/japones/3.png")
        self.japones4 = Sprite("images/personagens/japones/4.png")
        self.japones5 = Sprite("images/personagens/japones/5.png")
        self.japones6 = Sprite("images/personagens/japones/6.png")
        self.japones7 = Sprite("images/personagens/japones/7.png")
        self.japones8 = Sprite("images/personagens/japones/8.png")

        self.japonesKill0 = Sprite("images/personagens/japones/matando/0.png")
        self.japonesKill1 = Sprite("images/personagens/japones/matando/1.png")
        self.japonesKill2 = Sprite("images/personagens/japones/matando/2.png")
        self.japonesKill3 = Sprite("images/personagens/japones/matando/3.png")
        self.japonesKill4 = Sprite("images/personagens/japones/matando/4.png")
        self.japonesKill5 = Sprite("images/personagens/japones/matando/5.png")

        self.japones_list = [self.japones0, self.japones1, self.japones2, self.japones3,
                              self.japones4, self.japones5, self.japones6, self.japones7,
                              self.japones8]
        self.japones_listKill = [self.japonesKill0, self.japonesKill1, self.japonesKill2, self.japonesKill3,
                              self.japonesKill4, self.japonesKill5]
        #endregion

        #region Criança
        self.crianca0 = Sprite("images/personagens/crianca/0.png")
        self.crianca1 = Sprite("images/personagens/crianca/1.png")
        self.crianca2 = Sprite("images/personagens/crianca/2.png")
        self.crianca3 = Sprite("images/personagens/crianca/3.png")
        self.crianca4 = Sprite("images/personagens/crianca/4.png")
        self.crianca5 = Sprite("images/personagens/crianca/5.png")
        self.crianca6 = Sprite("images/personagens/crianca/6.png")
        self.crianca7 = Sprite("images/personagens/crianca/7.png")
        self.crianca8 = Sprite("images/personagens/crianca/8.png")

        self.crianca_list = [self.crianca0, self.crianca1, self.crianca2, self.crianca3,
                              self.crianca4, self.crianca5, self.crianca6, self.crianca7,
                              self.crianca8]
        self.crianca = Sprite("images/personagens/crianca/0.png")
        self.crianca.x = 200 - self.crianca.width
        self.crianca.y = 585 - self.crianca.height
        #endregion

        #region cultista
        self.cultista0 = Sprite("images/personagens/cultista/transformation/0.png")
        self.cultista1 = Sprite("images/personagens/cultista/transformation/1.png")
        self.cultista2 = Sprite("images/personagens/cultista/transformation/2.png")
        self.cultista3 = Sprite("images/personagens/cultista/transformation/3.png")
        self.cultista4 = Sprite("images/personagens/cultista/transformation/4.png")
        self.cultista5 = Sprite("images/personagens/cultista/transformation/5.png")
        self.cultista6 = Sprite("images/personagens/cultista/transformation/6.png")
        self.cultista7 = Sprite("images/personagens/cultista/transformation/7.png")
        self.cultista8 = Sprite("images/personagens/cultista/transformation/8.png")
        self.cultista9 = Sprite("images/personagens/cultista/transformation/9.png")
        self.cultista10 = Sprite("images/personagens/cultista/transformation/10.png")
        self.cultista11 = Sprite("images/personagens/cultista/transformation/11.png")

        self.cultista_list = [self.cultista0, self.cultista1, self.cultista2, self.cultista3,
                              self.cultista4, self.cultista5, self.cultista6, self.cultista7,
                              self.cultista8, self.cultista9, self.cultista10, self.cultista11]


        self.cultista = Sprite("images/personagens/cultista/cultista.png")
        self.cultista.x = 1082.39 - self.cultista.width
        self.cultista.y = 540 - self.cultista.height

        self.divinity0 = Sprite("images/personagens/cultista/divinity/0.png")
        self.divinity1 = Sprite("images/personagens/cultista/divinity/1.png")
        self.divinity2 = Sprite("images/personagens/cultista/divinity/2.png")
        self.divinity3 = Sprite("images/personagens/cultista/divinity/3.png")

        self.spell0 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile1.png")
        self.spell1 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile2.png")
        self.spell2 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile3.png")
        self.spell3 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile4.png")
        self.spell4 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile5.png")
        self.spell5 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile6.png")
        self.spell6 = Sprite("images/personagens/cultista/divinity/spell/evilProjectile7.png")

        self.divinity_list = [self.divinity0, self.divinity1, self.divinity2, self.divinity3]
        self.spell_list = [self.spell0, self.spell1, self.spell2, self.spell3,
                           self.spell4, self.spell5, self.spell6]

        self.divinity = Sprite("images/personagens/cultista/divinity/0.png")
        self.divinity.x = self.cultista.x
        self.divinity.y = self.cultista.y - 250

        self.spell = Sprite("images/personagens/cultista/divinity/spell/evilProjectile1.png")
        self.spell.x = self.divinity.x + self.spell.width
        self.spell.y = self.japones.y
        #endregion

        #region indices
        self.cronometoIndice = 0
        self.indice = 0
        self.indiceATK = 0
        self.indiceIDLE = 0
        self.indiceSPELL = 0
        self.indiceCrianca = 0
        self.contador_dialogo6 = 0

        self.transformando = False
        self.transformou = False
        self.spellando = False
        self.isgone = False

        self.andando = False
        self.atacando = False

        self.criancando = False
        #endregion

        #region Dialogo
        self.fundo_dialogo = Sprite("images/dialogo/fundo.png")
        self.fundo_dialogo.y = 500

        self.detetive_face = Sprite("images/dialogo/detetive_face.png")
        self.detetive_face.y = 520
        self.detetive_face.x = 100

        self.japones_face = Sprite("images/dialogo/japones_face.png")
        self.japones_face.y = 520
        self.japones_face.x = 100

        self.cultista_face = Sprite("images/dialogo/cultista.png")
        self.cultista_face.y = 520
        self.cultista_face.x = 1100

        self.crianca_face = Sprite("images/dialogo/crianca_face.png")
        self.crianca_face.y = 520
        self.crianca_face.x = 100
        #endregion

        self.cutscene_sound = Sound("sounds/Cutscenes.ogg")
        self.cutscene_sound.set_volume(10)

        self.roar_sound = Sound("sounds/roar.ogg")
        self.roar_sound.set_volume(30)

    def animate_transformation(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 5:
            self.indice += 1
            self.cronometoIndice = 0
        if self.indice == 11:
            self.indice = 0
        # region cultista
        self.cultista_list[self.indice].x = self.cultista.x
        self.cultista_list[self.indice].y = self.cultista.y
        self.cultista_list[self.indice].draw()
        # endregion

    def animate_divinity(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 20:
            self.indiceIDLE += 1
            self.cronometoIndice = 0
        if self.indiceIDLE == 3:
            self.indiceIDLE = 0
        # region cultista
        self.divinity_list[self.indiceIDLE].x = self.divinity.x
        self.divinity_list[self.indiceIDLE].y = self.divinity.y
        self.divinity_list[self.indiceIDLE].draw()
        # endregion

    def animate_spell(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.indiceSPELL += 1
            self.cronometoIndice = 0
        if self.indiceSPELL == 6:
            self.indiceSPELL = 0
        # region cultista
        self.spell_list[self.indiceSPELL].x = self.spell.x
        self.spell_list[self.indiceSPELL].y = self.spell.y
        self.spell_list[self.indiceSPELL].draw()
        # endregion

    def animate_Kuroshido(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.indice += 1
            self.cronometoIndice = 0
        if self.indice == 8:
            self.indice = 0
        # region cultista
        self.japones_list[self.indice].x = self.japones.x
        self.japones_list[self.indice].y = self.japones.y
        self.japones_list[self.indice].draw()
        # endregion

    def animate_KuroshidoAtacando(self):
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 20:
            self.indiceATK += 1
            self.cronometoIndice = 0
        if self.indiceATK == 5:
            self.indiceATK = 0
        # region cultista
        self.japones_listKill[self.indiceATK].x = self.japones.x
        self.japones_listKill[self.indiceATK].y = self.japones.y
        self.japones_listKill[self.indiceATK].draw()
        # endregion

    def animate_crianca(self):
        self.crianca.move_x(0.2)
        self.cronometoIndice += 100 * self.janela.delta_time()
        if self.cronometoIndice > 10:
            self.indiceCrianca += 1
            self.cronometoIndice = 0
        if self.indiceCrianca == 8:
            self.indiceCrianca = 0
        self.crianca_list[self.indiceCrianca].x = self.crianca.x
        self.crianca_list[self.indiceCrianca].y = self.crianca.y
        self.crianca_list[self.indiceCrianca].draw()

    def cena(self):
        self.detetive.draw()
        if (self.transformando):
            self.animate_transformation()
        elif(not self.transformando and not self.transformou):
            self.cultista.draw()
        elif (self.transformou):
            self.animate_divinity()

        if (self.andando and (self.japones.x + self.japones.width) < (self.divinity.x)):
            self.animate_Kuroshido()
            self.japones.move_x(0.8)
        elif (self.atacando):
            self.animate_KuroshidoAtacando()
            self.animate_divinity()
        else:
            self.japones.draw()

        if (self.spellando):
            self.animate_spell()
            self.spell.move_x(-0.8)
            if (self.spell.collided(self.japones)):
                self.japones.hide()
            if (self.spell.collided(self.detetive)):
                self.detetive.hide()

        if (self.isgone):
            self.divinity.hide()
            self.cultista.hide()

        if (self.criancando):
            self.animate_crianca()
        self.dialogo()

        if (self.crianca.x > self.janela.width):
            gamestates.GameState = 10

    def dialogo(self):
        self.contador_dialogo6 += gamestates.vel_cena

        if (1 < self.contador_dialogo6 < 5):
            self.fundo_dialogo.draw()
            self.cultista_face.draw()
            self.janela.draw_text("Agora vislumbrem a verdadeira forma de Cyaegha!",
                                  x=self.cultista_face.x - 800, y=620, size=20, color=(216, 168, 49), font_name="Verdana", bold=True, italic=False)
        if (5 < self.contador_dialogo6 < 8):
            self.transformando = True
        else:
            self.transformando = False
        if (self.contador_dialogo6 > 8):
            self.transformou = True
        if (8 < self.contador_dialogo6 < 13):
            self.roar_sound.play()
        if (13 < self.contador_dialogo6 < 18):
            self.fundo_dialogo.draw()
            self.detetive_face.draw()
            self.janela.draw_text("O que diabos é isso?",
                                  x=self.detetive_face.x + 200, y=620, size=20, color=(255, 255, 255), font_name="Verdana", bold=True, italic=False)
        if (18 < self.contador_dialogo6 < 28):
            self.fundo_dialogo.draw()
            self.japones_face.draw()
            self.janela.draw_text("Vá buscar ajuda Patrick, eu cuido dessa fera!",
                                  x=self.japones_face.x + 200, y=620, size=20, color=(255, 0, 0), font_name="Verdana", bold=True, italic=False)
        if (self.contador_dialogo6 > 19):
            self.andando = True
        if (self.contador_dialogo6 > 31):
            self.atacando = True
            self.andando = False
        if (self.contador_dialogo6 > 32):
            self.atacando = False
            self.spellando = True
        if (self.contador_dialogo6 > 37):
            self.spellando = False
        if (self.contador_dialogo6 > 42):
            self.transformou = False
            self.isgone = True

        if (42 < self.contador_dialogo6 < 47):
            self.criancando = True
            self.fundo_dialogo.draw()
            self.crianca_face.draw()
            self.janela.draw_text("Onde estão todos? Pai? Patrick?",
                                  x=self.crianca_face.x + 200, y=620, size=20, color=(0, 255, 0), font_name="Verdana",
                                  bold=True, italic=False)
            self.janela.draw_text("CADÊ VOCÊS?!",
                                  x=self.crianca_face.x + 200, y=640, size=20, color=(0, 255, 0), font_name="Verdana",
                                  bold=True, italic=False)

    def toca_musica(self):
        if gamestates.GameState == 9:
            self.cutscene_sound.play()
        else:
            self.cutscene_sound.stop()

    def run(self):
        self.background2.draw()
        self.cena()

        self.toca_musica()