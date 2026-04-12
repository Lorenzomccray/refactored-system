#!/bin/bash
set -e
INSTALL_DIR="$HOME/sovereignty-mcp"
echo "[sovereignty-mcp] Installing to $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# Install venv and deps
cd "$INSTALL_DIR"
python3 -m venv venv
venv/bin/pip install -q --upgrade pip
venv/bin/pip install -q mcp supabase httpx python-dateutil

# Make pulse script executable
chmod +x sovereignty/system_pulse.sh
cp sovereignty/system_pulse.sh ~/system_pulse.sh

# Install systemd service
sudo cp sovereignty-mcp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sovereignty-mcp
sudo systemctl restart sovereignty-mcp
echo "[sovereignty-mcp] Done. Status:"
sudo systemctl status sovereignty-mcp --no-pager
