from typing import Any, Union
import time
from time import strftime, localtime #biblioteca responsável em colocar os dados da data e hora do sistema em timestamp para ser usado no banco
import pymysql #biblioteca utilizada para comunicação entre python e mysql
import psutil #biblioteca responsável pela coleta de dados do sistema como cpu,memoria e disco

from pymysql.cursors import Cursor

#declarando as informações necessárias para a conexãocle com o banco de dados
conexao = pymysql.connect(
  host = 'localhost',
  user = 'root',
  passwd='',
  database = 'bancodados'
)
cursor = conexao.cursor()
#leitura de data e hora:
datahora = strftime("%Y-%m-%d %H:%M:%S", localtime())


codigocl = int(input('Digite o código do cliente: '))
codigope = int(input('Digite o código do Pedido: '))
tam =  int(input('Digite a quantidade de itens:'))

inserepedido = "insert into Pedido(codped, data, codcliente)values(%s, %s, %s)"
valorpedido = (codigope, datahora, codigocl)
for i in range(tam) :

    
    codigopr = int(input('Digite o código do Produto: '))
    quantidade = int(input('Digite a quantidade: '))
    valorunidade = int(input('Digite o valor da unidade: '))

    print()
    insereitem = "insert into item(codped, codproduto, quantidade, valorunidade)values(%s, %s, %s,%s)"
    valoritem = (codigope, codigopr, quantidade, valorunidade)
    conexao.commit()


print("obrigado pela preferencia")
    


    
