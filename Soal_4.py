class Buwahhhh:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

class Mangga(Buwahhhh):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

mangga_aromanis = Mangga("Mangga Aromanis", "kuning", "manis", ["A", "C"])
print(mangga_aromanis.nama)
print(mangga_aromanis.warna)
print(mangga_aromanis.rasa)
print(mangga_aromanis.vitamin)
