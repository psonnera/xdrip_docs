---
source_hash: ec23b1baed
source_commit: ea9ce3a
---
Démarrer un capteur dans xDrip a des fonctions très différentes selon le capteur.

### G6 et 1 {#g6-and-1}

La documentation de référence se trouve [ici](https://navid200.github.io/xDrip/docs/Proper-connectivity.html).

### G7 et 1+ {#g7-and-1}

Le capteur démarre automatiquement au moment de son insertion. Vous n'avez pas besoin de le démarrer dans xDrip.

<br>

### Libre {#libre}

Remarque : cette section ne s'applique PAS au Libre 2/2+ (UE) connecté à xDrip sans transmetteur. Pour ceux-ci, consultez les instructions [Libre 2 Direct](../install/libre2#starting-libre-2-sensors)

xDrip ne peut pas démarrer un capteur Libre, ni l'arrêter (en fait, ce capteur ne peut pas être arrêté : s'il ne tombe pas en panne, il fonctionne pendant toute sa durée de vie et s'arrête de lui-même au bout de 14 jours et 12 heures ; les capteurs Libre 3 fonctionnent 15 jours).

Pour démarrer votre capteur, vous devez utiliser le lecteur ou l'application du fabricant ; certaines applications tierces comme Glimp-S et eDropletNFC peuvent démarrer le capteur Libre 1. Juggluco peut démarrer les capteurs Libre 2 et 3.

Le démarrage du capteur dans xDrip sert uniquement à suivre sa durée de vie et à garantir la mise à jour des étalonnages. Cette opération est nécessaire et recommandée à chaque remplacement du capteur.

<br>

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Démarrer le capteur 
:::

Confirmez avec DÉMARRER LE CAPTEUR

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Démarrer un nouveau capteur
Ne pas cliquer sur 'démarrer le capteur' à moins que le capteur ne soit déjà installé et l'émetteur connecté.  

&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white; align: center;">  &ensp;DÉMARRER LE CAPTEUR&ensp;</span>
:::

Si vous avez inséré le capteur aujourd'hui (c'est-à-dire non démarré ou démarré récemment), répondez OUI, AUJOURD'HUI

::: xdripitem L'avez-vous installé aujourd'hui ?
Nous devons savoir quand le capteur a été installé pour améliorer la précision de calcul.  

<span style="color: cyan; float: right;">PAS AUJOURD'HUI&emsp;&emsp;OUI, AUJOURD'HUI&emsp;</span>
:::

Si vous avez répondu aujourd'hui, sélectionnez l'heure à laquelle vous avez physiquement démarré le capteur en faisant glisser l'aiguille bleue sur la bonne heure. En affichage 12 heures, appuyez sur `am` ou`pm`. En affichage 24 heures, déposez l'aiguille sur le cercle intérieur ou extérieur, selon l'heure. Appuyez sur OK.

<img src="../install/images/M-StaSHour.png" style="zoom:75%;" />

Faites glisser l'aiguille bleue des minutes sur la bonne valeur et appuyez sur `OK`.

<img src="../install/images/M-StaSMin.png" style="zoom:75%;" />

Le capteur nouvellement démarré poursuivra son préchauffage s'il a été démarré il y a moins d'une heure.

::: warning Attention
**Même si xDrip essaie de lire un capteur pendant sa phase de préchauffage, les valeurs peuvent être peu fiables, voire incohérentes, et ne doivent pas être utilisées.**
:::

<img src="../install/images/LibreWarmup.png" style="zoom:70%;" />

