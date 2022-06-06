from smtplib import SMTP

email_from = '' #email do remetente. 
email_to = '' #email do destinatario. 

smtp = 'smtp.gmail.com' #servidor que será usado

server = SMTP(smtp, 587) #setando servidor
server.starttls() #setando protocolo
server.login(email_from, open('senha.txt').read()) #autenticação do email no servidor.

msg =  '''
Esse eh um email enviado
por um algoritmo em python
''' #mensagem que será enviada

server.sendmail(email_from, email_to, msg) #enviando email.
server.quit() #encerrando o servidor.
print('Email enviado com sucesso') #confirmação de envio.

