---
source_hash: 5577d64214
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_cloud_upload_grey600_48dp.png" style="width:5%;" />&ensp;Chargement vers Cloud
:::

Le chargement vers le cloud vous permet d'envoyer vos glycémies vers divers services cloud ou bases de données.  
Cela permet de partager les données avec des appareils autres que xDrip et de produire des rapports. 

### Synchronisation Nightscout (REST-API) {#nightscout-sync-rest-api}

::: xdripitem Synchronisation Nightscout (REST-API)
&ensp;L'API REST est le moyen standard de se connecter à Nightscout  
:::

[Nightscout](https://nightscout.github.io/) est la méthode universelle pour partager vos valeurs de glycémie, créer des rapports et bien plus encore...

Une fois votre site Nightscout créé, activez la synchronisation pour envoyer les données depuis xDrip.

::: xdripitem Activée<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;L'API REST est le moyen standard de se connecter à Nightscout  
:::

Si vous voulez utiliser Nightscout pour partager vos glycémies, vérifiez que cette option est activée si vous utilisez un téléphone mobile avec une carte SIM et un forfait de données. Sinon, l'envoi n'aura lieu que lorsque vous êtes connecté à un réseau Wi-Fi, ce qui convient si vous utilisez Nightscout pour collecter des données pour vos rapports.

::: xdripitem Utiliser les données mobiles<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Charger même en utilisant les données mobiles  
:::

Si vous utilisez des filtres ou des plugins de calibration, vous pouvez sélectionner cette option pour envoyer à Nightscout les données telles qu'affichées par xDrip, au lieu des données non calibrées/non filtrées.

::: xdripitem Envoyer la glycémie affichée<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Utiliser le lissage du bruit et les plugins (si activés) pour les valeurs diffusées 
:::

L'URL de base est composée de votre API_SECRET (ou d'un jeton) et de l'URL de votre site.  
L'exemple fourni dans la boîte de dialogue concernait un Nightscout hébergé sur Azure.

::: xdripitem URL de base
&ensp;Format: https://password@hostname/api/v1/  
:::

Le format de l'URL doit être le suivant :

**`https://your-API_SECRET@your-site.domain.fqd/api/v1/`**

Vous trouverez l'API_SECRET dans les [variables](https://nightscout.github.io/nightscout/setup_variables/#nightscout-configuration) de votre Nightscout.

