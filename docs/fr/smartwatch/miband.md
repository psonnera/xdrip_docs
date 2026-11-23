---
source_hash: 47eb878cea
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_watch_grey600_48dp.png" style="width:5%;" />&ensp;Options montre intelligente  
&emsp;  MiBand
:::

La version officielle de xDrip prend en charge les MiBand 2, 3 et 4, ainsi que la diffusion vers [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration) pour les autres bracelets connectés.

::: info Prérequis
Assurez-vous d'avoir des valeurs de glycémie dans xDrip avant d'essayer de les afficher sur votre montre.  
Si xDrip ne reçoit pas de valeurs sur votre téléphone, elles ne s'afficheront pas sur la montre.
:::

## Installation {#install}

### Obtenir une clé d'authentification {#obtain-an-authentication-key}

#### Si vous avez déjà appairé votre montre avec l'application du fabricant {#if-you-already-paired-your-watch-with-the-vendor-app}

- Désappairez la montre.
- Désinstallez MiFit ou Zepp, ou l'application que vous utilisiez pour connecter votre montre.

- **Supprimez les anciens fichiers de clé** (avec un gestionnaire de fichiers sur votre téléphone) dans le dossier `freemyband` de la mémoire du téléphone.  
  Recommandé si vous n'arrivez pas à connecter xDrip à la montre.  
  *Remarque : le nom ci-dessous est un exemple*

<img src="./images/MiBand1.png" style="zoom:75%;" />

#### Installer l'application modifiée correspondant à votre montre {#install-the-patched-app-matching-your-watch}

