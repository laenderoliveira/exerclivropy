import os
pagina = open("index.html", "w", encoding="utf-8")
pagina.write("""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>""")

for raiz, diretorios, arquivos in os.walk("/home/laenderoliveira/Python/livro_nilo/"):
    pagina.write(f"<h2>Raiz: {raiz}</h2>")
    pagina.write("<ul>")
    for a in arquivos:
        tamanho = os.path.getsize(os.path.join(raiz, a))
        pagina.write(f"<li>{a} Tamanho: {tamanho} bytes</li>")
    pagina.write("</ul>")
pagina.write("</body></html>")
pagina.close()
