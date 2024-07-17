from utils import terminal



def option_period() -> tuple:
    print('\n========================================')
    print(' Período...')
    print('----------------------------------------')
    start = terminal(' Data inicial (dd/mm/aaaa):')
    final = terminal(' Data final (dd/mm/aaaa):')
    return (start, final)


def option_tecnico() -> str:

    ids: str = ['9', '20', '37', '38', '54', '55']

    print('\n========================================')
    print(' Técnico...')
    print('----------------------------------------')

    while True:

        print(' 9  - Weberson Ferreira')
        print(' 20 - Carlos Alberto')
        print(' 37 - Everson Araujo')
        print(' 38 - Ismael Rodrigues')
        print(' 54 - Saulo Viana')
        print(' 55 - Kaik Vitoriano')

        id = terminal('Digite o ID correspondente ao técnico:')

        if id in ids:
            return id
        else:
            print('\nO ID "{}" não corresponde a nenhum técnico.\nPor favor, selecione novamente...\n')
