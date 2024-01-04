# Calculateur de Rémunération pour Freelance

Ce projet est un outil de calcul de rémunération pour les freelances. Il permet de calculer la rémunération mensuelle basée sur le Taux Journalier Moyen (TJM) et le nombre de jours travaillés par semaine. 

Il offre également la possibilité d'ajuster le TJM pour maintenir le même revenu mensuel tout en modifiant le nombre de jours de travail.

## Fonctionnalités

- Calcul de la rémunération mensuelle en fonction du TJM et du nombre de jours de travail par semaine.
- Ajustement du TJM pour maintenir la même rémunération en modifiant le nombre de jours de travail.

## Comment l'utiliser

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/woprrr/freelancer-tools.git
   ```
2. Naviguez vers le dossier du projet :
   ```bash
   cd freelancer-tools
   ```
3. Exécutez le script principal :
   ```bash
   python main_script.py
   ```

## Exemple d'Utilisation

Lorsque vous exécutez `main_script.py`, le script vous demandera :

1. Votre Taux Journalier Moyen (en euros).
2. Le nombre de jours de travail par semaine.
3. Si vous souhaitez modifier le nombre de jours travaillés tout en conservant votre revenu mensuel (réponse oui/non).
4. Le nouveau nombre de jours de travail par semaine (si vous avez répondu oui à la question précédente).

## Tests

Des tests unitaires et fonctionnels sont inclus. Pour les exécuter :

```bash
python -m unittest test_business_logic.py test_main_script.py
```

ou pour jouer toute la suite d'un coup.

```bash
python -m unittest
```

## Contributions

Les contributions sont les bienvenues. Veuillez suivre les bonnes pratiques de développement et maintenir la qualité du code.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/woprrr/freelancer-tools/blob/main/LICENSE) pour plus de détails.
