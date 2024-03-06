#!/usr/bin/python3
import cgi, cgitb, mysql.connector

cgitb.enable()

form = cgi.FieldStorage()

email = form.getvalue('email')
password = form.getvalue('password')

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='exploreexpress'
    )

    if con.is_connected():
        print("Content-Type: text/html\n")
        print("<html><body>")

        cur = con.cursor()

        cur.execute("SELECT email FROM users WHERE email = %s", (email,))
        existing_email = cur.fetchone()

        if not existing_email:
            cur.execute("INSERT INTO users (email, password, rol) VALUES (%s, %s, 'user')", (email, password))
            con.commit()
            print("<div style='width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; flex-direction: column;'>")
            print("<img src='https://i.pinimg.com/originals/3e/80/39/3e8039242e517ee7edc05a4e226e0b80.gif'>")
            print("<h3>Registro exitoso. Redirigiendo a la pagina de viajes...</h2>")
            print("</div>")
            print('<meta http-equiv="refresh" content="2;url=/add_lugar.html" />')
            
        else:
            print("<div style='width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; flex-direction: column;'>")
            print("<img src='https://i.pinimg.com/originals/3e/80/39/3e8039242e517ee7edc05a4e226e0b80.gif'>")
            print("<h3>El correo electronico ya esta registrado. Redirigiendo a la pagina de inicio de sesion...</h2>")
            print("</div>")
            print('<meta http-equiv="refresh" content="2;url=/login.html" />')

        cur.close()
        con.close()

        print("</body></html>")

except Exception as e:
    print("Content-Type: text/html\n")
    print("<html><body>")
    print("<h1>Error en la conexión SQL</h1>")
    print("<p>{}</p>".format(e))
    print("</body></html>")
