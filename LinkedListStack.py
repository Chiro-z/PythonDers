class LinkedListStack():

  class _Node(): # liste düğümü
    """Öğe sınıfı"""
    def __init__(self, data):
      self.veri = data
      self.sonraki = None

  def __init__(self, ):
    self.head = None


  def push(self, veri):
    yeni_dugum = self._Node(veri)
    yeni_dugum.sonraki = self.head
    self.head = yeni_dugum


