from notebook import Note, Notebook

def display_notes(notes):
	for note in notes:
		print("Id: %d" %(note.id))
		print("Memo: %s" %(note.memo))
		print("------------------------------------------")

n = Notebook()
n.new_note("hello world")
n.new_note("hello again")
print(n.notes)
display_notes(n.notes)

print("********************************************")
print("search keyword: hello")
search_notes = n.search("hello")
display_notes(search_notes)
print("********************************************")

print("********************************************")
print("search keyword: world")
search_notes = n.search("world")
display_notes(search_notes)
print("********************************************")

print("********************************************")
print("search keyword: 1")
search_notes = n.search("1")
display_notes(search_notes)
print("********************************************")

print("********************************************")
print("after modify note 1:")
n.modify_memo(1, "Hi Master HaKu")
display_notes(n.notes)
print("********************************************")



