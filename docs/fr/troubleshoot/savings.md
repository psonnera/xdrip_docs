---
source_hash: 8a63383c39
source_commit: e9ebf28
---
Android propose de nombreuses options d'économie d'énergie. Elles sont utiles pour gagner en autonomie, mais elles peuvent facilement viser des fonctions indispensables à un système CGM.

Tous les réglages décrits ci-dessous se trouvent dans les paramètres Android de votre téléphone ; leur apparence varie beaucoup selon les personnalisations du fabricant.

<img src="./images/AS.png" style="zoom:75%;" />

## Économiseur de batterie {#battery-saver}

En dessous d'un certain niveau de batterie, Android arrête de nombreux services et empêche xDrip de fonctionner normalement.  Gardez toujours une batterie externe sur vous pour éviter cette situation.

Pendant l'utilisation normale du téléphone, assurez-vous qu'il n'est **pas** activé.

<img src="./images/AS-BS.png" style="zoom:75%;" />

## Économies de batterie des applications {#apps-battery-savings}

Les économies de batterie peuvent être réglées pour chaque application du téléphone. En cas de problème, vérifiez-les attentivement. Cela s'applique aussi à OOP, WatchDrip+ (si vous l'utilisez) et au Bluetooth.

::: warning Mises à jour d'Android
Les mises à jour d'Android peuvent rétablir ces réglages par défaut : vérifiez-les toujours après coup.
:::

#### Android 10 {#android-10}

<img src="./images/AS-Apps-DO.png" style="zoom:75%;" />

#### Android 11 et plus récent {#android-11-and-above}

<img src="./images/AS-Apps.png" style="zoom:75%;" />

xDrip doit fonctionner sans restriction.

<img src="./images/AS-Apps-UR.png" style="zoom:75%;" />

### Bluetooth {#bluetooth}

Vous trouverez probablement le Bluetooth dans les applications système (menu trois points).  
Certains téléphones Android n'affichent pas l'application Bluetooth.

<img src="./images/AS-Apps-SA.png" style="zoom:75%;" />

Le Bluetooth doit fonctionner sans restriction si xDrip se connecte directement à un capteur.

## Optimisations MIUI de Xiaomi {#xiaomi-miui-optimizations}

Les optimisations MIUI peuvent avoir un impact massif (négatif) sur la stabilité du système et la fiabilité de xDrip.
Si vous constatez un nombre accru de « valeurs manquées » avec MIUI 14 (ou peut-être des versions de MIUI plus anciennes), essayez de désactiver les optimisations MIUI.
Ce réglage se trouve dans les \&lt;Options pour les développeurs\>, masquées par défaut. Voici comment afficher les \&lt;Options pour les développeurs\> puis désactiver les optimisations MIUI.

### Activer les options pour les développeurs {#enable-developer-options}

Pour afficher les **\&lt;Options pour les développeurs\>**, procédez comme suit :

1. Ouvrez les **\&lt;Paramètres\>** de votre smartphone.
2. Sélectionnez **\&lt;À propos du téléphone\>**.
3. Appuyez 7 fois sur **\&lt;Version MIUI\>** (première entrée de la liste).
4. Le message **\&lt;Vous êtes maintenant développeur.\>** s'affiche.
5. L'entrée **\&lt;Paramètres\>** \-\> **\&lt;Paramètres supplémentaires\>** \-\> **\&lt;Options pour les développeurs\>** est maintenant visible.

### Désactiver les optimisations MIUI de Xiaomi {#disable-xiaomi-miui-optimizations}

Pour désactiver les optimisations MIUI, vous devez d'abord **activer les options pour les développeurs**. Procédez ensuite comme suit :

1. Ouvrez les **\&lt;Paramètres\>** de votre smartphone.
2. Sélectionnez **\&lt;Paramètres supplémentaires\>** \-\> **\&lt;Options pour les développeurs\>**.
3. **Uniquement pour MIUI 14 :** sur MIUI 14, l'option **\&lt;Activer l'optimisation MIUI\>** n'est **PAS** visible par défaut. Pour faire apparaître l'option manquante, faites défiler jusqu'à **\&lt;SAISIE AUTOMATIQUE\>** et appuyez plusieurs fois sur **\&lt;Rétablir les valeurs par défaut\>**. L'option voulue apparaît alors.
4. **Désactivez** l'option **\&lt;Activer l'optimisation MIUI\>** !
5. Redémarrez votre smartphone.

<br>

[*Dernière modification le 6/03/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.02.26)
