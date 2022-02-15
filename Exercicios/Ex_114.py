from ping3 import ping
import urllib
import urllib.request

#Minha forma
#a = ping('www.pudim.com.br')
#print('='*30)
#if a == False:
#    print('\033[31mNão é possivel acessar o site\033[m')
#else:
#    print('\033[33mÉ possível acessar o site\033[m')
#print('='*30)

#Forma Guanabara

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o site Pudim!\033[m')
else:
    print('\033[32mO site Pudim está online!')
    #print(site.read())
