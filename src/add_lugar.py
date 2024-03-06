#!/usr/bin/python3
import cgi
import cgitb
import mysql.connector

cgitb.enable()

form = cgi.FieldStorage()

nombre = form.getvalue('nombre')
img = form.getvalue('img')
precio = form.getvalue('precio')

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='exploreexpress'
    )

    if con.is_connected():
        cur = con.cursor()

        print("Content-Type: text/html\n")
        print("<!DOCTYPE html>")
        print("<html lang='en'>")
        print("<head>")
        print("    <meta charset='UTF-8'>")
        print("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
        print("    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'/>")
        print("    <script src='https://cdn.tailwindcss.com'></script>")
        print("    <title>Welcome</title>")
        print("</head>")
        print("<body>")
        print("<link rel='preconnect' href='https://fonts.googleapis.com' />")
        print("<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin />")
        print("<link href='https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;1,100;1,200&display=swap' rel='stylesheet' />")
        print("<style>")
        print("    * {")
        print("        font-family: 'Poppins', sans-serif;")
        print("    }")
        print("</style>")
        print("<main class='flex flex-col items-center justify-center mt-32'>")
        print("<header class='container'>")
        print("    <nav class='flex justify-between md:justify-around py-4 bg-white/80 backdrop-blur-md shadow-md w-full px-10 fixed top-0 left-0 right-0 z-10 px-8 md:px-3'>")
        print("        <div class='flex items-center'>")
        print("            <a class='cursor-pointer'>")
        print("                <h3 class='text-2xl font-medium text-blue-500'>")
        print("                    <img class='h-10 scale-[1.5] ml-[1em]' src='https://png.pngtree.com/png-clipart/20230810/original/pngtree-minimalist-mountain-logo-for-outdoor-adventures-and-landscape-design-vector-picture-image_10243625.png' alt='Store Logo' />")
        print("                </h3>")
        print("            </a>")
        print("        </div>")
        print("        <div class='items-center md:space-x-8 justify-center justify-items-center md:justify-items-center md:flex md:pt-2 w-full left-0 top-16 px-5 md:px-10 py-3 md:py-0 border-t md:border-t-0'>")
        print("            <a class='flex text-gray-600 hover:text-[#FF9E00] cursor-pointer transition-colors duration-300'>Inicio</a>")
        print("            <a class='flex text-gray-600 cursor-pointer transition-colors duration-300 hover:text-[#FF9E00] '>Viajes</a>")
        print("            <a class='flex text-gray-600 hover:text-[#FF9E00] cursor-pointer transition-colors duration-300'>Precios</a>")
        print("            <a class='flex text-gray-600 hover:text-[#FF9E00] cursor-pointer transition-colors duration-300'>Sobre Nosotros</a>")
        print("        </div>")
        print("        <div class='flex items-center space-x-5 hidden md:flex'>")
        print("            <a class='flex text-gray-600 hover:text-[#FF9E00] cursor-pointer transition-colors duration-300 font-semibold text-blue-600' href='http://localhost/index.html'>")
        print("                <svg class='fill-current h-5 w-5 mr-2 mt-0.5' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' width='24' height='24' viewBox='0 0 24 24'>")
        print("                    <path d='M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z' />")
        print("                </svg>")
        print("                Salir")
        print("            </a>")
        print("        </div>")
        print("        <button class='w-10 h-10 md:hidden justify-self-end rounded-full hover:bg-gray-100'>")
        print("            <svg class='mx-auto' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' width='24' height='24' viewBox='0 0 24 24'>")
        print("                <path d='M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z' />")
        print("            </svg>")
        print("        </button>")
        print("    </nav>")
        print("</header>")
        

        cur.execute("INSERT INTO lugares (nombre, img, precio, usuario_id) VALUES (%s, %s, %s, 1)", (nombre, img, precio))
        con.commit()

        cur.execute("SELECT nombre, img, precio FROM lugares")
        lugares = cur.fetchall()
        
        for lugar in lugares:
            print("<div class='relative flex w-1/2 my-5 flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-md animate__animated animate__fadeInUp'>")
            print("    <div class='relative mx-4 mt-4 h-96 overflow-hidden rounded-xl bg-white bg-clip-border text-gray-700'>")
            print("        <img src='{}' class='h-full w-full object-cover' />".format(lugar[1]))
            print("    </div>")
            print("    <div class='p-6'>")
            print("        <div class='mb-2 flex items-center justify-between'>")
            print("            <p class='block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased'>{}</p>".format(lugar[0]))
            print("            <p class='block font-sans text-base font-medium leading-relaxed text-blue-gray-900 antialiased'>{}</p>".format(lugar[2]))
            print("        </div>")
            print("        <p class='block font-sans text-sm font-normal leading-normal text-gray-700 antialiased opacity-75'>With plenty of talk and listen time, voice-activated Siri access, and an available wireless charging case.</p>")
            print("    </div>")
            print("    <div class='p-6 pt-0'>")
            print("        <button class='block w-full select-none rounded-lg bg-blue-gray-900/10 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-blue-gray-900 transition-all hover:scale-105 focus:scale-105 focus:opacity-[0.85] active:scale-100 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none' type='button'>DELETE</button>")
            print("    </div>")
            print("</div>")
        
        print("</main>")
        print("<footer class='bg-gray-800 pt-10 sm:mt-10 pt-10 w-full'>")
        print("    <div class='pt-2'>")
        print("        <div class='flex pb-5 px-3 m-auto pt-5 border-t border-gray-500 text-gray-400 text-sm flex-col md:flex-row max-w-6xl'>")
        print("            <div class='mt-2'>© Copyright 1998-year. All Rights Reserved.</div>")
        print("        </div>")
        print("    </div>")
        print("</footer>")
        print("</body>")
        print("</html>")

except Exception as e:
    print("Content-Type: text/html\n")
    print("<html><body>")
    print("<h1>Error en la conexión SQL</h1>")
    print("<p>{}</p>".format(e))
    print("</body></html>")