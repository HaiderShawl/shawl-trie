from pymongo import MongoClient


# connecting to Mongo Atlas database
client_db = MongoClient('mongodb+srv://user:user@cluster0.hmyig.mongodb.net/data?retryWrites=true&w=majority')
db = client_db.data.trie


# class to create new nodes for the trie
class createNode:
	def __init__(self):
		self.node = {}


# class to add, search, delete, display and autocomplete words in trie
class trieClass:
	def __init__(self):
		# getting the trie from the database
		self.root = db.find_one({ 'name':'trie' })['data']

		# self.root = {'a': {'p': {'p': {'l': {'e': {'*': True}, 'i': {'c': {'a': {'t': {'i': {'o': {'n': {'*': True}}}}}}}, 'o': {'o': {'*':True}}}, '*': True}}, 'c': {'a': {'a': {'*': True}}}}, 'b': {'a': {'t': {'h': {'*': True}}}}}


	def add(self, text):
		# creating objects with the word letters as their keys
		# eg. {'a': {'p': {'p': {'*': True}}}}
		# '*' denotes end of word

		keys = [c for c in text]
		length = len(keys)
		trieNode = self.root

		for i in range(0, length):
			if not keys[i] in trieNode:
				trieNode[keys[i]] = createNode().node

			trieNode = trieNode[keys[i]]
		
		trieNode['*'] = True

		return self.root


	def search (self, text):
		# searching for a word by checking each letter one by one

		keys = [c for c in text]
		length = len(keys)
		trieNode = self.root
		nodes = []

		for i in range(0, length):
			if not keys[i] in trieNode:
				return False, nodes

			trieNode = trieNode[keys[i]]
			nodes.append(trieNode)


		if not '*' in trieNode:
			return False, nodes
		
		return True, nodes


	def autocomplete(self,prefix):
		# checking if some words have the provided prefix and sending them to the look function

		keys = [c for c in prefix]
		length = len(keys)
		trieNode = self.root

		self.suggestions = []

		
		for i in range(0, length):
			if not keys[i] in trieNode:
				return "No keyword with provided prefix was found"
			trieNode = trieNode[keys[i]]


		# looking for words with provided prefix
		self.look(trieNode, prefix)

		return self.suggestions


	def look(self, obj, word):
		# taking the nodes and prefix and returning complete words
		keys = obj.keys()
		for key in keys:
			if key == '*':
				self.suggestions.append(word)

			else:
				self.look(obj[key], word+key)


	def delete(self, text):
		# removing the '*' at the end of the word if it exists in the trie

		search, nodes = self.search(text)
		if search:
			nodes.reverse()

			del nodes[0]['*']

			for node in nodes:
				if len(node) > 0:
					break
			
			print('Word deleted successfully!')

		else:
			print('The provided word does not exist in the trie.')


	def display(self, obj, level=0) :
		# displaying all words in the trie
		print(self.autocomplete(''))


	def save(self) :
		# saving the trie to the database
		db.update_one({
			'name': 'trie'
		}, {
			"$set": { 'data': self.root }
		})
