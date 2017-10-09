import os
import sys

diretorio = sys.argv[1]
pagina = open("index.html", "w", encoding="utf-8")
pagina.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")
for arquivo in os.listdir(diretorio):
    nome, extencao = os.path.splitext(arquivo)
    if extencao in [".jpg", ".png"]:
        caminho = os.path.join(diretorio, arquivo)
        pagina.write(f"<p><a href=\"{caminho}\">{nome}</a></p>")
pagina.write("</body></html>")
pagina.close()
