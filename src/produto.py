from random import randint

class Produto:
    produtos = []
    def __init__(self, codigo_cultura, nome_produto, quantidade_produto, comprimento, rua):        
        self._codigo = randint(1,100) 
        self._cultura = codigo_cultura
        self._nome_produto = nome_produto.title()    
        self._quantidade = quantidade_produto
        self._comprimento = comprimento    
        self._rua = rua            
        Produto.produtos.append(self)

    def __str__(self):
        return f'{self._codigo} | {self._cultura} | {self._nome_produto} | {self._quantidade} | {self._comprimento} | {self._rua}'

    def listar_produto():        
        print(f'{'cultura'.ljust(25)} | {'codigo do produto'.ljust(25)} | {'nome do produto'.ljust(25)} | {'quantidade de produto (mL)'.ljust(35)}  | {'largura rua '.ljust(25)} | {'comprimento'.ljust(25)} ')
        for item in Produto.produtos:            
                cultura_str = 'Cafe' if item._cultura == '1' else 'Cana de açucar'
                codigo_str = str(item._codigo)             
                quantidade_str = str(item._quantidade )        
                comprimento_str = str(item._comprimento )           
                rua_str = str(item._rua )           
                print(f'{cultura_str.ljust(25)} | {codigo_str.ljust(25)} | {item._nome_produto.ljust(25)} | {quantidade_str.ljust(35) }  | {rua_str.ljust(25) }  | {comprimento_str.ljust(25)}')     

    def atualizar_produto(codigo_produto, nome_produto, quantidade_produto, comprimento, rua):         
        for item in Produto.produtos:   
                if codigo_produto == item._codigo :         
                    item._nome_produto= nome_produto  
                    item._quantidade= quantidade_produto
                    item._comprimento = comprimento
                    item._rua = rua

    def deletar_produto(codigo_produto):         
        for indice, item in enumerate(Produto.produtos):
            if item._codigo == codigo_produto :
               del Produto.produtos[indice]

    def filtrar_produto(codigo_produto):
        return list(filter(lambda x: x._codigo == codigo_produto, Produto.produtos))
    
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False