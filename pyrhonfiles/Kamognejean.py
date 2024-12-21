# Exercices 1 _POO
class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        peri = 2*(self.longueur + self.largeur)
        return peri

    def surface(self):
        surf = self.longueur*self.largeur
        return surf

    # getters
    def get_longueur(self):
        return self.longueur
    def get_largeur(self):
        return self.largeur

    # setters
    def set_longeur(self,x):
        self.longueur = x
    def set_largeur(self,y):
        self.largeur = y

class Parallepipede(Rectangle):
    def __init__(self,longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return  self.longueur * self.largeur * self.hauteur

rectangle1 = Rectangle(12, 5)
para1 = Parallepipede(16,5,3)
rectangle2 = Rectangle(7,5,)
print('perimetre du rectandle  : ', rectangle1.perimetre())
print('Surface du rectangle :', rectangle1.surface())
print('Volume du parallepipede : ', para1.volume())
