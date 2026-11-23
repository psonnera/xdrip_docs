---
source_hash: 498f98f131
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Options montre intelligente  
&emsp;  BlueJay Watch
:::

Vous pouvez acheter votre montre BlueJay [ici : <img src="./images/M-S-SW-BJ1.png" style="zoom:100%;" />](https://bluejay.website/) 

La [BlueJay U3](https://bluejay.website/shop) est la montre actuelle, disponible dès maintenant. Elle fait tourner le paquet xDrip complet sous Android et se connecte directement à vos capteurs G6, G7 et Dexcom ONE/ONE+.

Les modèles plus anciens X2, GTS, U1 et U2 **ne sont plus vendus**. Leurs instructions de configuration sont conservées ci-dessous pour leurs propriétaires.  
Références des anciens modèles : [GTS](https://bluejay.website/shop/product/bluejay-gts-26) (autonome ou avec xDrip), [U1](https://bluejay.website/shop/product/bluejay-u1-27) et [U2](https://bluejay.website/shop/product/bluejay-u2-28).

::: info Partage de la glycémie
Les BlueJay X2/GTS fonctionnent uniquement en Bluetooth et ne peuvent pas partager les données de glycémie sans être connectées à xDrip sur votre téléphone.  
Les U1/U2/U3 font tourner xDrip complet et peuvent aussi relayer les valeurs vers un téléphone ou d'autres abonnés via Bluetooth (xDrip Link) ou Internet (xDrip Sync).
:::

Les montres BlueJay sont de puissants compagnons pour vos capteurs G6, G7 et 1/1+. Elles se connectent directement à l'émetteur, mais vous devez connaître leurs limites.

##### G6/G7 et 1/1+ {#g6g7-and-11}

Ces émetteurs ont deux emplacements Bluetooth : téléphone et non-téléphone.  
Vous pouvez configurer vos emplacements selon le tableau ci-dessous. Seuls deux appareils peuvent être connectés simultanément à l'émetteur, chacun utilisant son propre emplacement.  
Par défaut, BlueJay utilise l'emplacement non-téléphone. Voir [ici pour la GTS](#run-collector) comment modifier ce paramètre.

Les U1, U2 et U3 doivent être connectées en premier au capteur. Une fois connectées, vous pouvez aussi activer la seconde connexion et la montre choisira automatiquement l'emplacement libre.

| Application du fabricant | Récepteur                | Pompe connectée                            | Montre BlueJay                             |
| ------------------- | ----------------------- | ----------------------------------------- | ----------------------------------------- |
| Inutilisable        | Inutilisable            | Inutilisable                              | Emplacement non-téléphone **xDrip utilise l'emplacement téléphone** |
| **Utilise l'emplacement téléphone** | Inutilisable | Inutilisable                       | Emplacement non-téléphone                 |
| Inutilisable        | **Utilise l'emplacement non-téléphone** | Inutilisable               | Emplacement téléphone                     |
| Inutilisable        | Inutilisable            | t:slim, Omnipod 5 **utilisent les emplacements non-téléphone** | Emplacement téléphone |
| Inutilisable        | Inutilisable            | CamAPS, DBLG1 **utilisent l'emplacement téléphone** | Emplacement non-téléphone        |

*Remarque : xDrip utilise l'emplacement téléphone par défaut ; l'emplacement non-téléphone nécessite le mode Engineering*

## BlueJay U3 {#bluejay-u3}

La U3 fait tourner Android complet et le cœur de xDrip directement sur la montre. Vous la configurez sur la montre et pouvez, si vous le souhaitez, relayer les valeurs vers votre téléphone.

### Commandes de la U3 {#u3-controls}

La U3 a deux boutons physiques : un bouton **Gauche** (orange) et un bouton **Droit**. Sur les U1/U2, la commande de droite était une molette ; sur la U3, cet emplacement est occupé par l'appareil photo.

- Appuyez sur l'un des boutons pour allumer l'écran.  
- Le bouton **Droit** éteint l'écran.  
- Le bouton **Gauche** sert de retour.  
- Faites un appui long sur le bouton d'alimentation pour afficher le menu Arrêt / Redémarrage / SOS, puis faites glisser l'option voulue vers la droite.

### Recevoir les valeurs sur la U3 {#get-readings-on-the-u3}

Saisissez l'identifiant du capteur dans xDrip sur la montre, exactement comme sur un téléphone : allez dans Paramètres &ensp;›&ensp; Source de données matérielle &ensp;›&ensp; DexcomG5/G6/G7.

- **G6** : saisissez l'**ID de l'émetteur (TXID)**.  
- **G7 / Dexcom ONE+** : saisissez le **code d'appairage à 4 chiffres**.

Avec un nouveau capteur, saisissez d'abord l'ID ou le code sur la montre et laissez-la recevoir des valeurs avant de le saisir dans une application de téléphone. Avec un capteur déjà en cours d'utilisation et connecté à une application de téléphone, désactivez temporairement cette application (fermez-la, désactivez le Bluetooth ou éloignez-vous), connectez la montre, puis réactivez l'application du téléphone une fois que la montre reçoit des valeurs.

### Emplacement de l'émetteur {#transmitter-slot}

Par défaut, la U3 utilise l'**emplacement non-téléphone**. Consultez le [tableau des emplacements ci-dessus](#g6g7-and-11) pour choisir le bon emplacement. Pour passer la montre sur l'**emplacement téléphone**, scannez le QR code correspondant dans :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Configuration automatique
:::

Évitez de changer à répétition l'appareil associé à un emplacement : le capteur peut se bloquer. L'emplacement est une configuration fixe, pas un échange à chaud.

::: warning Mise à jour canal téléphone pour le G7
Si votre montre ne reçoit plus les valeurs du **G7**, appliquez la mise à jour logicielle de la montre : sur la montre, ouvrez **Paramètres Android › Software Upgrade**, en étant connecté au Wi-Fi et en charge (batterie > 25 %), recherchez les mises à jour et installez-les.  
Vous pouvez ensuite passer la montre sur le canal téléphone en scannant le QR code affiché dans xDrip **Paramètres › Configuration automatique**, puis redémarrer la montre.  
Avec cette méthode, la **montre et une application de téléphone ne peuvent pas toutes les deux** recevoir directement les valeurs du capteur : désactivez le collecteur de l'application du téléphone si la montre est le collecteur.
:::

### Mettre en veille une alarme xDrip {#snooze-an-xdrip-alarm}

Faites un appui long sur le **bouton Gauche orange** jusqu'à ce que la montre vibre.

### Relayer les valeurs vers votre téléphone ou vos abonnés {#relay-readings-to-your-phone-or-followers}

Lorsque la montre est le collecteur, vous pouvez quand même alimenter votre téléphone et d'autres appareils :

- **xDrip Link** : montre ↔ téléphone via Bluetooth lorsqu'ils sont à portée. Sur la montre, ouvrez l'application **xDrip Link**, activez-la et scannez son QR code dans xDrip sur le téléphone **Paramètres › Configuration automatique**. Les paramètres BlueJay saisis sur le téléphone (y compris le TXID ou le code d'appairage) sont copiés sur la montre. Si le téléphone ne doit pas collecter directement, réglez [Run Phone Collector](#run-phone-collector) sur **Off** sur le téléphone.  
- **xDrip Sync** : relaie les valeurs via Internet (Wi-Fi/4G) d'un appareil principal vers un ou plusieurs abonnés, y compris de montre à montre et de téléphone à montre.

::: info Fonctions de la montre hors xDrip
L'insertion d'une carte SIM, le Wi-Fi, l'appareil photo, les cadrans, les bracelets, les protections d'écran, le compte Google, les appels téléphoniques, le GPS, les appels SOS, la musique et la mise à jour logicielle de la montre sont documentés par le fabricant. Consultez la [FAQ / Top Tips](https://bluejay.website/faq) de BlueJay.
:::

## Anciens modèles : X2 / GTS {#legacy-models-x2-gts}

Les étapes suivantes s'appliquent aux anciennes montres X2 et GTS, qui ne sont plus vendues.

### Appairer votre montre avec xDrip (X2 et GTS) {#pair-your-watch-to-xdrip-x2-and-gts}

1 - Assurez-vous que la montre est chargée avant de commencer.

2 - Activez BlueJay et désactivez le collecteur de la montre.  

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

3 - Si vous avez une BlueJay GTS, passez à l'étape 6.  
Si vous avez une BlueJay X2, elle devrait afficher un QR code à l'écran.  
<img src="./images/M-S-SW-BJc5.png" style="zoom:40%;" />  
Si vous le voyez, passez à l'étape 7.

4 - Lancez BlueJay Panel et lancez la recherche (Scan).  

::: xdripitem Launch BlueJay Panel
:::
<img src="./images/M-S-SW-BJc1.png" style="zoom:76%;" />  
Lorsque la montre est détectée, vous devriez voir son adresse Mac. Sélectionnez-la.  
<img src="./images/M-S-SW-BJc2.png" style="zoom:66%;" /><br>  
Si xDrip ne trouve pas la montre, redémarrez votre téléphone et réessayez. Si vous ne la trouvez toujours pas, vous pouvez saisir manuellement l'adresse Mac de la montre ici   

::: xdripitem BlueJay Advanced Settings
&ensp;BlueJay Mac
:::

Le QR code devrait maintenant apparaître sur la montre ; si vous le voyez, passez à l'étape 7.

5 - Si le QR code ne s'affiche pas sur votre montre, sélectionnez QR et réessayez.  
<img src="./images/M-S-SW-BJc4.png" style="zoom:76%;" />  
Si vous ne voyez toujours pas le QR code, essayez REBOOT, puis [contactez](https://bluejay.website/contactus) le fabricant pour obtenir de l'aide ou demandez de l'aide [ici](https://gitter.im/jamorham/BlueJay).

6 - Sur la GTS, suivez cette séquence de menus pour afficher le QR code :  
Settings Menu -> Admin Menu -> Show QR Code  
<img src="./images/M-S-SW-BJc6.png" style="zoom:76%;" /> 

7 - Dans xDrip, scannez le QR code de la montre  

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Configuration automatique    
:::
Vous devez autoriser xDrip à accéder à l'appareil photo du téléphone.  
Scannez le QR code affiché sur la montre.  
<img src="./images/M-S-SW-BJc7.png" style="zoom:50%;" />

Configurez la montre en abonné : vous devriez voir votre glycémie en quelques minutes.

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Send Readings <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

Vérifiez dans [État du système](../troubleshoot/systemstatus) que la montre est bien appairée. Faites glisser jusqu'à l'onglet d'état avancé BlueJay.  

<img src="./images/M-S-SW-BJc8.png" style="zoom:66%;" />

Si le cœur de xDrip (xDrip Core) n'est pas installé, installez-le maintenant.

### Installer le cœur xDrip (xDrip Core) {#install-the-xdrip-core}

::: warning Mettez la montre en charge pendant l'installation du cœur
:::

Dans État du système de xDrip, onglet d'état avancé BlueJay, appuyez sur la ligne rouge xDrip Core: Not Installed.

<img src="./images/M-S-SW-BJd1.png" style="zoom:71%;" />

Sélectionnez OK pour mettre à jour la montre.

<img src="./images/M-S-SW-BJd2.png" style="zoom:79%;" />

Vérifiez ensuite État du système : le cœur devrait apparaître comme installé.

<img src="./images/M-S-SW-BJd3.png" style="zoom:66%;" />

### Run collector {#run-collector}

Run collector signifie que vous utiliserez la montre sans forcément avoir votre téléphone avec vous.

Si vous utilisez un modèle X2, vous devez configurer la montre avec xDrip.  
Pour la GTS, vous pouvez le faire directement via le [menu](https://bluejay.website/gts-menu-top) de la montre, sans utiliser xDrip.

Pour utiliser la montre avec xDrip, un émetteur doit être directement connecté à xDrip, avec des données de glycémie actuellement affichées dans xDrip.

Définissez quel emplacement se connectera à l'émetteur. Consultez le tableau [ci-dessus](#g6g7-and-11) pour configurer vos emplacements.

::: xdripitem BlueJay Advanced Settings
:::

##### Run Phone Collector {#run-phone-collector}

::: xdripitem Run Phone Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Also run the standard collector on this phone. Only turn this off if you don't want this phone itself to be connecting to the transmitter.
:::

Active ou désactive la connexion de xDrip à l'émetteur (via l'emplacement téléphone).

##### BlueJay uses Phone Slot {#bluejay-uses-phone-slot}

::: xdripitem BlueJay uses Phone Slot <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;This allows the BlueJay to occupy the phone slot on the transmitter. Select this if you want another non-phone device to be able to connect to the transmitter and you are not using a phone to connect to the transmitter.
:::

Par défaut, BlueJay utilise l'emplacement non-téléphone. Cette option lui permet d'utiliser l'emplacement téléphone, mais vous devez alors désactiver Run Phone Collector ci-dessus.

Une fois les emplacements configurés, vous pouvez activer la montre comme collecteur autonome.

::: xdripitem BlueJay Watch <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Run Collector <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Vous verrez alors que xDrip sur votre téléphone n'est plus connecté à l'émetteur : c'est BlueJay qui l'est.  
Lorsque votre montre est à portée Bluetooth, votre téléphone devrait recevoir la glycémie depuis BlueJay.

<img src="./images/M-S-SW-BJe4.png" style="zoom:66%;" />

## BlueJay GTS {#bluejay-gts}

La GTS n'a pas besoin de xDrip pour être configurée, mais les étapes ci-dessus s'appliquent aussi si vous souhaitez le faire.

Regardez la vidéo [ici](https://www.youtube.com/watch?v=JM5cw-xVAZk) pour une visite guidée.

Voyez ici [comment](https://www.youtube.com/watch?v=6YpjuZe2c_Q) vous connecter à l'émetteur.

## BlueJay U1/U2 (anciens modèles) {#bluejay-u1u2-legacy}

Les U1 et U2 ne sont plus vendues mais font tourner le même paquet xDrip complet que la U3 : la [configuration de la U3](#bluejay-u3) ci-dessus s'applique donc. Consultez la [FAQ / Top Tips](https://bluejay.website/faq) du fabricant pour des astuces sur les montres de la série U.

<br>

[*Dernière modification le 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
