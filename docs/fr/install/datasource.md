---
source_hash: 32e9d6dee6
source_commit: 9eea450
---
Tant qu'aucune source de données de glycémie n'est sélectionnée, xDrip affiche l'assistant de source de données. Vous pouvez l'activer ou le désactiver avec le [menu goutte de sang](../use/mainUI#blood-drop-menu), puis le bouton de l'assistant source.

<img src="./images/ChooseDataSource.png" style="zoom:50%;" />

Faites défiler jusqu'à voir votre capteur ou votre cas d'utilisation.

## G6, G7, 1, 1+ {#g6-g7-1-1}

Si vous connectez xDrip directement à votre capteur ([G6, G7, 1, 1+](./g6)), vous **ne pourrez pas** utiliser l'application du fabricant ni envoyer les données vers Clarity (vous pouvez utiliser [Nightscout](https://nightscout.github.io/) ou [Tidepool](../use/cloud#tidepool)). Vous pourrez peut-être partager via les serveurs [Share](../use/cloud#dex-share), mais cela doit d'abord être configuré avec les applications du fabricant.

<img src="./images/DS-DxDrip.png" style="zoom:50%;" />

Si vous utilisez les applications du fabricant (G6, G7, 1+), vous pouvez connecter xDrip comme [abonné Share](./dexshare), à condition qu'un abonné ait été configuré avec les applications du fabricant.

<img src="./images/DS-DShare.png" style="zoom:50%;" />

Avec [BYODA](./byod) (G6 uniquement), si vous avez activé Broadcast to xDrip, vous n'avez pas besoin de connexion réseau pour avoir les données dans xDrip. Utilisez la source de données Inter-app broadcast

<img src="./images/DS-BYOD.png" style="zoom:45%;" />

Vous pouvez ajouter xDrip à votre configuration actuelle et sélectionner [Companion app](./companion) pour que xDrip lise la glycémie dans les notifications de l'application du fabricant (G6, G7, 1, 1+, Stelo). Notez qu'avec l'application du fabricant, Stelo donne une valeur toutes les 15 minutes.

<img src="./images/DS-DComp.png" style="zoom:50%;" />

C'est aussi possible si vous utilisez [CamAPS](./companion), toujours avec la source de données Companion app

<img src="./images/DS-GCAPS.png" style="zoom:50%;" />

## Libre {#libre}

xDrip se connecte directement aux Libre 2/2+ UE ; vous pouvez utiliser les Libre 1 et les 14 jours US avec un transmetteur. Les autres capteurs Libre 2 et 3 ne sont pas pris en charge directement.

Vous pouvez connecter un Libre 2/2+ UE à xDrip en ajoutant [OOP2](../use/OOP). Vous **ne pouvez pas** utiliser l'application du fabricant pour les alarmes (seulement pour les scans NFC) ni envoyer les données vers les serveurs du fabricant (utilisez [Nightscout](https://nightscout.github.io/) ou [Tidepool](../use/cloud#tidepool)). Utilisez la source de données [Libre Bluetooth](./libreBT).

<img src="./images/DS-L2EU.png" style="zoom:50%;" />

Comme les Libre 1 n'ont pas de Bluetooth, vous devez ajouter un [transmetteur](./libreBT). Utilisez la source de données [Libre Bluetooth](./libreBT).  
Certains de ces transmetteurs fonctionnent aussi avec les Libre 2/2+ UE. Vérifiez que votre capteur ne nécessite pas d'[OOP](../use/OOP).

<img src="./images/DS-LBT.png" style="zoom:50%;" />

Depuis la version 2026.11.21, le groupe Libre propose aussi la source de données [Li3](./li3), qui connecte xDrip directement à un appareil Li3 par NFC et Bluetooth.

Pour les capteurs non pris en charge (Libre 2/2+ hors UE et Libre 3/3+), vous pouvez aussi utiliser Diabox ou Juggluco, puis [diffuser](./libre2patch) les données vers xDrip, qui les recevra avec la source de données [Libre 2 patched](./libre2patch) (et **non** l'application patchée elle-même).

<img src="./images/DS-LOther.png" style="zoom:50%;" />

Vous pouvez suivre un CGM Libre 2/2+ ou un Libre 3/3+ avec xDrip grâce à la source de données [Web follower](./webfollower).

<img src="./images/DS-L3Web.png" style="zoom:50%;" />

## Guardian et MiniMed {#guardian-and-minimed}

Avec une [pompe 640G/670G](./640_670), vous devez récupérer la glycémie depuis la pompe avec un lecteur de glycémie connecté à votre téléphone par un câble OTG.

<img src="./images/DS-M6xx.png" style="zoom:50%;" />

Vous pouvez ajouter xDrip à votre configuration actuelle et sélectionner [Companion app](./companion) pour que xDrip lise la glycémie dans les notifications de l'application du fabricant.

<img src="./images/DS-MComp.png" style="zoom:50%;" />

Vous pouvez suivre les données du capteur partagées via [Carelink](./carelinkfollow), mais cette fonction peut être fréquemment cassée par le fabricant.

<img src="./images/DS-MFoll.png" style="zoom:50%;" />

## [Aidex](./aidex) {#aidex}

Vous pouvez recevoir dans xDrip les données de l'application du fabricant.

Vous pouvez ajouter xDrip à votre configuration actuelle et sélectionner [Companion app](./companion) pour que xDrip lise la glycémie dans les notifications de l'application du fabricant.

## Sibionics {#sibionics}

L'[application patchée](https://t.me/s/kubarev_modz) vous permet d'utiliser xDrip avec la source de données [Inter-app broadcast](./640_670).

## CareSens Air {#caresens-air}

Vous pouvez recevoir dans xDrip les données de l'application du fabricant avec la source de données [CareSens Air](./caresens) (ou Inter-app broadcast).

<img src="./images/DS-CareSens.png" style="zoom:50%;" />

<br>

## Connexion Bluetooth à un capteur ou à un transmetteur {#bluetooth-connection-to-a-sensor-or-a-bridge}

Lorsque vous connectez xDrip directement à un capteur, il gère lui-même la connexion Bluetooth, ou la connexion à l'appareil Bluetooth qui envoie les données de votre capteur (appelé transmetteur). 

::: warning Attention
N'essayez **PAS** de vous connecter via Paramètres Android -> Connexions -> Bluetooth ! 
:::

<img src="./images/Install26.png" style="zoom:100%;" />

Si votre transmetteur est appairé à Android, dissociez-le avant de continuer.

<img src="./images/Install27.png" style="zoom:100%;" />

::: warning Un seul appareil à la fois
Les capteurs et les transmetteurs ne peuvent se connecter qu'à un seul smartphone (ou tablette) à la fois, et à une seule application à la fois.  
Vous devez désinstaller l'application du fabricant pour connecter xDrip à votre capteur ou transmetteur.  
Si un autre appareil est connecté à votre capteur ou transmetteur, éteignez-le ou désactivez l'autre application avant d'essayer de vous connecter avec xDrip.  
**Vous ne pouvez pas vous connecter à deux téléphones ou applications. Sauf pour les Dex G6/G7/1 et 1+ : le second appareil ne peut être qu'un récepteur/une pompe connectée ou une montre BlueJay.**
:::

<br>

Vous devriez maintenant voir l'assistant de sélection de la source de données.

<img src="./images/ChooseDataSource.png" style="zoom:50%;" />

Sinon, appuyez sur ce bouton pour afficher l'assistant.

<img src="./images/Install12.png" style="zoom:75%;" />

Si le bouton n'est pas visible, vous pouvez l'afficher par un appui long sur l'icône xDrip, en activant `Bouton de l'assistant source`.

<img src="../images/UImenu.png" style="zoom:75%;" />

<br>

## Sélection du capteur {#sensor-selection}

Les capteurs inutilisés et obsolètes ont été retirés de cette documentation.

### Les capteurs suivants sont pris en charge directement par xDrip : {#the-following-sensors-are-supported-directly-by-xdrip}

- [G6, G7, 1 et 1+](./g6)  
  <img src="./images/Dex.png" style="zoom:54%;" />    <img src="./images/Install31.png" style="zoom:50%;" />
- [Libre (avec transmetteur)](./libreBT)  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/Bridge.png" style="zoom:50%;" />
- Libre avec montre SWR50 patchée  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/LibreAlarm.png" style="zoom:51%;" />
- [Libre 2 (UE uniquement)](./libre2)  
  <img src="./images/Libre.png" style="zoom:54%;" />    <img src="./images/Bridge.png" style="zoom:50%;" />
- [Medtrum A6](./medtrum)  
  <img src="./images/Other.png" style="zoom:54%;" />    <img src="./images/Medtrum.png" style="zoom:53%;" />
- [CareSens Air](./caresens)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/CareSensAir.png" style="zoom:54%;" />

### Les capteurs et fonctions suivants sont pris en charge avec une application compagnon : {#the-following-sensors-and-features-are-supported-with-a-companion-app}

- [Libre 2 (UE uniquement)](./libre2patch)  
  <img src="./images/Libre.png" style="zoom:51%;" />    <img src="./images/Libre2Patch.png" style="zoom:53%;" />
- [Eversense](./eversense)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/Eversense.png" style="zoom:53%;" />
- [Pompes 640G/670G](./640_670)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/640670.png" style="zoom:53%;" />
- [Build your own app (BYODA)](./byod) pour les capteurs G6  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/640670.png" style="zoom:53%;" />
- [Aidex](./aidex)  
  <img src="./images/SmartGuide.png" style="zoom:53%;" />
- [Companion app](./companion) pour G6, G7, 1, 1+, CamAPS et Eversense  
  Voir ci-dessous.

<br>

## Mode abonné {#follower-mode}

- [xDrip Sync](./xdripfollower) (nécessite les Services Google Play)  
  <img src="./images/XDripSyncFollower.png" style="zoom:53%;" />
- [Nightscout](./nightscoutfollower)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/Nightscout.png" style="zoom:53%;" />
- [Dex Share](./dexshare)  
  <img src="./images/Other.png" style="zoom:52%;" />    <img src="./images/DexShare.png" style="zoom:53%;" />
- [Libre Web Follower](./webfollower)  
  Voir ci-dessous.
- [CareLink Follower](./carelinkfollow)  
  Voir ci-dessous.

<br>

## Changer de source de données {#changing-data-source}

Vous pouvez sélectionner une autre source de données sans passer par l'assistant, depuis le menu des paramètres :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle
:::

[G6, G7, 1 et 1+](./g6) 

::: xdripitem Source de données matérielle
&emsp;Dex<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre (avec transmetteur)](./libreBT) 

::: xdripitem Source de données matérielle
&emsp;Libre Bluetooth<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre whole house](https://github.com/tzachi-dar/LibreAllHouse)

::: xdripitem Source de données matérielle
&emsp;Libre Bluetooth + wifi<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Libre wifi<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[xDrip Sync](./xdripfollower)

::: xdripitem Source de données matérielle
&emsp;xDrip+ Sync Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

Libre avec montre SWR50 patchée 

::: xdripitem Source de données matérielle
&emsp;LibreAlarm<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Libre 2 (UE uniquement), Diabox ou Juggluco](./libre2patch)

::: xdripitem Source de données matérielle
&emsp;Libre (patched App)<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Pompes 640G/670G](./640_670), [Eversense](./eversense) et [Build your own app (BYODA)](./byod)

::: xdripitem Source de données matérielle
&emsp;Inter-app broadcast<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

Cette source de données s'appelait « 640G / EverSense » avant la version 2026.09.04.

[Medtrum A6/S7](./medtrum) 

::: xdripitem Source de données matérielle
&emsp;Medtrum A6<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Nightscout](./nightscoutfollower) 

::: xdripitem Source de données matérielle
&emsp;Nightscout Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Dex Share](./dexshare) 

::: xdripitem Source de données matérielle
&emsp;Dex Share Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Companion app](./companion) pour G6, G7, One et CamAPS

::: xdripitem Source de données matérielle
&emsp;Companion App<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[SmartGuide](./smartguide)

::: xdripitem Source de données matérielle
&emsp;SmartGuide<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[GlucoRx/Aidex](./aidex)

::: xdripitem Source de données matérielle
&emsp;GlucoRx/Aidex App<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[Web Follower](./webfollower) pour Libre 2 CGM et Libre 3

::: xdripitem Source de données matérielle
&emsp;Web Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

[CareLink](./carelinkfollow)

::: xdripitem Source de données matérielle
&emsp;CareLink Follower<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

##### Désactiver la collection de données {#disable-collection}

Si vous voulez désactiver xDrip.

::: xdripitem Source de données matérielle
&emsp;Désactiver la collection de données<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

<br>

::: info Remarque
La liste `Source de données matérielle` contient aussi `Bluetooth Wixel`, `xBridge Wixel`, `Wifi Wixel`, `Wifi Wixel + BT Wixel` et  `Wifi Wixel + xBridge Wixel` : ce sont des entrées anciennes/obsolètes qui ne sont pas traitées dans cette documentation.
:::

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
