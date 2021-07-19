from .cli import trie
from .cli import createNode
from pymongo import MongoClient

client_db = MongoClient('mongodb+srv://user:user@cluster0.hmyig.mongodb.net/data?retryWrites=true&w=majority')
db = client_db.data.trie



if __name__ == '__main__':
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