### Challenges ###

"""-- 1 --
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los números de 1 a 100
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            index = "fizzbuzz"
            print(index)
            continue
        elif index % 3 == 0:
            index = "fizz"
            print(index)
            continue
        elif index % 5 == 0:
            index = "buzz"
            print(index)
            continue
        else:
            print(index)
        
#fizzbuzz()

"""-- 2 --
¿ES UIN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return "son iguales. NO son un anagrama"
    elif sorted(first_word.lower()) == sorted(second_word.lower()):
        return f"{first_word} y {second_word} son un anagrama"
    elif sorted(first_word.lower()) != sorted(second_word.lower()):
        return "NO son un anagrama"

#print(is_anagram("roma", "amor"))

"""-- 3 --
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1
    print(prev)
    print(next)
    for index in range(0, 48):
        fib = prev + next
        print(fib)
        prev = next
        next = fib

#### otra forma de hacerlo ####

def fibonacci_2():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

#### forma ChatGPT ####

def fibonacci_3():
    prev = 0
    next = 1
    for _ in range(50):  # 50 números en total
        print(prev)
        prev, next = next, prev + next


#fibonacci()

"""-- 4 --
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(num):
    if num < 2:
        return False
    
    for index in range(2, num):
        if num % index == 0:
            return False
        
    return True

#print(es_primo(3))

def los_100_primos():
    for number in range(1,101):
        if number >= 2:

            es_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    es_divisible = True
                    break
            if not es_divisible:
                print(number)

#los_100_primos()

"""-- 7 --
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_words(text):
    list_words = list(text)
    list_invert_words = []
    dif_index = -1
    for i in range(0,len(list_words)):
        letter = list_words[i]
        i = dif_index
        dif_index -= 1
        list_invert_words.insert(i, letter)
    
    print(list_invert_words)

#invert_words("Soy Batman")

#### otra forma de hacerlo ####

def revert(text):
    reversed_text = ""
    text_len = len(text)
    print(text_len)
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]

    return reversed_text

#print(revert("Soy Batman"))

"""-- 10 --
CÓDIGO MORSE
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

morse_dict = {
    "A":"·—", "B":"—···", "C":"—·—·", "CH":"————", "D":"—··", "E":"·", "F":"··—·",
    "G":"——·", "H":"····", "I":"··", "J":"·———", "K":"—·—", "L":"·—··", "M":"——",
    "N":"—·", "Ñ":"——·——", "O":"———", "P":"·——·", "Q":"——·—", "R":"·—·", "S":"···",
    "T":"—", "U":"··—", "V":"···—", "W":"·——", "X":"—··—", "Y":"—·——", "Z":"——··",
    "0":"—————", "1":"·————", "2":"··———", "3":"···——", "4":"····—", "5":"·····",
    "6":"—····", "7":"——···", "8":"———··", "9":"————·",
    ".":"·—·—·—", ",":"——··——", "?":"··——··", "\"":"·—··—·", "/":"—··—·"
}

def morse_and_natural(text):
    is_natural = False
    break_for = False
    new_text = ""
    for char in text.upper():
        for clave in morse_dict:
            if char == clave:
                is_natural = True
                break_for = True
                break
        if break_for == True:
            break
    
    # True / natural
    if is_natural:
        for char in text.upper():
            for clave in morse_dict:
                if char == clave:
                    char = morse_dict[clave]
                    new_text += char + "  "
    # False / morse
    else:
        text = list(text.split("  "))
        for char in text:
            for clave, valor in morse_dict.items():
                if char == valor:
                    #acceder a la clave a partir del valor
                    new_text += clave
    
    print(new_text)

#morse_and_natural("···  ———  ···")
#morse_and_natural("SOS")


