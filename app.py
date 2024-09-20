#importações
import os
from time import sleep
from modelos.biblioteca import Biblioteca
from modelos.avaliacoes import Avaliacao

#Exibi o titulo (Biblioteca)
def titulo():
    os.system('cls')
    print('-='*65)
    print('            BIBLIOTECA')
    print('-='*65)

#Função para encerrar o programa
def finalizar_app():
    os.system('cls')
    print('Finalizar app...')
    sleep(0.5)

#Função para exibir as opções
def exibir_opcoes():
    sleep(1)
    print('''
          1.ADICIONAR NOVO LIVRO
          2.LISTAR LIVROS DA BIBLIOTECA
          3.FINALIZAR APP.
          4.LOCAR LIVRO''')
#funçao para guiar a tomada de direção
def opcao_escolhida():
    opcao = int(input('Opcão: '))
    
    if opcao == 1:
        
        adicionar_livro()
        adicao_avaliacao = str(input('Deseja adicionar uma avaliação:[S/N]')).strip().upper()
        
        if adicao_avaliacao == 'S' or adicao_avaliacao == 's':
            
            adicionar_avaliacao()
        voltar_ao_menu()
        
    elif opcao == 2:
        
        Biblioteca.listar_livros()
        adicao_avaliacao = str(input('Deseja adicionar uma avaliação:[S/N]')).strip().upper()
        
        if adicao_avaliacao == 'S' or adicao_avaliacao == 's':
            
            adicionar_avaliacao()
        voltar_ao_menu()
        
    elif opcao == 3:
        
        finalizar_app()
        
    elif opcao == 4:
        
        locar_livro()
        voltar_ao_menu()
        
    else:
        
        print('Opçao invalida')
        voltar_ao_menu()
#funçao para a locação de livro (muda o estado de disponibilidade do livro dependendo da escolha)
def locar_livro():
    os.system('cls')
    
    nome_do_livro = input('Digite o nome do livro:').strip().capitalize()
    livro = Biblioteca.buscar_livro_por_nome(nome_do_livro)
    
    if livro:
        
        if livro._disponivel:
            
            cobrança = str(input('Cobramos um valor de 0,50 centavos por dia, deseja prosseguir?[S/N]:')).strip().capitalize()
            
            if cobrança == 'S' or cobrança =='s':
                
                dias = int(input('Quantos dias de locação:'))
                valor = round(0.50*dias,1)
                print(f'A locação saiu pelo valor de R${valor}')
                livro.alternar_estado()
                sleep(0.5)
                print(f'Livro {nome_do_livro} locado com sucesso!!')
                
            else:
                
                print('Obrigado pela oportunidade, volte sempre!!!')
                
        else:
            
            print(f'Livro {nome_do_livro} não está disponivel para locaçao')
            
    else:
        print('Livro não encontrado, por favor verifique se temos o livro em nossa biblioteca')
        
def adicionar_avaliacao():
    os.system('cls')
    
    nome_do_livro = input('Digite o nome do livro:').strip().capitalize()
    livro = Biblioteca.buscar_livro_por_nome(nome_do_livro)
    
    if livro:
        
        try:
            cliente = input('Digite o nome do cliente: ').strip().capitalize()
            nota = int(input('Digite uma nota entre 0 e 5: '))
            
            if 0<= nota <=5:
                livro.adicionar_avaliacao(cliente,nota)
                print('Avaliação adicionada com Sucesso')
                
            else:
                print('Nota invalida, deve estar entre 0 e 5!')
                adicionar_avaliacao()
                
        except ValueError:
                print('Entrada errada, por favor digitar uma entrada valida!!')
                adicionar_avaliacao()

def adicionar_livro():
    
    nome = str(input('Digite o nome do livro: ')).strip()
    categoria = str(input('Digite a categoria do livro: ')).strip()
    ano = str(input('Digite o ano de lançamento do livro: ')).strip()
    sleep(0.9)
    livro = Biblioteca(nome,categoria,ano)
    print('Livro adicionado com sucesso!!!')
    disponivel = str(input('Livro está disponivel para retirada:[S/N]')).strip().capitalize()
    
    if disponivel == 'S' or disponivel == 's':
        livro.alternar_estado()
        print('O livro está disponivel para locação')
        
    elif disponivel == 'N' or disponivel == 'n':
        print('O livro não está disponivel para locação')
        
