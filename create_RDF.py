import csv

with open('Weekly_programme.csv', 'r', newline = '') as ifp, open('Trinities.csv', 'w', newline = '') as ofp:
								#h vivliothiki tha xeiristei moni tis to newline, to with frontizei na kleisi to arxeio
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)			        #to "csv.reader() pairnei ki alles parametrous
	headers = next(reader)
	print(headers)
	for i, row in enumerate(reader):			#oles i grammes ektos tis prwtis, giati thn prwti tin "travixame" hdh me ta headers
		for j, header in enumerate(headers):            #twra tha ftiaxoume "trinities" apo (id-header stilis-value) gia oles tis grammes-stiles
			writer.writerow([i+1, header, row[j]])	#print (i+1, header, row[headers.index(header)]), xwris "j" kai "enumerate"


with open('Trinities.csv', 'r', newline = '') as ifp, open('prefix_Trinities.csv', 'w', newline = '') as ofp:

	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for s,p,o in reader:									#Διάβασμα Trinities.CSV και προσθήκη  (id = "b", object = "l" ή "u")
		s  = "b:" + s
		if p == 'Day' or p == 'Start time' or p == 'End time':
			o  =  "l:" + o
		else:
			o = "u:" + o
		writer.writerow([s,p,o])


with open('prefix_Trinities.csv', 'r', newline = '') as ifp, open('URIs_Trinities.csv', 'w', newline = '') as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	convertions = {" ": "%20"}
	for s,p,o in reader:
		for special_char, conv in convertions.items():
			p = 'http://host/sw//myvocab#' + p.replace(special_char, conv)
		if o[0] == 'u':
			o = 'http://host/sw/you/resource/' + o.replace(" ", "%20")[2:]
		writer.writerow([s,p,o])

			#o = 'http://host/sw/you/resource/'
						#Μετατροπή των o pou einai "u" se URI 'http://host/sw/you/resource/' (%20=space kai otidipote allo den epitrepetai)

								# s='u: .....' s[2:]
								#Replace predicate (mesea stili) me http://host/sw/you/myvocab#


#prosthetei 0 stis monopsifies ores, pairnontas os eisodo ena string tis morfis hh:mm:ss
# p.x 9:10:00 ===> 09:10:00
# 09:10:00 ===> 09:10:00
def hour_format(time):
	hour = time.split(":")[0]
	if len(hour) == 1:
		return "0{time}".format(time=time)
	return time


with open('URIs_Trinities.csv', 'r', newline = '') as ifp:
	reader = csv.reader(ifp)
	for s,p,o in reader:
		s = s[2:]        # gia na emfanizetai to "b:"
		s = '_:' + s
		p = '<{uri}>'.format(uri=p)          # p = '<' + p + '>' ( the "easy way")
		if o[0] == 'l':
			o = o[2:]  #gia na min emfanizetai to "l:"
			if ':' in o:
				o = hour_format(o)
				#ftiaxtike i sinartisi hour_format
				#hour = o.split(":")[0]
				#if len(hour) == 1:
					#o = "0{o}".format(o=o)
				o = o + ":00"   # to prosthetoume gt to format einai 'hh:mm:ss'
				o = '"{literal}"'.format(literal = o)
				o = o +  '^^<http://www.w3.org/2001/XMLSchema#time>'
			else:
				o = '"{literal}"'.format(literal = o)
		else:
			o = '<{uri}>'.format(uri=o)
		print('{s} {p} {o} .'.format(s=s,p=p,o=o))






									#p = <> , o = literal ή URI , s = blank node
									# riot --validate .nt
