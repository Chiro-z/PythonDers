# Kok once gez
class Dugum:
    def __init__(self, data):
        self.data = data
        self.sag = None
        self.sol = None

def kok_once_gez(kok):
    if kok is None:
        return
    print(kok.data, end=" ")
    kok_once_gez(kok.sol)
    kok_once_gez(kok.sag)

# Ağaç oluşturma
kok = Dugum(1)
kok.sol = Dugum(2)
kok.sag = Dugum(3)
kok.sol.sol = Dugum(4)
kok.sol.sag = Dugum(5)

# Traversal çağrısı
kok_once_gez(kok)
////////////////////////////////////////
class Node:
    def __init__(self, data):
        self.data = data
        self.sag = None
        self.sol = None

def inorderTraversal(root):
    if root is None:
        return
    print(kok.data, end=" ")
    # sol alt ağacı Özyineli gez
    inorderTraversal(root.left)
    # bu düğümün verisi
    print(root.data, end = "")
#     Sağ alt ağacı Özyineli gez
    inorderTraversal(root.right)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node 4
    root.left.right = Node (5)
    inorderTraversal(root)
  ///////////////////////////////////////
class Dugum:
    def __init__(self, data):
        self.data = data
        self.sag = None
        self.sol = None

def kok_sonra_gez(kok):
    if kok is None:
        return

    # sol alt ağacı Özyineli gez
    kok_sonra_gez(kok_sol)
#     Sağ alt ağacı Özyineli gez
    kok_sonra_gez(kok.sag)
    # Bu düğümün verisi
    print(kok.data,end= "")
    
    
    kok = Dugum(1)
    kok.sol = Dugum(2)
    kok.sag = Dugum(3)
    kok.sol.sol = Dugum(4)
    kok.sol.sag = Dugum (5)
    kok_sonra_gez(kok)

