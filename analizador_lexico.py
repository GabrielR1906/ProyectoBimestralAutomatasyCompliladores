import re

# Definiciones
PALABRAS_CLAVE = {
    "iniciar_proceso", "terminar_proceso", "definir", "decimal", "numero", "texto", "bandera",
    "durante", "findurante", "por", "paso", "desde", "hasta",
    "si", "sino", "sientonces", "finsi", "entonces",
    "enviar", "cierto", "falso"
}
OPERADORES = {":=", "==", "<=", ">=", "<", ">", "+", "-", "*", "/", "(", ")", "{", "}", "//"}
TOKEN_STRING = r"'[^']*'"
TOKEN_NUMBER = r'\d+(\.\d+)?'
TOKEN_IDENTIFICADOR = r'[a-zA-Z_]\w*'

def analizar_lexico(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    for num_linea, linea in enumerate(lineas, 1):
        # Patrón ajustado para reconocer números decimales completos primero
        tokens = re.findall(
            r"//.*|:=|==|<=|>=|\d+\.\d+|\d+|[(){}]|\w+|'.*?'|[<>+\-*/]", 
            linea
        )
        for token in tokens:
            if token.startswith("//"):
                print(f"Línea {num_linea}: Comentario ignorado")
                break
            elif token in PALABRAS_CLAVE:
                print(f"Línea {num_linea}: [✔] Palabra clave reconocida → '{token}'")
            elif token in OPERADORES:
                print(f"Línea {num_linea}: [✔] Operador reconocido → '{token}'")
            elif re.fullmatch(TOKEN_NUMBER, token):
                print(f"Línea {num_linea}: [✔] Número reconocido → '{token}'")
            elif re.fullmatch(TOKEN_STRING, token):
                print(f"Línea {num_linea}: [✔] Cadena de texto reconocida → {token}")
            elif re.fullmatch(TOKEN_IDENTIFICADOR, token):
                print(f"Línea {num_linea}: [✔] Identificador válido → '{token}'")
            else:
                print(f"Línea {num_linea}: [✘] Error léxico → '{token}'")

if __name__ == "__main__":
    analizar_lexico("programa.txt")
