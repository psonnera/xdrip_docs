---
source_hash: 9c60a43392
source_commit: 7a18e7c
---
Aujourd'hui, presque tous les téléphones prennent en charge le scan NFC. Si c'est le cas du vôtre, vous pouvez scanner votre capteur Libre 1, US 14 jours, Libre 2/2+ (EU) et Libre Pro avec xDrip en plus de l'application LibreLink du fabricant. Attention : le scan NFC de xDrip **ne peut pas** démarrer un capteur, seul LibreLink (ou le lecteur) peut le faire. 

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;LibreAlarm
:::

## Sources de données prises en charge {#supported-data-sources}

Pour accéder au menu NFC, vous devez sélectionner l'une des sources de données Libre.

Si vous n'utilisez xDrip que pour scanner le capteur, choisissez LibreAlarm.

::: info Remarque
Si vous activez la prise en charge du scan NFC dans xDrip, désactivez toute autre application susceptible de lire les appareils NFC afin d'éviter les conflits. C'est particulièrement vrai pour l'application Libre du fabricant.
:::

#### Configurer le NFC {#configure-nfc}

Configurez le NFC exactement [comme ceci](../use/NFC).

## Capteurs pris en charge {#supported-sensors}

Seuls les Libre 1 et Pro sont pris en charge nativement par xDrip pour les lectures NFC. Pour scanner un Libre 14 jours US ou un Libre 2 Europe, vous devez installer un [algorithme hors processus (OOP)](../use/OOP) sur le téléphone.

| - Libre 1 / Pro - | - 14 jours US - | - Libre 2/2+ EU - |
| :---------------: | :------------: | :------------: |
|       `Oui`       |     `OOP2`      |     `OOP2`      |

::: info Intervalle minimal entre deux scans
Attendez au moins 60 secondes entre deux scans NFC.
:::

<br>

Passez ensuite à [Démarrer le capteur](../use/startsensor#libre), en sachant que vous devrez scanner le capteur pour obtenir les premières valeurs.

<br>



<br>

[*Dernière modification le 6/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
