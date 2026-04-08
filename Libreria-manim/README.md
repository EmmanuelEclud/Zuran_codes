# Transformaciones Lineales en Python

Este proyecto muestra cómo representar **transformaciones lineales y conceptos básicos de álgebra lineal** utilizando dos librerías de Python:

- **Matplotlib** → visualización estática de vectores
- **Manim** → animación del plano y vectores transformados

El objetivo es comparar ambas formas de visualización usando el mismo problema matemático.

---

## Problema utilizado

Se aplica la siguiente matriz de transformación:

\[
A =
\begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix}
\]

sobre el vector:

\[
v =
\begin{bmatrix}
1 \\
2
\end{bmatrix}
\]

Resultado:

\[
Av =
\begin{bmatrix}
4 \\
3
\end{bmatrix}
\]

---

## Archivos del proyecto

### `V1_Matplotlib.py`
Visualización estática utilizando **Matplotlib**.

Muestra:

- vector original
- vector transformado
- comparación visual en el mismo plano cartesiano

Ideal para explicación matemática rápida.

---

### `V3C1.py`
Animación utilizando **Manim**.

Muestra:

- plano cartesiano
- vector original
- vector resultado
- deformación del plano mediante matriz
- coincidencia entre el vector transformado y el resultado esperado

Ideal para videos educativos y demostraciones visuales.

---

## Librerías necesarias

Instalar las siguientes librerías:

- `numpy`
- `matplotlib`
- `manim`

---

## Instalación rápida

Ejecuta el siguiente comando en terminal:

```bash
pip install numpy matplotlib manim
```

---

## Ejecución

### Matplotlib
Ejecutar normalmente con Python:

```bash
python V1_Matplotlib.py
```

---

### Manim
Para generar el video animado ejecutar:

```bash
manim -pql V3C1.py TransformacionLineal
```

### Explicación del comando
- `-p` → abre el video al finalizar
- `ql` → calidad baja para render rápido
- `V3C1.py` → archivo Python
- `TransformacionLineal` → nombre de la clase de la escena

---

## Resultado esperado

El vector azul original:

\[
(1,2)
\]

debe transformarse y coincidir con el vector rojo:

\[
(4,3)
\]

confirmando que:

\[
A \cdot v = (4,3)
\]

---

## Objetivo educativo

Este proyecto fue creado con fines de aprendizaje para comprender:

- multiplicación matriz-vector
- transformación de bases
- deformación del plano
- representación gráfica de álgebra lineal
- uso de Python para visualización matemática

---
