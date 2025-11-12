class CYListe():
    class CYDugum():  # Çift Yönlü Düğüm
        def __init__(self, veri):
            self.veri = veri
            self.sonraki = None
            self.onceki = None

    def __init__(self):
        self.head = None

    def basa_ekle(self, veri):
        yeni = self.CYDugum(veri)
        if self.head is not None:
            self.head.onceki = yeni
            yeni.sonraki = self.head
        self.head = yeni

    def sona_ekle(self, veri):
        yeni = self.CYDugum(veri)
        if self.head is None:
            self.head = yeni
            return
        temp = self.head
        while temp.sonraki:
            temp = temp.sonraki
        temp.sonraki = yeni
        yeni.onceki = temp

    def araya_ekle(self, onceki_veri, veri):
        temp = self.head
        while temp and temp.veri != onceki_veri:
            temp = temp.sonraki
        if temp is None:
            print("Önceki düğüm bulunamadı.")
            return
        yeni = self.CYDugum(veri)
        yeni.sonraki = temp.sonraki
        yeni.onceki = temp
        if temp.sonraki:
            temp.sonraki.onceki = yeni
        temp.sonraki = yeni

    def bastan_sil(self):
        if self.head is None:
            return
        self.head = self.head.sonraki
        if self.head:
            self.head.onceki = None

    def sondan_sil(self):
        if self.head is None:
            return
        temp = self.head
        if temp.sonraki is None:
            self.head = None
            return
        while temp.sonraki:
            temp = temp.sonraki
        temp.onceki.sonraki = None

    def aradan_sil(self, veri):
        temp = self.head
        while temp and temp.veri != veri:
            temp = temp.sonraki
        if temp is None:
            print("Silinecek düğüm bulunamadı.")
            return
        if temp.onceki:
            temp.onceki.sonraki = temp.sonraki
        else:
            self.head = temp.sonraki
        if temp.sonraki:
            temp.sonraki.onceki = temp.onceki

    def yazdir(self):
        temp = self.head
        while temp:
            print(temp.veri, end=" <-> ")
            temp = temp.sonraki
        print("None")
