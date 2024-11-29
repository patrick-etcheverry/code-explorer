#!/bin/bash

# Liste tous les fichiers suivis par Git
for file in $(git ls-files); do
    # Modifie la date du fichier sans toucher son contenu
    touch "$file"
    git add "$file"
done

# Committez avec un message approprié
git commit -m "Mise à jour des métadonnées de date des fichiers"
