#Professora : LIVIANE PONTE REGO
#Disciplina: ALGORITMOS E LINGUAGEM DE PROGRAMAÇÃO II - T2020 (2022.1)
#Aluno: CÁSSIO SOUSA DA SILVA (CÁSSIO ARAPIUN)

#ATIVIDADE: JOGO TUBARÃO



posicaoTubaraoVertical = 0
posicaoTubaraoHorizontal = 0

while True:
  opcao = int(input("Digite o número que represente para onde você quer que o tubarão se desloque:\n\n[1] - Para Cima\n[2] - Para Baixo\n[3] - Para a Esquerda\n[4] - Para a Direita\n[5] - Encerra o Jogo\n\nDigite aqui sua escolha: "))

  if opcao == 1:
    posicaoTubaraoHorizontal += 0
    posicaoTubaraoVertical += 10
    
    print("-" * 70)
    print(f"\33[3mO Tubarão se Deslocou para Cima e agora se encontra na posição ({posicaoTubaraoHorizontal}, {posicaoTubaraoVertical})\33[m")
    print("-" * 70)
    print()

  elif opcao == 2:
    posicaoTubaraoHorizontal += 0
    posicaoTubaraoVertical += - 10


    print("-" * 70)
    print(f"\33[3mO Tubarão se Deslocou para Baixo e agora se encontra na posição ({posicaoTubaraoHorizontal}, {posicaoTubaraoVertical})\33[m")
    print("-" * 70)
    print()
    
  elif opcao == 3:
    posicaoTubaraoHorizontal += -10
    posicaoTubaraoVertical += 0


    print("-" * 75)
    print(f"\33[3mO Tubarão se Deslocou para Esquerda e agora se encontra na posição ({posicaoTubaraoHorizontal}, {posicaoTubaraoVertical})\33[m")
    print("-" * 75)
    print()

  elif opcao == 4:
    posicaoTubaraoHorizontal += 10
    posicaoTubaraoVertical += 0


    print("-" * 75)
    print(f"\33[3mO Tubarão se Deslocou para Direita e agora se encontra na posição ({posicaoTubaraoHorizontal}, {posicaoTubaraoVertical})\33[m")
    print("-" * 75)
    print()
    
  elif opcao == 5:
    print("\n\33[3mJogo encerrado com sucesso! Volte Sempre S2\33[m\n")
    print("sua posição final foi: \n", posicaoTubaraoVertical," no eixo X\n",posicaoTubaraoHorizontal," no eixo Y")
    break
  
  else:
    print("-"*60)
    print("\33[3mOpa! você digitou uma opção inválida, tente novamente.\33[m")  
    print("-"*60) 