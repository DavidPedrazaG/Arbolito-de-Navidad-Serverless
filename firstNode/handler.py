import json

def reverse_string(string):
    # an empty string for storing reversed string
    reversed_string = ""
    # looping through the string
    for char in string:
        # reversing the string
        reversed_string = char + reversed_string
    # returning a reversed string
    return reversed_string

def hello(event, context):
    
    arbol = ""
    arbol_reverse = ""
    rows = 20
    columns = (rows*2)+1
    space = " "
    point = "*"
    cant = 1
    for i in range(rows):
        arbol+=("\n")
        for j in range(columns):
            spaces = (columns-cant)/2
            if j <= spaces or j > spaces+cant:
                arbol+=(space)
            else:
                arbol+=(point)
        cant+=2
    cant= int(cant/3)
    for i in range(int(rows/3)):
        arbol+=("\n")
        for j in range(columns):
            spaces = (columns-cant)/2
            if j <= spaces or j > spaces+cant:
                arbol+=(space)
            else:
                arbol+=(point)

    arbol_reverse = reverse_string(arbol)
    print(arbol)
    print(arbol_reverse)
    arbol_html = arbol.replace("\n", "<br>")
    arbol_reverse_html = arbol_reverse.replace("\n", "<br>")
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': f"<html><body><pre>{arbol_html}{arbol_reverse_html}</pre></body></html>"
    }

    return response

