from rich import print
from rich.panel import Panel 

def menu():
    texto = Panel("""[yellow]1[/yellow] - [blue]adicionar animal[/blue]
[yellow]2[/yellow] - [blue]remover animal[/blue]
[yellow]3[/yellow] - [blue]adicionar adotante[/blue]
[yellow]4[/yellow] - [blue]remover adotante[/blue]
[yellow]5[/yellow] - [blue]listas animais[/blue]
[yellow]6[/yellow] - [blue]listas adotantes[/blue]
[yellow]7[/yellow] - [blue]buscar animal para adoção[/blue] 
[yellow]8[/] - [blue]sair do sistema[/]""", title="Menu Principal",width=34)
    print(texto)
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def linha(tam = 42):
    return '-' * tam

def leiaint(msg):
    ok = False 
    valor = 0 
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[031mERRO! Digite um número inteiro válido \033[m')
        if ok:
            break
    return valor