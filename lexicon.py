from abc import abstractmethod

class AbstractWord:
    def __init__(self, textFile):
        self.textFile = textFile

    @abstractmethod
    def alphabet_filter(self):
        pass

    @abstractmethod
    def one_letter_diff(self):
       pass

    @abstractmethod
    def create_lexicon(self):
        pass

    @abstractmethod
    def add_neighbours(self):
      pass

    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def read_data(self):
      pass


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class AVLTree(AbstractWord):
    def __init__(self):
        self.root = None
        self.nodes = []
    def traverse_in_order(self, node='root'):
        if node == 'root':
            node = self.root
        if node is not None:
            self.traverse_in_order(node.left)
            self.traverse_in_order(node.right)
            self.nodes.append(node.data)
        return self.nodes
    def insert(self, data):
        new_node = AVLNode(data)
        if self.root is None:
            self.root = new_node
            return

        p = self.root

        while True:
            if data <= p.data and p.left is not None:
                p = p.left
            elif data > p.data and p.right is not None:
                p = p.right
            else:
                break

        if data <= p.data:
            p.left = new_node
        else:
            p.right = new_node

        # self.rebalance_insertion_path(new_node)

class Word(AbstractWord):
    def __init__(self, fileName):
        self.fileName = fileName

    def alphabet_filter(self,my_str):
      # Remove all punctuation and numeric characters
      result = set()
      words = my_str.split()
      alphabetWord = ' '.join([w for w in words if w.isalpha()])
      alphabetWords = alphabetWord.split()
      for i in alphabetWords:
          result.add(i.lower())
      return result

    def create_lexicon(self, tree  = AVLTree()):
      f = open(self.fileName, "r")
      results=set((self.alphabet_filter(f.read())))
      for i in results:
        tree.insert(i)
      f.close()

# Write your add_neighbours() function here
class NeightbourWord(Word):
  
  def one_letter_diff(word1, word2):
    if len(word1) != len(word2):
        return False

    diff_count = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff_count += 1
            if diff_count > 1:
                return False

    return diff_count == 1
  
  def add_neighbours(l):
      results = []
      for i in l:
          neightbour_word=[]
          for j in l:
              if(NeightbourWord.one_letter_diff(i,j)):
                if(len(j)>0):
                    neightbour_word.append(j)
          results.append(neightbour_word)
      return results

  # Call your add_neighbours() function with your lexicon
  def read_data(self):
      tree = AVLTree()
      Word.create_lexicon(self, tree)
      rs = tree.traverse_in_order()
    #   neighbours = NeightbourWord.add_neighbours(rs)
      return rs
obj = NeightbourWord("in.txt")
print(obj.read_data())
