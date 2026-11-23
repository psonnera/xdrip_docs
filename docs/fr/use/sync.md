---
source_hash: 8ff0f07a91
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_google_circles_communities_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Synchronisation
:::

::: warning Ancienne synchronisation xDrip
En juillet 2024, Google a arrêté l'[API Firebase](https://firebase.google.com/docs/cloud-messaging/migrate-v1) obsolète que xDrip utilisait pour la synchronisation xDrip.  
Mettez à jour xDrip vers une version du [23 juillet 2024](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.07.23) ou plus récente pour utiliser l'ancienne méthode de synchronisation.  
Il est recommandé de mettre à jour xDrip vers la dernière version publiée.
:::

::: warning Attention
Les [services Google Play](https://play.google.com/store/apps/details?id=com.google.android.gms) sont indispensables pour utiliser cette fonction. Assurez-vous qu'ils sont présents, activés et non soumis à l'optimisation de la batterie.
:::

xDrip propose un mécanisme unique de synchronisation en temps réel entre appareils Android, qui rend le partage des glycémies et des traitements aussi simple que possible.

La clé de sécurité sous-jacente peut être personnalisée au lieu d'utiliser la clé du compte Google (non modifiable).

::: xdripitem Synchroniser en utilisant la clé de sécurité personnalisé <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Key est utilisé au lieu du compte Google
:::

##### Clé de sécurité de groupe de dispositifs {#handset-group-security-sync-key}

Une clé unique est créée à l'installation de xDrip (elle sera différente si vous réinstallez xDrip) et doit être la même sur tous les appareils utilisant la synchronisation xDrip. Même si vous pouvez personnaliser cette clé (lettres et chiffres), vous la laisserez généralement telle qu'elle a été générée.

::: xdripitem Clé de sécurité de groupe de dispositifs
&ensp;Clé de regroupement de synchronisation des appareils
:::

##### Soyez maître pour les Abonnés {#be-master-for-followers}

L'appareil qui reçoit les glycémies du capteur sera le maître, tous les autres seront des abonnés.  
Un seul maître peut utiliser une même clé de sécurité. Si deux maîtres sont détectés, le dernier arrivé est désactivé et repasse en mode abonné.

::: xdripitem Soyez maître pour les Abonnés <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Cet appareil envoie des données aux Abonnés
:::

##### Accepter les actions des Abonnés {#accept-followers-actions}

Vous pouvez configurer le téléphone maître pour qu'il reçoive et accepte les traitements et étalonnages des abonnés. Soyez extrêmement prudent avec cette fonction si vous utilisez les étalonnages automatiques. N'oubliez pas non plus que des démarrages et arrêts de capteur peuvent être envoyés par les abonnés et acceptés par le maître.

::: xdripitem Accepter les actions des Abonnés <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Les traitements et étalonnages des Abonnés seront acceptés
:::

##### Utiliser xDrip Cloud {#use-xdrip-cloud}

Après l'arrêt par Google, en juillet 2024, de l'[API Firebase](https://firebase.google.com/docs/cloud-messaging/migrate-v1) obsolète utilisée pour la synchronisation xDrip, une nouvelle méthode de partage a été développée.

::: warning Doit être réglé de la même façon sur tous les téléphones
Maître et abonnés. Soit activé pour tous, soit désactivé pour tous.
:::

::: xdripitem Utiliser xDrip Cloud <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Utilisez les nouveaux serveurs cloud de xDrip+. Les maîtres et les abonnés doivent tous avoir ce paramètre défini à l'identique.  
:::

Si xDrip consomme trop de batterie en données mobiles, vous pouvez essayer d'activer cette option.

::: xdripitem Économiser l'énergie <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Réduire la charge sur la batterie et le réseau en utilisant le traitement par lots et en excluant les données inutiles  
:::

##### Maison entière {#whole-house}

Basés sur le projet [Parakeet](https://github.com/jamorham/wixel-xDrip), plusieurs appareils **maîtres** peuvent former un réseau couvrant toute la maison.  
Si vous utilisez des capteurs Libre, vous pouvez aussi utiliser cette fonction : voir [ici](https://github.com/tzachi-dar/LibreAllHouse) comment créer votre réseau pour toute la maison.

::: xdripitem Maison entière <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Participer au réseau de la maison
:::

::: xdripitem Mode Libre dans toute la maison <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Ce téléphone sera un collecteur dans tout le réseau domestique
:::

##### Mise en veille à distance {#remote-snoozing}

La mise en veille à distance permet de propager la demande de mise en veille dans le groupe. Le maître comme les abonnés peuvent mettre les alarmes en veille. À utiliser avec précaution.

::: xdripitem Envoyer la mise en veille vers tous <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;La mise en veille rendra silencieux tous les combinés du groupe avec le paramètre d'acceptation ci-dessous activé sur eux
:::

::: xdripitem Confirmer l'envoi de mise en veille <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Ouvrir une boîte de dialogue pour confirmer l'envoi de chaque veille distante
:::

::: xdripitem Accepter les mises en veille distantes <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Autoriser les appareils distants à mettre sous silence les alarmes sur celle-ci
:::

::: xdripitem Le nom du WiFi doit correspondre <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Accepter uniquement si le nom du réseau WiFi distant commence par les mêmes lettres que les nôtres et correspond très étroitement
:::

##### Diffusion locale {#local-broadcast}

Diffusion locale envoie ou accepte des mises en veille vers/depuis d'autres applications (non xDrip) installées sur le même téléphone, indépendamment de la mise en veille à distance entre téléphones xDrip.

::: xdripitem Diffusion locale <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Envoyer des répétitions à d'autres applications sur ce combiné
:::

::: xdripitem Accepter la diffusion locale <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Accepter les mises en veille d'autres applications sur ce combiné
:::

##### Désactiver la synchronisation {#disable-sync}

Désactiver toutes les fonctionnalités de synchronisation désactive complètement le partage. Vous devrez peut-être redémarrer votre téléphone lorsque vous la réactiverez.

Vous pouvez utiliser cette option en cas d'échec complet de la synchronisation ou avec un téléphone sans services Google Play.

::: xdripitem Désactiver toutes les fonctionnalités de synchronisation <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Palliatif, arrête complètement toute synchronisation. Peut nécessiter le redémarrage après avoir été réactivé. Utiliser avec précaution!
:::

### Synchronisation milieu désertique {#desert-sync}

Synchronisation milieu désertique permet la synchronisation xDrip sans internet ni couverture de données mobiles.

::: xdripitem Synchronisation milieu désertique
<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xxhdpi/desert_sync.png" style="width:5%;" />&ensp;Suivi milieu désert
:::

Synchronisation milieu désertique vous permet de partager les données entre votre xDrip maître et ses abonnés lorsque internet n'est pas disponible. Cela peut arriver en voyage hors couverture réseau ou sur un intranet local (sans accès à internet).

Activez la synchronisation milieu désertique sur tous les appareils.

::: xdripitem Synchronisation milieu désertique <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Activer la fonctionnalité de synchronisation locale sans internet
:::

Si vous connaissez l'adresse IP du maître (cas des intranets locaux), saisissez-la ici.  
Vous trouverez l'adresse IP du maître dans les paramètres Android du téléphone - À propos du téléphone - Adresse IP.

::: xdripitem Adresse IP du maître
:::

Affichez maintenant le QR code des paramètres du maître et scannez-le sur vos abonnés avec [Configuration automatique](./copysettings#auto-configure).

::: xdripitem Afficher le code QR
Code-barres à scanner pour les abonnés afin de les configurer automatiquement
:::

Si vous voulez sécuriser votre connexion (intranets locaux et Wi-Fi public), vous pouvez activer https.

::: xdripitem Utiliser HTTPS <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Ajouter une autre couche de chiffrement pour les réseaux partagés, par exemple pour les Wi-Fi publics
:::

Si vous n'avez ni données mobiles ni Wi-Fi, mettez le téléphone maître en mode point d'accès Wi-Fi et connectez-y les abonnés (partage de connexion). La distance maximale entre les appareils sera limitée. Cela pèsera aussi beaucoup sur la batterie du maître : prévoyez une batterie externe de secours.  
En partage de connexion, vous devrez activer un [service web](./interapp#web-service) sur le maître. Assurez-vous que le secret est identique sur le maître et les abonnés.

Consultez l'état du système pour vérifier que tout se connecte correctement.

<img src="./images/M-S-SY8d2.png" style="zoom:75%;" />

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
