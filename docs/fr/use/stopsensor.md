---
source_hash: 2b688cafdf
source_commit: ea9ce3a
---
Arrêter un capteur dans xDrip a des fonctions très différentes selon le capteur.

### G6 et 1 {#g6-and-1}

La documentation de référence se trouve [ici](https://navid200.github.io/xDrip/docs/Proper-connectivity.html).

### G7 et 1+ {#g7-and-1}

Ces capteurs s'arrêtent d'eux-mêmes au bout de 10 jours et 12 heures. Certains émetteurs dotés d'un firmware différent annoncent à la place une durée de vie plus longue de 15 jours et 12 heures ; xDrip le détecte automatiquement à partir du firmware de l'émetteur, ce n'est pas un paramètre à choisir.

<br>

### Libre {#libre}

xDrip ne peut pas arrêter un capteur Libre ; en fait, ce capteur ne peut pas être arrêté : s'il ne tombe pas en panne, il fonctionne pendant toute sa durée de vie et s'arrête de lui-même au bout de 14 jours et 12 heures.

L'arrêt du capteur dans xDrip sert uniquement à invalider les étalonnages précédents. Cette opération est nécessaire et recommandée à chaque remplacement du capteur.

<br>



::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&emsp;Arrêter le capteur
:::

Confirmez avec ARRÊTER LE CAPTEUR, sauf si vous voulez seulement [réinitialiser tous les étalonnages](../calibrate/calibrate#reset-all-calibrations).

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Arrêt du capteur <span class='symbol'></span>
  &emsp;N'arrêtez votre capteur que lorsque vous planifiez de l'enlever, sinon laissez fonctionner!  


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;ARRÊTER LE CAPTEUR&ensp;</span>
:::

Confirmez que vous voulez arrêter le capteur.

::: xdripitem Êtes-vous sûr?
  &emsp;Voulez-vous arrêter le capteur?  


 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NON &emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;OUI&ensp;</span>
:::

Si vous changez d'avis et que le capteur n'a pas encore expiré, vous pouvez toujours le [« redémarrer »](./startsensor#libre) : la session en cours reprendra et un nouvel étalonnage pourra être demandé. xDrip ne redémarre pas physiquement les capteurs Libre.

<br>

### Abonnés et applications compagnon {#followers-and-companion-apps}

Arrêter un capteur n'a aucun intérêt avec une application abonnée.

::: warning Attention
La seule exception est [l'abonné xDrip Sync, qui peut transmettre la commande de démarrage ou d'arrêt au capteur s'il est directement connecté au xDrip principal](./sync#accept-followers-actions).  
N'utilisez pas Démarrer et Arrêter le capteur avec un abonné xDrip Sync, à moins d'être sûr que la personne qui a le téléphone xDrip principal saura quoi faire d'un capteur arrêté !
:::

<br>

[*Dernière modification le 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
