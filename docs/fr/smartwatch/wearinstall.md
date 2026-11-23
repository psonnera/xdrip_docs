---
source_hash: 6617aa448f
source_commit: 7a18e7c
---
Vous trouverez la documentation de référence [ici](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/WatchGuide.md).

::: info Le saviez-vous ?
Vous pouvez utiliser certaines de ces méthodes avec l'application Dexcom principale et AAPS.
:::

### Prérequis {#prerequisites}

Votre montre doit être compatible Android Wear OS et porter le logo suivant :

<img src="https://play-lh.googleusercontent.com/WmoV-m8b6x16sDRfzebu5b2vstcyBHRrpzCj6ODoh6hGuMa9Gg39EvnOk7z3qMa0_WM=s180-rw" style="zoom:50%;" align="left"/>

Vous trouverez les montres récentes [ici](https://wearos.google.com/).  
Toutes les montres connectées Wear OS sont directement compatibles avec xDrip, mais les [changements de Google](https://www.androidpolice.com/2021/02/12/wear-os-is-making-app-sideloading-much-more-difficult/) sur Wear OS ont rendu son installation plus complexe.  
De nouveaux changements de comportement de Samsung et de Google dans Wear OS 5 l'ont rendue encore plus compliquée.

### Versions de Wear OS {#wear-os-versions}

Les anciennes versions de Wear OS, comme 1.5 et 1.6, sont désormais plus compliquées à utiliser avec les téléphones récents.  
Wear OS 2 et 3 sont entièrement pris en charge.  
Wear OS 4 et 5 peuvent poser des difficultés.

### Wear OS 1.x {#wear-os-1x}

::: warning Android 15
L'ancien paquet Android Wear 2.9 n'est pas compatible avec Android 15.
:::

Il s'agit généralement de la Sony Smartwatch 3 ([SWR50](https://www.sony.com/electronics/support/other-products-xperia-smart-devices/swr50)). 

#### Méthode 1 (la plus simple) {#method-1-easiest}

1. Désappairez la montre de votre téléphone si elle était déjà appairée.
2. Désinstallez Wear OS de votre téléphone s'il est installé.  
   Si d'autres montres Android Wear sont connectées, vous devrez peut-être les appairer de nouveau.
3. Désactivez la mise à jour automatique des applications dans Google Play.
4. Installez [Android Wear 2.9.0.185084575 GMS](https://www.apkmirror.com/apk/google-inc/android-wear/android-wear-2-9-0-185084575-gms-release/android-wear-smartwatch-2-9-0-185084575-gms-android-apk-download/).
5. Ouvrez Android Wear et appairez la montre, acceptez et autorisez tout : si vous voulez désactiver certaines fonctions, vous le ferez une fois l'installation de xDrip terminée.
6. Une fois l'appairage terminé, vérifiez que la version de Google Play de votre montre est **supérieure à 9**.  
   Paramètres -> À propos -> Versions  
   <img src="./images/M-S-SW-AW3.png" style="zoom:75%;" />  
   Si ce n'est pas le cas : appuyez 3 fois dessus pour forcer la mise à jour, et patientez (jusqu'à plusieurs heures).  
   <img src="./images/M-S-SW-AW3a.png" style="zoom:75%;" />
7. Sélectionnez un cadran xDrip dans l'application Android Wear du téléphone  
   <img src="./images/M-S-SW-AW1.png" style="zoom:75%;" />   
   <img src="./images/M-S-SW-AW2.png" style="zoom:75%;" /> 
8. Réactivez la mise à jour automatique des applications Google Play et mettez à jour manuellement vers [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app).

#### Méthode 2 (avec un ordinateur) {#method-2-with-a-computer}

1. Installez [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app) et appairez la montre avec votre téléphone.
2. Vérifiez que la version des services Google Play de votre montre est supérieure à 9 (la version d'usine du dernier firmware est 8.7).  
   Paramètres -> À propos -> Versions  
   <img src="./images/M-S-SW-AW3.png" style="zoom:75%;" />   
   <img src="./images/M-S-SW-AW3a.png" style="zoom:75%;" />   
   Si c'est le cas, c'est terminé : voir plus haut comment sélectionner un cadran xDrip.  
   Sinon, continuez ci-dessous.
3. [Téléchargez](https://www.apkmirror.com/apk/google-inc/google-play-services-android-wear/google-play-services-android-wear-9-8-41-release/google-play-services-9-8-41-534-130237018-android-apk-download/download/) une version plus récente des services Google Play. Renommez le fichier avec un nom plus court, par exemple `GPS.apk`.
4. [Installez ADB et chargez-le sur la montre](../troubleshoot/ADB).

### Wear OS 2.x et 3.x {#wear-os-2x-and-3x}

#### Méthode 1 (la plus simple) {#method-1-easiest-1}

Il n'est pas toujours possible d'aller au bout de cette procédure : si elle échoue, essayez la méthode 2.

1. Désappairez la montre de votre téléphone si elle était déjà appairée.
2. Désinstallez Wear OS de votre téléphone s'il est installé.  
   Si d'autres montres Android Wear sont connectées, vous devrez peut-être les appairer de nouveau.
3. Désactivez la mise à jour automatique des applications dans Google Play.
4. Installez une ancienne version de Wear OS [2.51.0.398446042.gms](https://www.apkmirror.com/apk/google-inc/android-wear/android-wear-2-51-0-398446042-gms-release/wear-os-by-google-smartwatch-2-51-0-398446042-gms-android-apk-download/).
5. Ouvrez Android Wear et appairez la montre, acceptez et autorisez tout : si vous voulez désactiver certaines fonctions, vous le ferez une fois l'installation de xDrip terminée.
6. Sur la montre, ouvrez Paramètres, Applis et notifications, Infos sur les applis, Applis système et cherchez Google Play Store. Sélectionnez Désinstaller les mises à jour. Confirmez. (Remarque : la montre met automatiquement à jour son application, vous devez faire vite une fois la version rétrogradée.)  
   <img src="./images/M-S-SW-AW6.png" style="zoom:65%;" />
7. Sur la montre, ouvrez Google Play Store et faites défiler jusqu'à Applis sur votre téléphone. Sélectionnez xDrip et installez-le.  
   <img src="./images/M-S-SW-AW7.png" style="zoom:65%;" />
8. Choisissez un cadran xDrip par un appui long sur le cadran actuel.

#### Méthode 2 (la meilleure) {#method-2-best}

**Recommandé :** suivez [cette vidéo](https://www.youtube.com/watch?v=ejrmH-JEeE0) qui détaille la procédure.

Vous devez être connecté au Wi-Fi, et votre montre aussi.

1. Installez [Wear OS](https://play.google.com/store/apps/details?id=com.google.android.wearable.app) et appairez votre montre.
2. Installez et ouvrez [Wear Installer 2](https://play.google.com/apps/testing/org.freepoc.wearinstaller2) sur votre téléphone.  
   <img src="./images/M-S-SW-AW9.png" style="zoom:75%;" />
3. Activez le mode développeur sur la montre (instructions [ici](../troubleshoot/ADB#smartwatch) : uniquement sur la montre, puis revenez ici)
4. Activez le débogage ADB via Wi-Fi sur la montre.  
   <img src="./images/M-S-SW-AW8.png" style="zoom:65%;" />
5. Notez l'adresse IP de la montre.  
   <img src="./images/M-S-SW-AW10.png" style="zoom:65%;" />
6. Ouvrez l'application sur la montre et recopiez l'adresse IP dans l'application du téléphone.  
   Appuyez sur `Done`  
   <img src="./images/M-S-SW-AW11.png" style="zoom:75%;" />
7. Sélectionnez xDrip  
   <img src="./images/M-S-SW-AW12.png" style="zoom:75%;" />  
   Wear Installer va extraire l'apk de la montre.  
   <img src="./images/M-S-SW-AW13.png" style="zoom:75%;" />  
   Acceptez l'autorisation de débogage sur votre montre si elle vous est demandée.  
   <img src="./images/M-S-SW-AW14.png" style="zoom:75%;" />
8. Une fois prêt, sélectionnez `INSTALL` et laissez l'application travailler sans intervenir : cela peut prendre quelques minutes.  
   <img src="./images/M-S-SW-AW15.png" style="zoom:75%;" />
9. Surveillez les messages pendant la procédure, mais n'intervenez pas.  
   <img src="./images/M-S-SW-AW16.png" style="zoom:75%;" />
10. Une fois terminé, sélectionnez `FINISH`.  
    <img src="./images/M-S-SW-AW17.png" style="zoom:75%;" />
11. Si l'installation de xDrip sur la montre a échoué, recommencez.

##### Alternatives à la méthode 2 {#method-2-alternatives}

Utilisez [GeminiMan Wear OS Manager](https://play.google.com/store/apps/details?id=com.geminiman.wearosmanager) ou [Easy Fire Tools](https://play.google.com/store/apps/details?id=de.agondev.easyfiretools) (fonctionnement similaire).

#### Méthode 3 (avec un ordinateur) {#method-3-with-a-computer}

1. Installez [ADB](../troubleshoot/ADB).
2. Téléchargez xDrip sur un ordinateur et extrayez l'APK (c'est un fichier compressé).  
   **Ce doit être exactement la même version que celle de votre téléphone.**
3. Parcourez le paquet APK de xDrip avec un outil d'archives, triez les fichiers de `res` par taille et copiez le plus gros (c'est l'apk Wear intégré, simplement nommé autrement) dans votre dossier ADB.
4. Chargez l'extension Wear de xDrip sur la montre.

### Wear OS 5 {#wear-os-5}

Google et Samsung ont apporté d'importants changements à Wear OS 5 et ne permettent plus facilement l'installation de cadrans personnalisés.

L'installation du cadran AAPS doit se faire avec Wear Installer 2 en suivant [cette vidéo](https://www.youtube.com/watch?v=EvTGEnPA9PY).

**Si vous changez de cadran par erreur, vous devrez refaire la procédure ci-dessus.**

### Mettre à jour xDrip sur votre montre {#update-xdrip-on-your-watch}

#### Wear OS 1.x {#wear-os-1x-1}

Pour forcer la mise à jour de l'application de la montre, synchronisez simplement toutes les applications.  
<img src="./images/M-S-SW-AW32.png" style="zoom:75%;" />

#### Wear OS 2.0 à 4.0 {#wear-os-20-to-40}

Vous devrez désinstaller puis réinstaller l'application de la montre à chaque [mise à jour](../use/update) de xDrip sur votre téléphone pour garder les deux applications synchronisées.

Depuis le 13 avril 2021, xDrip peut mettre à jour automatiquement votre version Wear si une version compatible est déjà installée (au minimum la [Nightly du 13 avril 2021](https://github.com/NightscoutFoundation/xDrip/releases/tag/2021.04.13)).

Pour la version mise à jour, voici les [instructions](https://github.com/NightscoutFoundation/xDrip/issues/1648) :

- Installez la dernière version Nightly du composant WearOs de xDrip sur la montre, par exemple avec l'application Wear Installer, en rétrogradant le Play Store ou manuellement via adb (voir plus haut).
- Vérifiez que le mode développeur et le débogage adb via Wi-Fi sont activés sur la montre (voir plus haut : Wear OS 2 méthode 2 étape 4)
- Allez dans xDrip Prefs sur la montre et faites défiler jusqu'à `Force Update` : appuyez dessus
- La montre devrait vérifier ADB et demander une autorisation : sélectionnez `Always Allow`
- Elle vous dira probablement qu'ADB ne fonctionne pas parce qu'il manque l'autorisation
- Retournez dans xDrip Prefs sur la montre et appuyez sur Force Update
- Cette fois, elle devrait indiquer qu'ADB est correct, puis demander à l'application xDrip du téléphone d'envoyer la dernière version
- Celle-ci devrait se télécharger, puis xDrip s'installera tout seul.

Si les versions sont identiques, cela ne fera pas grand-chose, mais cette procédure permet de forcer xDrip à envoyer la dernière version à l'avenir ; xDrip devrait de toute façon détecter automatiquement les changements de version et se mettre à jour en arrière-plan. Pour vous amuser, vous pouvez installer la dernière Nightly sur la montre, puis rétrograder votre téléphone et vérifier que la mise à jour rétrograde aussi la version de l'application de votre montre. Les informations de version devraient s'afficher à côté du texte `Force Update`.

L'idée est que vous n'avez plus besoin d'utiliser Wear Installer ou la méthode utilisée lors de la première installation (par exemple adb sur PC ou rétrogradation du Play Store) puisque xDrip peut se mettre à jour lui-même.

#### Wear OS 5.0 {#wear-os-50}

Réinstallez le cadran avec [Wear Installer 2](#wear-os-5).

<br>

[*Dernière modification le 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
