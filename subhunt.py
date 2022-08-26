import sys
import urllib.request
import urllib.parse
import re,os

os.system('clear')

print ("""
   _____       _     _    _             _   
  / ____|     | |   | |  | |           | |  
 | (___  _   _| |__ | |__| |_   _ _ __ | |_ 
  \___ \| | | | '_ \|  __  | | | | '_ \| __|
  ____) | |_| | |_) | |  | | |_| | | | | |_ 
 |_____/ \__,_|_.__/|_|  |_|\__,_|_| |_|\__|
                                            
          Tegal1337
python3 subhunt.py domain.com                                  
""")
print ("Scanning Subdomain For", sys.argv[1])

for i, arg in enumerate(sys.argv, 1):
	domains = set()
	with urllib.request.urlopen('https://crt.sh/?q=' + urllib.parse.quote('%.' + arg)) as r:
		code = r.read().decode('utf-8')
		for cert, domain in re.findall('<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(arg) + ')</td>(?:\s|\S)*?</tr>', code, re.IGNORECASE):
			domain = domain.split('@')[-1]
			if not domain in domains:
				domains.add(domain)
				print(domain)
