from random import randint

class Produto:
    produtos = []
    def __init__(self, codigo_cultura, nome_produto, quantidade_produto, comprimento, rua):        
        self._codigo = randint(1,100) 
        self._cultura = codigo_cultura
        self._nome = nome_produto.title()    
        self._quantidade = quantidade_produto
        self._comprimento = comprimento    
        self._rua = rua    
        self._ativo = True
        Produto.produtos.append(self)

    def __str__(self):
        return f'{self._codigo} | {self._cultura} | {self._nome} | {self._quantidade} | {self._comprimento} | {self._rua}'

    def listar_produto():        
        print(f'{'cultura'.ljust(25)} | {'codigo do produto'.ljust(25)} | {'nome do produto'.ljust(25)} | {'quantidade'.ljust(25)} | {'comprimento'.ljust(25)} | {'largura rua '.ljust(25)} | {'status'}')
        for item in Produto.produtos:            
                cultura_str = 'Cafe' if item._cultura == 1 else 'Cana de açucar'
                codigo_str = str(item._codigo)             
                quantidade_str = str(item._quantidade )        
                comprimento_str = str(item._comprimento )           
                rua_str = str(item._rua )           
                print(f'{cultura_str.ljust(25)} | {codigo_str.ljust(25)} | {item._nome.ljust(25)} | {quantidade_str.ljust(25) } | {comprimento_str.ljust(25) } | {rua_str.ljust(25) } | {item._ativo }')

    def atualizar_produto(codigo_produto, nome_produto, quantidade_produto, comprimento, rua):         
        for item in Produto.produtos:   
                if codigo_produto == item.codigo :         
                    item._nome= nome_produto  
                    item._quantidade= quantidade_produto
                    item._comprimento = comprimento
                    item._rua = rua

    def deletar_produto(codigo_produto):         
        for indice, item in enumerate(Produto.produtos):
            if item._codigo == codigo_produto :
               item.remove(indice)
            
    @property
    def ativo(self):
        return 'true' if self._ativo else 'false'
