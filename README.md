# Test Enoki

## Requirements

Assurez-vous d'avoir docker et docker compose sur votre machine.

## Lancement

Clôner le projet :
```bash
git@gitlab.com:ryanfadeau/test-enoki.git
```
Lancer les docker : 

```bash
sudo docker-compose build
sudo docker-compose up
```
Dans un autre terminal, rentrer dans le container python et faire les migrations:
```bash
docker-compose exec python bash
python manage.py migrate
```
Vous pouvez créer un super user si vous le souhaitez : 
```bash
python manage.py createsuperuser
```

Aller à l'adresse : http://127.0.0.1:8000/ et l'application devrait démarrer

### Visualiser la base de donnée avec pgadmin
Aller à l'adresse : http://127.0.0.1:16543/
email: enoki@hotmail.fr
password : enoki