Vous pouvez aussi utiliser un [jeton](https://nightscout.github.io/nightscout/security/#create-authentication-tokens-for-users) admin pour vous authentifier ; l'URL ressemblerait alors à ceci :

**`https://xdrip-12ab34cd5678ef90@your-site.domain.fqd/api/v1/`**

Contactez le fournisseur si vous utilisez un service hébergé.

::: info Plusieurs sites
Si vous avez plusieurs sites Nightscout, xDrip peut envoyer vers plusieurs URL Nightscout **séparées par des espaces**.  
***Seules les valeurs de glycémie sont envoyées vers la ou les URL secondaires, pas les traitements***
:::

Si plusieurs appareils envoient vers Nightscout (ce qui n'est pas recommandé), vous voudrez peut-être aussi télécharger les traitements depuis Nightscout pour voir les informations envoyées par les autres.

::: xdripitem Télécharger les données<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Essayer également de télécharger des données depuis Nightscout  
:::

::: warning Calibration automatique
Il s'agit du même réglage [Calibration automatique](../calibrate/advancedcal#use-treatment-bg-values) que dans les calibrations. À utiliser avec précaution.
:::

::: xdripitem Calibration automatique<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibrer en utilisant les nouvelles valeurs de glycémies si les conditions semblent pouvoir le faire, sans demander confirmation (expérimental)  
:::

<br>

::: xdripitem Options supplémentaires
:::

Si votre Nightscout n'est disponible que sur un serveur local (sur une IP privée), n'essayez pas d'envoyer de données vers Nightscout lorsque vous n'êtes pas chez vous. Ignorez ceci pour un Nightscout dans le cloud.

::: xdripitem Ne pas effectuer les chargements par LAN<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Pour les serveurs locaux avec des adresses 192.168.x.x, ne pas essayer de charger quand il n’y a aucune connectivité réseau local. 
:::

Vous pouvez envoyer le niveau de batterie de votre transmetteur ou de votre capteur (si pris en charge).

::: xdripitem Charger la batterie du transmetteur<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Envoyer votre niveau de batterie du transmetteur à Nightscout. Décocher si votre capteur de batterie ne marche pas.
:::

::: xdripitem Envoyer le niveau de batterie de l'émetteur Dexcom<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Envoyer les statistiques de la batterie du Dexcom à Nightscout. Inclut toutes les données affichées sur l'écran Statut du Collecteur.
:::

Vous pouvez envoyer les [traitements](./mainUI#treatments) saisis localement vers le [Care Portal](https://nightscout.github.io/nightscout/setup_variables/#careportal-careportal) de Nightscout.

::: xdripitem Charger les traitements<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Envoyer des données de traitement à Nightscout. Décochez si votre portail ne marche pas.
:::

Vous pouvez configurer une alerte en cas d'échec de l'envoi, et ajouter des informations aux données de glycémie envoyées.

::: xdripitem Alerter en cas d'échecs<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Afficher et émettre une notification si le chargement vers Nightscout échoue.
:::

::: xdripitem Ajouter les informations sources au nom du périphérique<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Pour Dex, envoie le type de collecteur (par exemple OB1) et le statut de remplissage des valeurs (natives) vers Nightscout.
:::

##### Envoyer l'historique vers Nightscout {#backfill-data-to-nightscout}

Si vous avez créé récemment un site Nightscout et voulez y envoyer vos données historiques depuis la base de données de xDrip, vous pouvez utiliser la récupération d'historique (back-fill).

::: xdripitem Réécrire les données
&ensp;Envoyer les valeurs BG vers l'historique de récupération
:::

Sélectionnez le premier jour de la période à envoyer (jusqu'à aujourd'hui) et appuyez sur **DO IT!**  
Selon la quantité de données et la vitesse du réseau, l'envoi peut prendre très longtemps (des heures).

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Nightscout Backfill
Choose the date for the oldest record to send to Nightscout. Use with care!  


<div style="background-color: gray; color: white; text-align: center;">  &emsp;FEBRUARY 12, 2022 11:29PM&emsp;</div>  


<span style="background-color: gray; color: white; text-align: center;">  &emsp;DO IT!&emsp;</span>&emsp;ANNULER
:::

### MongoDB {#mongodb}

::: warning Attention
Cette méthode est obsolète pour Nightscout.
:::

Vous pouvez envoyer directement les glycémies et l'état de l'appareil vers une base de données Mongo.

::: xdripitem MongoDB
&ensp;Téléchargement direct de la base de données, non recommandé pour Nightscout
:::

L'envoi vers MongoDB est obsolète depuis le rachat de mLab par MongoDB et la migration de beaucoup d'utilisateurs vers Atlas : **vous ne pouvez pas utiliser d'URI de type DNS seed `mongodb+srv`**.  
N'utilisez cette fonction que si vous gérez votre propre base de données [Mongo](https://github.com/mongodb/mongo) ; le port par défaut est 27017.

La structure de l'[URI de chaîne de connexion](https://www.mongodb.com/docs/manual/reference/connection-string/#connection-string-uri-format) est :

```
mongodb://databaseusername:databasepassword@your.mongo.url/databasename
```

Pour que la base de données reste compatible avec Nightscout, ne modifiez pas Nom de la Collection ni Nom de la Collection d'état du périphérique par rapport aux valeurs par défaut (si vous les modifiez, vous devrez aussi modifier les variables correspondantes dans Nightscout, `MONGODB_COLLECTION` et `MONGO_DEVICESTATUS_COLLECTION`).

::: info
Les données envoyées peuvent ne pas s'afficher dans la page web de Nightscout, mais seulement dans les rapports Nightscout.
:::

### InfluxDB {#influxdb}

Vous pouvez aussi envoyer les données vers une base [InfluxDB](https://www.influxdata.com/products/influxdb-overview/) et utiliser Grafana pour les présenter.

::: xdripitem InfluxDB
&ensp;Si vous utilisez une base de données privée InfluxDB, ceci doit être activé
:::

Notez que votre URI InfluxDB s'exprime ainsi :

`https://host_address:port`, par exemple pour un serveur local : `https://192.168.0.56:8086`

### Dex Share {#dex-share}

::: warning Votre nom d'utilisateur ne peut pas être un numéro de téléphone
Créez un [compte dépendant](https://www.dexcom.com/faqs/how-do-i-create-a-dependent-account) pour avoir un nom d'utilisateur composé uniquement de texte.  
Une fois le nouveau compte dépendant créé, vérifiez que vous êtes connecté avec ce compte dans vos applications Dexcom et recréez tous les abonnés.
:::

Une fois que vous avez un abonné actif, créé par les applications Dexcom, vous pouvez utiliser xDrip pour envoyer les données vers Dexcom Share.

::: xdripitem Chargement Dexcom Share
&ensp;Chargement des données vers les serveurs Dexcom afin que vous puissiez utiliser vos données avec des applications Dexcom
:::

::: info
Vous pouvez envoyer vos glycémies vers Dexcom Share, **pas vers Dexcom Clarity**.
:::

::: xdripitem Charger les valeurs BG vers Dexcom Share<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Activer ceci pour charger vers les serveurs Dexcom Share
:::

Si vous utilisez un compte américain, activez cette option ; **pour tout autre pays, laissez-la désactivée**. 

::: xdripitem Compte Dex basé aux USA<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Activé = votre compte et les applications abonnés sont aux USA
:::

Saisissez les identifiants que vous utilisez pour vous connecter à Clarity.

::: xdripitem Utilisateur du compte Dexcom Share
&ensp;Votre login pour le site Dexcom Share
:::


::: xdripitem Mot de passe de compte Dexcom Share
&ensp;Votre mot de passe pour le compte Dexcom Share
:::

### Tidepool {#tidepool}

::: xdripitem Tidepool
&ensp;Envoyer les données au service Tidepool
:::

Si vous avez un compte [Tidepool](https://www.tidepool.org/), vous pouvez y envoyer automatiquement vos données et les partager avec votre endocrinologue.  
Si xDrip peut afficher les [informations de basale provenant d'un état externe](./display#basal-information), elles seront aussi envoyées vers Tidepool.

::: xdripitem Synchroniser vers Tidepool<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

Saisissez votre adresse e-mail et votre mot de passe (ceux utilisés lors de votre [inscription](https://app.tidepool.org/signup/personal)).

::: xdripitem Nom d'utilisateur
Votre nom d'utilisateur Tidepool, normalement votre adresse e-mail
:::

::: xdripitem Mot de passe de connexion
Mot de passe de connexion Tidepool
:::

Une fois cela fait, testez la connexion.

::: xdripitem Test de la connexion Tidepool
:::

Tidepool n'a pas besoin de données en temps réel : sélectionnez avec le curseur la période d'envoi des données. La valeur par défaut est de 15 minutes.

::: xdripitem Age des données (15)
:::

N'utilisez **PAS** les serveurs de test (laissez l'option désélectionnée).

::: xdripitem Utiliser les serveurs d'Intégration (test)<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

Vous pouvez choisir de n'envoyer les données que dans certaines conditions, pour économiser la batterie et les frais de données.

::: xdripitem Uniquement lors de la charge<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Télécharger des données uniquement pendant la charge
:::

::: xdripitem Seulement en Wi-Fi<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Télécharger des données uniquement lorsque vous êtes connecté à un réseau illimité comme le Wifi
:::

Si vous envoyez aussi manuellement les données de votre pompe, vous voudrez peut-être désactiver l'envoi des traitements par xDrip pour éviter les doublons.

::: xdripitem Ne pas télécharger les traitements<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Télécharger uniquement les données MGC pour éviter les doublons avec l'envoi manuel de la pompe
:::

##### Web Deposit {#web-deposit}

Web Deposit est une API simple d'envoi par lots, utilisée actuellement pour le diagnostic. Elle est cachée derrière le Mode développeur et n'est pas destinée à un usage courant.

### NightLite {#nightlite}

::: xdripitem NightLite
&ensp;Lightweight Nightscout compatible service intended for followers
:::

NightLite est un service d'abonné léger et compatible Nightscout, une alternative plus simple à l'hébergement de votre propre site Nightscout si vous avez seulement besoin de partager votre glycémie avec des abonnés.

Consultez la [configuration de l'abonné NightLite](./nightlite) pour la procédure d'installation complète.

::: xdripitem Upload to NightLite<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Whether to upload to the remote service
:::

::: xdripitem NightLite URL
&ensp;Typically entered by scanning QR code from dashboard  
&ensp;This contains your security key - do not disclose it
:::

Une fois l'option activée, vous pouvez afficher un QR code contenant vos informations de connexion NightLite, que vos abonnés pourront scanner.

::: xdripitem Afficher le code QR
:::

### Nocturne {#nocturne}

::: xdripitem Nocturne
&ensp;Télécharger vers Nocturne API V4
:::

[Nocturne](https://getnocturne.dev/) est le successeur moderne de Nightscout proposé par la Nightscout Foundation. Si vous gérez votre propre instance Nocturne, xDrip peut y envoyer directement les données.

::: xdripitem Activer l'envoi vers Nocturne<span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

Saisissez l'adresse de votre instance Nocturne.

::: xdripitem URL de l'instance Nocturne
&ensp;Entrez l'URL de votre instance Nocturne (par exemple https://mynocturne.example.com)
:::

Autorisez ensuite xDrip auprès de votre instance. Aucun mot de passe n'est stocké dans xDrip : un code s'affiche, que vous saisissez dans le navigateur sur la page d'approbation de votre instance Nocturne pour finaliser la connexion.

::: xdripitem Se connecter à Nocturne
&ensp;Autorisez xDrip+ avec votre instance Nocturne
:::

#### Connexion rapide depuis Nocturne {#quick-connect-from-nocturne}

Au lieu de saisir l'URL de l'instance, laissez Nocturne configurer xDrip pour vous. Dans votre instance Nocturne, ouvrez Connectors & Apps, puis Set Up an Uploader, et sélectionnez xDrip+ dans la liste CGM Apps.

<img src="./images/M-S-N1.png" style="zoom:75%;" />

La page Set up xDrip+ affiche un QR code Quick Connect.

<img src="./images/M-S-N2.png" style="zoom:60%;" />

::: warning Scannez ce QR code avec l'application appareil photo de votre téléphone, pas avec xDrip
Le QR code Quick Connect est un lien qui ouvre xDrip sur votre téléphone directement dans la configuration du connecteur Nocturne. Le scanner avec l'importateur de paramètres [Configuration automatique](./copysettings#auto-configure) de xDrip ne fonctionnera pas.
:::

xDrip affiche alors un code d'autorisation. Saisissez-le dans le champ Enter Authorization Code de cette même page Nocturne et appuyez sur Continue pour finaliser la connexion.

#### Autre méthode : QR code de paramètres {#alternate-method-settings-qr-code}

Si vous préférez préparer vous-même les paramètres Nocturne, utilisez le configurateur ci-dessous. Saisissez l'URL de votre instance, choisissez ce qu'il faut envoyer, puis scannez le QR code généré depuis xDrip avec [Configuration automatique](./copysettings#auto-configure) (Caméra, ou QR code depuis un fichier avec le PNG téléchargé). xDrip liste les paramètres et demande confirmation avant de les appliquer.

::: info Contrairement au QR code Quick Connect ci-dessus, celui-ci doit être scanné avec xDrip, pas avec l'application appareil photo.
:::

Une fois les paramètres importés, ouvrez Paramètres, Chargement vers Cloud, Nocturne, appuyez sur Se connecter à Nocturne et saisissez sur votre instance Nocturne le code d'autorisation affiché par xDrip. Les jetons d'autorisation ne font jamais partie du QR code.

<iframe src="./nocturne-qr.html" title="xDrip+ Nocturne QR configurator" style="width:100%; height:800px; border:1px solid #d9dee5; border-radius:8px; background:#f6f7f9;" loading="lazy"></iframe>

Vous pouvez aussi [ouvrir le configurateur dans une page séparée](./nocturne-qr.html){target="_blank"}.

Sélectionnez les données à envoyer. Les glycémies sont activées par défaut ; tout le reste est facultatif.

::: xdripitem Upload SGV<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger les glycémies du capteur CGM
:::

::: xdripitem Charger les traitements<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger des bolus, des glucides, des notes et des événements de l'appareil
:::

::: xdripitem Télécharger les calibrations<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger les étalonnages du capteur
:::

::: xdripitem Télécharger les tests sanguins<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger les résultats du lecteur de glycémie
:::

::: xdripitem Télécharger la fréquence cardiaque<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger les données de fréquence cardiaque
:::

::: xdripitem Télécharger le nombre de pas<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger les données du nombre de pas
:::

::: xdripitem Télécharger le statut de l'appareil<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger le niveau de batterie du téléphone et le statut de charge
:::

::: xdripitem Télécharger le suivi des mouvements<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Télécharger les classifications d'activité reconnues
:::

::: xdripitem Utiliser les données mobiles<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Autoriser les téléversements via les données mobiles
:::

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
