from pymongo import MongoClient

client_db = MongoClient('mongodb+srv://user:user@cluster0.hmyig.mongodb.net/data?retryWrites=true&w=majority')
db = client_db.data.trie


class createNode:
	def __init__(self):
		self.node = {}

class trie:
	def __init__(self):
		self.root = db.find_one({ 'name':'trie' })['data']
		# self.root = {'a': {'p': {'p': {'l': {'e': {'*': True}, 'i': {'c': {'a': {'t': {'i': {'o': {'n': {'*': True}}}}}}}, 'o': {'o': {'*':True}}}, '*': True}}, 'c': {'a': {'a': {'*': True}}}}, 'b': {'a': {'t': {'h': {'*': True}}}}}

		
	def add(self, text):
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
		keys = [c for c in prefix]
		length = len(keys)
		trieNode = self.root

		self.suggestions = []

		
		# checking if prefix exists in our trie
		for i in range(0, length):
			if not keys[i] in trieNode:
				return "No keyword with provided prefix was found"
			trieNode = trieNode[keys[i]]


		# looking for suggestions
		self.look(trieNode, prefix)

		return self.suggestions


	def look(self, obj, word):
		keys = obj.keys()
		for key in keys:
			if key == '*':
				self.suggestions.append(word)

			else:
				self.look(obj[key], word+key)


	def delete(self, text):
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


	def display(self, obj, prefix='') :
		keys = obj.keys()
		for key in keys:
			if key != '*':
				print(key, end=" ")
				self.display(obj[key], prefix+'  ')
			else: 
				print("")
				# prefix = prefix + " "
				print(prefix, end="")

				
				


trie = trie()

msg = input('Enter task (add, search, autocomplete, delete, display): ')

if msg == 'add':
	text = input('Type word to add: ')
	trie.add(text)
	print('Word has been added successfully!')

elif msg == 'search':
	text = input('Type word to search: ')
	print(trie.search(text)[0])

elif msg == 'autocomplete':
	text = input('Type prefix to autocomplete: ')
	print(trie.autocomplete(text))

elif msg == 'delete':
	text = input('Type word to delete: ')
	trie.delete(text)

elif msg == 'display':
	trie.prefix=''
	trie.display(trie.root)

else:
	print('Invalid task. Try Again')



# db.update_one({
# 	'name': 'trie'
# }, {
# 	"$set": { 'data': trie.root }
# })


