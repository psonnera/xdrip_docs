---
source_hash: a4207f8d58
source_commit: 7a18e7c
---
Vous trouverez la documentation de référence [ici](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Options montre intelligente  
&emsp;  Intégration Wear OS
:::

Une fois xDrip installé sur la montre appairée à votre téléphone, vous pouvez activer Wear.  
xDrip communiquera alors avec une version allégée de lui-même sur la montre.

::: xdripitem Intégration Wear OS <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Envoyer les données au cadran Wear OS.
:::

Pour quelques combinaisons de capteurs et de montres, xDrip peut être utilisé directement depuis la montre sans que le téléphone soit présent. Voir ci-dessous pour plus d'informations.

Activer le Service de collecte Wear permet à la montre de prendre le relais du téléphone lorsque xDrip sur le téléphone perd la connexion avec le capteur ou le transmetteur.

::: xdripitem Activer le Service de collecte Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Connecter Wear au collecteur BT lorsque le téléphone est hors de portée
:::

Forcer le Service de collecte Wear oblige la montre à être l'appareil principal connecté au capteur ou au transmetteur, même si le téléphone est à proximité (recommandé).

::: xdripitem Forcer le Service de collecte Wear <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Forcer le téléphone à utiliser le Service de collecte Wear
:::

Désactiver le forçage en cas de batterie faible fait que la montre abandonne la connexion au capteur ou au transmetteur pour la rendre au téléphone lorsque sa batterie est trop faible.

::: xdripitem Désactiver le forçage en cas de batterie faible <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Désactiver le forçage du Service de Collection Wear en cas de batterie faible
:::

Désactiver le forçage en cas de lectures manquées fait que la montre abandonne la connexion au capteur ou au transmetteur pour la rendre au téléphone après une certaine durée sans valeurs, définie dans le menu ci-dessous.

::: xdripitem Désactiver le forçage vers Wear en cas de lectures manquées <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
Désactiver le forçage du Service de Collecte Wear si des Minutes sont passées depuis la dernière lecture  
:::

Utiliser uniquement Wear peut être activé si vous avez configuré la montre une fois mais n'utiliserez pas votre téléphone pour vous connecter au capteur ou au transmetteur.

::: xdripitem Utiliser uniquement Wear <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Si vous prévoyez d'utiliser seulement un collecteur Wear et jamais votre téléphone.
:::

Si vous avez plusieurs montres Android Wear avec xDrip, vous pouvez choisir laquelle sera le collecteur. Les autres afficheront seulement les données de xDrip.

::: xdripitem Périphérique qui exécute le Service de Collecte
:::

::: info Changer de montre
Lorsque vous passez d'une montre à l'autre, xDrip peut ne pas réussir à communiquer son intention aux deux montres si l'une d'elles est éteinte. Si vous voulez changer de montre collectrice, forcez le collecteur dans xDrip et forcez aussi le collecteur dans le menu xDrip Prefs de la montre.
:::

Synchroniser les logs Wear est une fonction très utile en cas de problème : elle ajoute les journaux de la montre au [journal des événements](../use/3dotsmenu#events-log) de xDrip, avec un préfixe qui indique que l'activité a lieu sur la montre. Par défaut, le préfixe est `wear`, mais vous pouvez le personnaliser. Il est recommandé de garder cette option activée.

::: xdripitem Synchroniser les logs Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Envoyer les logs Wear vers l’observateur d’événements
:::

Afficher les Traitements ajoute les symboles des traitements sur le graphique de la montre.

::: xdripitem Afficher les Traitements <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Afficher les points de Traitements sur le graphique
:::

## Mode collecteur autonome {#standalone-collector-mode}

L'extension Wear de xDrip contient aussi la partie de xDrip qui se connecte à certains capteurs : la montre peut donc remplacer le téléphone et prendre en charge la communication et les valeurs, sans que votre téléphone soit à proximité.

Cette fonction n'est pas disponible pour tous les capteurs, voir le tableau ci-dessous :

| Capteur                      | Wear 1.x | Wear 2.x | Wear 3+ |
| ---------------------------- | -------- | -------- | ------- |
| G5/G6/1                      | Oui      | Limité*  | Non     |
| G7/1+                        | Non      | Non      | Non     |
| Libre 1 avec transmetteur    | Oui      | Oui      |         |
| Libre 14 jours US avec transmetteur | Oui**    | Oui**    |         |
| Libre 2/2+ EU sans transmetteur | Non       | Non       |         |
| Libre 2/2+ EU avec transmetteur | Oui**    | Oui**    |         |

***Limité\*:*** la plupart des montres Android Wear présentent des bugs qui les empêchent de fonctionner correctement avec le G5/G6. Dans le meilleur des cas, vous aurez une valeur toutes les 10 minutes. Certaines montres peuvent être [modifiées](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5) pour obtenir une valeur toutes les 5 minutes.

::: info Pourquoi ma montre ne peut-elle pas collecter seule les données d'un G5/G6 ?
La plupart des montres Android Wear sont livrées avec un firmware Bluetooth bogué qui casse le cycle de connexion du G5/G6 : la montre manque des valeurs ou n'en reçoit qu'une toutes les 10 minutes. La seule solution trouvée a été de modifier le firmware de la montre elle-même : déverrouiller le bootloader et flasher un correctif via un recovery personnalisé. Cela annule la garantie et n'existe que pour quelques montres anciennes (Asus Zenwatch 2/3, Huawei Watch et Watch 2, LG G Watch, Polar M600). L'explication complète, la liste des montres prises en charge et les téléchargements « care pack » se trouvent sur la page wiki [Patching Android Wear devices for use with the G5](https://github.com/NightscoutFoundation/xDrip/wiki/Patching-Android-Wear-devices-for-use-with-the-G5). Si votre montre n'y figure pas, elle ne peut pas collecter nativement les données d'un G5/G6 : utilisez-la plutôt comme affichage du téléphone.
:::

***Oui\*\*:*** il vous faut un téléphone fonctionnant avec [OOP1](../use/OOP) ou [OOP2](../use/OOP#oop2), et cette même application OOP doit aussi être [chargée](../troubleshoot/ADB#smartwatch) sur votre montre. Certains transmetteurs peuvent ne pas être compatibles.

### Prérequis {#prerequisites}

La fonction est disponible pour les combinaisons capteur/montre décrites ci-dessus.

L'extension xDrip est installée sur la montre, dans la même version que celle de votre téléphone.

La connectivité de xDrip est bonne sur votre téléphone (c'est-à-dire que les paramètres Bluetooth sont correctement définis).

xDrip sur la montre doit être autorisé à accéder à la position.  
<img src="./images/M-S-SW-AW33.png" style="zoom:75%;" />

### Séquence recommandée {#recommended-sequence}

Première tentative ou reprise après un échec :

1 - Dans xDrip sur votre téléphone : désactivez le forçage du collecteur, puis la collecte, puis Wear, dans cet ordre.  

::: xdripitem Forcer le Service de collecte Wear <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

::: xdripitem Activer le Service de collecte Wear <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

::: xdripitem Intégration Wear OS <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

2 - Activez les journaux Wear.  

::: xdripitem Synchroniser les logs Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Envoyer les logs Wear vers l’observateur d’événements
:::

3 - Redémarrez votre montre. Attendez qu'elle ait complètement démarré.

4 - Sur votre téléphone, activez uniquement Wear.  

::: xdripitem Intégration Wear OS <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

5 - Attendez que le graphique xDrip soit entièrement affiché sur la montre (attendre une nouvelle mesure ne fait pas de mal).

6 - Gardez le téléphone, la montre et le capteur proches les uns des autres, et activez d'abord la collecte, puis le forçage du collecteur.  

::: xdripitem Activer le Service de collecte Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

::: xdripitem Forcer le Service de collecte Wear <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

7 - L'appairage prend généralement 10 minutes : ouvrez le journal des événements de xDrip sur le téléphone et attendez les événements commençant par `wear`.  
<img src="./images/M-S-SW-AW31.png" style="zoom:75%;" />

8 - Si tout s'est bien passé, la montre devrait maintenant être en mode autonome.

##### Si la montre ne se connecte pas au transmetteur : {#if-the-watch-doesnt-connect-to-the-bridge}

- Dans le menu xDrip Prefs de la montre, cochez Force Collector.  
  <img src="./images/M-S-SW-AW-ST3b.png" style="zoom:75%;" />
- Depuis le menu à trois points du cadran xDrip, choisissez Restart Collector.  
  <img src="./images/M-S-SW-AW-3DM.png" style="zoom:75%;" />
- Dans les paramètres Bluetooth de la montre, trouvez votre transmetteur et faites semblant de l'appairer (vous ne pouvez pas appairer un Miaomiao avec la montre, mais elle va essayer d'établir une liaison avec lui). Une fois l'appairage échoué, attendez 10 minutes que les valeurs apparaissent.
- Si les valeurs n'apparaissent pas, désactivez Force Collector et recommencez la séquence.

## Partager les données en mode autonome {#sharing-data-in-standalone-mode}

Si vous voulez que la montre partage les données (xDrip Sync, Nightscout…), elle doit être connectée à votre téléphone et votre téléphone doit être connecté à Internet.

Ils n'ont pas besoin d'être au même endroit, mais la montre elle-même ne partage pas les données directement : elle les envoie à votre téléphone, et c'est votre téléphone qui les partage. Si la montre est connectée à Internet par Wi-Fi ou par une carte SIM avec forfait de données, elle devra les envoyer à votre téléphone (lui aussi connecté à Internet) et c'est votre téléphone qui partagera les données. Tant qu'ils sont tous les deux connectés à Internet, ils n'ont pas besoin d'être proches l'un de l'autre.

<img src="./images/M-S-SW-AW-XP24.png" style="zoom:75%;" />

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
