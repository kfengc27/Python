from sys import argv

script,filename=argv

txt=open(filename)
promote='<'
print "Here's u file %r:"%filename

print txt.read()

print "Type the filename again:"
file_again=raw_input(promote)
txt_again=open(file_again)

print txt_again.read()










