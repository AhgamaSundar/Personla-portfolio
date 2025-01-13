import smtplib,ssl
\

def send_mail(msg):
    
    host="smtp.gmail.com"
    port=465

    username="ahgamanatesan@gmail.com"
    password="vvjefocxkhzjtnrb"

    receiver="ahgamasundar40@gmail.com"
    context= ssl.create_default_context()
   
    with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,msg)
    