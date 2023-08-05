print("Projeto de Webscraping Bolsa de Valores")
import yfinance as yf
import pandas as pd
import datetime
from matplotlib import pyplot as plt
import mplcyberpunk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from email.message import EmailMessage

#Váriavel destinada a selecionar os ativos que serão buscados na base de dados.
ativos = ativos = ["PETR4.SA", "MGLU3.SA"]
hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365)
dados_mercado = yf.download(ativos,um_ano_atras,hoje)
print(dados_mercado)

#Alteração do nome das colunas e definição da várivel fechamento.
dados_fechamento = dados_mercado ["Close"]
dados_fechamento.columns = ("MAGALU", "PETROBRAS")
dados_fechamento = dados_fechamento.dropna()
print (dados_fechamento)

#Váriavel destinada a obter informação dos fechamentos mensais e anuais.
dados_fechamento_mensal = dados_fechamento.resample("M").mean()
dados_fechamento_anual = dados_fechamento.resample("Y").mean()

#Váriavel destinada a obter informações em relação ao retorno financeiro das ações buscadas.
retorno_no_ano = dados_fechamento_anual.pct_change().dropna()
retorno_no_mes = dados_fechamento_mensal.pct_change().dropna()
retorno_no_dia = dados_fechamento.pct_change().dropna()

#loc > referenciar elementos a partir do nome
#Iloc > selecionar elementos como uma matriz
retorno_dia_PETRO = retorno_no_dia.iloc [-1,0]
retorno_dia_MAGALU = retorno_no_dia.iloc[-1,1]

retorno_mes_PETRO = retorno_no_mes.iloc [-1,0]
retorno_mes_MAGALU = retorno_no_mes.iloc[-1,1]

retorno_ano_PETRO = retorno_no_ano.iloc [-1,0]
retorno_ano_MAGALU = retorno_no_ano.iloc[-1,1]

#Transformando os valores em %.
retorno_dia_PETRO = round(retorno_dia_PETRO * 100,2)
retorno_dia_MAGALU = round(retorno_dia_MAGALU * 100,2) 


retorno_mes_PETRO = round(retorno_mes_PETRO * 100,2)
retorno_mes_MAGALU = round(retorno_mes_MAGALU * 100,2)

retorno_ano_PETRO = round(retorno_ano_PETRO *100,2)
retorno_ano_MAGALU = round(retorno_ano_MAGALU * 100,2)

#Criação dos gráficos das ações.
plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'MAGALU', use_index = True, legend = False)
plt.title("MAGALU")
plt.savefig('MAGALU.png', dpi = 300)
plt.show()

plt.style.use('cyberpunk')
dados_fechamento.plot(y = 'PETROBRAS', use_index = True, legend = False)
plt.title("PETROBRAS")
plt.savefig('PETROBRAS.png', dpi = 300)
plt.show()

#Importação de arquivo environment para utilização de password.
#Primeiro deve acessar 'Senhas de App' no gmail, do email que será utilizado para envio do relatório
#criar uma senha de acesso secundário e copiar ela.
#Neste passo você deve abrir o diretório onde se encontra o arquivo .py do código, criar um bloco de notas
#neste bloco de notas você definira "password = (aqui você ira colar a senha retirada do passo acima)
#Depois você ira em "Salvar como", no bloco de notas, salvará com o nome (.env), e salvará o tipo do arquivo como "Todos"
#se tudo estiver correto, ao rodar o código sera exibida a mensagem 'true'.
import os
from dotenv import load_dotenv
print (load_dotenv())

#Acesso a porta web para envio de e-mail de forma automática.
import imghdr
smtp_server = ("smtp.gmail.com")
smtp_port = 587

#em username utilize o email que será utilizado para envio, neste caso, gmail
username = ("emailexemplo@gmail.com")
password = os.environ.get("password")

from_email = (username)

#aqui, selecione o destinatário a receber o email.
to_email = ("exemplo@gmail.com")

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = ("titulo do email/assunto")
body =(f'''Mensagem que irá conter no email// Relatório de valores das ações da Magazine Luiza e Petrobras")

                  MAGALU:

No ano a MAGALU está tendo uma rentabilidade de {retorno_ano_MAGALU}%, 
enquanto no mês a rentabilidade é de {retorno_mes_MAGALU}%.

No último dia útil, o fechamento da MAGALU foi de {retorno_dia_MAGALU}%.

PETRO:

No ano a PETROBRAS está tendo uma rentabilidade de {retorno_ano_PETRO}%, 
enquanto no mês a rentabilidade é de {retorno_mes_PETRO}%.

No último dia útil, o fechamento da PETROBRAS foi de {retorno_dia_PETRO}%.


Abs,
''')
msg.attach(MIMEText(body, 'plain'))

#Selecionar o diretório onde foram salvas as imagens dos gráficos.
image_path = (r"COPIE E COLE O DIRETÓRIO AQUI, SALVAR AS IMAGENS EM UMA PASTA SEPARADA APENAS PARA ELAS")
for filename in os.listdir(image_path):
    with open(os.path.join(image_path, filename), 'rb') as f:
        img_data = f.read()
    image_type = imghdr.what(None, img_data)
    image = MIMEImage(img_data, _subtype=image_type)
    image.add_header('Content-Disposition', 'attachment', filename=filename)

    msg.attach(image)

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(from_email, to_email, text)
server.quit()
