# shawl-trie
A python package which allows you to add, delete, search, autocomplete and display words in a trie hosted on MongoDB

### Requirements


- Python 3.7
- Pymongo


### Setup

Run the following code in terminal (MacOS / Linux)
```  
pip3.7 install shawlTrie 
```


### Usage

Run the following code in terminal (MacOS / Linux)
```
$ python3.7 -m shawlTrie

>> Enter task (add, search, autocomplete, delete, display):

```

#### Actions:
- [add](#add)<br>
- [search](/#search)<br>
- [autocomplete](#autocomplete)<br>
- [delete](#delete)<br>
- [display](#display)<br>




#### add:
Adds a word to the trie

```
>> Enter task (add, search, autocomplete, delete, display): add

>> Type word to add: application

>> Word has been added successfully!
```

#### search:
Returns true if word exists in trie. Otherwise, returns false

```
>> Enter task (add, search, autocomplete, delete, display): add

>> Type word to search: application

>> True
```
#### autocomplete:
Returns a list of autocomplete suggestions

```
>> Enter task (add, search, autocomplete, delete, display): autocomplete

>> Type prefix to autocomplete: app

>> ['apple', 'application', 'app']
```


#### delete:
Deletes a word from the trie

```
>> Enter task (add, search, autocomplete, delete, display): delete

>> Type word to delete: application

>> Word deleted successfully!
```

#### display:
Displays all the words in the trie

```
>> Enter task (add, search, autocomplete, delete, display): display

>> ['apple', 'application', 'app', 'bath']

```



