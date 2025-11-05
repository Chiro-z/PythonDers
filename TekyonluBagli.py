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
    else: # listede en az bir eleman var
      self.head.sonraki = yeni_dugum


