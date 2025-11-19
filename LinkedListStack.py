class LinkedListStack:

    class _Node:  # liste düğümü
        def __init__(self, data):
            self.veri = data
            self.sonraki = None

    def __init__(self):
        self.head = None

    def push(self, veri):
        yeni_dugum = self._Node(veri)
        yeni_dugum.sonraki = self.head
        self.head = yeni_dugum

    def pop(self):
        if self.head is None:
            raise IndexError("Stack boş, pop() çağrılamaz.")
        veri = self.head.veri
        self.head = self.head.sonraki
        return veri

    def top(self):
        if self.head is None:
            raise IndexError("Stack boş, top() çağrılamaz.")
        return self.head.veri

    def isEmpty(self):
        return self.head is None
# Stack oluştur
stack = LinkedListStack()

# Eleman ekle
stack.push(10)
stack.push(20)
stack.push(30)

# En üstteki elemanı gör
print("Top:", stack.top())   # Çıktı: 30

# Eleman çıkar
print("Pop:", stack.pop())   # Çıktı: 30
print("Pop:", stack.pop())   # Çıktı: 20

# Stack boş mu?
print("Boş mu?", stack.isEmpty())  # False

# Son elemanı çıkar
print("Pop:", stack.pop())   # Çıktı: 10

# Şimdi boş
print("Boş mu?", stack.isEmpty())  # True
