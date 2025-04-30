from usuario import Usuario

def obtener_usuarios_iniciales():
    return [
        Usuario("ainara", "Ainara", "De Miguel", "1977", "1234"),
        Usuario("joxe", "Joxe", "Zabaleta", "1988", "pass1234"),
        Usuario("luciag", "Lucía", "Gómez", "1992", "mypass789")
    ]
if __name__ == "__main__":
    from usuarios import GestorUsuarios
    gestor = GestorUsuarios("usuarios.txt")
    print("Archivo creado con datos iniciales.")
