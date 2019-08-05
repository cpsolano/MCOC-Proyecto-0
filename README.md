# MCOC-Proyecto-0

# Introducción
La perdida de significancia ocurre cuando se trabaja con aritmetica de precisión finita. Esto se puede observar al comparar una función de alguna librería de python, versus la forma numérica de obtener el resultado. En este caso, se mostrará con valores negativos de la **función exponencial**. 

# Ejemplo
A continuación se presentarán los resultados obtenidos en un rango de (-30,-20) comparando la forma numérica de obtener el valor exponencial y la función *exp* de la librería *math*.
Donde la forma numérica se obtiene por la sumatoria de (x^k/k!)

# Resultados 
Se muestra en color rojo, los valores obtenidos de forma numérica y en color azul, los valores obtenidos a partir de la función *exp*.

![Alt text](https://raw.githubusercontent.com/cpsolano/MCOC-Proyecto-0/master/figure_1.png)
    Se puede observar en este rango que los valores obtenidos son distintos con una diferencia a nivel decimal notoria. Esto se debe justamente a la aproximación que hace la consola al ser tantos decimales.
    Finalmente, se puede ver de forma mas exacta con los valores obtenidos en el output de la consola.

### Output de la consola
```
[-3.0668123563562199e-05, 2.0914916542212165e-05, 4.8020631768075438e-06, -4.4095894473309066e-06, 5.6020946323056647e-07, -7.1297804036720779e-07, 1.0297754191968734e-07, 6.0724696279418996e-08, -1.9731657492116485e-09, -3.1648595607706816e-09]

[9.357622968840175e-14, 2.543665647376923e-13, 6.914400106940203e-13, 1.8795288165390832e-12, 5.109089028063325e-12, 1.3887943864964021e-11, 3.775134544279098e-11, 1.026187963170189e-10, 2.7894680928689246e-10, 7.582560427911907e-10]
```

