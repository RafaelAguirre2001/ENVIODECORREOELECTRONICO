import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configuramos el servidor smtp

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'programaconmigo2201022@gmail.com' #colocamos el correo electronico que utilizaremos
smtp_password = 'kyqttzqxdgiesjzy' #aca colocamos la contraseña que generamos en la configuracion de nuestro correo .

#creamos cuerpo del mensaje

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'jarevaloagu@ucvvirtual.edu.pe' #el destinatario , el correo hacia donde vamos a enviar el mensaje
msg['Subject'] = 'Prueba de mensaje' # el titulo del correo
body = 'Hola mundo' # aca es el cuerpo del mensaje

msg.attach(MIMEText(body, 'plain'))

#ENVIO DE CORREO

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(smtp_username, msg['To'], msg.as_string())
server.quit()