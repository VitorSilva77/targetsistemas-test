def inverter_string(s):
    # Inicializando uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Percorrendo a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida


# Testando a função com uma string previamente definida
string_original = "Vitor Silva"
string_invertida = inverter_string(string_original)

print(string_invertida)
