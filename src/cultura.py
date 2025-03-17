from produto import Produto
import calcula
class Cultura():

    codigo_cultura = 1
    codigo_produto_int = 0
    quantidade_produto_int = 0
    comprimento_int = 0
    rua_int = 0
            
    def exibir_menu():        
        while True:       
            print("1. Cadastrar um novo produto")
            print("2. Atualizar produto")
            print("3. Deletar produto")
            print("4. Exibir produto")
            print("5. Cálculo do manejo de insumos")
            print("6. Sair do programa")        
            opcao = input("\nEscolha uma opção (1-6): ")
            if opcao == '1':
                while True:               
                    codigo_cultura = input("\nEscolha uma opção ((1) Café e (2) Cana de açucar: ")            
                    if(codigo_cultura == '1' or codigo_cultura == '2'): 
                        print("\n")
                        Cultura.cadastrar_produto(codigo_cultura)                                       
                        break
                    else:
                        print("Opção inálida. Por favor, escolha uma opção de 1 a 2.")                             
            elif opcao == '2':                
                Cultura.atualizar_produto()                
            elif opcao == '3':                
                Cultura.deletar_produto()
            elif opcao == '4':                
                Cultura.listar_produto()
            elif opcao == '5':                
                Cultura.calcular()
            elif opcao == '6':
                print("Saindo do programa.")
                break
            else:
                print("Opção inálida. Por favor, escolha uma opção de 1 a 6.")

    
    def cadastrar_produto(codigo_cultura):        
        nome_produto = input("Informe o nome do produto: ")        
        while(True):
            quantidade_produto = input("Quantidade de produto aplicada por mL/metro com o trator: ") 
            if quantidade_produto.isdecimal():
                quantidade_produto_int = float(quantidade_produto)
                break
            else:
                print("Quantidade de produto invalída")

        while(True):
            rua = input("Digite a largura de cada rua (em metros):")
            if rua.isdecimal():
                rua_int = float(rua)
                break
            else:
                print("Número de ruas invalída")

        while(True):
            comprimento =  input("Digite o comprimento total da lavoura (em metros): ")
            if comprimento.isdecimal():
                comprimento_int = float(comprimento)
                break
            else:
                print("Comprimento  invalída")     

        

        novo_produto = Produto(codigo_cultura, nome_produto, quantidade_produto_int, comprimento_int, rua_int)  
        print("Produto Cadastrado !!!")
        print(f'{'cultura'.ljust(25)} | {'codigo do produto'.ljust(25)} | {'nome do produto'.ljust(25)} | {'quantidade'.ljust(25)} | {'comprimento'.ljust(25)} | {'largura rua '.ljust(25)} | {'status'}')
        cultura_str = 'Cafe' if codigo_cultura == 1 else 'Açucar'
        codigo_str = str(novo_produto._codigo)             
        quantidade_str = str(novo_produto._quantidade) 
        comprimento_str = str(novo_produto._comprimento)           
        rua_str = str(novo_produto._rua)           
        print(f'{cultura_str.ljust(25)} | {codigo_str.ljust(25)} | {novo_produto._nome.ljust(25)} | {quantidade_str.ljust(25)} | {comprimento_str.ljust(25)} | {rua_str.ljust(25) } | {novo_produto._ativo }')     
        print("\n")

    def atualizar_produto():        
        while(True):
            codigo_produto = input("Informe o codigo produto: ")
            if codigo_produto.isnumeric():
                codigo_produto_int = int(codigo_produto)
                break
            else:
                print("Codigo produto invalído")   

        nome_produto = input("Informe o novo nome do produto: ")
        while(True):
            quantidade_produto = input("Informe a nova quantidade a produto: ") 
            if codigo_produto.isnumeric():
                quantidade_produto_int = float(quantidade_produto)
                break
            else:
                print("Codigo produto invalído")

        while(True):
            comprimento =  input("Digite o comprimento do lado do quadrado: ") 
            if comprimento.isnumeric():
                comprimento_int = int(comprimento)
                break
            else:
                print("Comprimento  invalída")

        while(True):
            rua = input("Quantas ruas a lavoura têm ?")
            if rua.isnumeric():
                rua_int = int(rua)
                break
            else:
                print("Número de ruas invalída")     

        Produto.atualizar_produto(codigo_produto_int, nome_produto, quantidade_produto_int, comprimento_int, rua_int)
        print("Produto Atualizado !!!")
        print(Produto.listar_produto())
        print("\n")

    def deletar_produto():
        codigo_produto = int(input("Informe o codigo produto:"))
        Produto.deletar_produto(codigo_produto)
        print("\n")
        
    def listar_produto():
       print(Produto.listar_produto())
       print("\n")    

    def calcular():
        calcula.calcular_insumos_por_produto()
        print("\n")
if(__name__ == "__main__"):
    Cultura.exibir_menu()