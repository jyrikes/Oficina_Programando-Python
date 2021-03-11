#RECEBENDO O VALOR DO PRODUTO E O DESCONTO

valor_produto = float(input("DIGITE O VALOR DO PRODUTO EM REAIS: "))

desconto = float(input("DIGITE O DESCONTO EM PORCENTAGEM APENAS O VALOR NUMERICO: "))

#CALCULANDO O DESCONTO

preco_atual = ((100-desconto)/100)*valor_produto

# ESCREVENDO O NOVO PREÇO COM O DESCONTO

print("\nO VALOR DO PRODUTO COM {}% DE DESCONTO É {} REAIS".format(desconto,preco_atual))
