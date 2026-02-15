## no modifica la polybar
+ ~~Dracula
- ~~flexoki
- ~~markaita-cyan
- officestyle-fixed-tooltip
- phocus

Corregir el color verde para 
- ~~cloudy soft
- ~~machiatto capussine

## Mejora del Rendimiento (RAM y SSD)

Dado que la D14 2020 suele venir con 8GB de RAM (no expandible), optimizar el uso de memoria es vital. 

- **Activa ZRAM:** Esto crea un área de intercambio comprimida en la RAM, evitando que el sistema se ralentice al usar el disco (SSD) cuando te quedas sin memoria.

```
sudo apt install zram-config
```

- **Evita el "Tearing" de pantalla:** Si notas que la imagen se corta al ver videos, evita usar el escalado fraccionario (usa 100% o 200%) y asegúrate de que el compositor de XFCE esté activo en **Configuración > Ajustes del gestor de ventanas > Compositor**.


## Polybar Gradient 

![[Pasted image 20260107142726.png]]

```
[gradient]
color-1 = #9DA9A0
color-2 = #859289 
color-3 = #475258 

[module/text1]
type = custom/text
content = ""
content-foreground = ${gradient.color-1}
content-background = ${gradient.color-2}
content-font = 3

[module/text2]
type = custom/text
content = ""
content-foreground = ${gradient.color-1}
content-background = ${gradient.color-2}
content-font = 3

[module/text3]
type = custom/text
content = ""
content-foreground = ${gradient.color-2}
content-background = ${gradient.color-3}
content-font = 3

[module/text4]
type = custom/text
content = ""
content-foreground = ${gradient.color-2}
content-background = ${gradient.color-3}
content-font = 3

[module/text5]
type = custom/text
content = ""
content-foreground = ${gradient.color-3}
content-font = 3

[module/text6]
type = custom/text
content = ""
content-foreground = ${gradient.color-3}
content-font = 3
```

Comando para que picture in picture salga siempre en todos los escritorios virtuales

```
wmctrl -l | grep Picture-in-Picture
```
```
wmctrl -i -r 0x046001d5 -b add,above,sticky
```


pendiente agregarle al script de actualizaciones apt list --upgradable
pendiente hacer animacion para cambio de tema y wallpaper
puedo mantener 5 escritorio en i3?


```
xrandr --output eDP --scale 0.9x0.9
```

```
clipcatctl clear
```


WTEXXM