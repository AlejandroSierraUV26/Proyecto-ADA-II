import timeit
from programacion_dinamica import solucion_dinamica
from fuerza_bruta import solucion_fuerza_bruta
from voraz import solucion_voraz

def medir_tiempo(func, *args):
    def wrapper():
        return func(*args)
    return timeit.timeit(wrapper, number=1)

def pruebas():
    pruebas = [
    ("a", "c"),
    ("ab", "ad"),
    ("ab", "abc"),
    ("abc", "a"),
    ("abc", "abd"),
    ("cat", "bat"),
    ("car", "bar"),
    ("dog", "log"),
    ("bag", "bug"),
    ("ten", "pen"),
    ("top", "tip"),
    ("hat", "bat"),
    ("pit", "pot"),
    ("son", "sun"),
    ("ape", "map"),
    ("bat", "bot"),
    ("bar", "far"),
    ("red", "reed"),
    ("fit", "sit"),
    ("fan", "tan"),
    ("apple", "aple"),
    ("axe", "axes"),
    ("boat", "coat"),
    ("play", "stay"),
    ("goal", "gale"),
    ("part", "park"),
    ("game", "fame"),
    ("home", "come"),
    ("house", "mouse"),
    ("hike", "like"),
    ("bake", "cake"),
    ("test", "tests"),
    ("hello", "hell"),
    ("task", "mask"),
    ("peak", "beak"),
    ("play", "pray"),
    ("hope", "cope"),
    ("wide", "side"),
    ("mark", "dark"),
    ("tree", "free"),
    ("bear", "dear"),
    ("side", "slide"),
    ("right", "light"),
    ("peace", "place"),
    ("close", "closes"),
    ("stone", "clone"),
    ("flame", "frame"),
    ("drone", "phone"),
    ("crawl", "drawl"),
    ("least", "beast"),
    ("shell", "spell"),
    ("shine", "shine"),
    ("order", "border"),
    ("actor", "factors"),
    ("saving", "savings"),
    ("coding", "cording"),
    ("begin", "begins"),
    ("coding", "codings"),
    ("house", "houses"),
    ("cloud", "cloudy"),
    ("robots", "robotic"),
    ("leader", "leavers"),
    ("better", "betters"),
    ("school", "schools"),
    ("better", "letters"),
    ("change", "changed"),
    ("pencil", "pencils"),
    ("strive", "strives"),
    ("powers", "flowers"),
    ("machine", "machines"),
    ("builder", "builders"),
    ("planner", "planners"),
    ("writing", "writers"),
    ("dreamer", "dreamers"),
    ("dancing", "dancers"),
    ("smarter", "smarters"),
    ("dancers", "dancing"),
    ("testing", "nesting"),
    ("writing", "written"),
    ("builder", "building"),
    ("speaker", "speakers"),
    ("creating", "creators"),
    ("machine", "machiner"),
    ("planning", "planners"),
    ("meeting", "meetings"),
    ("testing", "tested"),
]



    costos = {
        'avanzar': 1,
        'reemplazar': 1,
        'borrar': 6,
        'insertar': 1,
        'destruir': 2
    }

    i = 0
    txt = ""
    for palabra1, palabra2 in pruebas:
        txt += f"Prueba con palabra1: {palabra1}, palabra2: {palabra2}\n"
        i += 1
        print(f"Prueba con palabra1: {palabra1}, palabra2: {palabra2}")
        tiempo = medir_tiempo(solucion_dinamica, palabra1, palabra2, costos, 2)
        resultado = solucion_dinamica(palabra1, palabra2, costos)
        txt += f"D = {i}: {tiempo:.6f}\n"
        
        print(f"D = {i}: {tiempo:.6f} => {resultado}")

        tiempo = medir_tiempo(solucion_fuerza_bruta, palabra1, palabra2, costos)
        resultado = solucion_fuerza_bruta(palabra1, palabra2, costos)
        txt += f"F = {i}: {tiempo:.6f}\n"
        print(f"F = {i}: {tiempo:.6f} => {resultado}")

        tiempo = medir_tiempo(solucion_voraz, palabra1, palabra2, costos, 2)
        resultado = solucion_voraz(palabra1, palabra2, costos)
        
        txt += f"V = {i}: {tiempo:.6f}\n"
        print(f"V = {i}: {tiempo:.6f} => {resultado}")

        
        
        print("\n")
    with open("resultados.txt", "w") as f:
        f.write(txt)
        
    

if __name__ == "__main__":
    pruebas()