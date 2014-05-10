import sys
import codecs
import json

#get the file to convert
incoding = sys.argv[1]
outcoding = sys.argv[2]
infile = sys.argv[3]
outfile = sys.argv[4]

#get the conversion table
json_data = codecs.open('emoji_ios6.json',encoding='utf-8')
data = json.load(json_data)
json_data.close()

#get mapping for corrections
fixdict = {}
for line in data:
	if line[incoding] != "":
		fixdict[line[incoding]] = line[outcoding].decode('hex').decode('utf-8')

#convert
fin = codecs.open(infile,encoding='utf-8')
txt = fin.read()
final = u''
for c in txt:
	#check if c needs to be converted
	converted = c
	try:
		chex = ''.join(['{0:x}'.format(ord(x)) for x in unichr(int(repr(c)[4:-1], 16)).encode('utf-8')]).upper()
	except:
		chex = '0'
	if chex in fixdict:
		converted = fixdict[chex]
	final += converted

#write the output
fout = codecs.open(outfile, 'w', encoding='utf-8')
fout.write(final)
fout.close()



