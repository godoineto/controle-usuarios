from enum import Enum


class Level(Enum):
    VISITANTE = 1
    USUARIO = 2
    ADMINISTRATIVO = 3
    TECNICO = 4
    SUPER_USUARIO = 5

    def __repr__(self):
        return str(self.name)

# Autor: José Luiz de Godoi Neto
