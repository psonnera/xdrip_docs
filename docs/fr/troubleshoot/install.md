---
source_hash: 92fd90f109
source_commit: 7a18e7c
---
## Mon téléphone indique que cette application est très dangereuse {#my-phone-says-this-app-is-very-dangerous}

Les versions publiées sur GitHub depuis le [dépôt officiel](https://github.com/NightscoutFoundation/xDrip/releases) sont sûres. Ignorez ce message.

<img src="./images/Install18.png" style="zoom:75%;" />

<br>

## Je ne trouve pas le fichier que j'ai téléchargé {#i-cannot-find-the-file-i-downloaded}

Ouvrez un gestionnaire de fichiers et regardez dans le dossier Téléchargements (Download) de la mémoire interne de votre téléphone : vous devriez y voir un fichier nommé à peu près `xDrip-plus-20yymmdd-cccccccc.apk`

<br>

## Quand j'appuie sur le fichier .apk de xDrip, une liste de fichiers s'ouvre {#when-i-touch-the-xdrip-apk-it-opens-a-file-list}

Si le fichier xDrip-plus se termine par .zip, renommez-le en .apk et réessayez.

S'il est impossible de l'ouvrir avec le programme d'installation, essayez avec un [installateur d'APK](https://play.google.com/store/apps/details?id=com.apkinstaller.ApkInstaller).

<br>

## Je ne peux pas installer d'applications inconnues {#i-cannot-install-unknown-apps}

<img src="./images/Install19.png" style="zoom:75%;" />

Dans Paramètres Android -> [Sécurité](https://developer.android.com/distribute/marketing-tools/alternative-distribution#unknown-sources), vous devez autoriser l'application que vous utilisez pour ouvrir le fichier téléchargé à installer des fichiers de sources inconnues ; si c'est proposé, choisissez uniquement cette fois-ci.

Voici l'exemple de Chrome ; vous utilisez peut-être une autre application pour ouvrir le fichier .apk de xDrip.

<img src="./images/Install20.png" style="zoom:75%;" />

<br>

## Je ne peux pas installer l'application {#i-cannot-install-the-app}

<img src="./images/Install23.png" style="zoom:75%;" />

Vérifiez qu'aucune autre version de xDrip n'est installée : on ne peut mettre à jour ou rétrograder qu'une application du même développeur. Si nécessaire, [réinstallez](./reinstall) xDrip pour passer de la version officielle à une version dérivée (fork), et inversement.

<br>

## **Mon téléphone indique que cette application n'est pas sûre et a été conçue pour une ancienne version d'Android** {#my-phone-says-this-app-is-unsafe-and-has-been-built-for-an-older-android-version}

Ignorez cet avertissement avec Plus de détails, puis Installer quand même.

<img src="../install/images/Install01a.png" style="zoom:75%;" /> 

<br>

## xDrip a besoin de la localisation en arrière-plan {#xdrip-needs-background-location}

<img src="./images/Install21.png" style="zoom:60%;" />

Pour que xDrip puisse se connecter à un appareil Bluetooth, il doit avoir un [accès permanent à la localisation](../install/install#enable-location).

Sur les versions récentes d'Android, allez dans Paramètres Android -> Localisation -> Applications -> xDrip ou Paramètres Android -> Applications -> xDrip -> Localisation et vérifiez que Toujours autoriser est sélectionné.

<img src="../install/images/Install17.png" style="zoom:80%;" />

<br>

## xDrip doit être exclu de l'optimisation de la batterie {#xdrip-needs-battery-optimization-whitelisting}

<img src="./images/Install22.png" style="zoom:60%;" />

xDrip ne doit pas être optimisé du tout.

L'emplacement de ce réglage varie selon la marque et la version d'Android ; vous le trouverez généralement dans Paramètres Android -> Applications -> xDrip -> Batterie

<img src="./images/Install22b.png" style="zoom:100%;" />

Il peut être nécessaire de redémarrer votre téléphone pour appliquer ces changements. Si le message d'avertissement persiste, vérifiez que vous utilisez une version récente de xDrip : mettez-la à jour si nécessaire.

<br>

[*Dernière modification le 28/3/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.03.27)