Si vous utilisez [OOP1](./OOP#oop1) ou [OOP2](./OOP#oop2) sans étalonnage, la glycémie s'affichera immédiatement, sans étalonnage initial.

Si vous utilisez un capteur déjà démarré, une demande d'étalonnage apparaîtra dans les 15 minutes.

Si vous voyez une flèche violette, vous vous êtes peut-être trompé dans la date et l'heure de démarrage du capteur : des données de glycémie sont disponibles mais ne s'afficheront pas pendant le préchauffage d'une heure.

<img src="../install/images/PurpleArrow.png" style="zoom:70%;" />

<br>

xDrip va maintenant attendre les valeurs et afficher la progression. Restez sur cet écran. Les valeurs arrivent toutes les 5 minutes, cela devrait donc prendre moins de 20 minutes.

::: xdripitem Collecte des premières lectures
&ensp;✔ Collecteur de données en cours d'exécution  
&ensp;⧖  Réception des données du Collecteur  
&emsp;&nbsp;Reçu quelques données récentes  
&emsp;&nbsp;Reçu assez de bonnes données pour calibrer  
&ensp;***No data received yet***  
:::
Si la source de données indique LimiTTer alors que vous n'utilisez pas un vrai [LimiTTer](https://github.com/JoernL/LimiTTer), votre transmetteur n'est pas correctement connecté.

<img src="../install/images/M-SS-LimiTTer.png" style="zoom:70%;" />

L'indication ***No data received yet*** deviendra ***Need 3 recent readings***. Si aucune donnée n'est reçue, [vérifiez vos paramètres](../install/libreBT#bridge-settings).

::: xdripitem Collecte des premières lectures
&ensp;✔ Collecteur de données en cours d'exécution  
&ensp;✔ Réception des données du Collecteur  
&ensp;✔ Reçu quelques données récentes  
&ensp;⧖ Reçu assez de bonnes données pour calibrer  
&ensp;***Need 3 recent readings, got only one so far***  
&ensp;Next reading expected in 1 minute 
:::

Lorsque suffisamment de valeurs ont été reçues, la demande d'étalonnage s'affiche. En savoir plus sur l'étalonnage [ici](../calibrate/101).

Si votre glycémie est dans la plage normale (de préférence dans le bas de la plage normale pour un nouveau capteur) et stable depuis 10 minutes, sans glucides ni insuline actifs, vous pouvez étalonner.

Si votre glycémie varie rapidement ou n'est pas dans la plage normale, il est déconseillé d'étalonner maintenant. 

::: xdrip Calibrer le capteur?
Nous avons quelques valeurs!  
Ensuite, nous avons besoin d'un premier test de glycémie capillaire.  
Prêt à calibrer maintenant ?
:::

Deux valeurs peuvent être demandées pour le premier étalonnage ; vous pouvez n'en utiliser qu'une si vous êtes sûr qu'elle est valide : saisissez simplement deux fois la même valeur. Vous pouvez définir une seule valeur par défaut en [désactivant le double étalonnage](../calibrate/advancedcal#calibrations).

Votre glycémie devrait commencer à s'afficher sur le graphique principal.

<br>

### Abonnés et applications compagnon {#followers-and-companion-apps}

Il est parfois nécessaire de « démarrer » une session de capteur dans xDrip pour obtenir des valeurs.

Démarrer ou arrêter un capteur dans xDrip, avec une source abonné ou application compagnon, n'a aucun effet sur le capteur.

::: warning Attention
La seule exception est [l'abonné xDrip Sync, qui peut transmettre la commande de démarrage ou d'arrêt au capteur s'il est directement connecté au xDrip principal](./sync#accept-followers-actions).  
N'utilisez pas Démarrer et Arrêter le capteur avec un abonné xDrip Sync, à moins d'être sûr que la personne qui a le téléphone xDrip principal saura quoi faire d'un capteur arrêté !
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Démarrer le capteur 
:::

Confirmez avec DÉMARRER LE CAPTEUR

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Démarrer un nouveau capteur
Ne pas cliquer sur 'démarrer le capteur' à moins que le capteur ne soit déjà installé et l'émetteur connecté.  

&emsp;&emsp;&emsp;&emsp;<span style="background-color: grey; color: white; align: center;">  &ensp;DÉMARRER LE CAPTEUR&ensp;</span>
:::

Répondez PAS AUJOURD'HUI

::: xdripitem L'avez-vous installé aujourd'hui ?
Nous devons savoir quand le capteur a été installé pour améliorer la précision de calcul.  

<span style="color: cyan; float: right;">PAS AUJOURD'HUI&emsp;&emsp;OUI, AUJOURD'HUI&emsp;</span>
:::

xDrip devrait récupérer les valeurs à la prochaine mesure.

<br>

[*Dernière modification le 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
