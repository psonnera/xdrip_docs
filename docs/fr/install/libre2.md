---
source_hash: 03b49989fb
source_commit: e9ebf28
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Libre Bluetooth
:::

### Libre 2 Direct {#libre-2-direct}

Cette page explique comment activer la connexion Bluetooth directe entre le capteur et xDrip, sans transmetteur.

#### Prérequis {#prerequisites}

Le téléphone sur lequel vous avez installé xDrip possède un lecteur NFC.

Si l'application du fabricant est installée sur le téléphone que vous utilisez pour xDrip, **vous l'avez désinstallée**.  
Si elle est installée sur un autre téléphone ou si vous utilisez le lecteur Bluetooth, vous avez éloigné ces appareils ou les avez isolés pour qu'ils ne causent pas d'interférences.

#### Première configuration {#setting-up-for-the-first-time}

(Cliquez sur [Démarrer le capteur](#starting-libre-2-sensors) pour les capteurs suivants).

::: info Seuls les modèles de capteurs Libre 2/2+ Europe sont pris en charge
Vous devez installer la [dernière application OOP2](../use/OOP#oop2).
:::


La documentation de référence du Libre 2 se trouve [ici](https://www.minimallooper.com/post/how-to-setup-freestyle-libre-2-and-oop2-to-use-a-native-bluetooth-connection-in-xdrip) mais elle n'est plus à jour.

<br>

::: warning Attention
**Désinstallez toute application connectée au capteur et isolez le lecteur avant d'essayer de vous connecter à xDrip.**  
Si vous connectez votre capteur directement à xDrip, vous perdrez définitivement les alarmes de l'application du fabricant ou du lecteur, sans possibilité de les récupérer.  
Si vous n'êtes pas sûr que cela fonctionnera, testez le système avec un capteur en fin de vie.  
Comme avec les transmetteurs Libre, le succès et la fiabilité varient selon votre téléphone.  
Associer votre capteur à xDrip annule la garantie du fabricant sur la fonction Bluetooth du capteur.
:::

#### Configurer xDrip {#setup-xdrip}

Pour aller plus vite, vous pouvez scanner le QR code ci-dessous pour charger les paramètres nécessaires au Libre 2/2+ direct avec la fonction [Configuration automatique](../use/copysettings#auto-configure) de xDrip. Si vous consultez la documentation depuis le téléphone sur lequel vous installez xDrip, enregistrez d'abord les images, puis chargez-les avec la fonction « Fichier image » de la configuration automatique.

Ils règlent **la [calibration sur désactivée](../use/misc#oop2), recommandé pour une première utilisation**. Si vous voulez au contraire étalonner, [suivez ceci](./libre2direct-calib). La liste complète des paramètres importés est présentée [ici](./libre2direct-qr-settings).

QR codes - Cliquez sur l'image pour l'agrandir

Sans étalonnage             |  Avec étalonnage
:-------------------------:|:-------------------------:
[<img src="./images/qr_libre2direct-nocalib-30.png" style="zoom:50%;" />](./libre2direct-qr-settings) | [<img src="./images/qr_libre2direct-calib-30.png" style="zoom:50%;" />](./libre2direct-calib)

Si vous avez utilisé les QR codes, vous pouvez passer directement à [Démarrer les capteurs Libre 2](#starting-libre-2-sensors)

#### Configurer le NFC {#configure-nfc}

Configurez le NFC exactement [comme ceci](../use/NFC).

#### Démarrer les capteurs Libre 2 {#starting-libre-2-sensors}

Posez physiquement votre capteur Libre 2/2+ et démarrez-le avec le lecteur ou avec LibreLink. Notez l'heure à laquelle le capteur sera prêt. Si vous utilisez le même téléphone que xDrip, désactivez LibreLink sur le téléphone. Vous devriez voir des valeurs de glycémie en le scannant. Attendez maintenant 60 minutes que le capteur ait terminé son préchauffage et son auto-étalonnage.

#### Se connecter au capteur {#connect-to-the-sensor}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Arrêter le capteur  
:::

Si un capteur précédent est connecté à xDrip, arrêtez l'ancien capteur.

Scannez le capteur avec le NFC de xDrip et vérifiez que les messages « Scan en cours » puis « Scan OK ! » s'affichent.

::: info Remarque
Tenez le téléphone immobile pendant le scan du capteur et ne le bougez pas : c'est plus long que la lecture habituelle avec l'application du fabricant.  
N'oubliez pas d'attendre une minute entre deux scans NFC successifs.
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Démarrer le capteur  
:::

Démarrez le capteur dans xDrip. Lorsqu'on vous demande l'heure à laquelle vous avez physiquement démarré le capteur, n'indiquez pas une heure antérieure à la réalité pour éviter des valeurs incohérentes.

Attendez 60 secondes et scannez à nouveau avec xDrip. Cela ajoute le capteur comme appareil Bluetooth dont xDrip recevra les valeurs. Vous devriez voir la notification NOUVEAU CAPTEUR DÉMARRÉ. Si vous avez choisi « No calibration », vous devriez voir la première valeur immédiatement. Si vous avez choisi l'étalonnage, vous devriez alors être sur l'écran « Collecte des premières lectures ».
Vous devrez alors attendre entre 3 et 15 minutes que 3 valeurs soient reçues, puis la demande **Calibrer le capteur?** s'affichera, sauf si vous avez sélectionné « No calibration » dans les [paramètres OOP2](../use/misc#oop2).
Après la saisie de l'étalonnage, le capteur Libre 2/2+ devrait être associé à xDrip et fournir des valeurs toutes les 5 minutes.

Vous pouvez vérifier que tout fonctionne en comparant avec « Ce à quoi cela devrait ressembler » [ici](../troubleshoot/libre2direct#what-it-should-look-like)

Si vous avez du mal à obtenir les données directement du capteur, scannez-le toutes les 5 minutes avec le NFC de xDrip jusqu'à la demande d'étalonnage (si vous avez choisi l'[option d'étalonnage](../use/misc#oop2) avec OOP2).

<br>

#### **Des problèmes ?** {#problems}

Consultez la page de [dépannage](../troubleshoot/libre2direct).

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
