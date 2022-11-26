#Professora : LIVIANE PONTE REGO
#Disciplina: ALGORITMOS E LINGUAGEM DE PROGRAMAÇÃO II - T2020 (2022.1)
#Aluno: CÁSSIO SOUSA DA SILVA (CÁSSIO ARAPIUN)

#ATIVIDADE: COPA DO MUNDO

ponto = 0

for partida in range(0,3):

  partida = int(input("Digite o número que represente o resultado do brasil em cada partida\n\n[1]-Vitória\n[2]-Empate\n[3]-Derrota\n\nDigite aqui: "))
  if partida == 1:
    ponto += 3
  elif partida == 2:
    ponto += 2 
  else:
      ponto += 0

print(f"O total de pontos do Brasil na primeira rodada foi de {ponto} pontos")