def voltar_ao_menu():
    input('Aperte qualquer tecla para voltar ao menu inicial:')
    os.system('cls')
    main()
    
#Vilão
vilao = Biblioteca('Vilão','Fantasia','2013')
vilao.adicionar_avaliacao('Matheus', 10)
vilao.adicionar_avaliacao('Marcos',8)
vilao.adicionar_avaliacao('Sthefanny',5)
vilao.alternar_estado()

#Wicked
Wicked = Biblioteca('Wicked','Fantasia','2005')
Wicked.adicionar_avaliacao('Matheus',5)
Wicked.adicionar_avaliacao('lucas',3)
Wicked.adicionar_avaliacao('marcos',10)
Wicked.alternar_estado()


#livros gerado pelo chatgpt(não tenho criatividade suficiente para isso kkkk)

# Livro 1
livro1 = Biblioteca('1984', 'Distopia', '1949')
livro1.adicionar_avaliacao('Ana', 4)
livro1.adicionar_avaliacao('João', 5)
livro1.adicionar_avaliacao('Maria', 3)
livro1.alternar_estado()

# Livro 2
livro2 = Biblioteca('Orgulho e Preconceito', 'Romance', '1813')
livro2.adicionar_avaliacao('Carlos', 5)
livro2.adicionar_avaliacao('Juliana', 4)
livro2.adicionar_avaliacao('Pedro', 4)
livro2.alternar_estado()

# Livro 3
livro3 = Biblioteca('O Hobbit', 'Fantasia', '1937')
livro3.adicionar_avaliacao('Luana', 5)
livro3.adicionar_avaliacao('Tiago', 4)
livro3.adicionar_avaliacao('Fernanda', 5)
livro3.alternar_estado()

# Livro 4
livro4 = Biblioteca('O Código Da Vinci', 'Suspense', '2003')
livro4.adicionar_avaliacao('Roberta', 3)
livro4.adicionar_avaliacao('Felipe', 4)
livro4.adicionar_avaliacao('Tatiane', 4)
livro4.alternar_estado()

# Livro 5
livro5 = Biblioteca('Sapiens', 'Não-ficção', '2011')
livro5.adicionar_avaliacao('Ricardo', 5)
livro5.adicionar_avaliacao('Simone', 5)
livro5.adicionar_avaliacao('Lucas', 4)
livro5.alternar_estado()

# Livro 6
livro6 = Biblioteca('A Game of Thrones', 'Fantasia', '1996')
livro6.adicionar_avaliacao('Marcelo', 4)
livro6.adicionar_avaliacao('Isabela', 5)
livro6.adicionar_avaliacao('Gabriel', 4)
livro6.alternar_estado()

# Livro 7
livro7 = Biblioteca('O Sol é para Todos', 'Drama', '1960')
livro7.adicionar_avaliacao('Julia', 5)
livro7.adicionar_avaliacao('Ricardo', 4)
livro7.adicionar_avaliacao('Fernanda', 5)
livro7.alternar_estado()

# Livro 8
livro8 = Biblioteca('Cem Anos de Solidão', 'Realismo Mágico', '1967')
livro8.adicionar_avaliacao('Luiz', 4)
livro8.adicionar_avaliacao('Sofia', 5)
livro8.adicionar_avaliacao('Carlos', 4)
livro8.alternar_estado()

# Livro 9
livro9 = Biblioteca('O Pequeno Príncipe', 'Infantil', '1943')
livro9.adicionar_avaliacao('Marta', 5)
livro9.adicionar_avaliacao('Eduardo', 5)
livro9.adicionar_avaliacao('Lúcia', 4)
livro9.alternar_estado()

# Livro 10
livro10 = Biblioteca('Harry Potter e a Pedra Filosofal', 'Fantasia', '1997')
livro10.adicionar_avaliacao('Vanessa', 5)
livro10.adicionar_avaliacao('Rodrigo', 4)
livro10.adicionar_avaliacao('Ana', 5)
livro10.alternar_estado()


def main():
    titulo()
    exibir_opcoes()
    opcao_escolhida()
    


if __name__ == '__main__':
    main()