class Comentarios:
    def __init__(self,nome_cliente,comentario):
    
        self._nome_cliente = nome_cliente
        self._comentario = comentario
    
    @property
    def cliente(self):
        return self._nome_cliente
    
    def livro(self):
        return self._nome_do_livro
    
    @property
    def comentario(self):
        return self._comentario
    
    def __str__(self):
        return f',{self._cliente},{self._comentario}'