from abc import abstractmethod

class AbstractWord:
    def __init__(self, textFile):
        self.textFile = textFile

    @abstractmethod
    def alphabet_filter(self):
        pass

    @abstractmethod
    def create_lexicon(self):
        pass

    @abstractmethod
    def sorting_algorithm(self):
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

    def create_lexicon(self):
      f = open(self.fileName, "r")
      result=set((self.alphabet_filter(f.read())))
      f.close()
      return(result)

    def read_data(self):
      lexicon = []
      for i in Word.create_lexicon(self):
          lexicon.append(i)
      return lexicon
    
# Write your build_lexicon() solution here (and any other functions as you see fit)

def merge_sort(lst, first, last):
    if first == last:
        return

    mid = (first + last) // 2
    merge_sort(lst, first, mid)
    merge_sort(lst, mid + 1, last)

    merge(lst, first, mid, last)
    return lst

def merge(lst, left, mid, right):

    temp = []


    left_idx = left
    right_idx = mid + 1


    while left_idx <= mid and right_idx <= right:
        if lst[left_idx] <= lst[right_idx]:
            temp.append(lst[left_idx])
            left_idx += 1
        else:
            temp.append(lst[right_idx])
            right_idx += 1


    while left_idx <= mid:
        temp.append(lst[left_idx])
        left_idx += 1
    while right_idx <= right:
        temp.append(lst[right_idx])
        right_idx += 1


    for idx in range(left, right + 1):
        lst[idx] = temp[idx - left]

class Sort(Word):
  def sorting_algorithm(w):
          first=0
          last=len(w) - 1
          lst = []
          lst = merge_sort(w, first, last)
          print("Sorting with Merge Sort")
          return lst

# Write your add_neighbours() function here
class NeightbourWord(Word):
  def add_neighbours(l):
      results = []

      for i in l:
          neightbour_word=[]
          for j in l:
              same_chars=0
              founds = []
              for k in i:
                  found = j.find(k)
                  if(found>=0):
                      founds.append(found)
                      same_chars=same_chars+1
              if(same_chars>=2 and len(j)==len(i) and founds[0]-founds[1]<0):
                  neightbour_word.append(j)
          results.append(neightbour_word)
      return results

  # Call your add_neighbours() function with your lexicon
  def read_data(self):
      lexicons = Word.create_lexicon(self)
      neighbours = NeightbourWord.add_neighbours(lexicons)
      return neighbours
obj = NeightbourWord("in.txt")
print(obj.read_data())
