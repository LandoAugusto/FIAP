from produto import Produto

def calcular_area(comprimento, largura):
    return comprimento * largura

def calcular_insumos_por_produto():   
   for item in Produto.produtos:  
        
        print("\n")
        cultura_str = 'Cafe' if item._cultura == '1' else 'Cana de açucar'
        codigo_str = str(item._codigo)             
        quantidade_str = str(item._quantidade )        
        comprimento_str = str(item._comprimento )  
        rua_str = str(item._rua )      
        print(f'{'cultura'.ljust(25)} | {'codigo do produto'.ljust(25)} | {'nome do produto'.ljust(25)} | {'quantidade de produto (mL)'.ljust(35)} | {'comprimento'.ljust(25)} | {'largura rua '.ljust(25)} ')
        print(f'{cultura_str.ljust(25)} | {codigo_str.ljust(25)} | {item._nome_produto.ljust(25)} | {quantidade_str.ljust(35) } | {comprimento_str.ljust(25) } | {rua_str.ljust(25) } ')
         # Calcula a area
        largura_total = calcular_area(item._comprimento, item._rua)
        # Quantidade de produto aplicada por metro
        aplicacao_por_metro = item._quantidade / 1000

        # Calcula quantas ruas a lavoura tem
        quantidade_ruas = largura_total / item._rua

        # Calcula quantos litros serão necessários
        litros_necessarios = quantidade_ruas * item._comprimento * aplicacao_por_metro

        # Exibe os resultados
        print(f"A lavoura possui {largura_total:.2f} (em metros) de area total.")        
        print(f"A lavoura possui aproximadamente {quantidade_ruas:.2f} ruas.")
        print(f"Serão necessários cerca de {litros_necessarios:.4f} litros de {item._nome_produto} para cobrir toda a lavoura.")