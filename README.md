# Configuración de Dotfiles para Qtile

Este repositorio contiene mi configuración personal de Dotfiles, diseñada para trabajar con el gestor de ventanas Qtile en mi sistema Linux. Los Dotfiles incluyen ajustes y personalizaciones que he aplicado para mejorar la experiencia de usuario con Qtile y adaptar el entorno para que sea mas sencillo trabajar en el.

## Acerca de Qtile

[Qtile](http://www.qtile.org/) es un gestor de ventanas de código abierto y extremadamente configurable para el sistema X Window. Se diferencia por su enfoque en la configurabilidad y su extensibilidad mediante Python. La interfaz de usuario es impulsada principalmente por el teclado, lo que lo hace adecuado para aquellos que prefieren un control más preciso y eficiente sobre su entorno de escritorio.

## Estructura del Repositorio
```
.
├── dotcopy.py
├── gtk-3.0
│   └── bookmarks
├── kblyt.sh
├── kitty
│   ├── color.ini
│   └── kitty.conf
├── limpieza.py
├── neofetch
│   └── config.conf
├── nvim
│   └── lua
│       └── custom
│           ├── chadrc.lua
│           ├── configs
│           │   ├── conform.lua
│           │   ├── lspconfig.lua
│           │   └── overrides.lua
│           ├── highlights.lua
│           ├── init.lua
│           ├── mappings.lua
│           ├── plugins.lua
│           └── README.md
├── qtile
│   ├── config.py
│   ├── __pycache__
│   │   ├── config.cpython-311.pyc
│   │   └── spotify.cpython-311.pyc
│   └── spotify.py
├── ranger
│   ├── commands.py
│   ├── devicons.py
│   ├── plugins
│   │   ├── devicons_linemode.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── devicons_linemode.cpython-310.pyc
│   │       ├── devicons_linemode.cpython-311.pyc
│   │       ├── __init__.cpython-310.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── __pycache__
│   │   ├── devicons.cpython-310.pyc
│   │   └── devicons.cpython-311.pyc
│   ├── rc.conf
│   ├── rifle.conf
│   └── scope.sh
├── rofi
│   └── config.rasi
├── settings.json
├── update.sh
└── xfce4
    └── xfconf
        └── xfce-perchannel-xml
            ├── thunar.xml
            ├── xfce4-notifyd.xml
            ├── xfce4-power-manager.xml
            └── xfce4-settings-manager.xml
```
Este proyecto está bajo la Licencia [MIT](LICENSE).
