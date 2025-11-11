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

      tmp  = self.head # listenin ilk elemanı (başı)

      while tmp.sonraki is not None: # bu düğümden sonra düğüm yok; bu, sonuncu!
        tmp = tmp.sonraki

      tmp.sonraki = yeni_dugum # tmp son elemadır. yeni düğümü sonraki olarak ata.

  def gez(self,):
        tmp  = self.head # listenin ilke elemanı (başı)
        while tmp is not None: # bu düğümden sonra düğüm yok; bu, sonuncu!
          print(tmp.veri)
          tmp = tmp.sonraki

  def araya_ekle(self, aranan_veri, dugum_verisi ): # belirli bir veriye sahip düğümün ardına ekle
    aktif_dugum = self.head

    while aktif_dugum is not None:
      if aktif_dugum.veri == aranan_veri: # aranan düğüm bulundu
        # araya yeni düğümü ekle
        yeni_dugum = self._Node(dugum_verisi)
        yeni_dugum.sonraki = aktif_dugum.sonraki
        aktif_dugum.sonraki = yeni_dugum
        break

      aktif_dugum = aktif_dugum.sonraki # sonraki düğüme geç
  def sil(self, veri):
    tmp = self.head
    onceki = None

    while tmp is not None:
        if tmp.veri == veri:
            if onceki is None:  # silinecek düğüm baştaysa
                self.head = tmp.sonraki
            else:
                onceki.sonraki = tmp.sonraki
            return True  # silme başarılı
        onceki = tmp
        tmp = tmp.sonraki
    return False  # veri bulunamadı


