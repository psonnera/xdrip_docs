---
source_hash: 972ebaa79c
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;État du système
:::

L'état du système fournit des informations internes sur l'état du collecteur de xDrip (à partir d'un capteur ou en abonné) ainsi que sur le partage, les abonnés et les montres connectées directement.

Vous pouvez partager une capture d'écran avec le bouton de partage Android en haut à droite.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" />État du système<span class='symbol'><img src="../images/Share.png" style="zoom:75%;" /></span>
:::

### Page d'état classique {#classic-status-page}

Cette page affiche des informations sur la version actuellement installée.

::: xdripitem <div style="background-color: DodgerBlue; color: white; text-align: center;">  &emsp;Classic Status Page&emsp;</div>
&emsp;Version: a2bbca9-2024.11.26
:::

Les informations de version vous permettent de [retrouver rapidement la version ou pré-version correspondante](https://github.com/NightscoutFoundation/xDrip/releases). Avant la date de version, vous verrez la version de build.

Tout nom de version qui affiche des informations supplémentaires, comme debug, dev, un nom de montre connectée ou carelink, correspond à une [version dérivée (fork)](../install/download#forked-versions) de xDrip et peut ne pas contenir toutes les dernières fonctions de l'application officielle (mais sans doute quelques fonctions en plus).

Sur cette page, vous trouverez le type de source de données (celle que vous avez choisie pour recevoir vos valeurs de glycémie).

::: xdripitem Source de données:
:::

La ligne suivante indique la taille de la base de données de xDrip : la quantité de mémoire qu'elle occupe sur votre téléphone.

::: xdripitem Taille de la base de données :
:::

Dans le cas d'un capteur physique, après le type de source de données, vous verrez le nom de l'appareil Bluetooth réellement connecté à xDrip. Vous voyez aussi l'état de la connexion ; gardez à l'esprit que certains capteurs ne se connectent que brièvement toutes les 5 minutes, et Not connected n'indique donc pas forcément un vrai problème.

::: xdripitem Bluetooth Device:
:::
::: xdripitem Connection Status:
:::
::: xdripitem Sensor Start:
:::

Cette page ne se met pas à jour automatiquement : appuyez sur les flèches arrondies pour la rafraîchir.

<img src="./images/M-SS-CS2.png" style="zoom:75%;" />

#### Redémarrer le collecteur - Oublier ce périphérique {#restart-collector-forget-device}

::: xdrip <span style="background-color: white; color: black;">&ensp;REDÉMARRER LE COLLECTEUR&ensp;</span>&emsp;<span style="background-color: white; color: black;">&ensp;OUBLIER CE PÉRIPHÉRIQUE&ensp;</span>
:::

Redémarrer le collecteur relance le mécanisme de collecte interne de xDrip. L'effet dépend de la source de données.

Oublier ce périphérique n'a d'effet que lorsque xDrip est connecté à un appareil en Bluetooth.  
L'appareil sera déconnecté et vous devrez lancer un scan Bluetooth depuis le menu principal pour rétablir la connexion.

### Page d'état avancée {#advanced-status-page}

La plupart des sources de données disposent d'un onglet d'état avancé. Faites glisser votre doigt vers la gauche sur l'écran pour l'afficher.

<img src="./images/M-SS.png" style="zoom:75%;" />

##### Buggy Samsung {#buggy-samsung}

Renommé Buggy Handset, car d'autres appareils présentent cette non-conformité.

##### Buggy Handset {#buggy-handset}

Il ne s'agit pas d'une erreur : cela signifie simplement que xDrip [corrige](https://github.com/NightscoutFoundation/xDrip/issues/435) une non-conformité d'Android sur certains appareils.  
Il est recommandé de [l'activer](../use/misc#wake-workarounds) en cas de pertes de données.

<img src="./images/M-SS-CSBSsg.png" style="zoom:75%;" />

##### Slowest wake-up {#slowest-wake-up}

Indique quand xDrip a reçu les données par rapport à l'heure attendue. Quelques secondes sont acceptables, mais des minutes peuvent signaler un problème de connectivité.

<img src="./images/M-SS-CSWU.png" style="zoom:75%;" />

#### G6, G7, 1 et 1+ {#g6-g7-1-and-1}

Voir [ici](https://navid200.github.io/xDrip/docs/Connectivity-troubleshoot.html).

#### Libre Bluetooth {#libre-bluetooth}

Si vous utilisez un transmetteur, consultez la page dédiée [ici](./librebridge).

Si vous utilisez un Libre 2 en direct (c'est-à-dire sans transmetteur), consultez la page dédiée [ici](./libre2direct).

#### Abonné xDrip Sync {#xdrip-sync-follower}

::: warning Travail en cours
En juillet 2024, Google a arrêté l'[API Firebase](https://firebase.google.com/docs/cloud-messaging/migrate-v1) obsolète que xDrip utilisait pour xDrip Sync.  
Mettez à jour xDrip vers une version du [23 juillet 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) ou plus récente.
:::

L'abonné xDrip est très simple à [configurer](../use/syncsetup). En cas de problème, il s'agit la plupart du temps d'un souci de connexion réseau ou des services Google Play.  
Il est recommandé d'avoir aussi [Nightscout](https://nightscout.github.io/) comme solution d'abonné de secours lors du dépannage ou pour suivre un enfant.

<img src="./images/M-SS-xF.png" style="zoom:75%;" />

Les abonnés s'ajoutent à la liste lorsqu'ils sont identifiés ; si vous supprimez un abonné, il peut s'écouler un certain temps avant qu'il disparaisse réellement de la liste.

Pour les problèmes de configuration initiale, consultez [cette page](../install/xdripfollower).

#### Abonné Nightscout {#nightscout-follower}

La page d'état avancée montre l'activité lors du téléchargement depuis Nightscout. Si aucune donnée n'est disponible, vérifiez que Nightscout contient des valeurs de glycémie récentes.

En cas d'échec du téléchargement, si votre site Nightscout est régulièrement mis à jour par l'appareil principal et que vous voyez des erreurs de téléchargement NS, cela peut venir de problèmes réseau. Désactivez le Wi-Fi ou les données mobiles, puis faites l'inverse, pour écarter ce problème.

Si cela n'a jamais fonctionné, vérifiez que vous avez correctement [configuré](../install/nightscoutfollower) l'URL de votre abonné.

<img src="./images/M-SS-NF.png" style="zoom:75%;" />

Les anciennes versions d'Android peuvent utiliser des certificats expirés et empêcher ainsi le fonctionnement de l'abonné Nightscout. Il n'existe pas de solution de contournement.

<img src="./images/M-SS-NFcert.png" style="zoom:75%;" />

<br>

[*Dernière modification le 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)