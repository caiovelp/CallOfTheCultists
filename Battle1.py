from PPlay.window import *
from PPlay.sound import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import randint
import Imagens
import gamestates

gameData = {}
nomeDoPersonagem1 = "Patrick Vaughan"
gameData[nomeDoPersonagem1] = {"atk": 14,"df": 8, "agi": 12,"vida": 110,"energia": 40, "skills": {"Soco Rápido": ["Dano", 50, 5], "Golpe Devastador": ["Dano", 100, 15]}}
nomeDoPersonagem2 = "Kuroshido Nagawa"
gameData[nomeDoPersonagem2] = {"atk": 20,"df": 10, "agi": 7,"vida": 140, "energia": 30, "skills": {"Sabre Azul": ["Dano", 90, 10], "Erva Medicinal": ["Cura", 40, 5]}}
vilao1 = "O Açougueiro"
vilao2 = "Boarman"
vilao3 = "Líder do Culto"
gameData[vilao1] = {"atk": 30,"df": 8, "agi": 5,"vida": 400*gamestates.Dificuldade, "skills": {"Lâmina Rubra": 45}}
gameData[vilao2] = {"atk": 40,"df": 10, "agi": 4,"vida": 500*gamestates.Dificuldade, "skills": {"Machadada Rubra": 65}}
gameData[vilao3] = {"atk": 25,"df": 4, "agi": 10,"vida": 1000*gamestates.Dificuldade, "skills":{"Árvore Rubra": 55, "Gaiola Rubra": 75}}
gameData["itens"] = {"Incenso de Cura Pequeno": ["Cura", 5, 20, "Vida"], "Incenso de Cura Médio": ["Cura", 3, 60,"Vida"], "Incenso de Cura Grande": ["Cura", 2, 100,"Vida"],"Energético": ["Cura", 5, 20, "Energia"]}
sound_battle1 = Sound("sounds/battle1.ogg")
sound_battle1.set_volume(10)
sound_battle1.set_repeat(repeat=True)
sound_battle2 = Sound("sounds/battle2.ogg")
sound_battle2.set_volume(10)
sound_battle2.set_repeat(repeat=True)
sound_battle3 = Sound("sounds/battle3.ogg")
sound_battle3.set_volume(10)
sound_battle3.set_repeat(repeat=True)

