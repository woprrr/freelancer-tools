# Calculateur de Rémunération pour Freelance

Ce projet est un outil de calcul de rémunération pour les freelances. Il permet de calculer la rémunération mensuelle basée sur le Taux Journalier Moyen (TJM) et le nombre de jours travaillés par semaine. 

Il offre également la possibilité d'ajuster le TJM pour maintenir le même revenu mensuel tout en modifiant le nombre de jours de travail. Ce projet inclut également une application Django pour une interface web interactive.

## Fonctionnalités

- Calcul de la rémunération mensuelle en fonction du TJM et du nombre de jours de travail par semaine.
- Ajustement du TJM pour maintenir la même rémunération en modifiant le nombre de jours de travail.
- CommandeLine Django pour une utilisation en ligne de commmande.
- Interface web Django pour une utilisation facile et interactive. (En cours)

## Comment l'utiliser

### Utilisation de l'Application Web & Commande shell

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/woprrr/freelancer-tools.git
   ```
2. Naviguez vers le dossier du projet :
   ```bash
   cd freelancer-tools
   ```
3. Assurez-vous que Django est installé ou exécutez :
   ```bash
   pip install -r requirements.txt
   ```
4. Pour utiliser la commande personnalisée, exécutez :
   ```bash
   python manage.py freelance_calculate
   ```
5. Pour lancer le serveur Django et utiliser l'interface web, exécutez :
   ```bash
   python manage.py runserver
   ```
6. Accédez à l'application via un navigateur web à l'adresse `http://localhost:8000`.

### Dans l'Application Web

Suivez les instructions à l'écran dans l'interface web pour effectuer des calculs de rémunération.

## Tests

Des tests unitaires et fonctionnels sont inclus pour les composants Django. Pour exécuter les tests avec coverage :

```bash
coverage run --source='.' manage.py test
coverage report
```

Pour générer un rapport en HTML :

```bash
coverage html
```

Les rapports HTML seront disponibles dans le dossier `htmlcov`.

## Contributions

Les contributions sont les bienvenues. Veuillez suivre les bonnes pratiques de développement Python et maintenir la qualité du code.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/woprrr/freelancer-tools/blob/main/LICENSE) pour plus de détails.
