---
source_hash: 2d97e8913b
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation
:::

::: warning Ancienne synchronisation xDrip
En juillet 2024, Google a arrêté l'[API Firebase](https://firebase.google.com/docs/cloud-messaging/migrate-v1) obsolète que xDrip utilisait pour la synchronisation xDrip.  
Mettez à jour xDrip vers une version du [23 juillet 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) ou plus récente pour utiliser l'ancienne méthode de synchronisation.  
Il est recommandé de mettre à jour xDrip au moins vers la dernière version publiée.
:::

xDrip propose un mécanisme unique de synchronisation en temps réel entre appareils Android, qui rend le partage des glycémies et des traitements aussi simple que possible.

<br>

[Voici la vidéo de référence d'origine](https://www.youtube.com/watch?v=LcgjfbYcWkE).

### Prérequis {#prerequisites}

::: warning Attention
Les [services Google Play](https://play.google.com/store/apps/details?id=com.google.android.gms) sont indispensables pour utiliser cette fonction. Assurez-vous qu'ils sont présents, activés et non soumis à l'optimisation de la batterie.
:::

Le téléphone xDrip principal est l'appareil qui reçoit réellement les glycémies directement d'un capteur, d'un transmetteur ou d'une application.  
Faire d'un appareil abonné le principal de la synchronisation xDrip n'apporte pas grand-chose, sauf si l'appareil abonné ne peut pas utiliser la même source de données.

Votre principal doit recevoir les données de manière fiable. Si vous n'avez pas de données sur votre abonné, commencez toujours par dépanner le principal.

## Configurer le principal {#setup-master}

Faites du téléphone qui reçoit la source de données principale le maître (cochez la case) :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation  


&emsp;&emsp;&emsp;&emsp;**Soyez maître pour les Abonnés <span class='symbol' style="float: right;"><img src="../images/EN.png" style="zoom:75%;" />&emsp;&emsp;</span>**
:::

<br>

### Copier la clé de synchronisation {#copy-the-sync-key}

#### Option 1 (recommandée) {#option-1-recommended}

Sur le téléphone principal, affichez le QR code de la clé de synchronisation :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrcode_grey600_48dp.png" style="width:5%;" />&ensp;Affichage QR codes  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;XDRIP+ CLÉS DE SÉCURITÉ SEULEMENT&emsp;</div>
:::

Laissez le téléphone principal sur cette image pour le moment.

<img src="./images/M-S-QRe.png" style="zoom:75%;" />

##### Option 1 bis (le téléphone abonné ne peut pas lire le QR code) {#option-1-bis-follower-phone-cannot-read-the-qr-code}

Faites une capture d'écran du QR code et envoyez-la au téléphone abonné (MMS, WhatsApp, envoi sur Google Cloud, ...).

#### Option 2 (compliquée) {#option-2-complicated}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation  

&emsp;&emsp;&emsp;&emsp;**Clé de sécurité de groupe de dispositifs**
:::

<img src="./images/M-S-SY2.png" style="zoom:75%;" />

<br>

## Configurer l'abonné {#setup-follower}

Faites de tous les autres téléphones des abonnés (décochez la case) :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation  


&emsp;&emsp;&emsp;&emsp;**Soyez maître pour les Abonnés <span class='symbol' style="float: right;"><img src="../images/DIS.png" style="zoom:75%;" />&emsp;&emsp;</span>**
:::

<br>

Définissez la source de données de l'abonné :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;xDrip Sync Follower
:::

En savoir plus sur la source de données [xDrip Sync Follower](../install/xdripfollower).

<br>

::: warning Utiliser xDrip Cloud doit être réglé de la même façon sur tous les téléphones
Principal et abonnés. Soit activé pour tous, soit désactivé pour tous.
:::

::: xdripitem Utiliser xDrip Cloud
&ensp;Utilisez les nouveaux serveurs cloud de xDrip+. Les maîtres et les abonnés doivent tous avoir ce paramètre défini à l'identique.  
:::

Il est recommandé d'activer [Utiliser xDrip Cloud](./sync#use-xdrip-cloud) sur tous les appareils : c'est la méthode la plus pérenne.

### Copier la clé de synchronisation depuis le principal {#copy-the-sync-key-from-the-master}

#### Option 1 (recommandée) {#option-1-recommended-1}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configuration automatique  
&emsp;&emsp;&emsp;Caméra
:::

Vous devez autoriser xDrip à accéder à l'appareil photo du téléphone.  
Scannez le QR code affiché sur votre téléphone principal.

<img src="./images/M-S-ACS.png" style="zoom:75%;" />

Il vous sera demandé de confirmer l'importation de ces paramètres (assurez-vous d'importer des paramètres sûrs).

::: xdripitem Êtes-vous sûr?
&ensp;Importer les paramètres eulement des sources de confiance !  
&ensp;Veuillez confirmer l'importation les paramètres suivants :  

&ensp;paramètre1  
&ensp;paramètre2  
&ensp;paramètre3  

Non&emsp;&emsp;<span style="background-color: gray; color: white; text-align: center;">&ensp;Oui&ensp;</span>     
:::

#### Option 1 bis (le téléphone abonné ne peut pas lire le QR code) {#option-1-bis-follower-phone-cannot-read-the-qr-code-1}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configuration automatique  
&emsp;&emsp;&emsp;Fichier image
:::

Sélectionnez l'image contenant le QR code.

<img src="./images/M-S-SY3.png" style="zoom:75%;" />

::: xdripitem Êtes-vous sûr?
&ensp;Importer les paramètres eulement des sources de confiance !  
&ensp;Veuillez confirmer l'importation les paramètres suivants :   

&ensp;paramètre1  
&ensp;paramètre2  
&ensp;paramètre3  

Non&emsp;&emsp;<span style="background-color: gray; color: white; text-align: center;">&ensp;Oui&ensp;</span>  
:::

#### Option 2 (compliquée) {#option-2-complicated-1}

Modifiez le champ de la clé et saisissez **exactement** la même clé que sur le principal.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation  

&emsp;&emsp;&emsp;&emsp;**Clé de sécurité de groupe de dispositifs**
:::

<img src="./images/M-S-SY2.png" style="zoom:75%;" />

<br>

## Actions des abonnés {#follower-actions}

Par défaut, les abonnés peuvent envoyer au principal des traitements, des étalonnages et même des démarrages ou arrêts de capteur.  
Si vous voulez l'empêcher, désactivez [Accepter les actions des Abonnés](./sync#accept-followers-actions) sur le principal.

## Vérifier {#verify}

Pour vérifier que l'abonné reçoit bien les données, consultez [État du système](../troubleshoot/systemstatus#xdrip-sync-follower) sur le téléphone abonné.

<br>

[*Dernière modification le 21/07/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.19)
