---
source_hash: 6cdbd15c0c
source_commit: 7a18e7c
---
::: info Libre 2 EU
Seule la version européenne du Libre 2 est prise en charge par xDrip.  
Si vous voulez utiliser un Libre 2 d'une autre zone géographique, vous pouvez faire envoyer les données à xDrip par [une autre application](../install/libre2patch).
:::

<br>

## Application patchée {#patched-app}

En Europe, vous pouvez construire votre application patchée conformément à la directive 2009/24/CE, art. 6 (l'application peut varier d'un pays à l'autre). L'Allemagne bénéficie d'une exception au chapitre 6 du CLUF de l'application du fabricant.  
La distribution de l'application patchée n'est pas autorisée.

Vous trouverez des explications pour générer l'application sur [GitHub](https://github.com/search) en recherchant `xDrip-Patch`.

Le capteur en cours doit avoir été démarré avec l'application patchée pour que celle-ci puisse s'y connecter.  
Le Bluetooth de votre téléphone doit avoir été activé et les prérequis de l'application remplis **avant** le démarrage du capteur. Si vous avez démarré un capteur sans que ces prérequis soient remplis, vous ne pourrez peut-être pas activer les alarmes, et donc recevoir les données.

xDrip recevra automatiquement les données de l'application patchée grâce à la source de données matérielle spécifique [Libre2 (patched App)](../install/libre2patch).

#### Vérifier la connexion {#check-connection}

L'application patchée doit être connectée au capteur pour que xDrip en reçoive les données. En général, lorsqu'elle ne l'est pas, vous voyez un point d'exclamation en haut à gauche.

<img src="./images/LLnotconnected.png" style="zoom:75%;" />

Si votre système fonctionnait correctement et que cela arrive de manière inattendue, essayez de redémarrer votre téléphone, de le mettre en mode avion, puis de désactiver et réactiver le Bluetooth pour voir s'il retrouve la connexion.

Scanner le capteur peut être une bonne idée. Si le capteur ne donne pas de données après un scan, il est peut-être défectueux.

Ouvrir le menu peut vous indiquer les prérequis manquants pour que l'application se connecte au capteur.

#### Prérequis de connexion {#prerequisites-to-connection}

- Le service de localisation Android doit être autorisé, **Toujours**. Autorisez toujours l'application patchée (exemple ci-dessous pour xDrip)  
  <img src="../install/images/Install17.png" style="zoom:80%;" />
- Le téléphone doit être réglé sur [date, heure et fuseau horaire automatiques](../install/prerequisites#phone-time-accuracy)
- Au moins une des trois alarmes **doit être activée** dans l'application patchée
- Le Bluetooth doit être **activé**
- Les alarmes et rappels (sons) doivent être **autorisés** (Paramètres Android - Applications)
- Les notifications doivent être **autorisées** (Paramètres Android - Applications)
- Les notifications sur l'écran de veille doivent être **autorisées** (Paramètres Android - Applications)

<br>

## Connexion directe {#direct-connection}

Si vous voulez essayer pour la première fois de connecter xDrip directement à un capteur Libre 2 et que vous n'êtes pas sûr de réussir à faire fonctionner le système, il est fortement recommandé de le faire le dernier jour de votre capteur en cours.  
xDrip ne cassera pas le capteur, il empêchera seulement l'application du fabricant ou le lecteur de recevoir les alarmes ; si vous en dépendez, vous risquez de vous retrouver avec un capteur qui se comporte comme un Libre 1.

Plus d'informations sur le Libre 2 direct [ici](./libre2direct)

#### Prérequis {#prerequisites}

L'appareil qui a servi à démarrer le capteur doit être isolé (four à micro-ondes, éteint) pour éviter qu'il interfère avec l'appairage de xDrip. Il affichera l'icône de perte de connexion.

<img src="./images/FLnotconnected.png" style="zoom:75%;" />

Si vous avez installé xDrip sur le téléphone qui a servi à démarrer et scanner le capteur, il est recommandé de désinstaller l'application du fabricant : elle vous empêchera de vous connecter au Bluetooth du capteur et perturbera les scans NFC. Vous pourrez la réinstaller une fois xDrip connecté au capteur ; elle n'aura évidemment plus les alarmes du capteur.

Si vous ne voulez pas supprimer l'application du fabricant, vous devez désactiver son autorisation de localisation dans les paramètres Android.  
**xDrip doit être autorisé, toujours.  
L'application du fabricant ne doit JAMAIS être autorisée.**

Notez que si vous gardez l'application du fabricant sur votre téléphone, vous devrez choisir entre elle et xDrip à chaque scan NFC du capteur. Cela peut provoquer des erreurs de lecture dans xDrip.

#### Erreurs de scan du capteur {#sensor-scan-errors}

Vérifiez que vous avez correctement [configuré](../install/libreNFC#configure-nfc) le NFC de xDrip.  
Le scan prend plus de temps avec xDrip. Une fois l'emplacement de l'antenne NFC de votre téléphone trouvé, placez-vous au bon endroit et ne bougez plus.  
Vous ne pouvez pas scanner moins de 30 secondes après le scan précédent.

#### Impossible de se connecter au capteur {#cannot-connect-to-the-sensor}

Vérifiez qu'[OOP2](../use/OOP#oop2) est installé, activez [sans calibration](../use/misc#oop2), [arrêtez le capteur](../use/stopsensor#libre) et recommencez à partir d'[ici](../install/libre2#connect-to-the-sensor).

Scannez à plusieurs reprises toutes les 2 minutes pendant 10 minutes, puis laissez le système tranquille pendant 20 minutes.

Après plusieurs scans, vous devriez voir des valeurs dans xDrip.  
Vous devriez aussi voir des valeurs dans l'application OOP2.

<img src="./images/OOP2values.png" style="zoom:74%;" />

Si vous ne voyez pas de valeurs après le scan :

- Vérifiez bien que vous n'avez **PAS** activé [OOP1](../use/misc#out-of-process-algorithm) par erreur
- Vérifiez que xDrip a l'[accès à la localisation autorisé](../install/install#enable-location), **toujours**
- Redémarrez votre téléphone et réessayez

<br>

Consultez la page de [dépannage](./librebridge) si nécessaire.

<br>

[*Dernière modification le 18/06/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.06.15)
