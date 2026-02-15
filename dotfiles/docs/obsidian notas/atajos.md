# Atajos de Teclado i3 para Obsidian

## 📋 Información General
- **Tecla Mod:** `Super` (Windows/Command)
- **Archivo config:** `~/.config/i3/config`

## 🚀 Lanzar Aplicaciones
| Atajo | Acción |
|-------|--------|
| `Super + Enter` | Abrir terminal |
| `Super + d` | Lanzador dmenu |
| `Super + espacio` | Lanzador rofi |
| `Impr Pant` | Captura de pantalla |

## 🪟 Gestión de Ventanas
### Movimiento y Enfoque
| Atajo                     | Acción                    |
| ------------------------- | ------------------------- |
| `Super + j/k/l/;`         | Enfocar ventana (←/↓/↑/→) |
| `Super + ←/↓/↑/→`         | Enfocar ventana (flechas) |
| `Super + Shift + j/k/l/;` | Mover ventana (←/↓/↑/→)   |
| `Super + Shift + ←/↓/↑/→` | Mover ventana (flechas)   |

### Modificadores de Ventana
| Atajo                | Acción                           |
| -------------------- | -------------------------------- |
| `Super + f`          | Alternar pantalla completa       |
| `Super + t`          | Alternar flotante/mosaico        |
| `Super + Shift  + t` | Cambiar enfoque flotante/mosaico |
| `Super + q`          | Cerrar ventana                   |

## 🧩 Diseño y Contenedores
| Atajo | Acción |
|-------|--------|
| `Super + h` | Dividir horizontal |
| `Super + v` | Dividir vertical |
| `Super + s` | Layout apilado (stacking) |
| `Super + w` | Layout con pestañas (tabbed) |
| `Super + e` | Alternar división |
| `Super + a` | Enfocar contenedor padre |
| `Super + r` | Modo redimensionar |

### Modo Redimensionar
| Atajo | Acción |
|-------|--------|
| `j` o `←` | Reducir ancho |
| `k` o `↓` | Aumentar altura |
| `l` o `↑` | Reducir altura |
| `;` o `→` | Aumentar ancho |
| `Enter`/`Escape`/`Super + r` | Salir del modo |

## 🏢 Espacios de Trabajo
| Atajo | Acción |
|-------|--------|
| `Super + 1-0` | Cambiar a workspace 1-10 |
| `Super + Shift + 1-0` | Mover ventana a workspace 1-10 |

## 🔊 Multimedia
| Atajo | Acción |
|-------|--------|
| `XF86AudioRaiseVolume` | Subir volumen (+10%) |
| `XF86AudioLowerVolume` | Bajar volumen (-10%) |
| `XF86AudioMute` | Silenciar audio |
| `XF86AudioMicMute` | Silenciar micrófono |

## ⚙️ Sistema
| Atajo | Acción |
|-------|--------|
| `Super + Shift + c` | Recargar configuración |
| `Super + Shift + r` | Reiniciar i3 |
| `Super + Shift + e` | Salir de i3 |
| `Super + p` | Configurar pantallas |

## 🔧 Aplicaciones Especiales
- **Plank:** Auto-inicia como dock flotante
- **Polybar:** Barra de estado personalizada
- **Picom:** Compositor para efectos visuales
- **Feh:** Gestor de fondos de pantalla

---

## 📝 Notas
- Los workspaces están numerados del 1 al 10
- La tecla `Super` es generalmente la tecla Windows/Command
- La configuración incluye auto-arranque de varios servicios
- Scripts personalizados en `~/.config/polybar/`

## 🔄 Modo Recuperación
- `Super + Shift + r` para reiniciar sin perder layout actual
- `Super + Shift + c` para aplicar cambios en config

---

*Documento generado automáticamente desde configuración i3*