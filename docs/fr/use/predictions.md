---
source_hash: 74f3d09e63
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="./images/CrystalBall.png" style="width:5%;" />&ensp;Simulations prédictives
:::

Les paramètres de simulation prédictive de xDrip sont une fonction expérimentale, non approuvée médicalement. Relisez bien le [CLUF](../install/install#understand-what-is-xdrip) avant de l'activer. Ne vous en servez pas pour prendre des décisions médicales.

::: warning Attention
Si vous utilisez un système en boucle fermée, ne vous fiez pas à ces prédictions, car elles ne tiennent pas compte de la modulation du débit basal.
:::

::: xdripitem xDrip+ Simulations prédictives
&ensp;Afficher les simulations mathématiques basées sur les données de profil et les logs de glucides/insuline
:::

Activer les prédictions ajoute la courbe de prédiction violet clair sur le graphique principal. Cette courbe vous montre comment votre glycémie devrait théoriquement évoluer en fonction de l'insuline et des glucides saisis dans xDrip. Plus de détails sur l'affichage [ici](./display#treatments-and-predictions-curves).

<img src="./images/M-S-PS1a.png" style="zoom:75%;" />

xDrip peut gérer plusieurs types d'insuline. Voir [ci-dessous](#multiple-insulin-types).

::: xdripitem Types d'insuline multiples
&ensp;Options pour utiliser plusieurs types d'insuline
:::

### Ratio de glucides et sensibilité à l'insuline {#carb-ratio-and-insulin-sensitivity}

::: info Import automatique
Si vous utilisez [Accepter les traitements](./interapp#receiving-from-nsclient) depuis AAPS ou NSClient, ces paramètres et le profil basal sont importés automatiquement lors d'un changement de profil.
:::

Ces paramètres sont essentiels à la gestion du diabète et doivent être connus.  
Ils varient très probablement au cours de la journée et doivent être calculés pour chaque repas, ainsi qu'en dehors des repas.  
Chacun a ses propres paramètres. N'utilisez pas ceux de quelqu'un d'autre.

Le ratio de glucides est la quantité de glucides couverte par 1 unité d'insuline.

Par exemple, 10 signifie que chaque tranche de 10 g de glucides nécessite 1 unité d'insuline.

::: xdripitem Ratio de Glucides
&ensp;Ratio insuline:glucides 1u pour X grammes de glucides
:::

La sensibilité à l'insuline est la baisse de glycémie obtenue avec une unité d'insuline, sans glucides dans le sang.

Par exemple, 50 (ou 2,8) signifie qu'1 unité fait baisser la glycémie de 50 mg/dl (ou 2,8 mmol/l).

::: xdripitem Sensibilité à l'Insuline
&ensp;Baisse de la glycémie pour 1 Unité
:::

### Taux d'absorption des glucides {#carb-absorbtion-rate}

Le taux d'absorption des glucides est la vitesse à laquelle votre organisme assimile les glucides. Voir [ici](https://diyps.org/2014/05/29/determining-your-carbohydrate-absorption-rate-diyps-lessons-learned/) comment calculer ce paramètre.

::: xdripitem Taux d'absorption de glucides
&ensp;Glucides linéaires absorbés par heure
:::

Appuyer sur l'un des deux menus ci-dessus ouvre l'éditeur de profil de traitement.

<img src="./images/M-S-PS4a.png" style="zoom:75%;" />

Vous pouvez définir les glucides par unité d'insuline et le facteur de correction : pensez simplement à valider chaque saisie et à ne pas passer d'une ligne à l'autre sans l'avoir confirmée. Enregistrez une fois terminé.

<img src="./images/M-S-PS4b.png" style="zoom:75%;" />

Vous allez créer des blocs pour différentes heures de la journée.  
Pour créer (scinder) ou supprimer un bloc, faites un appui long sur la partie supérieure du bloc.

  <img src="./images/M-S-PS4c.png" style="zoom:75%;" />

Appuyer sur la barre horaire en haut d'un bloc permet de la modifier ; la modification se répercute aussi sur le bloc en dessous.  
Vous finirez par obtenir quelque chose comme ceci.

<img src="./images/M-S-PS4d.png" style="zoom:75%;" />

Si nécessaire, vous pouvez appliquer une modification globale en pourcentage à tous les paramètres avec le curseur du bas.  
N'oubliez pas d'enregistrer.

<img src="./images/M-S-PS4e.png" style="zoom:75%;" />

### Éditeur de profil Basal {#basal-profile-editor}

::: info Cette fonction est en cours de développement.
Le profil basal actuel est importé automatiquement depuis NSClient lorsque [Accepter les traitements](./interapp#receiving-from-nsclient) est activé.
:::

::: xdripitem Éditeur de profil Basal
&ensp;Éditeur graphique pour les profils basal de la pompe
:::

Vous pouvez afficher et modifier votre profil basal.

1. Sélectionnez le profil à modifier ou à afficher
2. Exporter (pas encore fonctionnel)
3. Enregistrer localement

<img src="./images/M-S-PS4f2.png" style="zoom:78%;" />

Pour modifier votre profil basal :

1.  Appuyez sur la barre horaire du basal à modifier : elle devient orange
2. Changez le pas si nécessaire
3. Utilisez la case numérotée positive ou la flèche vers le haut pour augmenter
4. Utilisez la case numérotée négative ou la flèche vers le bas pour diminuer
5. Utilisez set, ou appuyez deux fois sur la barre, pour appliquer la nouvelle valeur

<img src="./images/M-S-PS4f3.png" style="zoom:78%;" />

### Utiliser la tendance dynamique {#use-trend-momentum}

La tendance dynamique est indépendante des prédictions : c'est simplement une extrapolation mathématique de votre tendance glycémique actuelle (hausse/baisse/stable), c'est-à-dire : si la glycémie continue d'évoluer selon sa tendance, sans tenir compte de l'insuline et des glucides, où ira-t-elle ? Elle peut être utilisée pour les [alarmes de prévision de bas](./alarms#forecasted-low-alert).

La tendance dynamique peut être intégrée aux prédictions (recommandé).

::: xdripitem Utiliser la tendance dynamique
&ensp;Calculer y compris la tendance de glycémie
:::

Inclure la tendance actuelle (1) peut éviter des variations brusques de la prédiction et se rapprocher davantage de l'évolution réelle (2).

<img src="./images/M-S-PS5a.png" style="zoom:75%;" />

<img src="./images/M-S-PS5b.png" style="zoom:75%;" />

<img src="./images/M-S-PS5c.png" style="zoom:75%;" />

### CLUF {#eula}

Relisez le [CLUF](../install/install#understand-what-is-xdrip) avant d'utiliser cette fonction.

::: xdripitem Contrat de licence de l'utilisateur final
&ensp;Non destiné à l'usage médical - outil de recherche uniquement
:::

### Prédiction bas niveau {#low-level-prediction}

Vous pouvez configurer ici d'autres paramètres de prédiction.

::: xdripitem Valeurs de niveau de prédiction d'hypoglycémie
&ensp;Paramètres avancés pour les algorithmes
:::

La cible est utilisée par le calculateur de bolus. C'est la glycémie cible souhaitée.

La [durée d'action](https://www.diabettech.com/insulin/why-we-are-regularly-wrong-in-the-duration-of-insulin-action-dia-times-we-use-and-why-it-matters/) de l'insuline dépend de votre type d'insuline. Modifier cette valeur nécessite de redémarrer xDrip (ou le téléphone).

La glycémie cible est la valeur utilisée pour calculer les corrections suggérées.

::: xdripitem Glycémie cible par défaut
&ensp;100 / 5.6
:::

La durée d'action de l'insuline est un paramètre à discuter avec votre diabétologue. Avec un système en boucle fermée, cette valeur sera bien plus élevée. N'oubliez pas cependant que les prédictions de xDrip sont surtout utiles en multi-injections, pas avec une pompe.

::: xdripitem Durée de l'insuline en heures
&ensp;3
:::

Les paramètres hépatiques ont été introduits pour tenir compte de la réaction du glycogène hépatique aux hypoglycémies, mais ils sont difficiles à caractériser et doivent rester à leurs valeurs par défaut.

::: xdripitem Ratio de sensibilité du foie par défaut
&ensp;2
:::

::: xdripitem Impact maximum sur le foie par défaut (0-1)
&ensp;0.8
:::

### Types d'insuline multiples {#multiple-insulin-types}

::: xdripitem Types d'insuline multiples
:::

Sélectionnez les types d'insuline que vous utilisez.

Vous pouvez sélectionner jusqu'à trois types d'insuline, puis choisir celui utilisé pour le basal et celui utilisé pour le bolus.

::: xdripitem Editeur de profil de traitement
Activer au moins un et maximum trois profils.  
&ensp;☐&emsp;FIASP (ultra-fast acting)  
&ensp;☐&emsp;Afrezza (ultra-fast acting)  
&ensp;☐&emsp;Apidra (ultra-fast acting)  
&ensp;☐&emsp;Novorapid (fast acting)  
&ensp;☐&emsp;Humalog (fast acting)  
&ensp;☐&emsp;Lispro (fast acting)  
&ensp;☐&emsp;Actrapid (short acting)  
&ensp;☐&emsp;Insulatard (NPH)  
&ensp;☐&emsp;Toujeo (long acting)  
&ensp;☐&emsp;Lantus (long acting)  
&ensp;☐&emsp;Levemir (long acting)  
&ensp;☐&emsp;Basaglar (long acting)  
&ensp;☐&emsp;Tresiba (ultra-long acting) 
:::

Dans la partie inférieure de la boîte de dialogue, sélectionnez l'insuline utilisée pour le basal (action lente) et pour le bolus (action rapide) :

::: xdripitem Choisir le profil d'insuline basale.
:::

::: xdripitem Choisir le profil d'insuline de bolus. Également utilisé pour la pompe et le stylo...
:::

Une fois terminé, enregistrez vos choix.

::: xdripitem <span style="background-color: grey; color: white;"> &ensp;ANNULER&ensp;</span> &emsp;<span style="background-color: grey; color: white;"> &ensp;RÉINITIALISER&ensp;</span>  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white;"> &ensp;SAUVER&ensp;</span>  &emsp;
:::

Lorsque plusieurs types d'insuline sont configurés, l'utilisation des [traitements](./mainUI#treatments) vous demandera de choisir celui que vous utilisez pour ce traitement.

<img src="./images/M-S-PS2b3.png" style="zoom:75%;" />

Vous pouvez ajouter l'insuline basale à l'affichage et l'intégrer au calcul.  
Ce n'est pas recommandé, car en multi-injections l'insuline basale sert seulement à maintenir une glycémie de fond constante.  
Utilisez les [notes](./mainUI#treatment-notes) pour suivre les injections de basale.

Les différents types d'insuline s'affichent de façon identique sur le graphique principal.

::: xdripitem Utiliser l'activité Basal
&ensp;Tracer l'activité basale sur le graphique et l'incorporer dans le modèle prédictif
:::

<img src="./images/M-S-PS2c2.png" style="zoom:75%;" />

<br>

[*Dernière modification le 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
