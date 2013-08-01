import sys,os,shelve

def store_person(db):
	pid=raw_input('«Î ‰»Îπ§∫≈:')
	person={}
	person['name']=raw_input('name:')
	person['age']=raw_input('age:')
	person['phone']=raw_input('phone:')
	db[pid]=person
def lookup_peerson(db):
	pid=raw_input('enter id number:')
	field=raw_input('what could you like konw?(name,age,phone)')
	field=field.strip().lower()
	print field.capitalize()+':',db[pid][field]
def print_help():
	print '-----the available commands are:--------'
	print 'store :store information about a person'
	print 'lookup:looks up a  person from id number'
	print 'quit  :save changes and exit'
	print '?     :print this message'
def enter_command():
	cmd=raw_input('enter command(? for help):')
	cmd=cmd.strip().lower()
	return cmd
def main():
	database=shelve.open('d:\\pyhtondb.dat')
	try:
		while True:
			cmd=enter_command()
			if cmd=='store':
				store_person(database)
			elif cmd=='lookup':
				lookup_peerson(database)
			elif cmd=='?':
				print_help()
			elif cmd=='quit':
				return
	finally:
		database.close()
if __name__=='__main__':
	main()
	
