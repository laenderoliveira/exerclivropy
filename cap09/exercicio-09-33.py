import os
import sys

dir = sys.argv[1]
pagina = open("index.html", "w", encoding="utf-8")
pagina.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")
for arquivo in os.listdir(dir):
   nome, extencao = os.path.splitext(arquivo)
   if extencao in [".jpg", ".png"]:
       caminho_completo = os.path.join(dir, arquivo)
       print(caminho_completo)
       pagina.write(f"<p><a href=\"{caminho_completo}\">{nome}</a></p>")
pagina.write("""</body>
</html>""")
pagina.close()