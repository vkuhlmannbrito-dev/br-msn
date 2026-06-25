city=input("Digite o nome da sua cidade: ").strip()
first=city.split()
if city.find('Santo',) != -1 and first[0] == 'Santo':
    print("Santo")
else:print('Não tem Santo que salve sua cidade')
#semelhante
nome=input("Digite o seu nome: ")
if nome.find('Silva') != -1:
    print('Tu é br mesmo mermão')
else:
    print('Burguês safado')
#STR
nu=str(input("Digite seu nome: ")).strip()
print('silva' in nu.lower())