# Pergunta 5
strg = input("Digite a String desejada: ")
invertido = ""
for i in range(len(strg)-1, -1, -1):
    invertido += strg[i]
print(invertido)
