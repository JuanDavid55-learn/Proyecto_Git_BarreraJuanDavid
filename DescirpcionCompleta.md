"Empanadas Doña Pepa" es un emprendimiento dedicado a la venta de empanadas artesanales con diversos sabores y estilos. Para mejorar la gestión de su tienda y centralizar la información, el equipo ha decidido implementar un sistema que permita registrar los productos disponibles (empanadas) y optimizar su desarrollo colaborativo mediante Git y GitHub para tener toda la trazabilidad del desarrollo del proyecto.



### **Especificaciones Técnicas del Módulo**

1. **Gestión de Productos (Empanadas)**

- **Información Básica**: Registrar cada tipo de empanada con datos como el nombre, precio, ingredientes principales y disponibilidad (sí/no).
- **Gestión de Datos**: Permitir agregar nuevos tipos de empanadas, editar información existente y eliminar registros de empanadas descontinuadas.
- **Almacenamiento Local**: Los datos se deben guardar en un archivo JSON para garantizar un acceso y manipulación sencillos.

1. **Control de Versiones**

- **Ramas**: Utilizar al menos tres ramas adicionales a `main`, nombradas según su funcionalidad (ej. `feature/add-empanadas`, `feature/edit-empanadas`, `feature/delete-empanadas`).
- **Commits**: Realizar commits descriptivos y frecuentes que reflejen cada avance en el desarrollo del módulo.
- **Pull Requests (PRs)**: Crear PRs claros y detallados para integrar cambios en la rama principal. , donde cada PR debe incluir una descripción de los cambios realizados.

1. **Resolución de Conflictos**

- Simular un conflicto entre ramas para resolverlo manualmente. Documentar el proceso y la solución en el archivo README.

1. **Automatización y Organización**

- **GitHub Actions**: Configurar un flujo de trabajo que valide el formato del archivo JSON para evitar errores de sintaxis.
- **Issues y Proyectos**: Crear al menos 4 issues relacionados con las funcionalidades del módulo. Gestionarlos en un proyecto tipo kanban para organizar el flujo de trabajo.
- **Tags**: Generar un tag al finalizar el desarrollo del módulo indicando la versión estable (`v1.0.0`).

1. **Documentación**

- El repositorio debe incluir un README que contenga:
- Introducción al proyecto.
- Instrucciones de instalación y uso del sistema.
- Detalles del flujo de trabajo utilizado y estructura del repositorio.



Resultado esperado

La entrega de este trabajo se realizará de manera individual, donde se debe anexar un enlace a un repositorio público en GitHub llamado “Proyecto_Git_ApellidoNombre” (Proyecto_Git_Apellido1Nombre1Apellido2Nombre2 donde aplique) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

- Archivo principal de ejecución basado en Python.
- Archivos modularizados que den funcionalidad al programa principal de Python.
- Archivo JSON que almacene la información del programa en sí.
- Trazabilidad del progreso colectivo que hizo el equipo en el repositorio.
- Manejo de conflictos y `merges` entre ramas.
TrabajoPráctica_Git.md