# 🩸 BloodHound Setup Guide for AD Lab

## What is BloodHound?

BloodHound is a tool to analyze Active Directory relationships and find attack paths.

## Installation

### Linux (Kali/Ubuntu)

```bash
# Install Neo4j
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 4.4' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt update
sudo apt install neo4j

# Install BloodHound
sudo apt install bloodhound

# Start Neo4j
sudo systemctl start neo4j
