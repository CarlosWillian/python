import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.kupongo.com.br')
    print('\033[32mConectado ao site Kupon Go com sucesso!\033[m')
    print(site.read())
except:
    print('\033[31mNão foi possível acessar o site Kupon Go\033[m')

