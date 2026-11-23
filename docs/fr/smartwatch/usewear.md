---
source_hash: f17272d683
source_commit: 7a18e7c
---
Vous trouverez la documentation de référence [ici](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

## Découvrir l'extension Wear {#discover-wear-extension}

xDrip propose quatre cadrans natifs.

|                           XDrip                            |                      XDrip(BigChart)                       |
| :--------------------------------------------------------: | :--------------------------------------------------------: |
| <img src="./images/M-S-SW-AW-W1.png" style="zoom:75%;" /> | <img src="./images/M-S-SW-AW-W2.png" style="zoom:75%;" /> |
|                      **XDrip(Large)**                      |                     **XDrip(Circle)**                      |
| <img src="./images/M-S-SW-AW-W3.png" style="zoom:75%;" /> | <img src="./images/M-S-SW-AW-W4.png" style="zoom:75%;" /> |

Les cadrans avec graphique ont plusieurs éléments en commun avec l'écran principal de xDrip.

1. La dernière glycémie mesurée.  
   L'écart de glycémie avec la valeur précédente reçue.  
   La tendance par rapport à la mesure précédente.
2. Une ligne d'état.
3. Un graphique de glycémie.

 <img src="./images/M-S-SW-AW-SC1.png" style="zoom:75%;" />

Un double appui sur le graphique change l'échelle de temps.

<img src="./images/M-S-SW-AW-SC2.png" style="zoom:75%;" />

Comme l'extension Wear de xDrip contient une partie du code de l'application, vous trouverez des éléments de menu de xDrip sur la montre. Ils se trouvent dans les applications de la montre, et certains sont aussi accessibles depuis le graphique de la montre via le menu à trois points présent sur tous les cadrans.

<img src="./images/M-S-SW-AW-3DM.png" style="zoom:75%;" />

### xDrip Prefs. {#xdrip-prefs}

Ce menu contient les options d'affichage de votre cadran.  
Lorsque la montre est configurée en collecteur autonome, d'autres éléments sont visibles. Voir ci-dessous.

<img src="./images/M-S-SW-AW-XP.png" style="zoom:75%;" />

Le thème sombre affiche un fond noir avec un texte et un graphique blancs. S'il est désactivé, c'est l'inverse : fond blanc avec texte et graphique foncés.

<img src="./images/M-S-SW-AW-XP3.png" style="zoom:75%;" />

Refresh on change met à jour le cadran à chaque changement de données (toutes les 5 minutes au minimum). Si vous le désactivez, la montre mettra à jour son cadran toutes les minutes (ce qui consomme plus de batterie).

<img src="./images/M-S-SW-AW-XP4.png" style="zoom:75%;" />

Show treatment ajoute des points de traitement sur les cadrans avec graphique.

<img src="./images/M-S-SW-AW-XP5.png" style="zoom:75%;" />

Le format 24 heures force l'affichage de l'heure dans ce format.

<img src="./images/M-S-SW-AW-XP6.png" style="zoom:75%;" />

Show date affiche aussi la date sur le cadran.

<img src="./images/M-S-SW-AW-XP7.png" style="zoom:75%;" />

Si votre montre est configurée pour utiliser ses propres paramètres régionaux (langue), vous pouvez la forcer à utiliser ceux du téléphone.

<img src="./images/M-S-SW-AW-XP8.png" style="zoom:75%;" />

Les toasts sont des messages contextuels : vous pouvez les activer et obtenir des informations supplémentaires en appuyant sur les pas et l'état sur la montre.

<img src="./images/M-S-SW-AW-XP9.png" style="zoom:75%;" />

Si votre montre le permet et que vous avez autorisé xDrip Prefs. à accéder aux données des capteurs de la montre, le podomètre s'affichera sur le cadran et vous pourrez afficher les [données de pas](../use/display) dans xDrip sur votre téléphone.

<img src="./images/M-S-SW-AW-XP10.png" style="zoom:75%;" />

Si votre montre le permet et que vous avez autorisé xDrip Prefs. à accéder aux données des capteurs de la montre, la fréquence cardiaque s'affichera sur le cadran et vous pourrez afficher les [données de fréquence cardiaque](../use/display) dans xDrip sur votre téléphone.

<img src="./images/M-S-SW-AW-XP11.png" style="zoom:75%;" />

Si vous utilisez un système de boucle fermée open source (comme AAPS) qui diffuse des données vers xDrip, vous pouvez ajouter l'état de la boucle à la ligne d'état.

<img src="./images/M-S-SW-AW-XP12.png" style="zoom:75%;" />

Par défaut, le cadran affiche la batterie de l'appareil collecteur sous la forme `uploader` ou `wear`. Il s'agit d'une ancienne définition qui n'apporte rien si vous n'utilisez pas xDrip comme téléphone principal : elle n'affichera ni le niveau de batterie du téléphone principal ni celui d'un éventuel transmetteur, mais uniquement la batterie de votre téléphone et de votre montre.

<img src="./images/M-S-SW-AW-XP13.png" style="zoom:75%;" />

Permet d'afficher les cartes (alertes) avec un fond uni pour améliorer la lisibilité.

<img src="./images/M-S-SW-AW-XP14.png" style="zoom:75%;" />

Vous pouvez changer la taille de police de la ligne d'état : 10 ou 12 points.

<img src="./images/M-S-SW-AW-XP15.png" style="zoom:75%;" />

Vous pouvez changer la plage de temps du graphique, comme avec un double appui dessus.

<img src="./images/M-S-SW-AW-XP16.png" style="zoom:75%;" />

Ce menu contient les personnalisations du cadran circulaire.

<img src="./images/M-S-SW-AW-XP17.png" style="zoom:75%;" />

Couleur basse.

<img src="./images/M-S-SW-AW-XP18.png" style="zoom:75%;" />

Sur xDrip et xDrip Large, change la couleur du séparateur (ligne d'état) pour l'assortir au fond.

<img src="./images/M-S-SW-AW-XP19.png" style="zoom:75%;" />

Force update est disponible sur les montres Wear 2.0 et supérieures, s'il est proposé pour la version actuelle et activé comme expliqué [ici](./wearinstall#wear-os-2x-and-3x).

<img src="./images/M-S-SW-AW-XP20.png" style="zoom:75%;" />

Demigod est disponible pour les [montres modifiées](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5).

<img src="./images/M-S-SW-AW-XP21.png" style="zoom:75%;" />

### Keypad Treatment {#keypad-treatment}

Keypad Treatment est identique à l'[icône seringue](../use/mainUI#treatments) de xDrip.

<img src="./images/M-S-SW-AW-KT.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-XP22.png" style="zoom:75%;" />

### Spoken treatment {#spoken-treatment}

Spoken treatment (traitement vocal) fonctionne comme dans xDrip.

<img src="./images/M-S-SW-AW-ST.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-XP23.png" style="zoom:75%;" />

### Snooze Alert {#snooze-alert}

Toutes les alertes et alarmes ne sont pas disponibles sur la montre.

<img src="./images/M-S-SW-AW-SA.png" style="zoom:75%;" />

Sur Wear 1.x, les alarmes et alertes qui renvoient vers le téléphone doivent être mises en veille depuis l'application xDrip du téléphone.

<img src="./images/M-S-SW-AW-SA2.png" style="zoom:75%;" />

Sur Wear 2.x et supérieur, les alertes peuvent s'afficher sous forme de notifications : vous devrez alors ouvrir manuellement l'écran Mise en veille Alertes du téléphone ou les mettre en veille depuis l'application xDrip du téléphone.

<img src="./images/M-S-SW-AW-SA3.png" style="zoom:75%;" />

## [Mode collecteur autonome](./wear#standalone-collector-mode) {#standalone-collector-mode}

Le menu xDrip Prefs. contient des informations supplémentaires reprises de xDrip sur le téléphone lorsque les deux sont connectés.

#### Validation {#validation}

Un mécanisme de validation garantit que les deux utilisent les mêmes paramètres. Si la montre n'accepte pas un changement de paramètres venant de xDrip, ceux-ci seront automatiquement modifiés pour correspondre aux paramètres de la montre lorsque les deux seront connectés.

1. Les paramètres sont modifiés sur le téléphone
2. Les modifications sont envoyées à la montre, lorsqu'elle est connectée
3. La montre essaie d'appliquer les modifications de paramètres
4. Les paramètres de la montre sont renvoyés au téléphone (modifiés ou non)
5. Les paramètres du téléphone sont mis à jour pour refléter ceux de la montre, lorsqu'elle est connectée

<img src="./images/M-S-SW-AW-XP1.png" style="zoom:75%;" />

Cela fonctionne aussi dans l'autre sens. Si les paramètres de la montre sont modifiés, ils seront envoyés au téléphone lors de la connexion. xDrip sur le téléphone validera les modifications et les renverra à la montre en guise de confirmation.

1. Les paramètres sont modifiés sur la montre
2. Les modifications sont envoyées au téléphone, lorsqu'il est connecté
3. xDrip sur le téléphone valide les modifications de paramètres
4. Les paramètres du téléphone sont renvoyés à la montre (validés ou non)
5. Les paramètres de la montre sont mis à jour pour refléter ceux du téléphone, lorsqu'il est connecté

<img src="./images/M-S-SW-AW-XP2.png" style="zoom:75%;" />

#### xDrip Prefs. {#xdrip-prefs-1}

Lorsque le collecteur autonome est activé, des entrées supplémentaires apparaissent dans le menu.

BT collector indique quel collecteur de source de données matérielle est configuré dans xDrip sur votre téléphone.

<img src="./images/M-S-SW-AW-ST1.png" style="zoom:75%;" />

Enable collector correspond au paramètre de [Intégration Wear OS](./wear#standalone-collector-mode).

<img src="./images/M-S-SW-AW-ST2.png" style="zoom:75%;" />

De même pour Force collector. Si la montre n'est pas connectée au téléphone et que vous avez perdu la connexion avec votre capteur, vous pouvez l'utiliser pour forcer une tentative de reconnexion.

<img src="./images/M-S-SW-AW-ST3.png" style="zoom:75%;" />

En mode collecteur autonome, vous pouvez utiliser (certaines) alertes locales de la montre. Elles seront mises en veille sur la montre.

<img src="./images/M-S-SW-AW-ST4.png" style="zoom:75%;" />

Y compris l'alerte haute persistante.

<img src="./images/M-S-SW-AW-ST5.png" style="zoom:75%;" />

Si votre montre a un haut-parleur, elle peut aussi faire sonner les alarmes.

<img src="./images/M-S-SW-AW-ST6.png" style="zoom:75%;" />

Si vous vous connectez à un G5 ou un G6, vous trouverez des paramètres supplémentaires.

<img src="./images/M-S-SW-AW-ST8.png" style="zoom:75%;" />

Ce sont des copies des paramètres du téléphone Paramètres de débogage Dexcom - Old G5 Collector Settings.

<img src="./images/M-S-SW-AW-ST9.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST10.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST11.png" style="zoom:75%;" />

<img src="./images/M-S-SW-AW-ST12.png" style="zoom:75%;" />

Force screen on garantit que la montre sera complètement réveillée pendant la recherche.

<img src="./images/M-S-SW-AW-ST13.png" style="zoom:75%;" />

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
