# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
proxy = xmlrpc.client.ServerProxy('http://192.168.0.36:8014')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
#print(proxy.vote("kandidat_1"))
print(proxy.vote("kandidat_2"))

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
print(proxy.querry())

# lakukan pemanggilan fungsi lain terserah Anda
