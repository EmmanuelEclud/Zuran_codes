#Aqui esta el codigo visto el 09 del 04 del 2026.

from manim import *

class TransformacionLineal(Scene):
    def construct(self):
        # Dibuja el plano cartesiano
        plane = NumberPlane()
        self.play(Create(plane))

        # Vector original azul (1,2)
        vector_azul = Vector([1, 2], color=BLUE)
        self.play(GrowArrow(vector_azul))

        self.wait(1)#PIDOS

        # Vector resultado rojo (4,3)
        vector_rojo = Vector([4, 3], color=RED)
        self.play(GrowArrow(vector_rojo))

        self.wait(1)#PIDOS

        # Matriz de transformación
        matriz = [[2, 1],
                  [1, 1]]

        # Transformar plano y vector azul (1,2)
        self.play(
            ApplyMatrix(matriz, plane),
            ApplyMatrix(matriz, vector_azul),
            run_time=3
        )

        self.wait(2)#Para que no se cierre al insntante
