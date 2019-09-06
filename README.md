# iic2173-E0-base
Repositorio para la Entrega 0

Deben dejar sus servidores corriendo para ser revisados en cualquier momento, hasta que indiquemos que pueden bajarlos.

# Qué debe ir en el repo

* Configuración de nginx: nginx.conf y el contenido de la carpeta sites-enabled
* Código del servicio web
* Método de acceso al servidor. Después de la revisión podrán revocar los accesos que nos pasen. Esto puede ser:
  * Llave PEM
  * Llave con passphrase
  * Acceso vía usuario - password
  
# Qué debe ir aquí

* El nombre del dominio
* Instrucciones de uso
* Referencias a cualquier codigo que hayan usado de internet, a menos que estas se encuentren en el código

---
# [https://flo-chat.tk](https://flo-chat.tk)

# Instrucciones de uso
Esta es una aplicación en _flask_, montada en un servidor _AWS_ con _nginx_ y _gunicorn_. Para correr la aplicación en local se debe hacer `python wsgi.py`. Es necesario tener instalado Python 3.6+ y las dependencias indicadas en `requirements.txt`. Para el deploy se debe ingresar al servidor usando la clave `.pem`, entrar a la carpeta ubicada en `/home/ubuntu/chat-app` y hacer `git pull`. Después hay que reiniciar el servicio para que se actualicen los cambios. Esto se hace a través del comando `sudo systemctl restart chat-app`.

# Archivos Relevantes
En la carpeta `entrega` encontrarás los siguientes archivos:
- `arqui_de_sistemas.pem`: llave de acceso al servidor.
- `chat-app.service`: copia del archivo de configuración de _gunircorn_.
- `sites-enabled/default`: archivo default de _nginx_.
- `sites-enabled/flo-chat.tk`: archivo de _nginx_ del servidor que efectivamente estoy usando.

Los archivos `app.py`, `wsgi.py`, `message_form.py`, `templates/*` y `static/*` son los usados para el funcionamiento de la aplicación.

# Agradecimientos/Referencias
- [La que me ayudó a configurar gnuicorn](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)
- [Mi salvación de _ngnix_ y _aws_](https://shaneoneill.io/2018/10/21/setting-up-an-https-site-using-nodejs-aws-ec2-nginx-lets-encrypt-and-namecheap/)

Puedes escribir aqui ...