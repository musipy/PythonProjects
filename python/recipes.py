from database2 import Simpledb
db = Simpledb('recipes.txt')
db.insert('relish', 'Pickled cucumber and sugar')
db.insert('pesto', 'Basil and olive oil')
db.select_one('pesto')
db.delete('pesto')
db.modify('relish', 'Pickled cucumber and sugar AND OREGANO')

