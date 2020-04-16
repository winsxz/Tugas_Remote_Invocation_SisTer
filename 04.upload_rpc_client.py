# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
s = xmlrpc.client.ServerProxy('http://192.168.0.36:9999')

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    file = xmlrpc.client.Binary(handle.read())

# panggil fungsi untuk upload yang ada di server
s.file_upload(file)
