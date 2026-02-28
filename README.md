# Cargopy 🚀

**Cargopy** es una herramienta ligera inspirada en **cargo** de Rust para gestionar proyectos de Python de manera rápida y eficiente, desde la creación hasta la ejecución de scripts y manejo de paquetes.

---

## 🛠️ Uso

### Opciones disponibles

| Opción | Descripción |
|--------|-------------|
| `new <nombre>` | Crea un nuevo proyecto con el nombre indicado. |
| `cd` | Muestra la ruta raíz de tu proyecto. |
| `venv` | Inicializa un entorno virtual en tu proyecto. |
| `run <script>` | Ejecuta el script indicado (solo si existe). |
| `install <paquete>` | Instala el paquete de Python especificado. |
| `upgrade <paquete>` | Actualiza el paquete especificado. |
| `uninstall <paquete>` | Desinstala el paquete especificado. |

---

## ⚡ Ejemplos

```bash
# Crear un proyecto llamado "mi_proyecto"
cargopy new mi_proyecto

# Inicializar entorno virtual
cargopy venv

# Instalar requests
cargopy install requests

# Ejecutar script principal
cargopy run main.py
```

💡 Notas

- Asegúrate de tener Python instalado en tu sistema.
- run solo ejecutará scripts que existan dentro de tu proyecto.
- Maneja tus paquetes directamente desde Cargopy para mantener tu proyecto limpio y organizado.

¡Disfruta usando Cargopy! 🎉

