#import numpy

tabuleiro = [
    [7,0,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
"""

tabuleiro = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
"""
index = 0
tentativas = 0

def resolver(tabuleiro):
  global tentativas
  encontrado = encontrar_vazio(tabuleiro)
  if not encontrado:
    tentativas += 1
    print(f"Solução {tentativas}:")
    desenhar_tela(tabuleiro)
    return True
  else:
    linha, coluna = encontrado
  
  for i in range(1,10):
    if jogada_valida(tabuleiro,i,(linha,coluna)):
      tabuleiro[linha][coluna] = i
    
      (resolver(tabuleiro))
    
    tabuleiro[linha][coluna] = 0
  
  return False

def desenhar_tela(tabuleiro):
  for i in range(len(tabuleiro)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - - ")
    for j in range(len(tabuleiro[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")
      if j == 8:
        print(tabuleiro[i][j])
      else:
        print(str(tabuleiro[i][j]) + " ", end="")
  print("\n")

def encontrar_vazio(tabuleiro):
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[0])):
      if tabuleiro[i][j] == 0:
        return (i, j) #linha, coluna
  
  return None

def jogada_valida(tabuleiro, numero, posicao):
  #checar linha
  for i in range(len(tabuleiro[0])):
    if tabuleiro[posicao[0]][i] == numero and posicao[1] !=i:
      return False

  #checar coluna
  for i in range(len(tabuleiro)):
    if tabuleiro[i][posicao[1]] == numero and posicao[0]!= i:
      return False
  
  #checar caixa
  caixa_x = posicao[0] // 3
  caixa_y = posicao[1] // 3
  for i in range(caixa_x*3,caixa_x*3 + 3):
    for j in range(caixa_y*3,caixa_y*3 + 3):
      if tabuleiro[i][j] == numero and (i,j) != posicao:
        return False
  
  return True



desenhar_tela(tabuleiro)
resolver(tabuleiro)

