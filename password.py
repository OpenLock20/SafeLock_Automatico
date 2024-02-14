import subprocess

def cambiar_contrasena(usuario, nueva_contrasena):
    # Comando que cambia la contraseña del usuario.
    comando = f"echo '{usuario}:{nueva_contrasena}' | sudo chpasswd"
    
    # Ejecutar el comando.
    proceso = subprocess.run(comando, shell=True, check=True)

cambiar_contrasena('safelock', 'S4f3L0ck.1.2017')
