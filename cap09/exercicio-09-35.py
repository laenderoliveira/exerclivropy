import os
import urllib.request


pagina = open("index.html", "w", encoding="utf-8")
pagina.write("""<!DOCTYPE html>
<html lang="pt-br"><head>
    <meta charset="UTF-8"><title>Arquivos</title>
</head> <body>""")

for raiz, diretorios, arquivos in os.walk("/home/laenderoliveira/Python/livro_nilo/"):
    pagina.write(f"<h2>{raiz}</h2>")
    pagina.write("<ul>")
    for a in arquivos:
        caminho = os.path.join(raiz, a)
        tamanho = os.path.getsize(caminho)
        link = urllib.request.pathname2url(caminho)
        pagina.write(f"<li><a href={link}>{a} </a>({tamanho} bytes)</li>")
    pagina.write("</ul>")
pagina.write("</body></html>")
pagina.close()
