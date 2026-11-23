---
source_hash: 68f7c3719c
source_commit: 7a18e7c
---
xDrip offre un moyen simple de copier les paramètres d'un téléphone à un autre.

### Afficher le QR code des paramètres {#show-settings-qr-code}

Affichage QR codes affiche un QR code contenant les paramètres de xDrip.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrcode_grey600_48dp.png" style="width:5%;" />&ensp;Affichage QR codes
:::

::: xdrip Partager les paramètres via le code QR
&ensp;Utilisez les codes QR pour transférer les paramètres en utilisant Paramètres-> Configuration Automatique
:::

La clé de sécurité xDrip est utilisée pour la synchronisation xDrip ; si vous voulez seulement partager un code d'abonné (difficile à recopier à la main), utilisez ce bouton.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;XDRIP+ CLÉS DE SÉCURITÉ SEULEMENT&emsp;</div>
:::

Si vous avez utilisé des QR codes de personnalisation pour le xDrip de ce téléphone (G7, 1+, BlueJay, ...), vous pouvez les transférer directement vers un autre téléphone.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;EXPORT KEKS KEY TO ANOTHER PHONE&emsp;</div>
:::

Les paramètres généraux et de collecte comprennent les paramètres généraux et ceux de votre source de données matérielle.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;AFFICHAGE GÉNÉRAL ET COLLECTION&emsp;</div>
:::

Tous les paramètres comprennent l'ensemble des réglages (sauf les alarmes : vous devez les recréer manuellement).

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;COPIER TOUS LES PARAMÈTRES&emsp;</div>
:::

Vous obtenez un QR code que vous pouvez scanner avec Configuration automatique sur un autre téléphone.

<img src="./images/M-S-QRe.png" style="zoom:75%;" />

### Configuration automatique {#auto-configure}

Configuration automatique vous permet d'importer des paramètres depuis un QR code.

Assurez-vous que le QR code que vous allez scanner provient d'une source sûre.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_qrscan.png" style="width:5%;" />&ensp;Configuration automatique
:::

#### Caméra {#camera}

::: xdripitem Caméra
&ensp;Scannez un QR code avec votre mobile (recommandé)
:::

Vous devez autoriser xDrip à accéder à l'appareil photo du téléphone.

Vous pouvez ensuite scanner le QR code affiché sur un autre téléphone pour copier les paramètres que vous avez sélectionnés en l'affichant, comme expliqué [ci-dessus](#show-settings-qr-code).

<img src="./images/M-S-ACS.png" style="zoom:75%;" />

Les paramètres actuels seront remplacés ; une liste s'affiche pour que vous la confirmiez.

::: xdripitem Êtes-vous sûr?
&ensp;Importer les paramètres eulement des sources de confiance !  
&ensp;Veuillez confirmer l'importation les paramètres suivants :  


&emsp;paramètre1  
&emsp;paramètre2  
&emsp;paramètre3  

&emsp;Non &emsp;&emsp;&emsp;&emsp;Oui
:::

Un QR code *Copier tous les paramètres* ne contient pas les paramètres eux-mêmes : xDrip les télécharge une fois que vous avez confirmé. Depuis la version 2026.11.21, une confirmation vous est d'abord demandée.

::: xdripitem Êtes-vous sûr?
&ensp;Only import settings from sources you trust!  
&ensp;Please confirm to download and import all settings from this code.
:::

Vous devrez peut-être redémarrer votre téléphone pour appliquer les modifications.

#### Fichier image {#image-file}

Si l'appareil photo de votre téléphone est de mauvaise qualité ou absent, vous pouvez charger le QR code depuis un fichier.

Vous devez d'abord enregistrer dans vos images l'image du QR code à scanner.

::: xdripitem Fichier image
&ensp;Vous pouvez enregistrer un code QR en tant que fichier image (comme .png ou .jpeg) sur votre mobile. Ensuite, utilisez cette option pour scanner le code QR du fichier enregistré.
:::

Sélectionnez l'image contenant le QR code.

<img src="./images/M-S-SY3.png" style="zoom:75%;" />

Les paramètres actuels seront remplacés ; une liste s'affiche pour que vous la confirmiez.

::: xdripitem Êtes-vous sûr?
&ensp;Importer les paramètres eulement des sources de confiance !  
&ensp;Veuillez confirmer l'importation les paramètres suivants :  

&emsp;paramètre1  
&emsp;paramètre2  
&emsp;paramètre3  

&emsp;Non&emsp;&emsp;&emsp;&emsp;&emsp;Oui  
:::

Vous devrez peut-être redémarrer votre téléphone pour appliquer les modifications.

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
