#!/bin/bash

icono=$PWD/pdfsenuno.svg
ejecutable=$PWD/pdfsenuno.py
cat > ~/.local/share/applications/pdfsenuno.desktop << EOF
[Desktop Entry]
Type=Application
Categories=Utilitario
Name=PDFs en Uno
Comment=Juntar PDFs en Uno
Icon=$icono
Exec=python $ejecutable
Terminal=false
EOF

