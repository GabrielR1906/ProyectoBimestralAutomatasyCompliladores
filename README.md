# ProyectoBimestralAutomatasyCompliladores
Proyecto Bimestral Analizador léxico en phyton



## 1. Introducción

Este proyecto implementa un **analizador léxico en Python** para un lenguaje de programación personalizado orientado a simulaciones espaciales.

El objetivo es leer archivos fuente escritos en este lenguaje, analizar sus componentes léxicos (tokens) e informar si cada palabra o símbolo es válido, mostrando mensajes de éxito o error.

---

## 2. Definición del Lenguaje

### 2.1 Estructura general

Un programa válido en este lenguaje debe comenzar con:

```plaintext
iniciar_proceso
```

y terminar con:

```plaintext
terminar_proceso
```

Entre estas instrucciones se encuentran declaraciones de variables, asignaciones, ciclos, condicionales y comandos para enviar mensajes.

---

### 2.2 Instrucciones reconocidas y sintaxis

| Instrucción                | Descripción                                                                          | Sintaxis / Ejemplo                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `iniciar_proceso`          | Indica el inicio del programa                                                        | `iniciar_proceso`                                                                             |
| `terminar_proceso`         | Indica el fin del programa                                                           | `terminar_proceso`                                                                            |
| `definir`                  | Declara una variable con un tipo                                                     | `definir <tipo> <nombre_variable>`                                                            |
| Tipos válidos              | `numero`, `decimal`, `texto`, `bandera`                                              | `definir numero vidas`                                                                        |
| Asignación                 | Asigna un valor a una variable                                                       | `<variable> := <valor>`                                                                       |
| Valores válidos            | Números enteros, decimales, texto en comillas simples, booleanos (`cierto`, `falso`) | `vidas := 5` <br> `energia := 87.6` <br> `mensaje := 'texto'` <br> `sistema_activo := cierto` |
| `enviar`                   | Envía o muestra un mensaje o variable                                                | `enviar mensaje` <br> `enviar 'Alerta'`                                                       |
| Ciclo `durante`            | Ejecuta instrucciones mientras condición sea cierta                                  | `durante (<condición>) { ... } findurante`                                                    |
| Ciclo `por`                | Ejecuta un ciclo con contador                                                        | `por (i desde 0 hasta 3 paso 1) { ... }`                                                      |
| Condicional `si`           | Ejecuta si la condición es cierta                                                    | `si <condición> entonces { ... }`                                                             |
| Condicional `sino`         | Parte alternativa del `si`                                                           | `sino { ... }`                                                                                |
| Condicional `sientonces`   | Otra alternativa condicional                                                         | `sientonces { ... }`                                                                          |
| Fin de condicional `finsi` | Indica fin de una estructura condicional                                             | `finsi`                                                                                       |

---

### 2.3 Ejemplo de programa válido

```plaintext
iniciar_proceso

// declaracion de variables
definir numero vidas
definir decimal energia
definir texto mensaje
definir bandera sistema_activo

// asignacion de valores iniciales
vidas := 5
energia := 87.6
mensaje := 'Inicializando simulación espacial...'
sistema_activo := cierto

// notificar estado inicial
enviar mensaje

// ciclo principal de chequeo
durante (sistema_activo == cierto) {
    si energia < 20.0 entonces {
        enviar '¡Advertencia! Energía crítica'
        sistema_activo := falso
    } sino {
        energia := energia - 5.0
        enviar 'Energía estable. Continuando...'
    }
    si vidas <= 0 entonces {
        enviar 'No hay vidas disponibles. Fin de la simulación.'
        sistema_activo := falso
    }
}
findurante

// ciclo de recuperación de vidas
por (vidas desde 0 hasta 3 paso 1) {
    enviar 'Recuperando vida...'
}

// decision final
si energia > 50.0 entonces {
    enviar 'Estado óptimo. Misión exitosa.'
} sientonces {
    enviar 'Revisión de misión requerida.'
}
finsi

terminar_proceso
```

---

## 3. Analizador Léxico en Python

El archivo `analizador_lexico.py` contiene el código que:

* Abre un archivo fuente (como el ejemplo `programa.txt`).
* Analiza cada línea, tokenizando por palabras, números, operadores, cadenas, comentarios, etc.
* Identifica y clasifica los tokens en: palabras clave, operadores, identificadores, números (enteros y decimales), cadenas de texto.
* Muestra mensajes de éxito o error para cada token.

### 3.1 Código principal (resumen)

```python
import re

PALABRAS_CLAVE = {...}  # conjunto de palabras clave
OPERADORES = {...}     # conjunto de operadores y símbolos
TOKEN_STRING = r"'[^']*'"
TOKEN_NUMBER = r'\d+(\.\d+)?'
TOKEN_IDENTIFICADOR = r'[a-zA-Z_]\w*'

def analizar_lexico(nombre_archivo):
    # lectura línea por línea y tokenización con regex
    # clasificación y mensajes de salida

if __name__ == "__main__":
    analizar_lexico("programa.txt")
```

*El código completo está en el archivo `analizador_lexico.py`.*

---

## 4. Autómata Gráfico

![Autómata gráfico](Automata%20graficado.jpg)

### 4.1 Explicación del autómata

* **Estado inicial**: Espera reconocer la primera palabra clave o identificador válido.
* **Estados intermedios**: Validan la formación correcta de tokens, operadores, números (enteros y decimales), cadenas de texto y comentarios.
* **Estados finales**: Se alcanzan cuando un token está completo y listo para clasificarlo o cuando se detecta un error léxico.

El autómata es fundamental para el reconocimiento correcto de los tokens que luego procesa el analizador léxico.

---

## 5. Uso y ejecución

1. Coloca el archivo `programa.txt` con el código fuente del programa a analizar en el mismo directorio que `analizador_lexico.py`.
2. Ejecuta el analizador:

   ```bash
   python analizador_lexico.py
   ```
3. Observa en consola la salida, que indicará para cada token si fue reconocido correctamente o si hay errores.
