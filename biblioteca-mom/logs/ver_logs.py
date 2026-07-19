from pathlib import Path

caminho = Path("logs/sistema.log")

for encoding in ("utf-8", "cp1252", "latin-1"):
    try:
        with caminho.open("r", encoding=encoding) as arquivo:
            print(arquivo.read())
        break
    except UnicodeDecodeError:
        continue
else:
    raise RuntimeError("Não foi possível decodificar o arquivo de log com as codificações suportadas.")