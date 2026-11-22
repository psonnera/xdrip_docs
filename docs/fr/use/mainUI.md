---
source_hash: 3c47ed9511
source_commit: ea9ce3a
---
### Découvrir l'interface {#meet-the-user-interface}

Bienvenue dans xDrip !

<img src="./images/UI-basic.png" style="zoom:50%;" />

Si vous venez d'installer xDrip, commencez par quelques personnalisations de base :

1. [Choisissez l'unité d'affichage de votre glycémie](./settings)
2. [Ajoutez des alarmes](./alarms)
3. Si xDrip est connecté à un capteur, [partagez les données avec un autre téléphone équipé de xDrip](./syncsetup)
4. Affichez xDrip sur le téléphone lorsque [l'écran est verrouillé](./display#numbered-wall-on-locked-screen)
5. Ajoutez un [widget](#widget) sur l'écran d'accueil de votre téléphone
6. Ajoutez une [montre connectée](../smartwatch/smartwatch)
7. Partagez vos données avec votre diabétologue grâce à [Tidepool](https://www.tidepool.org/) : si vous avez un compte Tidepool, il suffit de [configurer xDrip](./cloud#tidepool)
8. Envoyez vos données vers [Nightscout](https://nightscout.github.io/) (recommandé)

### Indications de base {#basic-indications}

Voici les indications affichées par défaut lorsque xDrip reçoit des données.

<img src="./images/UI-indications.png" style="zoom:75%;" />

1. Depuis combien de temps la valeur a été reçue, et l'écart de glycémie avec la valeur précédente.
2. La dernière valeur de glycémie mesurée.
3. La tendance par rapport à la mesure précédente.

##### Flèche de tendance {#trend-arrow}

::: info Remarque
La flèche indique la tendance par rapport à la mesure précédente. D'autres applications CGM utilisent un algorithme pour calculer cette indication : le résultat peut donc être différent.  
En cas de valeurs manquantes, la flèche peut indiquer une hausse ou une chute rapide : comparez toujours avec l'indication `1`.
:::

Vous pouvez personnaliser les informations affichées en `1` dans les [Paramètres de Graph](./display#graph-settings).

Vous pouvez [personnaliser l'aspect de la flèche de tendance](#blood-drop-menu), mais pas son comportement (elle utilise toujours l'écart avec la valeur précédente).

Voici comment s'affiche la flèche de tendance classique, en fonction de l'écart entre la glycémie précédente et la glycémie actuelle.

| Écart de glycémie (précédente et actuelle)                   |                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| Variation d'au plus +/- 5 mg/dl (0,28 mmol/l)                | <img src="./images/ArrowFlat.png" style="zoom:75%;" />   |
| Variation supérieure à la précédente et inférieure à +/- 10 mg/dl (0,56 mmol/l) | <img src="./images/ArrowUpDn.png" style="zoom:75%;" />   |
| Variation supérieure à la précédente et inférieure à +/- 17,5 mg/dl (0,97 mmol/l) | <img src="./images/ArrowUpDn+.png" style="zoom:75%;" />  |
| Variation supérieure à la précédente                         | <img src="./images/ArrowUpDn++.png" style="zoom:75%;" /> |



### Traitements {#treatments}

Vous pouvez enregistrer des traitements avec l'icône de seringue.

<img src="./images/UI-Treat.png" style="zoom:75%;" />

Ajoutez un ou plusieurs éléments à votre traitement.

#### Glycémie capillaire {#blood-test}

Elle s'affiche dans l'unité choisie dans xDrip.

<img src="./images/UI-Treat1.png" style="zoom:75%;" />

#### Grammes de glucides {#grams-of-carbs}

<img src="./images/UI-Treat2.png" style="zoom:75%;" />

#### Unités d'insuline {#units-of-insulin}

::: info Remarque
Si vous avez activé [plusieurs types d'insuline](./predictions#multiple-insulin-types), sélectionnez aussi le type d'insuline de ce traitement.
:::

<img src="./images/UI-Treat3.png" style="zoom:75%;" />

#### Heure {#time}

Et enfin l'heure du traitement (si ce n'est pas maintenant), au format 24 heures, avec ou sans séparateur.

::: info Remarque
Vous pouvez choisir une heure de traitement entre 23 heures dans le passé et 1 heure dans le futur.
:::

<img src="./images/UI-Treat4.png" style="zoom:75%;" />

Les traitements sont valides lorsque la coche verte apparaît en haut à droite. Appuyez dessus pour confirmer la saisie.

<img src="./images/UI-Treat6.png" style="zoom:75%;" />

Un résumé s'affiche. Appuyez sur l'icône verte `+` pour confirmer ou sur l'icône rouge `x` pour annuler.

<img src="./images/UI-Treat5.png" style="zoom:75%;" />

Une fois validés, de nouveaux symboles apparaissent sur votre graphique.

Les unités et les glucides s'affichent ainsi :

<img src="./images/UI-Treat7.png" style="zoom:75%;" />

Et les glycémies capillaires ainsi (le symbole est carré, contrairement aux [calibrations](../calibrate/calibrate) qui sont rondes) :

<img src="./images/UI-Treat8.png" style="zoom:75%;" />

#### Modifier et supprimer {#edit-and-delete}

Lorsqu'ils sont visibles, vous pouvez supprimer les traitements ainsi :

- Appuyez sur le traitement, puis regardez en bas de l'écran : appuyez sur Ajouter une note 

<div style="background-color: black; color: white; text-align: left;">  &emsp;18:45 Traitement&emsp;<span style="color: cyan; float: right;">AJOUTER UNE NOTE&emsp;</span></div>

ou sur Glycémie.

<div style="background-color: black; color: white; text-align: left;">  &emsp;10:06 85 mg/dl&emsp;<span style="color: cyan; float: right;">GLYCÉMIE&emsp;</span></div>

- Vous pouvez saisir une note ou appuyer sur EFFACER pour supprimer l'entrée. Cela s'applique aux glycémies capillaires, aux glucides et à l'insuline.

::: xdripitem Remarque sur le traitement
<span style="color: cyan;">_____________________________________________________________________________________</span>  
<small>Utiliser la saisie vocale la prochaine fois</small> ☐  


<span style="color: cyan; float: left;">EFFACER&emsp;</span><span style="color: cyan; float: right;">ANNULER&emsp;TERMINÉ&emsp;</span>
:::

Si vous appuyez sur une glycémie capillaire pour la modifier, vous pouvez aussi la convertir en calibration avec CALIBRER. C'est possible si vous n'avez pas sélectionné **Never use them** dans la [Calibration avancée](../calibrate/advancedcal).

::: xdripitem Action de test sanguin
Que voulez-vous faire?  


<span style="color: cyan; float: left;">RIEN&emsp;</span><span style="color: cyan; float: right;">EFFACER&emsp;CALIBRER&emsp;</span>
:::

##### Traitements dictés {#spoken-treatments}

Vous pouvez utiliser l'icône du microphone pour saisir oralement des traitements ou des commandes avancées.

Un appui long sur l'icône du microphone vous permet d'écrire des [commandes avancées](./spokencommands).

### Notes de traitement {#treatment-notes}

Indépendamment des traitements, vous pouvez saisir des notes.

<img src="./images/UI-Note.png" style="zoom:75%;" />

Saisissez le commentaire de votre choix (par exemple des unités d'insuline lente), ou utilisez l'icône du microphone pour dicter la note.

::: xdripitem Remarque sur le traitement
<span style="color: cyan;">_____________________________________________________________________________________</span>  
<small>Utiliser la saisie vocale la prochaine fois</small> ☐  


<span style="color: cyan; float: left;">EFFACER&emsp;</span><span style="color: cyan; float: right;">ANNULER&emsp;TERMINÉ&emsp;</span>
:::



Elles sont ajoutées au graphique ainsi :

<img src="./images/UI-Note2.png" style="zoom:75%;" />

Appuyez dessus pour les modifier ou les supprimer.

### Annuler et Rétablir {#undo-and-redo}

1. Annuler revient en arrière dans les simulations de traitements, les calibrations et les notes. Au bout de 30 minutes, le bouton disparaît à nouveau.
2. Rétablir avance de nouveau dans les simulations de traitements, les calibrations et les notes. Au bout de 30 minutes, le bouton disparaît à nouveau.

<img src="./images/UI-UndoRedo.png" style="zoom:77%;" />

### [Menu principal](./hamburger) {#main-menu}

Aussi appelé menu hamburger ou tiroir de navigation, c'est le menu principal : vous y trouverez ou y ajouterez les actions les plus courantes, ainsi que tous les paramètres et personnalisations.

<img src="../images/hamburger_menu.png" style="zoom:75%;" />

### Menu goutte de sang {#blood-drop-menu}

Un appui long sur la zone centrale, entre le menu principal et le menu trois points, ouvre un autre menu pour personnaliser l'interface.

<img src="../images/UImenu.png" style="zoom:75%;" />

##### Bouton de l'assistant source {#source-wizard-button}

Affiche le bouton qui vous guide dans le choix de la source de données, comme décrit [ici](../install/datasource).

::: xdripitem <span style="background-color: grey; color: white;">  &emsp;&emsp;DÉMARRER L'ASSISTANT CONFIGURATION DE SOURCE&emsp;</span>
:::

##### Afficher les boutons de l'heure {#show-time-buttons}

Ajoute une rangée de quatre préréglages pour la durée affichée sur le graphique principal : 24, 12, 6 et 3 heures.  
Un appui long sur un bouton verrouille l'affichage sur cette durée.

::: xdripitem <span style="background-color: grey; color: white;"> &ensp;24 HEURES&ensp;</span> &emsp;<span style="background-color: grey; color: white;"> &ensp;12 HEURES&ensp;</span>  &emsp;<span style="background-color: grey; color: white;"> &ensp;6 HEURES&ensp;</span>  &emsp;<span style="background-color: grey; color: white;"> &ensp;3 HEURES&ensp;</span>
:::

##### Période de vérouillage toujours utilisée {#locked-time-period-always-used}

Utilise par défaut la dernière durée d'affichage choisie.

##### Afficher l'aperçu du graphique {#show-chart-preview}

Active ou désactive le petit graphique sur 24 heures en bas de l'écran.

<img src="./images/UI-ChartPreview.png" style="zoom:75%;" />

##### Afficher le statut du Collecteur {#show-collector-status}

Affiche sous le graphique principal des messages d'information sur l'état du collecteur.

<img src="./images/UI-CollStatus.png" style="zoom:75%;" />

##### Afficher l'expiration du capteur {#show-sensor-expiry}

Affiche sous le graphique principal le temps restant avant l'expiration du capteur.

<img src="./images/UI-SensorExpiry.png" style="zoom:75%;" />

##### Afficher la flèche de tendance graphique {#show-graphical-trend-arrow}

Ajoute une option pour choisir d'autres styles de flèche.

Utilisez la clé <img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_wrench_grey600_48dp.png" style="width:3%;" /> et le menu déroulant ▼ pour les sélectionner.  
Les flèches en couleur comportent un curseur de teinte pour changer la couleur. 

L'angle des flèches de tendance graphiques dépend de l'écart avec la valeur précédente (5 minutes), et non pas seulement plat/45/90 degrés comme les flèches classiques.

<img src="./images/UI-GraphicArrow.png" style="zoom:90%;" />

### [Menu trois points](./3dotsmenu) {#three-dots-menu}

Ce menu contient des raccourcis vers des paramètres et d'autres fonctions spécifiques.

<img src="../images/3dots_menu.png" style="zoom:75%;" />

### Widget {#widget}

Si votre téléphone prend en charge les widgets, faites un appui long sur une zone vide de l'écran d'accueil et sélectionnez Widgets.  
Faites défiler les applications jusqu'à trouver xDrip. 

<img src="./images/Widget1.png" style="zoom:75%;" />

Gardez le doigt sur le widget et faites-le glisser à l'emplacement souhaité.

<img src="./images/Widget2.png" style="zoom:75%;" />

Vous pouvez le redimensionner avec les points bleus.

<img src="./images/Widget3.png" style="zoom:75%;" />

Donnez-lui la taille qui vous convient. Vous pouvez ensuite personnaliser les couleurs et l'aspect du contenu dans les [paramètres d'affichage](./display).

<img src="./images/Widget4.png" style="zoom:75%;" />

### Économiseur d'écran {#screensaver}

Si votre téléphone prend en charge cette fonction, vous pouvez activer xDrip comme économiseur d'écran dans les paramètres Android.

<img src="./images/ScreenSaver1.png" style="zoom:75%;" />

Lorsque le téléphone est en charge, il affiche un petit graphique et la valeur de glycémie.

<img src="./images/ScreenSaver2.png" style="zoom:75%;" />

<br>

[*Dernière modification le 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
