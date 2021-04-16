from random import  choice

class RandomWalk():
    #Uma classe para gerar posiçoes aleatorias
  def __init__(self,num_ponts=5000):
      self.num_ponts = num_ponts

      #todos os passeios começam em 0
      self.x_valores = [0]
      self.y_valores = [0]

  def fill_walk(self):
      #continua dando passos ate que o passeio alcance o tamanho desejado
      while len(self.x_valores) < self.num_ponts:
          x_direction = choice([1,-1])
          x_distance = choice([0,1,2,3,4,5])
          x_stop = x_direction * x_distance

          y_diretion = choice([1,-1])
          y_distance =  choice([0,1,2,3,4,5])
          y_stop = y_diretion * y_distance

          #Rejeita a movimentaçao quando for nulo
          if x_stop == 0 and y_stop == 0:
              continue
          #calcula os proximos valores de x e y

          next_x = self.x_valores[-1] + x_stop
          next_y = self.y_valores[-1] + y_stop

          self.x_valores.append(next_x)
          self.y_valores.append(next_y)

