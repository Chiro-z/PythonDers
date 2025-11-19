#@title Sabit Dizi Üzerinde Yığın Uygulaması
class DizideYigin():# Sabit Dizi üzerinde Yığın yapısı

  def __init__(self, kapasite):
    self.kapasite = kapasite
    self.top = -1 # en üstteki veri (eleman) indeksi; -1 => boş
    self.yigin = [None] * self.kapasite # dizi

  def isFull(self, ): # dolu ise True
    if self.top >= self.kapasite -1 :
        return True
    return False

  def isEmpty(self,):
      if self.top == -1: # veri yok
        return True
      return False

  def push(self, veri): # veriyi sona ekle
    # yığın dolu mu?
    if self.isFull():
      print("Yığın dolu!")
    else: # yığında hâlâ yer var
      self.top += 1
      self.yigin[self.top] = veri
      print("Veri yığına eklendi")

  def pop(self):
      if self.isEmpty():
        print("Yığında veri yok!")
        return None
      else:
        tmp = self.yigin[self.top]
        self.yigin[self.top] = None
        self.top -= 1
        return tmp
