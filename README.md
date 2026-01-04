# Odoo_Event 🎉

## 📌 Description du projet
**Odoo_Event** est un module Odoo dédié à la **gestion des événements**.  
Il permet de créer, organiser et suivre des événements via une interface intuitive intégrée à Odoo.

Ce projet a été réalisé dans un cadre **académique**, en respectant la structure standard d’un module Odoo et en utilisant **Docker** pour simplifier l’installation et l’exécution de l’environnement.

---

## ⚙️ Fonctionnalités principales
- Création et gestion des événements
- Ajout d’une image pour chaque événement
- Localisation de l’événement via une carte
- Gestion des participants
- Génération de documents PDF
- Statistiques et tableaux de suivi
- Interface simple et ergonomique

---

## 🛠️ Technologies utilisées
- **Odoo**
- **Python**
- **XML**
- **Docker & Docker Compose**
- **PostgreSQL**
- **HTML / CSS (QWeb)**

---

## 📂 Structure du projet
Odoo_Event/
│── addons/
│ └── tp_gestion_event/
│ ├── models/
│ ├── views/
│ ├── security/
│ ├── reports/
│ ├── manifest.py
│ └── init.py
│── docker-compose.yml
│── README.md


---

## 🚀 Installation et exécution

### 🔹 Prérequis
- Docker
- Docker Compose

### 🔹 Étapes d’installation

1. Cloner le dépôt :
git clone https://github.com/Inessbounouifa/Odoo_Event.git
cd Odoo_Event
2. Lancer les conteneurs Docker :
docker-compose up -d
3. Accéder à Odoo via le navigateur :
http://localhost:8069


