---
source_hash: 09c4f80004
source_commit: 7a18e7c
---
# Libre2 Direct {#libre2-direct}

Le Libre2 (UE uniquement) peut se connecter directement à xDrip sans transmetteur. Cette page décrit à quoi doit ressembler un système qui fonctionne.

Voir ici pour [apprendre à le configurer...](../install/libre2#prerequisites)

## Ce que vous devez voir {#what-it-should-look-like}

Une fois la configuration correcte et un nouveau capteur en marche, les pages d'état et les journaux de xDrip doivent ressembler à ce qui est montré ci-dessous. Remarque : rien ne change dans l'onglet Uploaders pour le fonctionnement en Libre 2 direct.


Allez dans l'État du système de xDrip, puis dans BT Device. Si vous ne savez pas comment faire, consultez d'abord [cette page](./systemstatus).

## Page d'état classique {#classic-status-page}

<img src="./images/classic-status-connected.png" style="zoom:40%;" />

### Version {#version}
Dépend de votre version de xDrip

### Source de données {#data-source}
Doit afficher LimiTTer. Même si c'est trompeur, c'est le comportement normal.

### Bluetooth Device {#bluetooth-device}
C'est l'identifiant de série unique du capteur. Il commence par ABBOTT...

### Connection Status {#connection-status}
Doit indiquer « connected ».

### Sensor Start {#sensor-start}
L'heure de démarrage du capteur.

### Bouton Redémarrer le collecteur {#restart-collector-button}
Arrête la fonction de collecte de xDrip puis la relance de zéro (y compris la connexion Bluetooth
 à l'appareil qui avait été arrêtée)

### Bouton Oublier ce périphérique {#forget-device-button}
Retire l'appareil Bluetooth des appareils connus : vous devez faire un scan Bluetooth pour le retrouver et l'appairer,
 ou refaire un scan NFC.

### Bouton Rafraîchir {#refresh-button}
L'état n'est pas en temps réel, contrairement à l'onglet BT Device ; Rafraîchir vérifie l'état de la connexion.
<br>


## Page BT Device {#bt-device-page}

Faites glisser l'écran vers la gauche pour afficher la page BT Device.

<img src="./images/bt-device-connected.png" style="zoom:40%;" />

### Bluetooth Collector Status {#bluetooth-collector-status}

### Phone Service State {#phone-service-state}

Indique normalement l'heure de la dernière connexion.
Il affiche parfois XXX Blu Con XXX, mais c'est une phase temporaire qui laissera place à Last Connect HH:MM


### Bluetooth Device {#bluetooth-device-1}

Le Bluetooth doit toujours être connecté.

### Device Mac Address {#device-mac-address}
Doit être une suite de six paires de chiffres hexadécimaux. Unique pour chaque capteur.

### Bluetooth Pairing {#bluetooth-pairing}

Doit rester sur « Disabled, tap to enable ». Faites attention à NE PAS appuyer dessus.  
Si vous appuyez dessus par erreur, appuyez à nouveau jusqu'à ce qu'il revienne à désactivé.

### Slowest wake up {#slowest-wake-up}

Vous pouvez l'ignorer. xDrip ne passe pas son temps à attendre les valeurs : il commence à les attendre après un certain délai (traditionnellement 5 minutes). Si aucune donnée n'arrive à ce moment-là, vous verrez « Woke up early », ce qui signifie que xDrip s'attendait à ce que des données soient prêtes mais qu'il n'y en a pas. Slowest wake up est le plus long délai rencontré avant de recevoir normalement des données.

### Next Wake up {#next-wake-up}

Doit indiquer 5 minutes

<br>


# Journal des événements {#event-logs}

Dans le menu vertical ... en haut à droite de l'écran principal, sélectionnez Afficher le journal d'événements

<img src="./images/event-log-normal.png" style="zoom:40%;" />

### LibreOOPAlgorithm {#libreoopalgorithm}

Vous devez voir une série de commentaires de la forme
HH:MM Creating BG time = NNN raw = RRRR
où HH:MM est l'heure, NNN un compteur de temps interne (une nouvelle valeur a un nombre supérieur à la précédente) et RRRR la valeur brute lue sur le capteur, en dixièmes de mg/dl (1000 correspond à 100 mg/dl, soit 5,5 mmol/l).
Cela montre que le capteur est connecté et que de bonnes valeurs sont relevées.
Une valeur doit arriver chaque minute, même si certaines peuvent manquer, comme c'est le cas ici.

<br>

## Impossible de scanner un nouveau capteur en NFC - délai NFC dépassé {#cannot-nfc-scan-new-sensor-nfc-timeout}
Un problème apparaît, surtout en Europe : impossible de démarrer le capteur par un scan NFC. Au lieu du message « Scan OK ! » après « Scan en cours », vous verrez « Délai de lecture NFC » ou « Délai de diagnostic NFC ». Regardez dans les journaux de débogage. Si vous voyez le message « Sensor type unknown, returning libre1 as failsafe » ou « Libre sensor of type Libre1 detected », vous devez mettre à jour OOP2 et xDrip.

<img src="./images/libre2direct-failsafe-to-libre1.png" style="zoom:40%;" />

Vous devrez télécharger une version d'OOP2 de fin mai 2023 ou plus récente, et mettre à jour
xDrip-plus vers la version 2023-05-27 ou ultérieure. Une nouvelle version des capteurs, « C5 », au firmware mis à jour, nécessite ces versions à jour.

## Pertes de connexion Bluetooth avec un téléphone Samsung ? {#losing-bluetooth-connection-with-samsung-phone}
Plusieurs utilisateurs de téléphones Samsung signalent qu'ils perdent parfois la connexion avec le capteur. Si c'est votre cas, vous pouvez essayer de modifier certains paramètres Bluetooth. Cliquez sur le QR code puis scannez-le comme indiqué.


[<img src="./images/qr_libre2direct_samsung_30.png" style="zoom:50%;" />](./libre2direct-qr-samsung)


[*Dernière modification le 4/6/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.05.26)

