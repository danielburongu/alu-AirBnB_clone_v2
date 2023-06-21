#!/usr/bin/env bash

echo -e "\e[1;32m START\e[0m"

# Updating the packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated\e[0m"
echo

# Configure firewall
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allow incoming NGINX HTTP connections\e[0m"
echo

# Create the directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;32m Directories created\e[0m"
echo

# Add test string
echo "<h1>Welcome to www.beta-scribbles.tech</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
echo -e "\e[1;32m Test string added\e[0m"
echo

# Prevent overwrite
if [ -d "/data/web_static/current" ]; then
    echo "Path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current
fi
echo -e "\e[1;32m Prevent overwrite\e[0m"
echo

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

# Update Nginx configuration
sudo sed -i '/^server {/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
echo -e "\e[1;32m Nginx configuration updated\e[0m"
echo

# Restart Nginx
sudo service nginx restart
echo -e "\e[1;32m Nginx restarted\e[0m"