Rendez-vous sur [https://www.freemyband.com/](https://www.freemyband.com/)

Téléchargez et installez [Zepp](https://www.freemyband.com/2019/08/amazfit-gtr-auth-key.html) pour les montres Amazfit.  
(ou)  
Téléchargez et installez [MiFit](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html) pour les bracelets Xiaomi.

Connectez-vous avec votre adresse e-mail et votre mot de passe. Créez un compte si nécessaire.

Appairez votre bracelet.

Activez la visibilité de la montre. Si vous ne trouvez pas cette option, vérifiez que vous avez indiqué un âge de 18 ans ou plus.

Vérifiez qu'un fichier de clé a bien été créé dans le dossier `freemyband` de la mémoire du téléphone.

Vous pouvez désinstaller l'application modifiée. Ce n'est pas obligatoire. Si vous voulez installer l'application d'origine, connectez-vous avec le même compte e-mail.

## Sans WatchDrip+ {#not-using-watchdrip}

::: info Uniquement MiBand 2, 3 et 4
:::

### Configurer xDrip {#setup-xdrip}

Activez la fonction MiBand. Gardez votre montre près de votre téléphone jusqu'à ce qu'elle soit détectée.

::: xdripitem Utiliser le bracelet MiBand <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

<img src="./images/M-S-SW-MB-I1.png" style="zoom:80%;" />

L'adresse Mac devrait se remplir automatiquement.

::: xdripitem Adresse Mac (FF:EE:DD:CC:BB:AA)
&ensp;Laisser vide pour la recherche automatique
:::

**Si ce n'est pas le cas** (inattendu)**:**   
Supprimez le ou les fichiers du dossier `freemyband`.  
Ouvrez l'application de montre modifiée.  
Réessayez : désactivez puis réactivez la fonction MiBand.

Vous pouvez aussi essayer de saisir manuellement l'adresse mac de la montre. Vous la trouverez dans le nom du fichier du dossier `freemyband`.  
Par exemple, si le nom est `mibandFFEEDDCCBBAA.txt`, l'adresse mac correspondante sera `FF:EE:DD:CC:BB:AA`.

<img src="./images/M-S-SW-MB-I2.png" style="zoom:75%;" />

Surveillez les messages toast : pendant l'authentification de la montre, vous devriez voir ceci :

<img src="./images/M-S-SW-MB-I3.png" style="zoom:75%;" />

Si l'autorisation échoue, supprimez le ou les fichiers du dossier `freemyband` et ouvrez l'application modifiée pour le régénérer.

<img src="./images/M-S-SW-MB-I4.png" style="zoom:75%;" />

Si xDrip n'arrive pas à obtenir automatiquement la clé d'authentification, vous pouvez essayer de la saisir manuellement. Vous la trouverez en ouvrant le fichier.

<img src="./images/M-S-SW-MB-I5.png" style="zoom:75%;" />

Assurez-vous que la montre est connectée et correspond à l'adresse mac avant de saisir la clé manuellement.

::: xdripitem Clé d'authentification
&ensp;Définissez la clé d'authentification pour MiBand4 (pour obtenir une clé d'authentification, suivez les instructions sur [https://www.freemyband.com](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html))
:::

Une fois la montre connectée et authentifiée, activez Envoyer les valeurs. Attendez la valeur suivante dans xDrip : le cadran devrait se mettre à jour.

::: xdripitem Envoyer les valeurs <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Améliorer la date de la montre pour représenter les valeurs de glycémie. Meilleur en mmol/l - voir la documentation 
:::

Pour forcer la mise à jour de la montre, vous pouvez envoyer une valeur manuellement. Surveillez attentivement les messages toast.

::: xdripitem Mettre à jour la glycémie manuellement
:::

Si vous avez des problèmes d'affichage du graphique, essayez de désactiver les valeurs MTU élevées.

::: xdripitem Disable high MTU values <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

### Fonctions {#features}

::: xdripitem Utiliser le bracelet MiBand <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Synchroniser les données avec les bracelets de fitness MiBand
:::

Vous pouvez activer et désactiver l'intégration MiBand avec l'interrupteur principal. En cas de problème, n'hésitez pas à la désactiver puis la réactiver pour la redémarrer.

::: xdripitem Adresse Mac
&ensp;Laisser vide pour la recherche automatique
:::

L'adresse mac de la montre devrait être détectée automatiquement si le champ est laissé vide. Vous pouvez la modifier manuellement et saisir les 6 valeurs hexadécimales à deux chiffres de votre montre, séparées par des deux-points.

::: xdripitem Clé d'authentification
&ensp;Définissez la clé d'authentification pour MiBand4 (pour obtenir une clé d'authentification, suivez les instructions sur [https://www.freemyband.com](https://www.freemyband.com/2019/08/mi-band-4-auth-key.html))
:::

Lorsqu'une adresse mac valide est trouvée, le champ de la clé apparaît aussi. S'il ne se remplit pas automatiquement, vous pouvez saisir manuellement la clé d'authentification de 32 caractères.

::: xdripitem Envoyer les valeurs <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Améliorer la date de la montre pour représenter les valeurs de glycémie. Meilleur en mmol/l - voir la documentation 
:::

Vous devez l'activer pour que les valeurs soient envoyées à la montre.

::: xdripitem Vibrer lors des lectures <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Envoyer les alarmes <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Envoyer les notifications au bracelet pour les alarmes glycémiques
:::

::: xdripitem Envoyer les appels <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Envoyer des notifications d'appel au bracelet (Android 6+)
:::

Vous pouvez activer différentes options pour que la montre vibre à chaque valeur, reçoive les alarmes ou reçoive les notifications sous forme d'appels téléphoniques.

::: xdripitem Mettre à jour la glycémie manuellement
:::

Vous pouvez forcer le rafraîchissement du cadran avec Mettre à jour la glycémie manuellement.

::: xdripitem Fonctionnalités / Écrans MiBand
:::

D'autres personnalisations sont disponibles dans ce menu.

::: xdripitem Allow to use custom watchface <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Ces fonctions vous permettent de créer votre propre cadran et de modifier l'image de fond.  
Laissez-les désactivées tant que vous n'avez pas correctement placé les fichiers nécessaires dans le dossier xdrip du téléphone.

Pour des astuces et des exemples, regardez [ici](https://github.com/twinko).

::: xdripitem Disable high MTU values <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Disable high MTU values (désactiver les valeurs MTU élevées) peut être utilisé en cas de problèmes d'affichage du cadran.

## Avec WatchDrip+ {#using-watchdrip}

### Installer [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration/) {#install-watchdrip}

:::: info Désactivez MiBand dans xDrip si vous utilisez WatchDrip+
::: xdripitem Utiliser le bracelet MiBand <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::
::::

### Configurer xDrip {#setup-xdrip-1}

Activez API du service Broadcast dans Paramètres -> Paramètres inter applications

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_open_in_app_grey600_48dp.png" style="width:5%;" />&ensp;Paramètres inter applications
:::

::: xdripitem API du service Broadcast <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Active la communication de xDrip avec des applications tiers en utilisant la nouvelle API
:::

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
