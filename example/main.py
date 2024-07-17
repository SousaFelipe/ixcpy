from ixcpy import Connection
from ixcpy.data import Excel

from options import option_period, option_tecnico
from source import append_source, load_source, merge_source
from utils import terminal, clear_screen



SERVER = 'seu_domínio_ixc.com.br'
TOKEN = 'SEU_TOKEN_IXC'



def ptbr_to_iso(ptbr_date: str) -> str:
    splitted: list[str] = ptbr_date.split('/')
    return '-'.join(splitted[::-1])

def iso_to_ptbr(iso_date: str) -> str:
    date: str = iso_date.split(' ')[0]
    time: str = iso_date.split(' ')[1]
    return '/'.join(date.split('-')[::-1]) + " " + time

def formula(index: int) -> str:
    row: int = index + 2
    return f'=TEXT($F{row}-$E{row}; "H:mm")'



def chamados_source():
    id_tecnico = option_tecnico()
    inicio_periodo, final_periodo = option_period()

    return load_source(
        connection=Connection(
            server=SERVER,
            token=TOKEN,
            table='su_oss_chamado',
            ssl=True
        ),
        args=[
            'status="F"',
            'id_tecnico="{}"'.format(id_tecnico),
            'data_inicio>="{} 00:00:00"'.format(ptbr_to_iso(ptbr_date=inicio_periodo)),
            'data_final<="{} 23:59:00"'.format(ptbr_to_iso(ptbr_date=final_periodo))
        ]
    )

def assuntos_source():
    return load_source(
        connection=Connection(
            server=SERVER,
            token=TOKEN,
            table='su_oss_assunto',
            ssl=True
        ),
        args=['ativo="S"']
    )



if __name__ == '__main__':
    clear_screen()

    chamados = chamados_source()

    if len(chamados) > 0:
        assuntos = assuntos_source()
    
        append_source(src=chamados, new_key='tempo', parser=formula)
        merge_source(src=chamados, merge=assuntos, search='id_assunto', replace='assunto')

        filename = terminal('\nSalvar o arquivo como:')

        excel = Excel(
            headers=[
                'id',
                'assunto',
                'data_abertura',
                'data_fechamento',
                'data_inicio',
                'data_final',
                'tempo'
            ]
        )

        excel.load(
            data=chamados,
            parsers={
                'data_abertura': lambda arg: iso_to_ptbr(arg),
                'data_fechamento': lambda arg: iso_to_ptbr(arg),
                'data_inicio': lambda arg: iso_to_ptbr(arg),
                'data_final': lambda arg: iso_to_ptbr(arg)
            }
        )

        excel.build()
        result = excel.save(sheet=filename)
        print('\n{}\n'.format(result))

    else:
        print('\nNenhum registro foi encontrado...\n')
