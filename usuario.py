class Usuario:
    def __init__(self, usuario, nombre, apellido, anio_nac, passwd):
        self._usuario = usuario
        self._nombre = nombre
        self._apellido = apellido
        self._anio_nac = anio_nac
        self._passwd = passwd

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def anio_nac(self):
        return self._anio_nac

    @anio_nac.setter
    def anio_nac(self, valor):
        self._anio_nac = valor

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, valor):
        self._passwd = valor

    def to_linea(self):
        return f"{self._usuario};{self._nombre};{self._apellido};{self._anio_nac};{self._passwd}"

    @staticmethod
    def from_linea(linea):
        partes = linea.strip().split(';')
        return Usuario(*partes)
