# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer 

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('10.30.40.33', 8009), 
                        requestHandler=RequestHandler) as server:    
    server.register_introspection_functions()
    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    dictionary = {
        'kandidat_1': 0,
        'kandidat_2': 0
    }
   
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):
        
        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
        if dictionary.get(x) != None:
            dictionary[x] = dictionary[x] + 1
            message = "Anda telah memilih" + x
            lock.release()
            return message
        else:
            lock.release()
            message = "Anda memilih kandidat yang tidak tersedia di Dictionary"
            return message

        # critical section berakhir, harus diunlock
        lock.release()
    
    # register fungsi vote_candidate() sebagai vote
    server.register_function(vote_candidate, 'vote')

    # buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        total_vote = 0
        for i in dictionary:
            total_vote = total_vote + dictionary[i]
        if total_vote == 0:
            lock.release()
            return "Yang anda pilih tidak terdaftar"
        
        # hitung hasil persentase masing-masing kandidat
        persentase = []
        message = ""
        for i in dictionary:
            hasil = (dictionary[i] / total_vote) * 100
            message = message + i + " " + "memperoleh" + " " + str(hasil) + "%\n"
        # critical section berakhir
        lock.release()    
        return message
        
    # register querry_result sebagai querry
    server.register_function(querry_result, 'querry')

    print ("Server voting berjalan...")
    # Jalankan server
    server.serve_forever()
