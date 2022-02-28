import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('\033[31mO site do pudim não esta acessivel!\033[m')

else:
    print('\033[32mConsegui acessar o site do pudim\033[m')
