---
source_hash: 51a5c41463
source_commit: 7a18e7c
---
De nombreux transmetteurs Libre commerciaux sont disponibles sur le marché ; par ordre de sortie, on trouve Blucon, MiaoMiao, Droplet et Bubble, pour ne citer que les plus connus. Ils reposent tous sur le concept LimiTTer et l'implémentation blueReader : une puce de lecture NFC CR95LF et un microcontrôleur BLE Nordic Semiconductor. La première lit le capteur et le second envoie les données en Bluetooth à votre téléphone (ou à votre montre Wear) toutes les 5 minutes.

::: info Remarque
**Tant que votre transmetteur arrive à lire le capteur et à transmettre les données, vous pouvez considérer qu'il fonctionne correctement.**
:::

Lorsque xDrip affiche des valeurs manquantes, vous devez comprendre ce qui ne va pas. Ce n'est pas toujours facile.

::: info
Commencez par les choses simples : redémarrez d'abord votre téléphone.
:::

Puisque vous êtes ici, vérifiez vos [paramètres Bluetooth de xDrip](../install/libreBT#bridge-settings) et n'hésitez pas à en désactiver certains.

Allez ensuite dans État du système, puis dans BT Device. Si vous ne savez pas comment faire, consultez d'abord [cette page](./systemstatus).

### Page d'état classique {#classis-status-page}

**Si votre transmetteur apparaît comme LimiTTer, cela signifie probablement qu'il n'est pas connecté ou pas reconnu.**

Tous les appareils apparaissent comme LimiTTer tant qu'ils ne sont pas connectés ; seuls la connexion directe Libre 2 et quelques autres transmetteurs (le BluCon par exemple) restent indiqués comme LimiTTer (et évidemment [LimiTTer](https://github.com/JoernL/LimiTTer) lui-même).

<img src="./images/M-SS-CSL2.png" style="zoom:75%;" />

Vérifiez la version de xDrip et assurez-vous qu'elle est assez récente pour prendre en charge le transmetteur auquel vous vous connectez.

xDrip a connu trop de versions et d'améliorations pour donner un tableau précis des versions minimales requises.  
Utilisez au moins la [dernière version publiée](../install/download#latest-release) de xDrip et, si vous pensez que votre transmetteur nécessite des fonctions plus récentes, essayez de passer à la dernière [pré-version](../install/download#pre-release).

 Ne désinstallez pas xDrip pour changer de version. Vous pouvez facilement [passer d'une version à l'autre](../use/update) sans perdre vos données ni vos paramètres.

### Page BT Device {#bt-device-page}

Faites glisser l'écran vers la gauche pour afficher la page BT Device.

<img src="./images/M-SS.png" style="zoom:75%;" />

<img src="./images/M-SS-BTLBf.png" style="zoom:75%;" />

#### Bluetooth Pairing {#bluetooth-pairing}

Si vous êtes déjà passé par ici : **Bluetooth Pairing doit être désactivé. Si vous l'avez modifié par erreur, appuyez sur la ligne pour revenir à cet état :**

<img src="./images/M-SS-BTLBc.png" style="zoom:75%;" />

#### Bluetooth Device {#bluetooth-device}

Le Bluetooth doit toujours être connecté.

<img src="./images/M-SS-BTLBe.png" style="zoom:75%;" />

Premières actions à effectuer si le Bluetooth n'est pas connecté :

1. Vérifiez vos [paramètres Bluetooth](../install/libreBT#bridge-settings) et utilisez Redémarrer le collecteur dans l'onglet classique de l'État du système. Si le redémarrage du collecteur vous a permis de retrouver la connexion, le problème vient peut-être de vos paramètres Bluetooth ou des paramètres d'économie d'énergie du téléphone.  
2. Ouvrez Paramètres Android -> Applications -> xDrip : vérifiez qu'il peut s'exécuter en arrière-plan et qu'il n'est pas optimisé pour économiser la batterie.  
3. Toujours dans Applications, cherchez les applications système Bluetooth (elles peuvent être masquées par défaut et accessibles depuis le menu à trois points, en haut à droite) : vérifiez que tous les services Bluetooth peuvent s'exécuter en arrière-plan et ne sont pas optimisés.

Si le transmetteur n'est toujours pas visible, essayez un [Scan Bluetooth](../install/libreBT#connect-bluetooth-bridge) pour le trouver.

- Si le scan Bluetooth ne le trouve pas, continuez [ici](#bluetooth-scan-doesnt-find-the-bridge).
- Si le scan Bluetooth vous permet de le sélectionner mais qu'il ne reste pas connecté, continuez [ici](#bridge-doesnt-stay-connected).

#### Phone Service State {#phone-service-state}

Phone Service State indique la dernière fois que des données ont été reçues du transmetteur ; cela doit remonter à moins de 5 minutes.  
Next Wake up décompte le temps jusqu'aux prochaines données attendues, puis repart de 5 minutes.

<img src="./images/M-SS-BTLBa.png" style="zoom:75%;" />

Si vous avez configuré une montre Android Wear comme collecteur, consultez la page [mode collecteur autonome](../smartwatch/wear#standalone-collector-mode). Si vous n'avez pas de montre Android Wear avec xDrip correctement installé, [désactivez le collecteur Wear](../smartwatch/wear).

 <img src="./images/M-SS-BTLBg.png" style="zoom:75%;" />

N'essayez pas de connecter votre transmetteur à une montre connectée tant que le fonctionnement avec votre téléphone n'est pas fiable (aucune perte de connexion).

#### Informations sur le transmetteur {#bridge-information}

Vous verrez aussi diverses informations sur le transmetteur, comme l'adresse Mac et les versions matérielle et firmware. Notez que le niveau de batterie n'est pas disponible sur les transmetteurs Blucon : 100 % signifie seulement qu'il est encore utilisable. 

<img src="./images/M-SS-BTLBb.png" style="zoom:75%;" />

Il est fortement recommandé de [mettre à jour](./bridgeFW) le firmware de votre appareil vers la dernière version disponible.

#### No Sensor Found {#no-sensor-found}

Les erreurs No sensor found sont généralement dues à un mauvais positionnement du transmetteur sur le capteur. Certains transmetteurs n'ont aucune tolérance quant à la distance et à l'angle par rapport à la zone d'antenne du capteur. Cela peut aussi venir d'un problème interne au transmetteur, d'un problème de firmware...  
Comme ce message reste affiché, vérifiez que l'heure indiquée est récente. S'il indique en permanence il y a 5 minutes, le capteur n'est pas détecté. Si c'est arrivé il y a quelques heures, ignorez-le simplement.

<img src="./images/M-SS-BTLBd.png" style="zoom:75%;" />

Si vous utilisez un transmetteur peu sensible au positionnement, il présente peut-être une panne interne ou un firmware corrompu.

- Réinitialisez-le d'abord et chargez-le complètement.
- Essayez de recharger ou de [mettre à jour](./bridgeFW) son firmware.

Si vous utilisez un capteur autre qu'un Libre 1, vous devrez peut-être ajouter un algorithme OOP (Out Of Process).

Utilisez [Oublier ce périphérique](./systemstatus#restart-collector-forget-device) dans xDrip et installez l'application du fabricant pour écarter une panne de l'appareil. Contactez le fabricant pour obtenir de l'aide.

### Le scan Bluetooth ne trouve pas le transmetteur {#bluetooth-scan-doesnt-find-the-bridge}

::: info Remarque
C'est tout à fait normal lorsque votre transmetteur est connecté à xDrip.
:::

1. Vérifiez qu'il n'est pas appairé à un autre téléphone ou à une autre application. Si vous utilisez le transmetteur avec une autre application, retirez-le de cette application ou désinstallez l'application qui s'y connecte. Si vous avez utilisé le transmetteur sur un autre téléphone, éteignez celui-ci maintenant ou supprimez l'application qui se connectait à votre transmetteur.
2. Réinitialisez-le. Contactez le fabricant pour savoir comment faire.
3. Mettez-le en charge ou remplacez la pile.  
   Vous pouvez faire un scan Bluetooth avec l'appareil en charge ; si vous ne pouvez vous y connecter que pendant la charge, la batterie interne est peut-être morte.

 Installez l'application du fabricant pour écarter une panne de l'appareil. Contactez le fabricant pour obtenir de l'aide. 

### Le transmetteur ne reste pas connecté {#bridge-doesnt-stay-connected}

Lorsque vous faites un scan Bluetooth, vous voyez et pouvez sélectionner votre transmetteur (il apparaît généralement en bleu comme appareil connu), mais il ne reste pas connecté : lors d'un nouveau scan Bluetooth, il réapparaît.

##### Solution 1 : {#solution-1}

1. État du système, Page d'état classique -> Oublier ce périphérique
2. Menu principal, Scan Bluetooth -> Sélectionnez n'importe quel appareil Bluetooth qui n'est pas votre transmetteur
3. Attendez 10 secondes
4. État du système, Page d'état classique -> Oublier ce périphérique
5. Menu principal, Scan Bluetooth -> Sélectionnez votre transmetteur

##### Solution 2 : {#solution-2}

1. État du système, Page d'état classique -> Oublier ce périphérique
2. Mettez le téléphone en mode avion
3. Attendez 10 secondes
4. Désactivez le mode avion
5. Désactivez le Bluetooth
6. Attendez 10 secondes
7. Activez le Bluetooth
8. Menu principal, Scan Bluetooth -> Sélectionnez votre transmetteur

<br>

[*Dernière modification le 28/3/2022*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2022.03.27)
