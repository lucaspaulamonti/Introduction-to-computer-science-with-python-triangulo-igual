# Escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False.
if(__name__)=='__main__':
    class Triangulo():
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
        def perimetro(self):
            self.perim=((self.a)+(self.b)+(self.c))
            return self.perim
        def semelhantes(self,triangulo):
            triangulo_1=[self.a,self.b,self.c]
            triangulo_2=[triangulo.a,triangulo.b,triangulo.c]
            sorted(triangulo_1)
            sorted(triangulo_2)
            if triangulo_1[0]/triangulo_2[0]==triangulo_1[1]/triangulo_2[1]==triangulo_1[2]/triangulo_2[2]:
                return True
            else:
                return not True
        pass
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!