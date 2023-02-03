# Trie-tietorakenne, poikkeavuutena käänteinen järjestys
# TODO: suomenna loppuun saakka

class TrieSolmu:
    def __init__(self, lapset, päätesolmu, arvo, arvojakauma=None):
        self.lapset = lapset
        self.päätesolmu = päätesolmu
        self.arvo = arvo
        self.arvojakauma = arvojakauma

    def __repr__(self):
        return f"TrieSolmu({self.lapset.__repr__()}, {self.päätesolmu.__repr__()}, {self.arvo.__repr__()}, {self.arvojakauma})"

class Trie:
    def __init__(self, root=None, size=1):
        if root != None:
            self.root = root
        else:
            self.root = TrieSolmu({}, False, "")
        self.size = size
    
    def add(self, element, arvo, is_distribution=False):
        rev = element[::-1]
        current = self.root
        for i in range(len(element)):
            char = rev[i]
            if char in current.lapset.keys():
                current = current.lapset[char]
            else:
                current.lapset[char] = TrieSolmu({}, False, rev[:i+1])
                current = current.lapset[char]
                self.size += 1
        if is_distribution:
            current.arvojakauma = arvo
        else:
            if current.arvojakauma == None:
                current.arvojakauma = {}
            if not arvo in current.arvojakauma.keys():
                current.arvojakauma[arvo] = 0
            current.arvojakauma[arvo] += 1
        current.päätesolmu = True

    def compute_value_distributions(self):
        self.compute_value_distribution_at(self.root)
    
    def compute_value_distribution_at(self, node):
        if node.arvojakauma == None:
            node.arvojakauma = {}
        for child in node.lapset.values():
            self.compute_value_distribution_at(child)
        for child in node.lapset.values():
            for key in child.arvojakauma.keys():
                if not key in node.arvojakauma:
                    node.arvojakauma[key] = 0
                node.arvojakauma[key] += child.arvojakauma[key]
        
    def longest_common_prefix_node(self, element):
        rev = element[::-1]
        current = self.root
        broken = False
        best = None
        for char in rev:
            if char in current.lapset.keys():
                current = current.lapset[char]
            else:
                broken = True
                break
            if current.päätesolmu:
                best = current
        return (best, current)
    
    def lookup_by_longest_common_suffix(self, element, whole=True):
        
        best, current = self.longest_common_prefix_node(element)
        
        if whole:
            
            # Jos ei löydy kokonaista sanaa, palautetaan None
            
            if best == None:
                return None
            else:
                return best.arvo[::-1]
        else:
            
            # Seurataaan jotakin haaraa loppuun saakka
        
            while not current.päätesolmu:
                current = current.lapset[list(current.lapset.keys())[0]]
            return current.arvo[::-1]
    
    def value_distribution_for_longest_common_suffix(self, element):
        _, current = self.longest_common_prefix_node(element)
        return current.arvojakauma
    
    def deep_copy(self):
        other = Trie()
        def recursion(node):
            if node.päätesolmu:
                other.add(node.arvo[::-1], node.arvojakauma, True)
            for key in node.lapset.keys():
                recursion(node.lapset[key])
        recursion(self.root)
        return other

    def __repr__(self):
        return f"Trie({self.root}, {self.size})"
