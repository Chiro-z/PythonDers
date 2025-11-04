class TYListe:
    class _Node:
        """Öğe Düğüm"""
        def __init__(self, veri):
            self.veri = veri
            self.sonraki = None

    def __init__(self):
        self.head = None  # Listenin ilk elemanı

    def dugum_ekle(self, veri):
        yeni_dugum = self._Node(veri)  # Yeni düğüm oluştur

        if self.head is None:
            self.head = yeni_dugum  # Liste boşsa, yeni düğüm baş olur
        else:
            tmp = self.head
            while tmp.sonraki is not None:
                tmp = tmp.sonraki  # Listenin sonuna kadar ilerle
            tmp.sonraki = yeni_dugum  # Son düğümün sonrakine yeni düğümü bağla

    def liste_gez(self):
        tmp = self.head
        index = 0
        while tmp is not None:
            print(f"{index}. düğüm:{tmp.veri}")
            tmp = tmp.sonraki
            index+=1
# TYListe sınıfını tanımladıktan sonra test etmek için:

# Liste nesnesi oluştur
liste = TYListe()

# Düğümler ekle
liste.dugum_ekle("Mehmet")
liste.dugum_ekle("Akin")
liste.dugum_ekle("Mahmut")

# Listeyi gez ve ekrana yazdır
liste.liste_gez()
