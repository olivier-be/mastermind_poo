import random
class MASTERMIND:

    def __init__(self):
        self.couleur=["blanc","noire","rouge","vert","bleu","jaune"] #
        self.nombrea_léatoire=[self.couleur[random.randint(0,5)] for i in range(4) ]
        self.resultat_joueur=[] #= résultat précédement rentrer
        self.score=0 # 1 point = une manche
        self.vie=6 # nombre de vie et retire une vie si une ligne est terminé
    def start(self):
        """
        démare le jeu
        et réalise un boucle
        au
        :return:
        """
        print(self.couleur,self.nombrea_léatoire)
        for i in range(len(self.couleur)):
            tab=[0]*4
            tab_result=[0]*4
            for e in range(4):
                print(e,"valeur de la case")
                tab[e]=input()
                if tab[e]== self.nombrea_léatoire[e]:
                    tab_result[e]=1
            if 0 in tab_result:
                self.vie-=1
            else:
                self.score+=1

            if self.vie==0:
                print("perdu")
                print("score")
            else:
                print("gagné")
                print(self.vie,"vie",self.score,"score")

            print(tab_result)
            print(self.vie)




y=MASTERMIND()
y.start()

