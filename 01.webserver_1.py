# import library socket karena akan digunakan request reply protocol sederhana
import socket

# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80
ip = '10.30.40.33'
port = 80

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding 
s.bind((ip, port))

# socket mendengarkan
s.listen(5)

# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"
print('Server berjalan dan melayani HTTP pada port 80')

# loop forever
while True:
    # socket menerima koneksi
    c, addr = s.accept()
    
    # socket menerima data
    data = c.recv(1024)
    
    # print data hasil koneksi
    print(data.decode())
    
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
    http_response = """\HTTP/1.1 200 OK

<html>
<head>
<title>Web Server Sederhana</title>
</head>
<body>
<center>
<h>Heading 1</h1>
<p>Ini adalah contoh paragraf.</p>
<img src="https://www.surfertoday.com/images/stories/surfetiquette.jpg">
</center>
</body>
</html>
"""
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8 
    c.sendall(http_response.encode('utf-8'))
    # tutup koneksi
    c.close()

# Selamat! Kamu telah berhasil membuat web server sederhana. 
