# Sistema de ajuda PyHelp - Interactive Help
cores = ("\033[m", "\033[0;41m", "\033[0;42m", "\033[0;44m", "\033[7;40m")

def sistema_p(mensagem, cor=0):
    print(cores[cor], end="")
    print("=" * (len(mensagem) + 4))
    print(f"  {mensagem}")
    print("=" * (len(mensagem) + 4))
    print(cores[0], end="")

def py_help():
    from time import sleep
    sistema_p("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > ")).lower()
    while True:
        if comando in "fim":
            sistema_p("ATÉ LOGO!", 1)
            break
        sistema_p(f"Acessando o manual do comando '{comando}'", 3)
        sleep(2)
        print(cores[4])
        help(comando)
        print(cores[0])
        sistema_p("SISTEMA DE AJUDA PyHELP", 2)
        comando = str(input("Função ou Biblioteca > ")).lower()


py_help()
