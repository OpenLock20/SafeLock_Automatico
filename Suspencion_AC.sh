#!/bin/bash

# Desactivar la suspensión en AC
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 0

echo "La suspensión en AC ha sido desactivada."

