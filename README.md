## Auditoría de Seguridad

Se realizó una auditoría de seguridad sobre los archivos principales de la aplicación utilizando **Bandit**, herramienta de análisis estático de seguridad para código Python.

### Resultados de la auditoría

| ID | Vulnerabilidad | Archivo | Línea | Severidad | Estado |
|---|---|---|---:|---|---|
| B105 | Contraseña escrita directamente en el código | `app.py` | 10 | 🟢 Baja | ✅ Corregida |
| B608 | Construcción insegura de consulta SQL | `app.py` | 25 | 🟠 Media | ✅ Corregida |
| B311 | Uso de generador pseudoaleatorio | `app.py` | 30 | 🟢 Baja | ⚠️ Revisada |
| B201 | Flask ejecutándose con `debug=True` | `app.py` | 35 | 🔴 Alta | ✅ Corregida |
| B104 | Aplicación vinculada a todas las interfaces | `app.py` | 35 | 🟠 Media | ⚠️ Revisada |
| B101 | Uso de `assert` en pruebas | `test_app.py` | 7 | 🟢 Baja | ✅ Corregida |

### Correcciones realizadas

- **B105:** Se eliminaron las credenciales de base de datos escritas directamente en el código y se utilizaron variables de entorno mediante `os.getenv()`.
- **B608:** Se validó que el identificador recibido mediante la URL sea un número entero antes de utilizarlo en la consulta simulada.
- **B311:** Se revisó el uso de `random.random()`. Se mantiene debido a que se utiliza únicamente para simular fallos aleatorios del servicio y no para funciones criptográficas.
- **B201:** Se deshabilitó el modo `debug` de Flask utilizando `debug=False`.
- **B104:** Se mantiene `0.0.0.0` debido a que la aplicación necesita aceptar conexiones desde el contenedor Docker y posteriormente desde el servidor EC2.
- **B101:** Se mantiene el `assert` porque forma parte de una prueba automatizada y se agregó `# nosec B101` para indicar que su uso es intencional.

### Comando utilizado

```bash
bandit app.py test_app.py -f txt
