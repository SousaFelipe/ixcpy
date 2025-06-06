
# ixcpy

Um wrapper de conexão com a API do IXC

Esta biblioteca não faz parte do conjunto oficial de bibliotecas da IXCsoft!\
O desenvolvimento é feito de forma independente e utiliza apenas as funcionalidades providas pela API oficial do IXC.
Todas as funcionalidades se resumem a uma interface de comunicação com a API do sistema IXC.\
Você poderá encontrar orientações de como parametrizar as requisições, na Wiki oficial da API do IXC.


## Observações

Para estabelecer uma conexão corretamente, é necessário fornecer o token de autenticação da API do IXC (Link nas referências abaixo) e o domínio do seu servidor IXC, nos parâmetros do construtor da classe Connection.

Exemplo:

```python
connection = Connection(
  server='seu_domínio_ixc.com.br',  # Também pode ser um enderço de IP
  token='seu_token_ixc',            # Verificar a última referência
  table='su_oss_chamado',           # Exemplo de requisição na tabela de Ordens de Serviço
  ...
)
```


## Clone & Setup

```bash
git clone https://github.com/SousaFelipe/ixcpy.git
```
```bash
cd ixcpy
```
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
```bash
python -m pip install -r requirements.txt
```


## Referências

  - [Site da IXCsoft](https://ixcsoft.com/)
  - [Wiki oficial da API do IXC](https://wikiapiprovedor.ixcsoft.com.br/)
  - [Tutorial de como gerar um Token de API no IXC](https://wiki.ixcsoft.com.br/pt-br/API/como_gerar_um_token_para_integra%C3%A7%C3%B5es_API)
