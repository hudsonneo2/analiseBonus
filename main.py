import pandas as pd
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6857a1e35bcad12d62769136eb7fc80a'
auth_token = 'a87da179efa21fa0d7029c1ca9f3a3b9'
client = Client(account_sid, auth_token)

# pandas
# openpyxl = os dois são para integrar o excel com o py
# twilio = integrar o py com sms


# Passo a passo de solução

# Abrir os 6 arquivos do excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas']> 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'no mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')
        message = client.messages.create(
            to='+5511965819947',
            from_ = '+13608428751',
            body=f'no mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, vendas: {vendas}',)
        print(message.sid)


# Para cada arquivo:

# Verifica se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envie um SMS com Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
