---
source_hash: 3c220d5612
source_commit: 7a18e7c
---
### Préparer votre appareil pour le débogage {#prepare-your-device-for-debug}

Cette étape est obligatoire pour s'y connecter via ADB par une connexion physique. Si votre appareil n'a pas de connecteur USB physique, vous devez utiliser ADB via Wi-Fi (documentation à venir).

Si vous voulez déboguer un smartphone, passez directement [ici](#smartphone).

#### Montre connectée {#smartwatch}

1. Activez les Options pour les développeurs  
   Paramètres -> À propos -> Versions -> Numéro de build  
   Appuyez 7 fois sur le numéro de build jusqu'à ce que la montre affiche « vous êtes développeur ».   
   <img src="../smartwatch/images/M-S-SW-AW4.png" style="zoom:75%;" />  
2. Paramètres -> Options pour les développeurs -> Débogage ADB  
   Activez le débogage ADB  
   <img src="../smartwatch/images/M-S-SW-AW5.png" style="zoom:75%;" />

#### Smartphone {#smartphone}

1. Activez les Options pour les développeurs  
   Paramètres -> À propos du téléphone -> Informations sur le logiciel -> Numéro de build  
   Appuyez 7 fois sur le numéro de build jusqu'à ce que le téléphone affiche « vous êtes développeur ».   
   <img src="./images/ADB5.png" style="zoom:75%;" />  
2. Paramètres -> Options pour les développeurs -> Débogage USB  
   Activez le débogage ADB  
   <img src="./images/ADB6.png" style="zoom:75%;" />

### Installer ADB sur un ordinateur Windows {#install-adb-on-a-windows-computer}

1. Téléchargez [Android Debug Bridge](https://developer.android.com/studio/releases/platform-tools#downloads) sur votre ordinateur.  
   `1` Ouvrez le dossier Téléchargements  
   `2` Ouvrez le fichier téléchargé  
   `3` Sélectionnez tous les fichiers  
   `4` Copiez-les dans le `5` dossier adb que vous avez créé dans C:

   <img src="./images/ADB0.png" />

2. Ouvrez une nouvelle fenêtre d'invite de commandes (`Démarrer -> Exécuter - > cmd`) avec les droits d'administrateur.  
   <img src="./images/ADB1.png" />

### Installer une application avec ADB sous Windows {#sideload-an-app-with-adb-in-windows}

1. Branchez votre appareil (montre/téléphone) à votre ordinateur avec un câble USB et déverrouillez l'écran.
2. Saisissez `cd \adb`  
   <img src="./images/ADB2.png" />
3. Saisissez `adb devices`  
   <img src="./images/ADB3.png" />
4. Regardez l'appareil connecté et autorisez le débogage, en choisissant toujours.  
   <img src="./images/ADB10.png" style="zoom:75%;" />  
   <img src="./images/ADB9.png" style="zoom:75%;" />
5. Saisissez à nouveau `adb devices`  
     Votre appareil doit maintenant apparaître dans la liste.  
   <img src="./images/ADB4.png" />
6. Copiez le fichier à installer dans le dossier C:\ADB (appelons-le `myapplication.apk` pour l'exemple ; si son nom contient des espaces, renommez-le en quelque chose de court et simple, comme `oop.apk` ou `xdrip.apk`).
7. Saisissez la commande `adb install -r myapplication.apk` et attendez la fin de l'opération (remplacez `myapplication` par le nom de votre application).
8. L'application doit maintenant être présente sur votre appareil.

### Installer ADB sur un Mac {#install-adb-on-a-mac}

1. Téléchargez [Android Debug Bridge](https://developer.android.com/studio/releases/platform-tools#downloads) sur votre ordinateur.  
   `1` Ouvrez le dossier Téléchargements dans le Finder  
   `2` Faites un clic droit sur le dossier platform-tools  
   `3` Sélectionnez Nouveau terminal au dossier

<img src="./images/ADB7.png" />

### Installer une application avec ADB sous macOS {#sideload-an-app-with-adb-in-ios}

1. Branchez votre appareil (montre/téléphone) à votre ordinateur avec un câble USB et déverrouillez l'écran.

2. Saisissez `./adb devices`  
   <img src="./images/ADB8.png" />

3. Regardez l'appareil connecté et autorisez le débogage, en choisissant toujours.    
   <img src="./images/ADB10.png" style="zoom:75%;" />  
   <img src="./images/ADB9.png" style="zoom:75%;" />

4. Saisissez à nouveau `./adb devices`  
     Votre appareil doit maintenant apparaître dans la liste.  

5. Copiez le fichier à installer dans le dossier platform-tools (appelons-le `myapplication.apk` pour l'exemple ; si son nom contient des espaces, renommez-le en quelque chose de court et simple, comme `oop.apk` ou `xdrip.apk`).

6. Saisissez la commande `./adb install -r myapplication.apk` et attendez la fin de l'opération (remplacez `myapplication` par le nom de votre application).

7. L'application doit maintenant être présente sur votre appareil.


### INSTALL_FAILED_VERSION_DOWNGRADE {#install_failed_version_downgrade}

Cela signifie probablement que l'application est déjà présente sur votre appareil dans une version plus récente.

Essayez de la trouver et de la désinstaller.

S'il est impossible de la désinstaller, essayez de l'installer avec l'option de rétrogradation :

(Windows)	`adb install -r -d myapplication.apk`

(Mac)	`./adb install -r -d myapplication.apk`

<br>

[*Dernière modification le 4/8/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.08.02)
