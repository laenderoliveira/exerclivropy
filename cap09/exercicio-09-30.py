f = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comedia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora"]
}

pagina = open("index.html", "w", encoding="utf-8")
pagina.write("<!DOCTYPE html>")
pagina.write("<html lang=\"en\">")
pagina.write("<head>")
pagina.write("<meta charset=\"UTF-8\">")
pagina.write("<title>Title</title>")
pagina.write("</head>")
pagina.write("<body>")
for genero, filmes in f.items():
    pagina.write(f"<h1>{genero}</h2>")
    pagina.write("<ul>")
    for filme in filmes:
        pagina.write(f"<li>{filme}</li>")
    pagina.write("</ul>")
pagina.write("</body>")
pagina.write("</html>")
pagina.close()
