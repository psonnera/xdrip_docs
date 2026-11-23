---
source_hash: 711cdaceb9
source_commit: 7a18e7c
---
**Il s'agit d'une source de données générique pour différentes applications, pas seulement pour l'application du fabricant patchée.**

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Libre (patched app)
:::

Les applications listées ci-dessous utilisent le même protocole pour envoyer des données à xDrip.

::: info Remarque
Les valeurs des applications externes sont traitées comme des données de capteur à tous égards, y compris pour les [limitations d'étalonnage](../calibrate/calibrate#libre-2-patched-app).
:::

Cela ne devrait plus être nécessaire, mais si vous ne voyez pas de données dans xDrip, [Démarrez le capteur](../use/startsensor#followers-and-companion-apps).

<br>

#### Libre 2 EU [application patchée](../troubleshoot/libre2#patched-app) {#libre-2-eu-patched-app}

::: info Application patchée
L'application patchée elle-même n'existe que pour la version européenne du Libre 2.  
S'agissant d'une ancienne application, elle est **rarement compatible avec les versions d'Android supérieures à 12**.
:::

<br>

#### Juggluco {#juggluco}

Si vous utilisez [Juggluco](https://www.juggluco.nl/Juggluco/index.html), vous pouvez diffuser vers xDrip en activant Send to xDrip. Les données doivent être reçues en streaming dans Juggluco pour que des mesures apparaissent dans xDrip.

<img src="./images/Juggluco.png" style="zoom:50%;" />

<br>

#### Diabox {#diabox}

Si vous utilisez une version récente de [Diabox](https://sirius.thetaphi.de/diabox/), vous pouvez diffuser vers xDrip en activant l'option ci-dessous :

<img src="./images/Diabox4.png" style="zoom:75%;" />

<br>

#### LinkUpConnect {#linkupconnect}

LinkUpConnect est un abonné au serveur du fabricant ; il vous faut un Libre 3 pour avoir des données CGM dans l'application.  
Les données doivent être disponibles dans l'application d'abonné du fabricant.  
Activez l'option `Forward to xDrip`.

<img src="./images/LinkUpConnect.png" style="zoom:75%;" />

<br>

#### Lissage {#smoothing}

Cette source de données est soumise par défaut à un lissage de 25 minutes. La durée de lissage peut être ajustée dans le [menu NFC](../use/NFC#smooth-libre-3-data-when-using-xxx-method) pour réduire le retard induit, si le niveau de bruit le permet.

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
