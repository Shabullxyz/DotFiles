import os
import shutil
import argparse

def limpiar_directorio():
    # Ruta del directorio actual
    directorio_actual = os.getcwd()

    # Lista de elementos a excluir
    elementos_a_excluir = {'.git', '.gitignore', 'limpieza.py', 'folders.py', 'update.sh', 'files.py', 'README.md', 'update.py', 'Dotfiles.py'}

    try:
        # Itera sobre todos los elementos del directorio
        for elemento in os.listdir(directorio_actual):
            # Ruta completa del elemento
            ruta_elemento = os.path.join(directorio_actual, elemento)

            # Verifica si el elemento debe excluirse
            if elemento not in elementos_a_excluir:
                if os.path.isfile(ruta_elemento):
                    # Elimina archivos
                    os.remove(ruta_elemento)
                    print(f"Archivo eliminado: {elemento}")
                elif os.path.isdir(ruta_elemento):
                    # Elimina directorios y su contenido
                    shutil.rmtree(ruta_elemento)
                    print(f"Directorio eliminado: {elemento}")

        print("Limpieza completada. Se conservaron archivos necesarios para el mantenimiento de los Dotfiles.")
    except Exception as e:
        print(f"Error al limpiar el directorio: {e}")



def copiar_archivos(directorio_destino):
    # Rutas específicas a archivos y directorios
    directorio_personal = os.path.expanduser("~")

    # Crear la carpeta 'inhome' en el directorio de destino
    carpeta_inhome = os.path.join(directorio_destino, "inhome")
    os.makedirs(carpeta_inhome, exist_ok=True)

    # Archivos a copiar en la carpeta 'inhome' (excepto settings.json)
    archivos_a_copiar = [".zshrc", ".xprofile", ".p10k.zsh", ".gitconfig", ".fzf.zsh"]

    # Copiar los archivos en la carpeta 'inhome'
    for archivo in archivos_a_copiar:
        origen = os.path.join(directorio_personal, archivo)
        destino = os.path.join(carpeta_inhome, archivo)
        shutil.copy(origen, destino)
        print(f"Archivo '{archivo}' copiado a '{carpeta_inhome}'")

    # Copiar settings.json manteniendo la estructura de carpetas
    destino_settings = os.path.join(directorio_destino, "Code", "User", "settings.json")
    
    # Crear los directorios necesarios si no existen
    os.makedirs(os.path.dirname(destino_settings), exist_ok=True)
    
    # Copiar el archivo
    shutil.copy(os.path.join(directorio_personal, ".config", "Code", "User", "settings.json"), destino_settings)
    print(f"Archivo 'settings.json' copiado a '{destino_settings}'")

    # Resto del código para copiar directorios (sin cambios)



def directorios(directorio_destino):
    # Rutas específicas a archivos y directorios
    directorio_personal = os.path.expanduser("~")
    # settings_json = os.path.join(directorio_personal, ".config", "Code", "User", "settings.json")
    nvim_custom_dir = os.path.join(directorio_personal, ".config", "nvim", "lua", "custom")

    # Verifica si el directorio de destino existe, si no, créalo
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    # Archivos a copiar
    #archivos_a_copiar = [".zshrc", ".xprofile", ".p10k.zsh", ".gitconfig", ".fzf.zsh"]

    # Directorios a copiar
    directorios_a_copiar = ["gtk-3.0", "kitty", "neofetch", "qtile", "ranger", "rofi", "xfce4"]

    # Copia archivos del directorio personal
    # for archivo in archivos_a_copiar:
    #     origen = os.path.join(directorio_personal, archivo)
    #     destino = os.path.join(directorio_destino, archivo)
    #     shutil.copy(origen, destino)
    #     print(f"Archivo '{archivo}' copiado a '{directorio_destino}'")

    # Copia settings.json desde Code/User/
    #shutil.copy(settings_json, os.path.join(directorio_destino, "settings.json"))
    #print(f"Archivo 'settings.json' copiado a '{directorio_destino}'")

    # Copia directorios del directorio personal
    for directorio in directorios_a_copiar:
        origen = os.path.join(directorio_personal, ".config", directorio)
        destino = os.path.join(directorio_destino, directorio)
        shutil.copytree(origen, destino)
        print(f"Directorio '{directorio}' copiado a '{directorio_destino}'")

    # Copia directorio nvim/lua/custom/
    destino_nvim = os.path.join(directorio_destino, "nvim", "lua", "custom")
    shutil.copytree(nvim_custom_dir, destino_nvim)
    print(f"Directorio 'nvim/lua/custom' copiado a '{directorio_destino}'")


def main():
    # Configuración del argumento de línea de comandos
    parser = argparse.ArgumentParser(description='Copia archivos y/o directorios a un directorio especificado.')
    parser.add_argument('directorio_destino', help='Directorio de destino donde copiar los elementos')

    # Analiza los argumentos de la línea de comandos
    args = parser.parse_args()

    # Llama a la función para copiar archivos y/o directorios
    copiar_archivos(args.directorio_destino)
    directorios(args.directorio_destino)

if __name__ == "__main__":
    limpiar_directorio()
    main()

