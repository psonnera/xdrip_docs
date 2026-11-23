---
source_hash: 4a69400131
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_open_in_app_grey600_48dp.png" style="width:5%;" />&ensp;Paramètres inter applications
:::

<br>

Paramètres inter applications propose deux façons de relier xDrip à d'autres applications : la diffusion locale (interne à ce téléphone) et le service web (interne et externe).

### Diffusion locale {#local-broadcast}

La diffusion locale fait envoyer à xDrip des messages internes qui peuvent être utilisés par d'autres applications comme Nightwatch ou AAPS.

::: xdripitem Diffusion locale <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Activer la diffusion locale de données pour que d'autres applications (par exemple NightWatch) puisse écouter les nouvelles valeurs
:::

Si vous utilisez des plugins d'étalonnage ou un filtrage, vous pouvez choisir de diffuser les données brutes ou les données filtrées/étalonnées.

::: xdripitem Envoyer la glycémie affichée <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utiliser le lissage du bruit et les plugins (si activés) pour les valeurs diffusées
:::

Par sécurité, vous pouvez aussi bloquer la diffusion des données bruitées. Par défaut, seul le niveau de bruit extrême n'est pas diffusé.

::: xdripitem Blocage du bruit
&ensp;Niveau à partir duquel les données bruitées ne devraient pas être diffusées car cela pourrait perturber les applis réceptrices
:::

Les applications et téléphones récents devraient accepter la diffusion compatible. Ne la décochez pas.

::: xdripitem Diffusion Compatible <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Envoyer des broadcasts sans verrouiller le modèle de permission ancien
:::

