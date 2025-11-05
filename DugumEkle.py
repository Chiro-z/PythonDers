# Tek Yönlü Bağlı Liste Sınıfı
class TYListe():

  class _Node(): # liste düğümü
    """Öğe sınıfı"""
    def __init__(self, data):
      self.veri = data
      self.sonraki = None

  def __init__(self,): # başlangıç ayarları
    self.head = None # head listenin ilk elemanı; yani listenin kendisi

  def dugum_ekle(self, veri ):
    yeni_dugum = self._Node(veri) # yeni düğüm

    if self.head is None: # liste boş
      self.head = yeni_dugum # yeni_dugum listenin ilk elemanı
    else: # listede en az bir eleman var. önce sonuncu elemanı bul.
    # sonra ekleme yap (son elemana yeni düğümü bağla)

      tmp  = self.head # listenin ilke elemanı (başı)

      while tmp.sonraki is not None: # bu düğümden sonra düğüm yok; bu, sonuncu!
        tmp = tmp.sonraki

      tmp.sonraki = yeni_dugum # tmp son elemadır. yeni düğümü sonraki olarak ata.

  def gez(self,):
        tmp  = self.head # listenin ilke elemanı (başı)

        while tmp is not None: # bu düğümden sonra düğüm yok; bu, sonuncu!
          print(tmp.veri)
          tmp = tmp.sonraki


def araya_ekle(self, veri, konum):
    yeni_dugum = self._Node(veri)

    if konum == 0:
        yeni_dugum.sonraki = self.head
        self.head = yeni_dugum
        return

    aktif_dugum = self.head
    indeks = 0

    while aktif_dugum is not None and indeks < konum - 1:
        aktif_dugum = aktif_dugum.sonraki
        indeks += 1

    if aktif_dugum is None:
        print("Konum listenin dışında!")
        return

    yeni_dugum.sonraki = aktif_dugum.sonraki
    aktif_dugum.sonraki = yeni_dugum