"""-- 11 --
EXPRESIONES EQUILIBRADAS
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
  en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
  No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def balanced_expressions(text):
    list_text = list(text)
    dict_symbols = {"{":"}", "[":"]", "(":")"}
    pila = []

    for element in text:
        if element in "{[(":
            pila.append(element)
        elif element in "}])":
            try:
                open_symbol = pila[-1]
            except IndexError:
                return False
            dict_close_symbol = dict_symbols[open_symbol]
            if element == dict_close_symbol:
                #print(f"Se ha abierto con '{open_symbol}' y cerrado con '{element}'")
                del pila[-1]
            else:
                return False
    if len(pila) > 0:
        print("Se ha abierto sin cerrar")
        return False
    
    return True
            


#print(balanced_expressions("{[a+b] - (a) + 7}")) # True
#print(balanced_expressions("{a+b]-(a)+78}")) # False
#print(balanced_expressions("{a + b [c] * (2x2)}}}}"))
#print(balanced_expressions("{ [ a * ( c + d ) ] - 5 }"))
#print(balanced_expressions("{ a * ( c + d ) ] - 5 }"))
#print(balanced_expressions("{a^4 + (((ax4)}"))
#print(balanced_expressions("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
#print(balanced_expressions("{{{{{{(}}}}}}"))
#print(balanced_expressions("(a"))


""" -- 12 --
ELIMINANDO CARACTERES
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.
"""

def rm_same_char(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    out1 = ""
    out2 = ""

    for char in str2:
        if char not in str1:
            out2 += char

    for char in str1:
        if char not in str2:
            out1 += char
            
    return out1, out2

#print(rm_same_char("Abcd", "aeiOu"))


""" --- 14 ---
FACTORIAL RECURSIVO
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
Ejemplo: factorial de 4 --> 4 * 3 * 2 * 1
 """

def factorial_recurs(num):
    if num <= 1:
        return 1
    
    return num * factorial_recurs(num-1)

#print(factorial_recurs(4))
#print(factorial_recurs(5))


""" --- 15 ---
¿ES UN NÚMERO DE ARMSTRONG / NARCISISTA?
Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
***Un número de Armstrong es un entero positivo que es igual a la suma de sus propios dígitos, cada uno elevado
a la potencia del número total de dígitos que posee. Por ejemplo, 153 es un número de Armstrong porque tiene tres dígitos,
y la suma de sus dígitos elevados al cubo (1³ + 5³ + 3³ = 1 + 125 + 27) es igual a 153.***
"""

def is_armstrong(num):
    num_list = list(str(num))
    result = 0

    for digit in num_list:
        result += int(digit) ** len(str(num))

    if result == num: return True
    else: return False


#print(is_armstrong(153))
#print(is_armstrong(370))
#print(is_armstrong(371))


"""--- 16 ---
¿CUÁNTOS DÍAS?
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
  - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
  - La función recibirá dos String y retornará un Int.
  - La diferencia en días será absoluta (no importa el orden de las fechas).
  - Si una de las dos cadenas de texto no representa una fecha correcta se
    lanzará una excepción.
"""

from datetime import datetime

def dif_time(fecha1, fecha2):
    try:
        fecha1_date = datetime.strptime(fecha1, "%d/%m/%Y").date()
        fecha2_date = datetime.strptime(fecha2, "%d/%m/%Y").date()
        #print(fecha1_date, fecha2_date)
    except ValueError as e:
        return "Fechas introducidas incorrectamente"
    
    diff = abs(fecha1_date - fecha2_date) # con abs() en caso de ser -4, sería 4. Así con todo. Da el valor absoluto
    return diff.days


#print(dif_time("18/05/1998", "23/09/2025"))
#print(dif_time("23/09/2025", "28/09/2016"))


"""
--- 18 ---
CARRERA DE OBSTÁCULOS
Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
  - La función recibirá dos parámetros:
        - Un array que sólo puede contener String con las palabras
          "run" o "jump"
        - Un String que represente la pista y sólo puede contener "_" (suelo)
          o "|" (valla)
  - La función imprimirá cómo ha finalizado la carrera:
        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
          será correcto y no variará el símbolo de esa parte de la pista.
        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
        - Si hace "run" en "|" (valla), se variará la pista por "/".
  - La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

def obstacle_race(obstacles, runner_movements):
    runner_movements = list(runner_movements)
    final_mov = []
    for obst, mov in zip(obstacles, runner_movements):
        if (obst == "run" and mov == "_") or (obst == "jump" and mov == "|"):
            final_mov.append(mov)

        elif obst == "run" and mov != "_":
            final_mov.append("/")

        elif obst == "jump" and mov != "|":
            final_mov.append("x")

    final_mov = "".join(final_mov)
    print(final_mov)
    for element in final_mov:
        if element in "x/":
            return False
    
    return True

print(obstacle_race(["run", "jump", "jump", "run"], "_|_|"))
print(obstacle_race(["run", "jump", "run", "jump"], "_|_|"))
