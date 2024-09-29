# Proyecto SISVITA (SERVIDOR)

## Descripción:

La **API** para el proyecto que permite la realización de **tests de ansiedad**. Su objetivo es **evaluar y proporcionar** información sobre el **nivel de ansiedad** de los usuarios.

## Tecnologías:

- **Lenguaje de programación**: *Python*
- **Framework**: *Flask* 
- **Base de datos**: *PostgreSQL*

## Instalación:

1. **Clonar el repositorio:**

    ```bash
    git clone git@github.com:JoArDiTo/sisvita-backend.git
    cd sisvita-backend
    ```

2. **Crear y activar el entorno virtual:**

    - **Windows:**

      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

    - **Linux:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    En caso de no tener la librería **virtualenv** se puede instalar con el siguiente comando

    ```bash
    pip install virtualenv
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Tener la base de datos creada**

    Asegúrate de tener una **base de datos PostgreSQ**L creada y configurada. Puedes crear una base de datos con el siguiente comando:

    ```sql
    CREATE DATABASE nombre_de_tu_base_de_datos;
    ```

5. **Configurar las variables de entorno:**

    Crear un archivo `.env` en la raíz del proyecto siguiendo el patrón de `.env.local`. Asegúrate de configurar todas las variables necesarias.


6. **Ejecutar el programa:**

    ```bash
    flask run
    ```
