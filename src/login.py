#!/usr/bin/python3
import cgi
import cgitb
import mysql.connector

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
        cur = con.cursor()

        cur.execute("SELECT id FROM users WHERE email = %s AND password = %s", (email, password))
        usuario_id = cur.fetchone()

        if usuario_id:
            cur.execute("SELECT nombre, img, precio FROM lugares WHERE usuario_id = %s", (usuario_id[0],))
            lugares = cur.fetchall()

            if lugares:
                print("Content-Type: text/html\n")
                print("<html><body>")
                print("<h1>Panel de control de {}</h1>".format(email))
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()

                print("<ul>")
                for user in users:
                    print("<li>")
                    print("ID: {}, Nombre: {}, Email: {}, Rol : {}".format(user[0], user[1], user[2], user[3]))
                    print("</li>")
                print("</ul>")

                print("<div style='width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; flex-direction: column;'>")
                for lugar in lugares:
                    print("<h2>Nombre: {}</h2>".format(lugar[0]))
                    print("<img src='{}' style='width: 500px '>".format(lugar[1]))
                    print("<h3>Precio: {}</h3>".format(lugar[2]))
                print("</div>")
                print("</body></html>")
            else:
                print("Content-Type: text/html\n")
                print("<html><body>")
                print("<div style='width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; flex-direction: column;'>")
                print("<img src='https://i.pinimg.com/originals/3e/80/39/3e8039242e517ee7edc05a4e226e0b80.gif'>")
                print("<h2>No tienes ningun viaje ¡Vamos a añadirlos !</h2>")
                print("</div>")
                print('<meta http-equiv="refresh" content="2;url=/add_lugar.html" />')
                print("</body></html>")
        else:
            print("Content-Type: text/html\n")
            print("<html><body>")
            print("<div style='width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; flex-direction: column;'>")
            print("<img src='https://i.pinimg.com/originals/3e/80/39/3e8039242e517ee7edc05a4e226e0b80.gif'>")
            print("<h3>Validando credenciales...</h2>")
            print("</div>")
            print('<meta http-equiv="refresh" content="1;url=/login.html" />')
            print("</body></html>")

        cur.close()
        con.close()

except Exception as e:
    print("Content-Type: text/html\n")
    print("<html><body>")
    print("Error:", e)
    print("</body></html>")

