from flask import Flask
import random
facts_list = {
    "fact1": "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "fact2": "Según un estudio realizado en 2018, más del 50 porciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "fact3": "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "fact4": "Según un estudio de 2019, más del 60 porciento de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "fact5":"Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "fact6":"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", 
    "fact7": "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", 
    "fact8": "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas",
        }

song_list = {
    "song1": """<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/08D9ts2y0ILCTAEFpRlGwl?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>""",
    "song2": """<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/1bBHEYHcRVvvff6tugQwS7?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>""",
    "song3": """<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/7vZvoyOXvTGqu3FjBPRPTC?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>""",
    "song4": """<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/4sC7exiqCrik9sU7B8ASGO?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>""",
    "song5": """<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/5xZ3LXjXiNqjWNDPfRqCPV?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>""",
    }

random_item = random.choice(list(facts_list.values()))
message = random_item
app = Flask(__name__)

@app.route("/datos")
def random_fact():
    return message
@app.route("/randomsong")
def songr():
    return random.choice(list(song_list.values()))
app.run(debug=True)