Vous pouvez indiquer le récepteur identifié si vous voulez que xDrip n'envoie ses messages qu'à une application précise. L'usage le plus courant est lorsque xDrip est la source de données d'[AAPS](https://androidaps.readthedocs.io/en/latest/Configuration/xdrip.html#identify-receiver).

::: xdripitem Identifier le récepteur
&ensp;Envoyer uniquement au package nommé
:::

##### Réception depuis NSClient. {#receiving-from-nsclient}

xDrip peut aussi recevoir des messages avec cette fonction : vous pouvez activer ou désactiver la réception des données et des traitements provenant d'autres applications qui diffusent.

::: xdripitem Accepter la Glycémie <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Traiter les données de glucose reçues de l'application NSClient
:::

::: xdripitem Accepter les traitements <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Traiter les données de traitement reçues de NSClient
:::

Vous pouvez activer ou désactiver (**à désactiver pour AAPS !!!**) le son joué après la mise à jour du profil xDrip.

::: xdripitem Importer des sons <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Jouer des sons lors de l'importation de données significatives telles que des profils
:::

Soyez prudent si vous acceptez les étalonnages d'autres applications.

::: xdripitem Accepter les Calibrations <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Traiter les calibrations reçus à partir d'autres applications
:::

### Service web {#web-service}

Documentation d'origine [ici](https://github.com/NightscoutFoundation/xDrip/blob/master/Documentation/technical/Local_Web_Services.md).

::: warning Attention
Si une autre application utilise le port 17580 (comme Diabox), désactivez cette fonction.  
Notez que le service n'est pas disponible en http sécurisé et que les applications [Fitbit](../smartwatch/smartwatch#fitbit) récentes peuvent refuser ses données.
:::

Le service web ouvre un service web local sur votre appareil pour permettre à d'autres appareils (montres) et applications d'en recevoir des données.  
Le serveur web répond aux requêtes à l'adresse `127.0.0.1` sur le port `17580`

::: xdripitem Service Web xDrip <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Exploiter un serveur web local permettant d'interagir avec Fitbit Ionic
:::

Par défaut, le service web n'est accessible qu'à votre appareil ; vous pouvez l'ouvrir pour que d'autres appareils du réseau puissent y accéder. Assurez-vous d'avoir vraiment besoin de cette fonction et d'en comprendre les implications de sécurité. Assurez-vous qu'un secret partagé est défini.

::: xdripitem Service Web Ouvert <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Accepter les connexions depuis n'importe quel réseau au lieu de se limiter à l'intérieur de cet appareil. Il y a des implications de sécurité pour activer ceci ! Le Secret partagé sera requis si défini. 
:::

::: xdripitem Secret du Service Web xDrip
&ensp;Secret partagé pour le service web ouvert (doit correspondre à votre secret Nightscout API)
:::

#### Option d'ouverture {#open-option}

Le service dispose d'une option `Open Web Service` (Service Web Ouvert). Si elle est activée, les connexions peuvent passer par n'importe quelle interface réseau au lieu d'être limitées au réseau local de bouclage de l'appareil. En général, activer cette option expose la connexion Wi-Fi / LAN / Bluetooth PAN de l'appareil, mais elle pourrait aussi être exposée via le réseau mobile si l'opérateur fournit des adresses IP publiques.

Soyez très prudent en activant cette option, car des fonctions puissantes sont accessibles, par exemple l'interface tasker. Il est préférable de l'utiliser avec l'option d'authentification décrite ci-dessous.

#### Authentification {#authentication}

Pour des raisons de sécurité (n'importe qui sur le réseau peut accéder à ce service), vous devriez le protéger par un mot de passe ; si vous avez un site Nightscout, utilisez votre API_SECRET.

Si le `xDrip Web Service Secret` (Secret du Service Web xDrip) est défini à autre chose qu'une chaîne vide (la valeur par défaut), les requêtes arrivant par les réseaux ouverts hors bouclage devront fournir un en-tête http `api-secret` contenant le hash SHA1 du même mot de passe secret, sinon leur connexion sera refusée. Les informations de refus sont enregistrées dans le Journal des événements et renvoyées dans la réponse http. Le code de résultat 403 (forbidden) est renvoyé lorsqu'une connexion est refusée.

De plus, si un client fournit l'en-tête `api-secret` alors que le secret xDrip n'est pas défini, la requête sera refusée. Cette fonction permet aux appareils clients de s'assurer qu'ils se connectent à la bonne instance de xDrip (en utilisant des secrets différents). Cela peut être important, par exemple en boucle fermée.

L'authentification n'est pas requise sur l'interface réseau locale de bouclage (127.0.0.1)

```
api-secret: 915858afa2278f25527f192038108346164b47f2
```

Ci-dessus, l'en-tête http pour le mot de passe `Abc`

#### Point d'accès Nightscout Pebble {#nightscout-pebble-endpoint}

`/pebble` émule la même URL de Nightscout : avec un cadran qui le prend en charge, vous pouvez saisir l'adresse dans le cadran, par exemple définir le point d'accès des données du cadran Pebble Nightscout à :

```
http://127.0.0.1:17580/pebble
```

#### Point d'accès sgv.json {#sgvjson-endpoint}

`/sgv.json` émule `/api/v1/entries/sgv.json?count=24` de Nightscout

```
http://127.0.0.1:17580/sgv.json
```

Le premier enregistrement contient une indication sur les unités utilisées : `units_hint` vaut `mgdl` ou `mmol` pour indiquer la préférence de l'utilisateur, mais les valeurs sont toujours envoyées en mgdl

Vous pouvez aussi accéder au point d'accès des pas en ajoutant un paramètre de requête

```
http://127.0.0.1:17580/sgv.json?steps=1234
```

Dans ce cas, cherchez le nombre `steps_result` dans le premier enregistrement de la réponse json : 200 indique un succès, toute autre valeur un échec de l'enregistrement du nombre de pas. La valeur des pas doit être le compteur de pas cumulé actuel de l'appareil.

Vous pouvez aussi accéder au point d'accès de la fréquence cardiaque en ajoutant un paramètre de requête

```
http://127.0.0.1:17580/sgv.json?heart=123
```

Dans ce cas, cherchez le nombre `heart_result` dans le premier enregistrement de la réponse json : 200 indique un succès, toute autre valeur un échec de l'enregistrement de la fréquence cardiaque. La valeur doit être la fréquence cardiaque actuelle en bpm mesurée par l'appareil.

Vous pouvez combiner les deux comme dans une chaîne de requête classique :

```
http://127.0.0.1:17580/sgv.json?steps=1234&heart=123
```

Une autre option, `brief_mode=Y`, permet d'exclure certains champs de données des résultats pour réduire la taille de la réponse.

Une autre option, `no_empty=Y`, permet qu'un jeu de données vide renvoie `""` au lieu de `"[]"`

Une autre option, `all_data=Y`, permet d'obtenir en plus les données de la session de capteur précédente.

Une autre option, `sensor=Y`, permet d'obtenir des données sur l'âge du capteur

Une autre option, `collector=Y`, permet d'obtenir les messages d'alerte du collecteur. Rien n'est renvoyé si le message est vide.

Vous pouvez aussi accéder au point d'accès tasker en ajoutant un paramètre de requête

```
http://127.0.0.1:17580/sgv.json?tasker=osnooze
```

cherchez `tasker_result` dans la première ligne de la réponse json pour savoir si l'opération a réussi ou échoué.

`OSNOOZE` est une mise en veille opportuniste que vous pouvez appeler même si aucune alerte n'est en cours

`SNOOZE` est la mise en veille tasker classique, qui envoie la mise en veille aux abonnés et utilise plus de CPU

#### Point d'accès treatments.json {#treatmentsjson-endpoint}

`/treatments.json` émule `/api/v1/treatments.json?count=24` de Nightscout

```
http://127.0.0.1:17580/treatments.json
```

#### Point d'accès status.json {#statusjson-endpoint}

Ce point d'accès implémente un petit sous-ensemble des données que vous pourriez recevoir du status.json de Nightscout

```
http://127.0.0.1:17580/status.json
```

Les résultats ressemblent à ceci :

```
{"thresholds":{"bgHigh":9.4,"bgLow":3.9}}
```

Les seuils haut et bas définis dans l'application, exprimés dans les unités locales.

#### Point d'accès Libre 2 {#libre-2-endpoint}

`/Libre2ConnectCode.json` renvoie le tampon de déverrouillage Bluetooth et l'adresse Mac de l'appareil.

Il est utilisé par [whole house](./sync#whole-house).

```
http://127.0.0.1:17580/Libre2ConnectCode.json
```

#### Point d'accès Tasker {#tasker-endpoint}

Le point d'accès `/tasker` vous permet d'envoyer des requêtes à l'interface tasker via http. Ainsi, un cadran qui ne prend en charge que des points d'accès web (par exemple FitBit) pourrait envoyer une demande de mise en veille comme ci-dessous :

```
http://127.0.0.1:17580/tasker/SNOOZE
```

#### Point d'accès des pas {#steps-endpoint}

`/steps` permet de définir les données actuelles du compteur de pas

```
http://127.0.0.1:17580/steps/set/1234
```

Il doit s'agir du compteur de pas cumulé actuel de l'appareil qui mesure les pas, pas d'un historique.

#### Point d'accès de la fréquence cardiaque {#heart-endpoint}

`/heart` permet de définir la fréquence cardiaque actuelle en bpm

```
http://127.0.0.1:17580/heart/set/123/1
```

Il doit s'agir de la fréquence cardiaque actuelle en BPM sur l'appareil de mesure, pas d'un historique. Le premier paramètre est le BPM et le second la précision. Si vous n'êtes pas sûr du paramètre de précision, mettez simplement 1.

<br>

### API du service Broadcast {#broadcast-service-api}

Ce service permet de diffuser les valeurs de xDrip sous forme d'API et peut être utilisé par des applications externes comme [WatchDrip+](https://bigdigital.home.blog/2022/06/16/watchdrip-a-new-application-for-xdrip-watch-integration) (activez la fonction pour WatchDrip+).

::: xdripitem API du service Broadcast <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Active la communication de xDrip avec des applications tiers en utilisant la nouvelle API
:::

::: xdripitem Inclure l'InA dans l'API <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Inclure l'InA (insuline active) sur le point de terminaison de l'API de service Web utilisé par certaines Smartwatch
:::

::: xdripitem Récupérer l'InA depuis l'application compagnon <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Récupérer l'InA (insuline active) depuis l'application compagnon s'exécutant sur le même appareil, par exemple l'app. Omnipod 5
:::

<br>

### Google Health connect {#google-health-connect}

Vous pouvez partager des informations avec Google Health.

::: xdripitem Google Health Connect
&ensp;Envoyer et recevoir des données de Google Health Connect et Google Fit
:::

[Health Connect](https://play.google.com/store/apps/details?id=com.google.android.apps.healthdata&hl=en&gl=US) doit être installé sur votre appareil ; il est disponible à partir d'Android 8.

::: xdripitem Utiliser Health Connect <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Nécessite Android 8+ et l'application Google compagnon ou Android 14+
:::

Vous pouvez ensuite choisir d'utiliser les données entrantes et d'autoriser les données sortantes.

xDrip peut partager les pas, la fréquence cardiaque et la glycémie avec Google Health.

::: xdripitem Recevoir les données de Health Connect <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
:::

::: xdripitem Envoyer des données à Health Connect <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
:::

::: xdripitem Gérer les permissions
&ensp;Ouvrir les paramètres Health Connect pour gérer manuellement les autorisations
:::

Sur certaines versions d'Android (notamment 15 et 16), xDrip n'est pas autorisé à ouvrir directement son écran d'autorisations Health Connect. Il ouvre alors l'application Health Connect : allez dans *Autorisations des applis* (App permissions) et sélectionnez xDrip pour les gérer. Si Health Connect ne peut pas du tout être ouvert, un message vous demande d'ouvrir vous-même l'application Health Connect et d'y gérer les autorisations de xDrip.

[*Dernière modification le 15/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.13)
