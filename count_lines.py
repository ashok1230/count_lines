class reverse:
    def __init__(self,name):
	self.name=name
	fd=open(self.name,'r')
	txt=fd.read()
	fd.close()
        print txt
        lst = txt.splitlines()
	print len(lst)
reverse('details.txt')