def animacoes(nomeDaHabilidade, protagonista, amigoDoProta, inimigo, controle, salvarPX, salvarPY, salvarAX, salvarAY, salvarIX, salvarIY, spriteAnima, morte1, morte2, spriteAnima2):
    #Animações aliados
    #Animações Patrick Vaughan
    if nomeDaHabilidade == "ataque Patrick Vaughan":
        if controle == 0:
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
            protagonista.x = inimigo.x - inimigo.width
            protagonista.y = inimigo.y
            protagonista.set_sequence_time(0, 3, 400, 0)
            controle = 1
        if not protagonista.playing:
            nomeDaHabilidade = None
            controle = 0
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.set_total_duration(400)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
    if nomeDaHabilidade == "Soco Rápido":
        if controle == 0:
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
            protagonista.x = inimigo.x - inimigo.width
            protagonista.y = inimigo.y
            protagonista.set_sequence_time(0, 3, 100, 0)
            controle = 1
        if not protagonista.playing:
            nomeDaHabilidade = None
            controle = 0
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.set_total_duration(400)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
    if nomeDaHabilidade == "Golpe Devastador":
        if controle == 0:
            protagonista = Sprite("Imagens/Golpe Devastador.png", 9)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
            protagonista.set_sequence_time(0, 8, 200, 0)
            controle = 1
        if not protagonista.playing and controle == 1:
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
            protagonista.x = inimigo.x - inimigo.width
            protagonista.y = inimigo.y
            protagonista.set_sequence_time(0, 3, 1000, 0)
            controle = 2
        if not protagonista.playing and controle == 2:
            nomeDaHabilidade = None
            controle = 0
            protagonista = Sprite("Imagens/Patrick Vaughan.png", 2)
            protagonista.set_total_duration(400)
            protagonista.x = salvarPX
            protagonista.y = salvarPY
    #Animações Kuroshido Nagawa
    if nomeDaHabilidade == "ataque Kuroshido Nagawa":
        if controle == 0:
            amigoDoProta = Sprite("Imagens/ataque Kuroshido Nagawa.png", 6)
            amigoDoProta.x = salvarAX
            amigoDoProta.y = salvarAY
            amigoDoProta.x = inimigo.x - amigoDoProta.width*(3/4)
            amigoDoProta.y = inimigo.y - inimigo.height/2
            amigoDoProta.set_sequence_time(0, 7, 200, 0)
            controle = 1
        if not amigoDoProta.playing:
            nomeDaHabilidade = None
            controle = 0
            amigoDoProta = Sprite("Imagens/Kuroshido Nagawa.png", 3)
            amigoDoProta.set_total_duration(600)
            amigoDoProta.x = salvarAX
            amigoDoProta.y = salvarAY
    if nomeDaHabilidade == "Sabre Azul":
        if controle == 0:
            amigoDoProta = Sprite("Imagens/ataque Kuroshido Nagawa.png", 6)
            amigoDoProta.x = salvarAX
            amigoDoProta.y = salvarAY
            amigoDoProta.x = inimigo.x - amigoDoProta.width*(3/4)
            amigoDoProta.y = inimigo.y - inimigo.height/2
            amigoDoProta.set_sequence_time(0, 7, 100, 0)
            controle = 1
        if not amigoDoProta.playing and controle == 1:
            amigoDoProta = Sprite("Imagens/ataque Kuroshido Nagawa 2.png", 6)
            amigoDoProta.x = inimigo.x - inimigo.width
            amigoDoProta.y = inimigo.y - inimigo.height*(3/2)
            amigoDoProta.set_sequence_time(0, 7, 100, 0)
            controle = 2
        if not amigoDoProta.playing and controle == 2:
            amigoDoProta = Sprite("Imagens/ataque Kuroshido Nagawa 3.png", 6)
            amigoDoProta.x = inimigo.x
            amigoDoProta.y = inimigo.y - inimigo.height/2
            amigoDoProta.set_sequence_time(0, 7, 100, 0)
            controle = 3
        if not amigoDoProta.playing and controle == 3:
            amigoDoProta = Sprite("Imagens/ataque Kuroshido Nagawa 4.png", 6)
            amigoDoProta.x = inimigo.x - inimigo.width
            amigoDoProta.y = inimigo.y
            amigoDoProta.set_sequence_time(0, 7, 100, 0)
            controle = 4
        if not amigoDoProta.playing and controle == 4:
            nomeDaHabilidade = None
            controle = 0
            amigoDoProta = Sprite("Imagens/Kuroshido Nagawa.png", 3)
            amigoDoProta.set_total_duration(600)
            amigoDoProta.x = salvarAX
            amigoDoProta.y = salvarAY
    if nomeDaHabilidade == "Erva Medicinal":
        if controle == 0:
            spriteAnima = Sprite("Imagens/Erva Medicinal.png", 1)
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width / 2
            spriteAnima.y = amigoDoProta.y + amigoDoProta.height/8
            spriteAnima.set_sequence_time(0, 2, 1000, 0)
            controle = 1
        if controle == 1:
            spriteAnima.draw()
            spriteAnima.update()
        if not spriteAnima.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
    if nomeDaHabilidade == "Energético":
        if controle == 0:
            spriteAnima = Sprite("Imagens/Energético.png", 1)
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width / 2
            spriteAnima.y = amigoDoProta.y
            spriteAnima.set_sequence_time(0, 2, 1000, 0)
            controle = 1
        if controle == 1:
            spriteAnima.draw()
            spriteAnima.update()
        if not spriteAnima.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
    #Animações itens
    if nomeDaHabilidade == "Incenso de Cura Pequeno":
        if controle == 0:
            spriteAnima = Sprite("Imagens/IncensoPequeno.png", 1)
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width / 2
            spriteAnima.y = amigoDoProta.y
            spriteAnima.set_sequence_time(0, 2, 1000, 0)
            controle = 1
        if controle == 1:
            spriteAnima.draw()
            spriteAnima.update()
        if not spriteAnima.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
    if nomeDaHabilidade == "Incenso de Cura Médio":
        if controle == 0:
            spriteAnima = Sprite("Imagens/IncensoMédio.png", 1)
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width / 2
            spriteAnima.y = amigoDoProta.y
            spriteAnima.set_sequence_time(0, 2, 1000, 0)
            controle = 1
        if controle == 1:
            spriteAnima.draw()
            spriteAnima.update()
        if not spriteAnima.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
    if nomeDaHabilidade == "Incenso de Cura Grande":
        if controle == 0:
            spriteAnima = Sprite("Imagens/IncensoGrande.png", 1)
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width / 2
            spriteAnima.y = amigoDoProta.y
            spriteAnima.set_sequence_time(0, 2, 1000, 0)
            controle = 1
        if controle == 1:
            spriteAnima.draw()
            spriteAnima.update()
        if not spriteAnima.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
    #Animações inimigos
    #Animação O Açougueiro
    if nomeDaHabilidade == "ataque O Açougueiro1":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque O Açougueiro.png", 6)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x - inimigo.width*(1/16)
            inimigo.y = protagonista.y - protagonista.height/2
            inimigo.set_sequence_time(0, 7, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/O Açougueiro.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "ataque O Açougueiro2":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque O Açougueiro.png", 6)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = amigoDoProta.x + inimigo.width*(1/8)
            inimigo.y = amigoDoProta.y
            inimigo.set_sequence_time(0, 7, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/O Açougueiro.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Lâmina Rubra1":
        if controle == 0:
            inimigo = Sprite("Imagens/Lâmina Rubra.png", 6)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x - inimigo.width*(1/16)
            inimigo.y = protagonista.y - protagonista.height/2
            inimigo.set_sequence_time(0, 7, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/O Açougueiro.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Lâmina Rubra2":
        if controle == 0:
            inimigo = Sprite("Imagens/Lâmina Rubra.png", 6)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = amigoDoProta.x + inimigo.width*(1/8)
            inimigo.y = amigoDoProta.y
            inimigo.set_sequence_time(0, 7, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/O Açougueiro.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    #Animações Boarman
    if nomeDaHabilidade == "ataque Boarman1":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque Boarman.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x + protagonista.width/2
            inimigo.y = protagonista.y
            inimigo.set_sequence_time(0, 4, 300, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Boarman.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "ataque Boarman2":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque Boarman.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x + protagonista.width/2
            inimigo.y = protagonista.y + protagonista.height/1.5
            inimigo.set_sequence_time(0, 4, 300, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Boarman.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Machadada Rubra1":
        if controle == 0:
            inimigo = Sprite("Imagens/Machadada Rubra.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x + protagonista.width/2
            inimigo.y = protagonista.y
            inimigo.set_sequence_time(0, 4, 300, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Boarman.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Machadada Rubra2":
        if controle == 0:
            inimigo = Sprite("Imagens/Machadada Rubra.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x + protagonista.width/2
            inimigo.y = protagonista.y + protagonista.height/1.5
            inimigo.set_sequence_time(0, 4, 300, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Boarman.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    #Animações Líder do Culto
    if nomeDaHabilidade == "ataque Líder do Culto1":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque Líder do Culto.png", 8)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = protagonista.x + protagonista.width/2
            inimigo.y = protagonista.y
            inimigo.set_sequence_time(0, 9, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "ataque Líder do Culto2":
        if controle == 0:
            inimigo = Sprite("Imagens/ataque Líder do Culto.png", 8)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.x = amigoDoProta.x + amigoDoProta.width/2
            inimigo.y = amigoDoProta.y + amigoDoProta.height/4
            inimigo.set_sequence_time(0, 9, 200, 0)
            controle = 1
        inimigo.update()
        if not inimigo.playing:
            nomeDaHabilidade = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Árvore Rubra1":
        if controle == 0:
            inimigo = Sprite("Imagens/Líder Árvore Rubra.png", 4)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.set_sequence_time(0, 5, 200, 0)
            controle = 1
        if not inimigo.playing and controle == 1:
            inimigo = Sprite("Imagens/Líder Árvore Rubra2.png", 2)
            spriteAnima = Sprite("Imagens/Árvore Rubra.png", 2)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            spriteAnima.x = protagonista.x + protagonista.width/5
            spriteAnima.y = protagonista.y
            inimigo.set_sequence_time(0, 3, 300, 0)
            spriteAnima.set_sequence_time(0, 3, 300, 0)
            controle = 2
        inimigo.update()
        if controle == 2:
            spriteAnima.draw()
            spriteAnima.update()
        if not inimigo.playing and controle == 2:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Árvore Rubra2":
        if controle == 0:
            inimigo = Sprite("Imagens/Líder Árvore Rubra.png", 4)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.set_sequence_time(0, 5, 200, 0)
            controle = 1
        if not inimigo.playing and controle == 1:
            inimigo = Sprite("Imagens/Líder Árvore Rubra2.png", 2)
            spriteAnima = Sprite("Imagens/Árvore Rubra.png", 2)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width/4
            spriteAnima.y = amigoDoProta.y + amigoDoProta.height/5
            inimigo.set_sequence_time(0, 3, 300, 0)
            spriteAnima.set_sequence_time(0, 3, 300, 0)
            controle = 2
        inimigo.update()
        if controle == 2:
            spriteAnima.draw()
            spriteAnima.update()
        if not inimigo.playing and controle == 2:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Gaiola Rubra1":
        if controle == 0:
            inimigo = Sprite("Imagens/Líder Gaiola Rubra1.png", 4)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.set_sequence_time(0, 5, 200, 0)
            controle = 1
        if not inimigo.playing and controle == 1:
            inimigo = Sprite("Imagens/Líder Gaiola Rubra2.png", 3)
            spriteAnima = Sprite("Imagens/Gaiola Rubra.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            spriteAnima.x = protagonista.x
            spriteAnima.y = protagonista.y
            inimigo.set_sequence_time(0, 4, 300, 0)
            spriteAnima.set_sequence_time(0, 4, 300, 0)
            controle = 2
        inimigo.update()
        if not inimigo.playing and controle == 2:
            spriteAnima2 = Sprite("Imagens/Fogo.png", 4)
            spriteAnima2.x = protagonista.x
            spriteAnima2.y = protagonista.y
            spriteAnima2.set_sequence_time(0, 5, 300, 0)
            controle = 3
        if controle == 2 or controle == 3:
            spriteAnima.draw()
            spriteAnima.update()
        if controle == 3:
            spriteAnima2.draw()
            spriteAnima2.update()
        if controle == 3 and not spriteAnima2.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if nomeDaHabilidade == "Gaiola Rubra2":
        if controle == 0:
            inimigo = Sprite("Imagens/Líder Gaiola Rubra1.png", 4)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            inimigo.set_sequence_time(0, 5, 200, 0)
            controle = 1
        if not inimigo.playing and controle == 1:
            inimigo = Sprite("Imagens/Líder Gaiola Rubra2.png", 3)
            spriteAnima = Sprite("Imagens/Gaiola Rubra.png", 3)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
            spriteAnima.x = amigoDoProta.x + amigoDoProta.width/4
            spriteAnima.y = amigoDoProta.y
            inimigo.set_sequence_time(0, 4, 300, 0)
            spriteAnima.set_sequence_time(0, 4, 300, 0)
            controle = 2
        inimigo.update()
        if not inimigo.playing and controle == 2:
            spriteAnima2 = Sprite("Imagens/Fogo.png", 4)
            spriteAnima2.x = amigoDoProta.x + amigoDoProta.width/4
            spriteAnima2.y = amigoDoProta.y
            spriteAnima2.set_sequence_time(0, 5, 300, 0)
            controle = 3
        if controle == 2 or controle == 3:
            spriteAnima.draw()
            spriteAnima.update()
        if controle == 3:
            spriteAnima2.draw()
            spriteAnima2.update()
        if controle == 3 and not spriteAnima2.playing:
            nomeDaHabilidade = None
            spriteAnima = None
            controle = 0
            inimigo = Sprite("Imagens/Líder do Culto.png", 1)
            inimigo.x = salvarIX
            inimigo.y = salvarIY
    if morte1 == 0:
        protagonista.update()
    if morte2 == 0:
        amigoDoProta.update()
    return nomeDaHabilidade, controle, protagonista, amigoDoProta, inimigo, spriteAnima, spriteAnima2
def itens(personagem, gameData,janela,contador, listaDeItens, mouse):
    listaDeObjetos = []
    menuItens = Sprite("Imagens/FundoItem.jpg")
    menuItens.draw()
    coeficientex = 0
    coeficientey = 1
    for i in range(len(listaDeItens)):
        item = Sprite("Imagens/RetânguloVerdeParaItens.jpg")
        if coeficientex*item.width < janela.width:
            item.x = 10 + coeficientex*item.width + (item.width/4)*coeficientex
            item.y = coeficientey*item.height
            coeficientex += 1
        else:
            coeficientey += 1
            coeficientex = 1
            item.x = 10 + coeficientex*item.width + (item.width/4)*coeficientex
            item.y = coeficientey * item.height
        listaDeObjetos.append(item)
        item.draw()
        janela.draw_text("%s "%listaDeItens[i], item.x, item.y,23, (255, 255, 255), "ABERUS")
        janela.draw_text("%s: " % gameData["itens"][listaDeItens[i]][0] + "%d "% gameData["itens"][listaDeItens[i]][2] + "de %s"%gameData["itens"][listaDeItens[i]][1], item.x, item.y + item.height/4, 23, (255, 255, 255), "ABERUS")
        janela.draw_text("Quantidade: %d" % gameData["itens"][listaDeItens[i]][1], item.x, item.y + item.height / 2, 23, (255, 255, 255), "ABERUS")
    for num, j in enumerate(listaDeObjetos):
        if mouse.is_over_object(j) and mouse.is_button_pressed(1) and gameData["itens"][listaDeItens[num]][1] > 0:
            if gameData["itens"][listaDeItens[num]][3] == "Vida":
                gameData["itens"][listaDeItens[num]][1] -= 1
                return gameData["itens"][listaDeItens[num]][0], gameData["itens"][listaDeItens[num]][2], 0, 0, listaDeItens[num],gameData
            if gameData["itens"][listaDeItens[num]][3] == "Energia":
                gameData["itens"][listaDeItens[num]][1] -= 1
                return gameData["itens"][listaDeItens[num]][0], 0, 0, -(gameData["itens"][listaDeItens[num]][2]), listaDeItens[num],gameData
    return None,None,contador, 0, None,gameData

def dano(atk, df):
    x = randint(-5, 5)
    dano = ((1.5)*atk - (0.5)*df + x)
    return dano

def skills(personagem, gameData, teclado, contador, energia, atacar, habilidade, item,janela):
    lista = []
    skill1 = Sprite("Imagens/RetânguloAmareloParaSkill.jpg")
    skill2 = Sprite("Imagens/RetânguloAmareloParaSkill.jpg")
    skill3 = Sprite("Imagens/RetânguloAmareloParaSkill.jpg")
    for i in gameData[personagem]["skills"]:
        lista.append(i)
    skill1.x = atacar.x
    skill1.y = atacar.y
    skill2.x = habilidade.x
    skill2.y = habilidade.y
    skill3.x = item.x
    skill3.y = item.y
    skill1.draw()
    skill2.draw()
    skill3.draw()
    if len(lista) > 0:
        janela.draw_text("%s "%lista[0], skill1.x, skill1.y,30, (255, 255, 255), "ABERUS")
        janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[0]][2]+ "%s"%gameData[personagem]["skills"][lista[0]][0], skill1.x, skill1.y + skill1.height/4, 30, (255, 255, 255), "ABERUS")
        janela.draw_text("Tecla: Z",skill1.x, skill1.y + skill1.height/2, 30, (255, 255, 255), "ABERUS")
    if len(lista) > 1:
        janela.draw_text("%s " % lista[1], skill2.x, skill2.y, 30, (255, 255, 255), "ABERUS")
        janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[1]][2]+ "%s"%gameData[personagem]["skills"][lista[1]][0], skill2.x,skill2.y + skill2.height / 4, 30, (255, 255, 255), "ABERUS")
        janela.draw_text("Tecla: X", skill2.x, skill2.y + skill2.height/2, 30, (255, 255, 255), "ABERUS")
    if len(lista) > 2:
        janela.draw_text("%s " % lista[2], skill3.x, skill3.y, 30, (255, 255, 255), "ABERUS")
        janela.draw_text("Custo: %d, " % gameData[personagem]["skills"][lista[2]][2]+ "%s"%gameData[personagem]["skills"][lista[2]][0], skill3.x,skill3.y + skill3.height / 4, 30, (255, 255, 255), "ABERUS")
        janela.draw_text("Tecla: C", skill3.x, skill3.y + skill3.height/2, 30, (255, 255, 255), "ABERUS")
    if teclado.key_pressed("z") and len(lista) > 0 and (energia - gameData[personagem]["skills"][lista[0]][2]) >= 0:
        gasto = gameData[personagem]["skills"][lista[0]][2]
        return gameData[personagem]["skills"][lista[0]][0], gameData[personagem]["skills"][lista[0]][1], 0, gasto, lista[0],gameData
    if teclado.key_pressed("x") and len(lista) > 1 and (energia - gameData[personagem]["skills"][lista[1]][2]) >= 0:
        gasto = gameData[personagem]["skills"][lista[1]][2]
        return gameData[personagem]["skills"][lista[1]][0], gameData[personagem]["skills"][lista[1]][1], 0, gasto, lista[1],gameData
    return None, None, contador, 0, None,gameData

def turn(personagem, gameData, atacar, habilidade, item, mouse, inimigo, contador, energia,janela, listaDeItens):
    teclado = Window.get_keyboard()
    atacar.draw()
    habilidade.draw()
    item.draw()
    if mouse.is_over_object(atacar) and mouse.is_button_pressed(1) and contador == 0:
        return "Dano", dano(gameData[personagem]["atk"], gameData[inimigo]["df"]), contador, 0, ("ataque %s"%personagem), gameData
    if (mouse.is_over_object(habilidade) and mouse.is_button_pressed(1)) or contador == 1:
        contador = 1
        if teclado.key_pressed("ESC"):
            contador = 0
        return skills(personagem,gameData, teclado, contador, energia, atacar, habilidade, item, janela)
    if (mouse.is_over_object(item) and mouse.is_button_pressed(1)) or contador == 2:
        contador = 2
        if teclado.key_pressed("ESC"):
            contador = 0
        return itens(personagem,gameData,janela,contador, listaDeItens, mouse)
    return None, None, contador, 0, None,gameData

def battle(nomeDoPersonagem1, nomeDoPersonagem2, inimigo, gameData):
    #variáveisDeControle
    contador = 0
    cadencia = 0
    actionGauge1 = 0
    actionGauge2 = 0
    actionGauge3 = 0
    morte1 = 0
    morte2 = 0
    listaDeItens = []
    animacao = None
    controleAnimacao = 0
    for i in gameData["itens"]:
        listaDeItens.append(i)
    #
    #Sprites
    janela = Window(1280, 720)
    battleground = Sprite("Imagens/Battleground(3).jpg")
    menuOpcoes = Sprite("Imagens/RetânguloRoxoManeiro.jpg")
    atacar = Sprite("Imagens/Atacar.jpg")
    habilidade = Sprite("Imagens/Habilidade.jpg")
    protagonista = Sprite("Imagens/%s.png"%nomeDoPersonagem1, 2)
    amigoDoProta1 = Sprite("Imagens/%s.png"%nomeDoPersonagem2, 3)
    chefe = Sprite("Imagens/%s.png"%inimigo)
    item = Sprite("Imagens/Item.jpg")
    mouse = Window.get_mouse()
    janela.set_title("Call Of Cultists")
    retanguloVermelho = Sprite("Imagens/RetanguloVermelho.jpg")
    barraAcao1 = Sprite("Imagens/ActionGaugeVazia.png")
    barraAcao1P = Sprite("Imagens/ActionGaugePreencher.png")
    barraAcao2 = Sprite("Imagens/ActionGaugeVazia.png")
    barraAcao2P = Sprite("Imagens/ActionGaugePreencher.png")
    #definir variaveis
    turno = ""
    pontosDeVida1at = gameData[nomeDoPersonagem1]["vida"]
    pontosDeVida2at = gameData[nomeDoPersonagem2]["vida"]
    pontosDeVida3at = gameData[inimigo]["vida"]
    energia1at = gameData[nomeDoPersonagem1]["energia"]
    energia2at = gameData[nomeDoPersonagem2]["energia"]
    #definir posição
    menuOpcoes.y = battleground.height
    atacar.x = janela.width - (atacar.x + 2*atacar.width + 2*(atacar.width/4))
    atacar.y = battleground.height + atacar.height/4
    habilidade.x = janela.width - (habilidade.x + habilidade.width + habilidade.width/4)
    habilidade.y = battleground.height + habilidade.height/4
    item.x = atacar.x + atacar.width/2
    item.y = battleground.height + item.height + 3*(item.height/4)
    protagonista.y = battleground.height/2
    amigoDoProta1.x = 0 - amigoDoProta1.width/3.5
    amigoDoProta1.y = battleground.height/2 + protagonista.height/2
    chefe.x = janela.width - 4*chefe.width
    chefe.y = battleground.height/2
    retanguloVermelho.height = 10
    if retanguloVermelho.width <= chefe.width:
        retanguloVermelho.x = chefe.x - chefe.width/2 + retanguloVermelho.width/2
    else:
        retanguloVermelho.x = chefe.x - retanguloVermelho.width/2 + chefe.width/2
    retanguloVermelho.y = chefe.y - 10
    barraAcao1.x = (6/4)*atacar.width
    barraAcao1.y = battleground.height + atacar.height/2
    barraAcao1P.x = (6/4)*atacar.width
    barraAcao1P.y = battleground.height + atacar.height / 2
    barraAcao2.x = (6/4)*atacar.width
    barraAcao2.y = battleground.height + 2*atacar.height
    barraAcao2P.x = (6/4)*atacar.width
    barraAcao2P.y = battleground.height + 2 * atacar.height
    rV0 = retanguloVermelho.width

    #sprites para animações
    spriteAnima = None
    spriteAnima2 = None
    #animações
    protagonista.set_total_duration(400)
    amigoDoProta1.set_total_duration(600)

    #SalvarPosicoes
    salvarPX = protagonista.x
    salvarPY = protagonista.y
    salvarAX = amigoDoProta1.x
    salvarAY = amigoDoProta1.y
    salvarIX = chefe.x
    salvarIY = chefe.y

    while True:
        if gamestates.SoundStates == 1:
            sound_battle1.play()
        elif gamestates.SoundStates == 2:
            sound_battle2.play()
        elif gamestates.SoundStates == 3:
            sound_battle3.play()

        #desenho
        battleground.draw()
        menuOpcoes.draw()
        janela.draw_text("Nome", atacar.width / 2, battleground.height + atacar.height / 8, 25, (0, 0, 0),"New Times Roman")
        janela.draw_text("%s "%nomeDoPersonagem1, atacar.width/2, battleground.height + atacar.height/2, 25, (255, 255, 255), "New Times Roman")
        janela.draw_text("PV %d"%pontosDeVida1at + " / " + "%d"%gameData[nomeDoPersonagem1]["vida"],atacar.width/2, battleground.height + atacar.height, 25, (255, 255, 255), "New Times Roman")
        janela.draw_text("EN %d "%energia1at + " / " + "%d"%gameData[nomeDoPersonagem1]["energia"], atacar.width/2, battleground.height + (3/2)*atacar.height, 25, (255, 255, 255), "New Times Roman")
        janela.draw_text("%s " % nomeDoPersonagem2, atacar.width / 2, battleground.height + 2*atacar.height, 25, (255, 255, 255),"New Times Roman")
        janela.draw_text("PV %d" % pontosDeVida2at + " / " + "%d" % gameData[nomeDoPersonagem2]["vida"], atacar.width / 2, battleground.height + (5/2)*atacar.height, 25, (255,255,255), "New Times Roman" )
        janela.draw_text("EN %d" % energia2at + " / " + "%d" % gameData[nomeDoPersonagem2]["energia"], atacar.width / 2,battleground.height + 3 * atacar.height, 25, (255, 255, 255), "New Times Roman")
        janela.draw_text("%s " % inimigo, retanguloVermelho.x - chefe.width/16, retanguloVermelho.y - 2*retanguloVermelho.height, 20, (255, 0, 0),"ABERUS")
        protagonista.draw()
        amigoDoProta1.draw()
        chefe.draw()
        retanguloVermelho.draw()
        barraAcao1.draw()
        barraAcao1P.draw()
        barraAcao2.draw()
        barraAcao2P.draw()
        if animacao == None:
            #situação de morte
            if pontosDeVida1at <= 0 and morte1 == 0:
                morte1 = 1
                pontosDeVida1at = 0
                salvarPosix = protagonista.x
                salvarPosiy = protagonista.y
                protagonista = Sprite("Imagens/%sMorto.png"%nomeDoPersonagem1, 1)
                protagonista.x = salvarPosix
                protagonista.y = salvarPosiy
            if pontosDeVida1at > 0 and morte1 == 1:
                morte1 = 0
                salvarPosix = protagonista.x
                salvarPosiy = protagonista.y
                protagonista = Sprite("Imagens/%s.png"%nomeDoPersonagem1, 2)
                protagonista.x = salvarPosix
                protagonista.y = salvarPosiy
                protagonista.set_total_duration(400)
            if pontosDeVida2at <= 0 and morte2 == 0:
                morte2 = 1
                pontosDeVida2at = 0
                salvarPosix = amigoDoProta1.x
                salvarPosiy = amigoDoProta1.y
                amigoDoProta1 = Sprite("Imagens/%sMorto.png"%nomeDoPersonagem2, 1)
                amigoDoProta1.x = salvarPosix
                amigoDoProta1.y = salvarPosiy
            if pontosDeVida2at > 0 and morte2 == 1:
                morte2 = 0
                salvarPosix = amigoDoProta1.x
                salvarPosiy = amigoDoProta1.y
                amigoDoProta1 = Sprite("Imagens/%s.png"%nomeDoPersonagem2, 3)
                amigoDoProta1.x = salvarPosix
                amigoDoProta1.y = salvarPosiy
                amigoDoProta1.set_total_duration(600)
            #animações
            if morte1 == 0:
                protagonista.update()
            if morte2 == 0:
                amigoDoProta1.update()
            #sistemas
            if janela.delta_time and turno == "":
                if actionGauge2 < 1 and actionGauge3 < 1 and morte1 == 0:
                    actionGauge1 += 0.0005 * gameData[nomeDoPersonagem1]["agi"]
                    if actionGauge1 >= 1:
                        actionGauge1 = 1
                        turno = nomeDoPersonagem1
                    barraAcao1P.width = (barraAcao1.width) * actionGauge1
                if actionGauge1 < 1 and actionGauge3 < 1 and morte2 == 0:
                    actionGauge2 += 0.0005 * gameData[nomeDoPersonagem2]["agi"]
                    if actionGauge2 >= 1:
                        actionGauge2 = 1
                        turno = nomeDoPersonagem2
                    barraAcao2P.width = (barraAcao2.width) * actionGauge2
                if actionGauge1 < 1 and actionGauge2 < 1:
                    actionGauge3 += 0.0005 * gameData[inimigo]["agi"]
                    if actionGauge3 >= 1:
                        actionGauge3 = 1
                        turno = inimigo
            #chefe.update()
            if turno == nomeDoPersonagem1 and cadencia == 60:
                cod, num, contador, gasto, animacao,gameData = turn(nomeDoPersonagem1, gameData, atacar, habilidade, item, mouse, inimigo,contador, energia1at,janela,listaDeItens)
                if cod == "Dano":
                    pontosDeVida3at -= dano(num, gameData[inimigo]["df"])
                    energia1at -= gasto
                    turno = ""
                    actionGauge1 = 0
                    retanguloVermelho.width = rV0 * (pontosDeVida3at / gameData[inimigo]["vida"])
                    cadencia = 0
                if cod == "Cura":
                    pontosDeVida1at += num
                    if pontosDeVida1at >= gameData[nomeDoPersonagem1]["vida"]:
                        pontosDeVida1at = gameData[nomeDoPersonagem1]["vida"]
                    pontosDeVida2at += num
                    if pontosDeVida2at >= gameData[nomeDoPersonagem2]["vida"]:
                        pontosDeVida2at = gameData[nomeDoPersonagem2]["vida"]
                    energia1at -= gasto
                    if energia1at >= gameData[nomeDoPersonagem1]["energia"]:
                        energia1at = gameData[nomeDoPersonagem1]["energia"]
                    turno = ""
                    actionGauge1 = 0
                    cadencia = 0
            if turno == nomeDoPersonagem2 and cadencia == 60:
                cod, num, contador, gasto, animacao, gameData = turn(nomeDoPersonagem2, gameData, atacar, habilidade, item, mouse, inimigo,contador, energia2at,janela,listaDeItens)
                if cod == "Dano":
                    pontosDeVida3at -= dano(num, gameData[inimigo]["df"])
                    energia2at -= gasto
                    turno = ""
                    actionGauge2 = 0
                    retanguloVermelho.width = rV0 * (pontosDeVida3at / gameData[inimigo]["vida"])
                    cadencia = 0
                if cod == "Cura":
                    pontosDeVida1at += num
                    if pontosDeVida1at >= gameData[nomeDoPersonagem1]["vida"]:
                        pontosDeVida1at = gameData[nomeDoPersonagem1]["vida"]
                    pontosDeVida2at += num
                    if pontosDeVida2at >= gameData[nomeDoPersonagem2]["vida"]:
                        pontosDeVida2at = gameData[nomeDoPersonagem2]["vida"]
                    energia2at -= gasto
                    if energia2at >= gameData[nomeDoPersonagem2]["energia"]:
                        energia2at = gameData[nomeDoPersonagem2]["energia"]
                    turno = ""
                    actionGauge2 = 0
                    cadencia = 0
            #AI inimigo
            if turno == inimigo:
                listaSkillsI = []
                for k in gameData[inimigo]["skills"]:
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
                        animacao = "ataque %s"%inimigo + str(alvo)
                        pontosDeVida1at -= dano(gameData[inimigo]["atk"], gameData[nomeDoPersonagem1]["df"])
                    if alvo == 2:
                        animacao = "ataque %s" % inimigo + str(alvo)
                        pontosDeVida2at -= dano(gameData[inimigo]["atk"], gameData[nomeDoPersonagem2]["df"])
                if 6 <= acaoDoBoss < 8 and len(listaSkillsI) > 0:
                    if alvo == 1:
                        animacao = listaSkillsI[0] + str(alvo)
                        pontosDeVida1at -= dano(gameData[inimigo]["skills"][listaSkillsI[0]], gameData[nomeDoPersonagem1]["df"])
                    if alvo == 2:
                        animacao = listaSkillsI[0] + str(alvo)
                        pontosDeVida2at -= dano(gameData[inimigo]["skills"][listaSkillsI[0]],gameData[nomeDoPersonagem2]["df"])
                if 8 <= acaoDoBoss <= 9 and len(listaSkillsI) > 1:
                    if alvo == 1:
                        animacao = listaSkillsI[1] + str(alvo)
                        pontosDeVida1at -= dano(gameData[inimigo]["skills"][listaSkillsI[1]], gameData[nomeDoPersonagem1]["df"])
                    if alvo == 2:
                        animacao = listaSkillsI[1] + str(alvo)
                        pontosDeVida2at -= dano(gameData[inimigo]["skills"][listaSkillsI[1]],gameData[nomeDoPersonagem2]["df"])
                turno = ""
                actionGauge3 = 0
            if janela.delta_time() and cadencia != 60:
                cadencia += 1
            if pontosDeVida3at <= 0 and animacao == None:
                return "Vitoria"
            if pontosDeVida1at <= 0 and pontosDeVida2at <= 0 and animacao == None:
                return "Game Over"
        else:
            animacao, controleAnimacao, protagonista, amigoDoProta1, chefe, spriteAnima, spriteAnima2 = animacoes(animacao, protagonista, amigoDoProta1, chefe, controleAnimacao, salvarPX, salvarPY, salvarAX, salvarAY, salvarIX, salvarIY, spriteAnima, morte1, morte2, spriteAnima2)
        #
        janela.update()

'''battle(nomeDoPersonagem1, nomeDoPersonagem2, vilao1, gameData)
battle(nomeDoPersonagem1, nomeDoPersonagem2, vilao2, gameData)
battle(nomeDoPersonagem1, nomeDoPersonagem2, vilao3, gameData)'''
