class DinamikBaslangicliKuyruk:
    def __init__(self, kapasite):
        self.kapasite = kapasite
        self.baslangic = 0
        self.boyut = 0
        self.kuyruk = [None] * self.kapasite
        self.tail = 0

        def enqueue(self, veri ):
            """tail, verinin yazılacağı aktif bellek indeksi"""
            self.kuyruk[self.tail] = veri
            if self.tail == self.kapasite:
            
