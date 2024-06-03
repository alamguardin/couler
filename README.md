# Couler: Un CLI para manejar tus tareas

## ¿Como usar?

### Instalacion

Clona el repositorio:
```bash
git clone https://github.com/alamguardin/couler.git
```

Instala Auto Py to Exe:
```bash
pip install auto-py-to-exe
```

Ejecuta Auto Py to Exe:
```bash
auto-py-to-exe
```

Al ejecutar ```auto-py-to-exe``` se abrira una ventana. Debes marcar las opciones de **One Directory** y **Console Based**, luego de ello prosigues a convertir el archivo .py a .exe.

[Aqui podras saber mas de auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)

Una vez compilado el archivo, sigue agregar la ruta de archivo a la variable de entorno Path; si no sabes como agregar una variable de entono [aqui te explican como hacerlo](https://www.java.com/es/download/help/path.html).

## Iniciando Couler

Antes de iniciar Couler debes dirigirte a la ruta del proyecto a gestionar; una vez alli ejecutamos el siguiente comando.

```bash
couler init
```

Ya iniciado couler, podemos crear, completar y eleminar tareas.

### Creando una tarea

```bash
couler add 'Any Description'

Output:

Tarea creada satisfactoriamente!
```

### Mostrando una lista de tareas
```bash
couler list

output:

Status  Description     ID

𐄂       Any Description 24a805c0
✔       Some one        876724b2
```

### Marcando una tarea como completada
```bash
couler check 876724b2 //id task

output:

Tarea completada con exito!
```

### Eliminando tareas

```bash
couler delete 876724b2

output:

Tarea eliminada con satisfactoriamente!
```