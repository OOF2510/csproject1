#!/usr/bin/env bash
echo "[Desktop Entry]
Version=1.0
Type=Application
Name=AutoClicker
Comment=
Exec=python3 /workspace/csproject1/src/main.py
Icon=application-x-executable
Path=
Terminal=true
StartupNotify=false" > /home/gitpod/Desktop/AutoClicker.desktop
chmod +x /home/gitpod/Desktop/AutoClicker.desktop
sudo apt-get update
sudo apt-get install -y build-essential cmake fonts-noto fonts-noto-color-emoji fonts-noto-extra python3 python3-pip python3-tk
pip3 install -r /workspace/csproject1/requirements.txt
