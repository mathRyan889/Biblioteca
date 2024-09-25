# Comentarios.py
lista_de_comentarios = list()  # Lista global para armazenar todos os comentários

class Comentarios:
    def __init__(self, nome_cliente, comentario):
        self._nome_cliente = nome_cliente
        self._comentario = comentario
        lista_de_comentarios.append(self)  # Adiciona o comentário ao criar uma nova instância

    @property
    def cliente(self):
        return self._nome_cliente

    @property
    def comentario(self):
        return self._comentario

    def __str__(self):
        return f'{self._nome_cliente}, {self._comentario}'

    @classmethod
    def adicionar_comentario(cls, nome_cliente, comentario):
        # Adiciona diretamente à lista de comentários ao criar uma nova instância
        Comentarios(nome_cliente, comentario)
        
    @classmethod
    def exibir_comentario(cls):
        # Exibe todos os comentários armazenados
        for c in lista_de_comentarios:
            print('-=' * 30)
            print(f'[CLIENTE]: {c._nome_cliente}\n[COMENTARIO]: {c._comentario}')
            print('-=' * 30)
