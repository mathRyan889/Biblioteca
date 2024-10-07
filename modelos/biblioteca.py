from modelos.avaliacoes import Avaliacao # importa a classe Avaliação
lista_de_livros = list() # lista com os livros adicioanados
class Biblioteca :
    def __init__(self,nome,categoria,ano): #Bloco construtor, define os parametros de todos os livros
        self._nome = nome.capitalize()
        self._categoria = categoria.upper()
        self._ano = ano
        self._avaliacao = []
        self._disponivel = False
        lista_de_livros.append(self) #adiciona livro a lista
        

    @property #Transforma o metodo em um atribudo da classe, facilitando sua manipulação
    def __str__(self):#Lê os atributos com string
        return f'Nome: {self._nome} || Categoria: {self._categoria} || Ano: {self._ano}'
    
    @classmethod #torna o metodo um metodo da classe, permitindo que ele altere detalhes dentro da classe
    def listar_livros(cls):
        print(f'{"NOME".ljust(25)}||{"CATEGORIA".ljust(25)}||{'ANO'.ljust(25)}||{'AVALIAÇÕES'.ljust(25)}||{'DISPONIBILIDADE'}')
        for livro in lista_de_livros:
            print(f'{livro._nome.ljust(25)}||{livro._categoria.ljust(25)}||{livro._ano.ljust(25)}||{str(livro.calculo_de_media).ljust(25)}||{'DISPONIVEL'if livro._disponivel else 'INDISPONIVEL'}')

        
    
    @classmethod
    def buscar_livro_por_nome(cls, nome): #metodo para encontrar um livro pelo o nome
        nome = nome.capitalize()
        for livro in lista_de_livros: #Para cada livro em listra_de_livros executar:
            if livro._nome == nome: # Se o livro da lista for igual ao nome da busca, retornar livro
                return livro
        return None
    
    
          
    def alternar_estado(self):
        self._disponivel = not self._disponivel #inverte o estado booleano para false ou True
    
    def adicionar_avaliacao(self,cliente,nota):
        if 0 <= nota <= 5 : # se 0 for menor ou igual a nota ou 5 for menor ou igual a zero executar:
            avaliacao = Avaliacao(cliente,nota) #A variavel avalicão recebe os atributos da classe Avaliação
            self._avaliacao.append(avaliacao)
    
            
    @property 
    def calculo_de_media(self):#metodo para calcular a media das avaliações
        if not self._avaliacao: # Se não houver avaliação
            return '-'
        soma = sum([avaliacao.nota for avaliacao in self._avaliacao])
        quantidade = len(self._avaliacao)
        media = round(soma/quantidade,1)
        return media
    