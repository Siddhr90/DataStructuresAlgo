class TrieNode:
    def __init__(self):
        self.children = {}                              # we are using dictionary because we want to connect children to children
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)             # gets value of key, None if not present
            if node is None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")

    def searchString(self,word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)                      # returns the value which is a Trienode
            if node is None:
                return False
            currentNode = node

        if currentNode.endOfString is True:
            return True
        else:
            return False                                   # just a prefix in this case

def deleteString(root, word, index):                       # Not that this function is outside the class
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    # case 1 : has a common prefix with another worddue
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)        # node cannot be deleted so we move on to next node
        return False
    # case 2: we are at the last char of this word
    if index == len(word) - 1:
        # but this word is a prefix of some other word
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        # if there is no other node (this word is not prefix of another node)and only EOS is True , we remove that node
        else:
            root.children.pop(ch)
            return True                 # we are okay to delete that node

    # case 3 : some other word is a prefix of this node
    if currentNode.endOfString is True:
        deleteString(currentNode, word, index+1)
        return False

    # case of a normal node
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted is True:
        root.children.pop(ch)
        return True
    else:
        return False






newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")                # O(m) Time and Space C, where m is length of word
#newTrie.insertString("App")
#print(newTrie.searchString('App'))          # O(m) Time and O(1) space C
#print(newTrie.searchString('Ap'))
deleteString(newTrie.root,"App", 0)
print(newTrie.searchString("App"))
