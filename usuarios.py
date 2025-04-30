from usuario import Usuario
from datos_iniciales import obtener_usuarios_iniciales
import os

class GestorUsuarios:
    def __init__(self, fichero):
        self.fichero = fichero
        self._crear_archivo_si_no_existe()

    def _crear_archivo_si_no_existe(self):
        if not os.path.exists(self.fichero):
            with open(self.fichero, 'w') as archivo:
                archivo.write("")  

    def cargar_usuarios(self):
        try:
            with open(self.fichero, 'r') as f:
                return [Usuario.from_linea(linea) for linea in f]
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios):
        with open(self.fichero, 'w') as f:
            for usuario in usuarios:
                f.write(usuario.to_linea() + '\n')

    def anadir_usuario(self, nuevo_usuario):
        usuarios = self.cargar_usuarios()
        usuarios.append(nuevo_usuario)
        self.guardar_usuarios(usuarios)

    def eliminar_usuario(self, usuario_id):
        usuarios = self.cargar_usuarios()
        usuarios = [u for u in usuarios if u.usuario != usuario_id]
        self.guardar_usuarios(usuarios)

    def buscar_usuario(self, usuario_id):
        usuarios = self.cargar_usuarios()
        for usuario in usuarios:
            if usuario.usuario == usuario_id:
                return usuario
        return None

    def mostrar_usuarios(self):
        usuarios = self.cargar_usuarios()
        for usuario in usuarios:
            print(usuario.to_linea())
