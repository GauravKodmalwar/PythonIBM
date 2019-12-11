import re

txt = "Python training today at DF944734 wwet 7574 AM"
p = re.compile('[0-9].?')
print(p.findall(txt))

print(re.match(r'[0-9].?', txt))

p1 = re.compile('[A-Z][a-z]* ')
print(p1.findall("Python training today at DF944734 wwet 7574 AM"))

p2 = re.compile('91[0-9]{8} ')
print(p2.findall("""91576782 9191576782 9157678298 Python 989 
915767820
"""))

p3 = re.compile('^[0-9]*[A-z]*')
print(p3.findall("""67Python training today at D944734 wwet 7574 AM
8301DDF followed by
asdfasdf asdfas 
asdfasdfa asdfadfas asdfdasfas
asdfasdfasfasd"""))

help(re.match)

print(re.findall("$.com", "gauravsdfd.com python@ibm.com"))