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

        print(' 1 - John Doe')
        print(' 2 - John Doe')
        print(' 3 - John Doe')
        print(' 4 - John Doe')
        print(' 5 - John Doe')

        id = terminal('Digite o ID correspondente ao técnico:')

        if id in ids:
            return id
        else:
            print('\nO ID "{}" não corresponde a nenhum técnico.\nPor favor, selecione novamente...\n')
