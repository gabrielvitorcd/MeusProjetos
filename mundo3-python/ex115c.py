from utilidadescev import arquivo
def selecionarcor():
    c = [
    '\033[m',          # 0 - sem cor (fundo normal, letras normais)
    '\033[0;31m',      # 1 - vermelho
    '\033[0;32m',      # 2 - verde
    '\033[0;33m',      # 3 - amarelo
    '\033[0;34m',      # 4 - azul
    '\033[0;35m',      # 5 - roxo
    '\033[0;37m',      # 6 - branco
    ]
    return c


def leiaInt(msg=': '):
  global entrada
  while True:
    try:
        entrada = int(input(msg)) 
        return entrada          #return cria um break no laco
    except(ValueError,TypeError):
        print(f'{selecionarcor()[1]}ERRO!{selecionarcor()[0]} Digite um número inteiro válido.')
        continue
    except KeyboardInterrupt:
       print(f'\n{selecionarcor()[1]} O usuario preferiu terminar o programa {selecionarcor()[0]}')
       return 0
    else:
        print('fim1')
def linha():
    print('-'*30)

def titulo(msg):
    linha()
    print(f'{msg}'.center(30))
    linha()

def menu(lista):
    global opc
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{selecionarcor()[3]} {c}{selecionarcor()[0]} -{selecionarcor()[4]} {item}{selecionarcor()[0]}')
        c+=1
    linha()
    opc =  leiaInt('Escolha de 1 a 3: ')
    return opc
        
arq = 'cadastro.txt'
if not arquivo.arquivoExiste(arq): # se o arquivo nao existir == return False
    arquivo.criarArquivo(arq)      #funcao que cria o arquivo e exibe uma msg se foi criado
    
while True:

    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    
    if opc == 1:
        arquivo.lerArquivo(arq)
    elif opc == 2:
        titulo('CADASTRO NOVO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        
        arquivo.gravarArquivo(arq,nome,idade)
    elif opc == 3:
        break
    else:
        print(f'{selecionarcor()[1]} ERRO! Digite um opcao valida{selecionarcor()[0]}')
print('Programa finalizado')