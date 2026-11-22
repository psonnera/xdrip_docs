---
source_hash: a6ac1989f7
source_commit: 0bbdbd2
---
Vous avez besoin d'un téléphone Android.

![https://www.android.com/static/images/logos/andy-peace.png](https://www.android.com/static/images/logos/andy-peace.png)

- La version minimale d'Android prise en charge est la 8.0 (la prise en charge d'Android 7 a été retirée avec la version du [12 juillet 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)).
- Si vous connectez xDrip à un capteur, votre téléphone doit prendre en charge le Bluetooth Low Energy (BLE) : vous pouvez le vérifier avec des utilitaires [comme celui-ci](https://play.google.com/store/apps/details?id=com.treeteam.blechecker).
- Si vous voulez utiliser la fonction principal - abonné intégrée à xDrip (appelée xDrip Sync), les deux téléphones doivent avoir les [Services Google Play](https://play.google.com/store/apps/details?id=com.google.android.gms) installés.
- Pour utiliser les fonctions de scan NFC des capteurs Libre 1 et 2/2+ (UE uniquement), ou pour vous connecter directement à un capteur Libre 2/2+ (UE), votre téléphone doit disposer d'un lecteur NFC compatible.
- Si vous utilisez Android 16 ou plus récent, assurez-vous d'utiliser une version récente de xDrip (au moins la [dernière version stable](./download#latest-release), nous en parlerons plus loin : continuez la lecture).

### Services Google Play {#google-play-services}

​	![http://www.gstatic.com/android/market_images/web/favicon_v3.ico](http://www.gstatic.com/android/market_images/web/favicon_v3.ico)

Si votre téléphone n'a pas les Services Google Play (certains téléphones Huawei et chinois ne les ont pas), vous pouvez quand même utiliser xDrip, mais pas la fonction xDrip Sync qui en dépend, comme indiqué ci-dessus.  
Vous pouvez rencontrer des problèmes inattendus avec des systèmes alternatifs basés sur Android.  
Dans ce cas, assurez-vous de [désactiver les fonctions de synchronisation](../use/sync#disable-sync).

### Family Link {#family-link}

<img src="https://families.google/intl/it_ALL/familylink/static/img/fl-icon.svg" style="zoom:25%;" />

Pour installer xDrip sur un téléphone supervisé par [Google Family Link](https://families.google.com/families), **vous devez le désactiver** le temps d'installer l'application.  
Si vous voulez le réactiver ensuite, assurez-vous que xDrip a toutes les autorisations et aucune limite de temps.

### Profil professionnel {#work-profile}

<img src="https://developer.android.com/static/images/work/cards/briefcase_600px.png" style="zoom:15%;" />

Si vous utilisez un téléphone géré par votre entreprise, vous ne pourrez peut-être pas installer xDrip à cause des règles de l'entreprise.

Vous pouvez essayer d'installer l'application depuis un ordinateur avec [Android Debug](../troubleshoot/ADB#smartphone), après avoir activé les options pour les développeurs sur votre téléphone. N'oubliez pas de supprimer xDrip de votre profil professionnel si nécessaire, car il peut être installé dans les deux environnements.

### Précision de l'heure du téléphone {#phone-time-accuracy}

Synchronisez l'horloge de votre téléphone avec le réseau (Paramètres Android -> [Date et heure](https://support.google.com/android/answer/2841106)).  
Vérifiez que vous êtes sur le bon fuseau horaire et que l'heure d'été y correspond.

<img src="./images/Install16.png" style="zoom:65%;" />

### Économies d'énergie {#energy-savings}

**[Désactivez](../troubleshoot/savings)** tous les réglages d'économie d'énergie/de batterie d'Android avant d'installer xDrip.  
Vous pourrez essayer d'en rétablir certains après avoir vérifié que xDrip fonctionne correctement, mais **n'optimisez jamais** xDrip.

<br>

### Play Protect {#play-protect}

::: info Remarque
En général, Google Play Protect ne bloque pas xDrip, mais il peut bloquer [OOP](../use/OOP).
:::

Si xDrip s'arrête de fonctionner chaque nuit entre minuit et 3 h du matin, essayez de désactiver Google Play Protect.  
Comme il s'agit d'une fonction de sécurité importante pour votre téléphone, évitez d'ouvrir des liens inconnus et de télécharger des jeux : gardez votre téléphone CGM aussi sûr que possible si vous décidez de désactiver Play Protect.

Vous trouverez Google Play Protect dans les paramètres de l'application Play Store de votre téléphone.

<img src="./images/Install45.png" style="zoom:75%;" />

<br>

[Passer au téléchargement de xDrip](./download)

<br>

[*Dernière modification le 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.15)
