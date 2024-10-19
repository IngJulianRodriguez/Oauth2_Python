1. Instalar Dependencias:
Asegúrate de tener requests y cryptography instalados. Puedes instalarlos usando pip:
pip install -r requirements.txt

2. Configurar el Proyecto:
Llena el archivo config.json con las credenciales de tus proveedores de OAuth2.

3. Ejecutar el Ejemplo de Uso:
Ejecuta example_usage.py para probar la autenticación y autorización con uno de los proveedores configurados:
python example_usage.py

4. Ejecutar Pruebas:
Ejecuta las pruebas unitarias para asegurarte de que todo funciona correctamente:
python test_oauth2_client.py

5. Seguridad:
Asegúrate de almacenar la clave de cifrado generada en token_storage.py de manera segura.

6. Ejemplo de implementación
En el archivo app.py se muestra un ejemplo de implementación del artefacto en un proyecto existente