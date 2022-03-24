from PPlay.sprite import *
from PPlay.window import *
from random import *

class Battle():
    def __init__(self, janela):
        self.janela = janela

        self.mouse = Window.get_mouse()
        self.teclado = Window.get_keyboard()

        self.gameData = {}
        self.nomeDoPersonagem1 = "Patrick Vaughan"
        self.gameData[self.nomeDoPersonagem1] = {"atk": 6, "df": 5, "agi": 12, "vida": 100, "energia": 40,
                                                 "skills": {"Soco Rápido": ["Dano", 50, 5], "Golpe devastador": ["Dano", 100, 20]}}
        self.nomeDoPersonagem2 = "Kuroshido Nagawa"
        self.gameData[self.nomeDoPersonagem2] = {"atk": 10, "df": 10, "agi": 7, "vida": 140, "energia": 30,
                                                 "skills": {"Sabre Azul": ["Dano", 90, 10], "Erva Medicinal": ["Cura", 40, 5]}}
        self.vilao = "O Açougueiro"
        self.gameData[self.vilao] = {"atk": 13, "df": 8, "agi": 5, "vida": 300, "skills": {"Cutelo Vermelho": 50}}
        self.gameData["itens"] = {"Incenso de Cura Pequeno": ["Cura", 3, 20, "Vida"],
                             "Incenso de Cura Médio": ["Cura", 2, 60, "Vida"],
                             "Incenso de Cura Grande": ["Cura", 1, 100, "Vida"],
                             "Energético": ["Cura", 5, 20, "Energia"]}
        self.gameData["animações"] = {}

        #region Sprites da batalha
        self.battleground = Sprite("images/batalha/Battleground.jpg")
        self.menuOpcoes = Sprite("images/batalha/RetânguloRoxoManeiro.jpg")
        self.atacar = Sprite("images/batalha/Atacar.jpg")
        self.habilidade = Sprite("images/batalha/Habilidade.jpg")
        self.protagonista = Sprite("images/batalha/Patrick.png", 2)
        self.amigoDoProta1 = Sprite("images/batalha/Kuroshido.png", 3)
        self.chefe = Sprite("images/batalha/Butcher.png")
        self.item = Sprite("images/batalha/Item.jpg")
        self.retanguloVermelho = Sprite("images/batalha/RetanguloVermelho.jpg")
        self.barraAcao1 = Sprite("images/batalha/ActionGaugeVazia.png")
        self.barraAcao1P = Sprite("images/batalha/ActionGaugePreencher.png")
        self.barraAcao2 = Sprite("images/batalha/ActionGaugeVazia.png")
        self.barraAcao2P = Sprite("images/batalha/ActionGaugePreencher.png")
        self.menuItens = Sprite("images/batalha/FundoItem.jpg")

        #Sprites Skills
        self.skill1 = Sprite("images/batalha/RetânguloAmareloParaSkill.jpg")
        self.skill2 = Sprite("images/batalha/RetânguloAmareloParaSkill.jpg")
        self.skill3 = Sprite("images/batalha/RetânguloAmareloParaSkill.jpg")

        #endregion

    def animacoes(self, nomeDaHabilidade):
        # if nomeDaHabilidade == "ataque Patrick Vaughan":
        # print(nomeDaHabilidade)
        # if nomeDaHabilidade == "ataque Kuroshido Nagawa":
        # print(nomeDaHabilidade)
        return None

    def itens(self, personagem, gameData,janela,contador, listaDeItens, mouse):
        listaDeObjetos = []
        self.menuItens.draw()
        coeficientex = 0
        coeficientey = 1
        for i in range(len(listaDeItens)):
            item = Sprite("images/batalha/RetânguloVerdeParaItens.jpg")
            if coeficientex * item.width < janela.width:
                item.x = 10 + coeficientex * item.width + (item.width / 4) * coeficientex
                item.y = coeficientey * item.height
                coeficientex += 1
            else:
                coeficientey += 1
                coeficientex = 1
                item.x = 10 + coeficientex * item.width + (item.width / 4) * coeficientex
                item.y = coeficientey * item.height
            listaDeObjetos.append(item)
            item.draw()
            janela.draw_text("%s " % listaDeItens[i],
                             item.x, item.y, 23, (255, 255, 255), "ABERUS")
            janela.draw_text("%s: " % gameData["itens"][listaDeItens[i]][0] + "%d " % gameData["itens"][listaDeItens[i]][2] + "de %s" % gameData["itens"][listaDeItens[i]][1],
                             item.x, item.y + item.height / 4, 23, (255, 255, 255), "ABERUS")
            janela.draw_text("Quantidade: %d" % gameData["itens"][listaDeItens[i]][1],
                             item.x, item.y + item.height / 2, 23, (255, 255, 255), "ABERUS")
        for num, j in enumerate(listaDeObjetos):
            if mouse.is_over_object(j) and mouse.is_button_pressed(1) and gameData["itens"][listaDeItens[num]][1] > 0:
                if gameData["itens"][listaDeItens[num]][3] == "Vida":
                    gameData["itens"][listaDeItens[num]][1] -= 1
                    return gameData["itens"][listaDeItens[num]][0], gameData["itens"][listaDeItens[num]][
                        2], 0, 0, self.animacoes(gameData["itens"][listaDeItens[num]][0]), gameData
                if gameData["itens"][listaDeItens[num]][3] == "Energia":
                    gameData["itens"][listaDeItens[num]][1] -= 1
                    return gameData["itens"][listaDeItens[num]][0], 0, 0, -(
                    gameData["itens"][listaDeItens[num]][2]), self.animacoes(
                        gameData["itens"][listaDeItens[num]][0]), gameData
        return None, None, contador, 0, None, gameData

    def dano(self, atk, df):
        dano = ((1.5) * atk - (0.5) * df)
        return dano

    def skills(self, personagem, gameData, teclado, contador, energia, atacar, habilidade, item, janela):
        lista = []
        for skill in gameData[personagem]["skills"]:
            lista.append(skill)
        self.skill1.x = atacar.x
        self.skill1.y = atacar.y
        self.skill2.x = habilidade.x
        self.skill2.y = habilidade.y
        self.skill3.x = item.x
        self.skill3.y = item.y
        self.skill1.draw()
        self.skill2.draw()
        self.skill3.draw()
        if len(lista) > 0:
            janela.draw_text("%s " % lista[0], self.skill1.x, self.skill1.y, 30, (255, 255, 255), "ABERUS")
            janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[0]][2] + "%s" %
                             gameData[personagem]["skills"][lista[0]][0], self.skill1.x, self.skill1.y + self.skill1.height / 4, 30,
                             (255, 255, 255), "ABERUS")
            janela.draw_text("Tecla: Z", self.skill1.x, self.skill1.y + self.skill1.height / 2, 30, (255, 255, 255), "ABERUS")
        if len(lista) > 1:
            janela.draw_text("%s " % lista[1], self.skill2.x, self.skill2.y, 30, (255, 255, 255), "ABERUS")
            janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[1]][2] + "%s" %
                             gameData[personagem]["skills"][lista[1]][0], self.skill2.x, self.skill2.y + self.skill2.height / 4, 30,
                             (255, 255, 255), "ABERUS")
            janela.draw_text("Tecla: X", self.skill2.x, self.skill2.y + self.skill2.height / 2, 30, (255, 255, 255), "ABERUS")
        if len(lista) > 2:
            janela.draw_text("%s " % lista[2], self.skill3.x, self.skill3.y, 30, (255, 255, 255), "ABERUS")
            janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[2]][2] + "%s" %
                             gameData[personagem]["skills"][lista[2]][0], self.skill3.x, self.skill3.y + self.skill3.height / 4, 30,
                             (255, 255, 255), "ABERUS")
            janela.draw_text("Tecla: C", self.skill3.x, self.skill3.y + self.skill3.height / 2, 30, (255, 255, 255), "ABERUS")
        if teclado.key_pressed("z") and len(lista) > 0 and (energia - gameData[personagem]["skills"][lista[0]][2]) >= 0:
            gasto = gameData[personagem]["skills"][lista[0]][2]
            return gameData[personagem]["skills"][lista[0]][0], gameData[personagem]["skills"][lista[0]][1], 0, gasto, \
                   lista[0], gameData
        if teclado.key_pressed("x") and len(lista) > 1 and (energia - gameData[personagem]["skills"][lista[1]][2]) >= 0:
            gasto = gameData[personagem]["skills"][lista[1]][2]
            return gameData[personagem]["skills"][lista[1]][0], gameData[personagem]["skills"][lista[1]][1], 0, gasto, \
                   lista[1], gameData
        return None, None, contador, 0, None, gameData

    def turn(self, personagem, gameData, atacar, habilidade, item, mouse, inimigo, contador, energia, janela, listaDeItens):
        teclado = Window.get_keyboard()
        atacar.draw()
        habilidade.draw()
        item.draw()
        if mouse.is_over_object(atacar) and mouse.is_button_pressed(1) and contador == 0:
            return "Dano", self.dano(gameData[personagem]["atk"], gameData[inimigo]["df"]), contador, 0, (
                        "ataque %s" % personagem), gameData
        if (mouse.is_over_object(habilidade) and mouse.is_button_pressed(1)) or contador == 1:
            contador = 1
            if teclado.key_pressed("ESC"):
                contador = 0
            return self.skills(personagem, gameData, teclado, contador, energia, atacar, habilidade, item, janela)
        if (mouse.is_over_object(item) and mouse.is_button_pressed(1)) or contador == 2:
            contador = 2
            if teclado.key_pressed("ESC"):
                contador = 0
            return self.itens(personagem, gameData, janela, contador, listaDeItens, mouse)
        return None, None, contador, 0, None, gameData

    def batalha(self):
        #constantes
        contador = 0
        cadencia = 0
        actionGauge1 = 0
        actionGauge2 = 0
        actionGauge3 = 0
        morte1 = 0
        morte2 = 0
        listaDeItens = []
        for item in self.gameData["itens"]:
            listaDeItens.append(item)

        #definir variáveis
        turno = ""
        pontosDeVida1at = self.gameData[self.nomeDoPersonagem1]["vida"]
        pontosDeVida2at = self.gameData[self.nomeDoPersonagem2]["vida"]
        pontosDeVida3at = self.gameData[self.vilao]["vida"]
        energia1at = self.gameData[self.nomeDoPersonagem1]["energia"]
        energia2at = self.gameData[self.nomeDoPersonagem2]["energia"]

        #definir posição
        self.menuOpcoes.y = self.battleground.height
        self.atacar.x = self.janela.width - (self.atacar.x + 2 * self.atacar.width + 2 * (self.atacar.width / 4))
        self.atacar.y = self.battleground.height + self.atacar.height / 4
        self.habilidade.x = self.janela.width - (self.habilidade.x + self.habilidade.width + self.habilidade.width / 4)
        self.habilidade.y = self.battleground.height + self.habilidade.height / 4
        self.item.x = self.atacar.x + self.atacar.width / 2
        self.item.y = self.battleground.height + self.item.height + 3 * (self.item.height / 4)
        self.protagonista.y = self.battleground.height / 2
        self.amigoDoProta1.x = 0 - self.amigoDoProta1.width / 3.5
        self.amigoDoProta1.y = self.battleground.height / 2 + self.protagonista.height / 2
        self.chefe.x = self.janela.width - 4 * self.chefe.width
        self.chefe.y = self.battleground.height / 2
        self.retanguloVermelho.height = 10
        self.retanguloVermelho.x = self.chefe.x - self.chefe.width / 2
        self.retanguloVermelho.y = self.chefe.y
        self.barraAcao1.x = (6 / 4) * self.atacar.width
        self.barraAcao1.y = self.battleground.height + self.atacar.height / 2
        self.barraAcao1P.x = (6 / 4) * self.atacar.width
        self.barraAcao1P.y = self.battleground.height + self.atacar.height / 2
        self.barraAcao2.x = (6 / 4) * self.atacar.width
        self.barraAcao2.y = self.battleground.height + 2 * self.atacar.height
        self.barraAcao2P.x = (6 / 4) * self.atacar.width
        self.barraAcao2P.y = self.battleground.height + 2 * self.atacar.height
        rV0 = self.retanguloVermelho.width

        #animacoes
        self.protagonista.set_total_duration(400)
        self.amigoDoProta1.set_total_duration(600)

        #sistemas
        if self.janela.delta_time and turno == "":
            if actionGauge2 < 1 and actionGauge3 < 1 and morte1 == 0:
                actionGauge1 += 0.0005 * self.gameData[self.nomeDoPersonagem1]["agi"]
                if actionGauge1 >= 1:
                    actionGauge1 = 1
                    turno = self.nomeDoPersonagem1
                self.barraAcao1P.width = (self.barraAcao1.width)* actionGauge1
            if actionGauge1 < 1 and actionGauge3 < 1 and morte2 == 0:
                actionGauge2 += 0.0005 * self.gameData[self.nomeDoPersonagem2]["agi"]
                if actionGauge2 >= 1:
                    actionGauge2 = 1
                    turno = self.nomeDoPersonagem2
                self.barraAcao2P.width = (self.barraAcao2.width) * actionGauge2
            if actionGauge1 < 1 and actionGauge2 < 1:
                actionGauge3 += 0.0005 * self.gameData[self.vilao]["agi"]
                if actionGauge3 >= 1:
                    actionGauge3 = 1
                    turno = self.vilao
        #desenho
        self.battleground.draw()
        self.menuOpcoes.draw()
        self.janela.draw_text("Nome",
                              self.atacar.width / 2, self.battleground.height + self.atacar.height / 8, 25, (0, 0, 0), "New Times Roman")
        self.janela.draw_text("%s " % self.nomeDoPersonagem1
                              , self.atacar.width / 2, self.battleground.height + self.atacar.height / 2, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("PV %d" % pontosDeVida1at + " / " + "%d" % self.gameData[self.nomeDoPersonagem1]["vida"],
                              self.atacar.width / 2, self.battleground.height + self.atacar.height, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("EN %d " % energia1at + " / " + "%d" % self.gameData[self.nomeDoPersonagem1]["energia"],
                              self.atacar.width / 2, self.battleground.height + (3 / 2) * self.atacar.height, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("%s " % self.nomeDoPersonagem2,
                              self.atacar.width / 2, self.battleground.height + 2 * self.atacar.height, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("PV %d" % pontosDeVida2at + " / " + "%d" % self.gameData[self.nomeDoPersonagem2]["vida"],
                              self.atacar.width / 2, self.battleground.height + (5 / 2) * self.atacar.height, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("EN %d" % energia2at + " / " + "%d" % self.gameData[self.nomeDoPersonagem2]["energia"],
                              self.atacar.width / 2, self.battleground.height + 3 * self.atacar.height, 25, (255, 255, 255), "New Times Roman")
        self.janela.draw_text("%s " % self.vilao,
                              self.retanguloVermelho.x - self.chefe.width / 16, self.retanguloVermelho.y - 2 * self.retanguloVermelho.height, 20, (255, 0, 0), "ABERUS")
        self.protagonista.draw()
        self.amigoDoProta1.draw()
        self.chefe.draw()
        self.retanguloVermelho.draw()
        self.barraAcao1.draw()
        self.barraAcao1P.draw()
        self.barraAcao2.draw()
        self.barraAcao2P.draw()

        #animações
        if morte1 == 0:
            self.protagonista.update()
        if morte2 == 0:
            self.amigoDoProta1.update()

        #chefe.update()
        if turno == self.nomeDoPersonagem1 and cadencia == 60:
            cod, num, contador, gasto, animacao, self.gameData = self.turn(self.nomeDoPersonagem2, self.gameData, self.atacar, self.habilidade, self.item, self.mouse, self.vilao, contador, energia1at, self.janela, listaDeItens)
            if cod == "Dano":
                pontosDeVida3at -= self.dano(num, self.gameData[self.vilao]["df"])
                energia1at -= gasto
                turno = ""
                actionGauge1 = 0
                self.retanguloVermelho.width = rV0 * (pontosDeVida3at / self.gameData[self.vilao]["vida"])
                self.animacoes(animacao)
                cadencia = 0
            if cod == "Cura":
                pontosDeVida1at += num
                if pontosDeVida1at >= self.gameData[self.nomeDoPersonagem1]["vida"]:
                    pontosDeVida1at = self.gameData[self.nomeDoPersonagem1]["vida"]
                pontosDeVida2at += num
                if pontosDeVida2at >= self.gameData[self.nomeDoPersonagem2]["vida"]:
                    pontosDeVida2at = self.gameData[self.nomeDoPersonagem2]["vida"]
                energia2at -= gasto
                if energia2at >= self.gameData[self.nomeDoPersonagem2]["energia"]:
                    energia2at = self.gameData[self.nomeDoPersonagem2]["energia"]
                turno = ""
                actionGauge2 = 0
                cadencia = 0
        #AI inimigo
        if turno == self.vilao:
            listaSkillsI = []
            for k in self.gameData[self.vilao]["skills"]:
                listaSkillsI.append(k)
            a = 1
            if morte1 == 1:
                a = 2
            b = 2
            if morte2 == 1:
                a = 1
                b = 1
            alvo = randint(a,b)
            c = 1
            d = 10
            if len(listaSkillsI) < 2:
                d = 7
            acaoDoBoss = randint(c, d)
            if 0 < acaoDoBoss < 6:
                if alvo == 1:
                    self.animacoes("ataque %s"%self.vilao)
                    pontosDeVida1at -= self.dano(self.gameData[self.vilao]["atk"], self.gameData[self.nomeDoPersonagem1]["df"])
                if alvo == 2:
                    self.animacoes("ataque %s" % self.vilao)
                    pontosDeVida2at -= self.dano(self.gameData[self.vilao]["atk"], self.gameData[self.nomeDoPersonagem2]["df"])
            if 6 <= acaoDoBoss < 8 and len(listaSkillsI) > 0:
                if alvo == 1:
                    self.animacoes(listaSkillsI[0])
                    pontosDeVida1at -= self.dano(self.gameData[self.vilao]["skills"][listaSkillsI[0]], self.gameData[self.nomeDoPersonagem1]["df"])
                if alvo == 2:
                    self.animacoes(listaSkillsI[0])
                    pontosDeVida2at -= self.dano(self.gameData[self.vilao]["skills"][listaSkillsI[0]], self.gameData[self.nomeDoPersonagem2]["df"])
            if 8 <= acaoDoBoss <= 9 and len(listaSkillsI) > 1:
                if alvo == 1:
                    self.animacoes(listaSkillsI[1])
                    pontosDeVida1at -= self.dano(self.gameData[self.vilao]["skills"][listaSkillsI[1]], self.gameData[self.nomeDoPersonagem1]["df"])
                if alvo == 2:
                    self.animacoes(listaSkillsI[1])
                    pontosDeVida2at -= self.dano(self.gameData[self.vilao]["skills"][listaSkillsI[1]], self.gameData[self.nomeDoPersonagem2]["df"])
            turno = ""
            actionGauge3 = 0
        if self.janela.delta_time() and cadencia != 60:
            cadencia += 1
        #situação de morte
        if pontosDeVida1at <= 0 and morte1 == 0:
            morte1 = 1
            pontosDeVida1at = 0
            salvarPosix = self.protagonista.x
            salvarPosiy = self.protagonista.y
            self.protagonista = Sprite("images/batalha/PatrickDead.png", 1)
            self.protagonista.x = salvarPosix
            self.protagonista.y = salvarPosiy
        if pontosDeVida1at > 0 and morte1 == 1:
            morte1 = 0
            salvarPosix = self.protagonista.x
            salvarPosiy = self.protagonista.y
            self.protagonista = Sprite("images/batalha/Patrick.png", 2)
            self.protagonista.x = salvarPosix
            self.protagonista.y = salvarPosiy
            self.protagonista.set_total_duration(400)
        if pontosDeVida2at <= 0 and morte2 == 0:
            morte2 = 1
            pontosDeVida2at = 0
            salvarPosix = self.amigoDoProta1.x
            salvarPosiy = self.amigoDoProta1.y
            self.amigoDoProta1 = Sprite("images/batalha/KuroshidoDead.png", 1)
            self.amigoDoProta1.x = salvarPosix
            self.amigoDoProta1.y = salvarPosiy
        if pontosDeVida2at > 0 and morte2 == 1:
            morte2 = 0
            salvarPosix = self.amigoDoProta1.x
            salvarPosiy = self.amigoDoProta1.y
            self.amigoDoProta1 = Sprite("images/batalha/Kuroshido.png", 3)
            self.amigoDoProta1.x = salvarPosix
            self.amigoDoProta1.y = salvarPosiy
            self.amigoDoProta1.set_total_duration(600)
        if pontosDeVida3at <= 0:
            return "Vitória"
        if pontosDeVida1at <= 0 and pontosDeVida2at <= 0:
            return "Game Over"

    def run(self):
        self.batalha()