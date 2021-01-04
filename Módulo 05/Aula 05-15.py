import json
from pathlib import Path

arquivo = Path('.\Módulo 05\pikachu.json').read_text()
dados = json.loads(arquivo)

print(dados['abilities'][1]['ability']['name'])
