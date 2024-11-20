from modelos.repositorios.repositorio_personajes import RepositorioPersonajes

repo_personajes = None

def obtenerRepoPersonajes():
    global repo_personajes
    if repo_personajes == None:
        repo_personajes = RepositorioPersonajes()
    return repo_personajes