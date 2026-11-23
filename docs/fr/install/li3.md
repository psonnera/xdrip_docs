---
source_hash: a98504fa65
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Li3
:::

La source de données Li3, ajoutée dans la version [2026.11.21](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21), connecte xDrip directement à un appareil Li3. Vous pouvez aussi la sélectionner avec l'[assistant de source](./datasource), dans le groupe Libre.

xDrip démarre une nouvelle session, ou reprend une session en cours, par un scan NFC. Il reçoit ensuite les valeurs par Bluetooth.

- Les valeurs arrivent toutes les 5 minutes, ou toutes les minutes si [Libre 1 minute](../use/misc) est activé.
- Lorsque la connexion revient après une interruption, xDrip complète les valeurs manquantes à partir de l'historique de l'appareil. Les valeurs déjà enregistrées ne sont jamais remplacées.
- **Cette source de données ne peut pas être étalonnée.** Si vous essayez, xDrip affiche *This sensor cannot be calibrated.* (ce capteur ne peut pas être calibré).

::: warning Attention
Lorsque xDrip démarre ou reprend une session, l'application officielle ne reçoit plus ses valeurs ni ses alarmes.
:::

<br>

## Avant de commencer {#before-you-start}

- Votre téléphone doit disposer du NFC. Sans NFC, xDrip affiche *This phone has no NFC, so it cannot start a Li3.* (ce téléphone n'a pas de NFC, il ne peut donc pas démarrer un Li3).
- Activez le NFC dans les paramètres du téléphone. xDrip propose d'activer son propre scan NFC s'il est désactivé.
- xDrip a besoin de l'autorisation de localisation, et la localisation doit être activée, pour rechercher l'appareil en Bluetooth. L'écran Li3 demande ce qui manque.
- Une connexion Internet est nécessaire une fois, pour télécharger l'identifiant d'application (app credential).
- Si ce n'est pas encore fait, [vérifiez que xDrip ne sera pas mis en veille](./install#make-sure-xdrip-will-not-be-put-to-sleep).

<br>

## L'écran Li3 {#the-li3-screen}

L'écran Li3 liste les étapes de configuration, indique où vous en êtes et lit les scans NFC tant qu'il est ouvert.  
Il s'ouvre de lui-même lorsque vous sélectionnez la source de données Li3, et lorsque vous appuyez sur Démarrer le capteur alors qu'aucun capteur n'est démarré. Vous pouvez aussi l'ouvrir depuis État du système :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;État du système  
&emsp;Li3 Status  
&ensp;&emsp;Li3 &emsp;Open
:::

Tant que la configuration n'est pas terminée, xDrip affiche aussi une notification qui ouvre cet écran : *Li3 setup not finished; open System Status, Li3*.

Si vous scannez l'appareil alors qu'un autre écran est ouvert, xDrip ouvre l'écran Li3 et vous demande de scanner à nouveau depuis celui-ci : *Scan the device again on the Li3 screen to start it or take it over*.

<br>

## Configuration {#setup}

#### 1. Télécharger l'identifiant d'application {#1-download-the-app-credential}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;DOWNLOAD APP CREDENTIAL&emsp;</div>
:::

L'appareil s'appaire à l'aide d'un identifiant d'application. S'il n'a pas encore été téléchargé, xDrip propose de le télécharger à l'ouverture de l'écran Li3.  
Une fois le téléchargement terminé, la ligne App credential sous les boutons indique *Downloaded*. Si le téléchargement échoue, vérifiez votre connexion Internet et appuyez de nouveau sur Download.

#### 2. ID de compte (uniquement pour reprendre une session démarrée par une application officielle) {#2-account-id-only-to-take-over-a-session-started-by-an-official-app}

Passez cette étape pour démarrer une nouvelle session pour xDrip.

Pour reprendre une session démarrée par une application officielle, xDrip a besoin de l'ID de compte (Account ID) de cette application.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;LOOK UP ACCOUNT ID&emsp;</div>
:::

Connectez-vous avec le compte qui a démarré la session, et non avec un compte abonné. xDrip ne conserve que l'ID de compte, ni l'e-mail ni le mot de passe.  
Si la connexion est refusée en raison de nouvelles conditions d'utilisation, ouvrez l'application officielle avec ce compte, acceptez les conditions, puis réessayez.  
Si la recherche échoue, vous pouvez saisir vous-même l'ID de compte dans les [paramètres Li3](#li3-settings).

Choisissez ensuite l'application qui a démarré la session :

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;SENSOR APP: LI3 APP&emsp;</div>
:::

::: xdripitem Which app started this session?
&ensp;Li3 app  
&ensp;Multi-sensor app
:::

#### 3. Scanner l'appareil {#3-scan-the-device}

L'écran Li3 ouvert, scannez l'appareil avec votre téléphone. xDrip pose l'une de ces questions :

| Appareil              | ID de compte défini                                               | Pas d'ID de compte                                                |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Neuf                 | **Start Sensor** : xDrip reçoit les valeurs. L'application officielle pourra reprendre l'appareil plus tard avec le même compte. | **Start Sensor** : la session est réservée à xDrip sur ce téléphone. **L'appareil ne pourra jamais passer à une application officielle, et il est perdu si xDrip est réinstallé.** |
| Session en cours | **Take over Li3** : l'application officielle ne reçoit plus ses valeurs ni ses alarmes. | Ne fonctionne que pour une session démarrée par xDrip sur ce téléphone. Pour une session démarrée par une application officielle, recherchez d'abord son ID de compte. |

Sans ID de compte, vous pouvez appuyer sur *Look up account ID*, ou sur *Scan anyway* pour continuer sans.

Appuyez sur OK, puis **scannez à nouveau l'appareil dans les cinq minutes** pour confirmer.  
Lorsque cela fonctionne, xDrip affiche *Li3 ready, connecting by Bluetooth*.

Si l'appareil refuse la commande, vérifiez que l'application et l'ID de compte sont bien ceux avec lesquels la session a été démarrée.  
Si xDrip utilise déjà cet appareil, rien n'est envoyé. Pour l'appairer à nouveau, appuyez sur Oublier ce périphérique dans l'écran Li3, puis scannez-le.

#### 4. Attendre la première valeur {#4-wait-for-the-first-reading}

Un appareil neuf n'envoie aucune valeur pendant sa première heure environ.

<br>

## Paramètres Li3 {#li3-settings}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;&ensp;Paramètres moins courants  
&emsp;&emsp;&emsp;Autres options diverses  
&emsp;&emsp;&emsp;&emsp;Li3
:::

::: xdripitem Account ID
&ensp;Needed to take over a session in progress. Leave empty to start a new session for xDrip on this phone only.
:::

Look up account ID, dans l'écran Li3, le remplit pour vous.

::: xdripitem Official app
&ensp;The app the account uses
:::

Li3 app (par défaut) ou Multi-sensor app. C'est le même choix que le bouton Sensor app de l'écran Li3.

::: xdripitem Smooth Li3 readings <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Average recent readings to make them smoother
:::

Les paramètres NFC qui ne s'appliquent pas au Li3 (âge du capteur, jours avant expiration, multibloc, toute balise, streaming Bluetooth Libre 2) sont masqués tant que Li3 est la source de données.

<br>

## État {#status}

L'écran Li3 et État du système → Li3 Status affichent :

- **Device** (appareil)
- **Stage** (étape) : ce que fait xDrip en ce moment, par exemple :
    - *No device; scan one with NFC*
    - *No app credential; tap Download on the Li3 screen*
    - *Looking for the device; keep the phone near it*
    - *Lost the device; trying again soon*
    - *Connected; waiting for a reading*
    - *Session ended; scan a new device with NFC*
- **Last error** (dernière erreur)
- **Reading not stored** (valeur non enregistrée), lorsque xDrip a refusé une valeur : pas de valeur valide, heure de début de session apparemment erronée, ou valeur marquée comme non fiable par l'appareil
- **Started** (démarré) et **Sensor life** (durée de vie du capteur) (ou *Expired*)
- **Last reading** (dernière valeur)
- **App credential** (identifiant d'application)

#### Oublier ce périphérique {#forget-device}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;OUBLIER CE PÉRIPHÉRIQUE&emsp;</div>
:::

xDrip cesse de communiquer avec cet appareil. Pour l'utiliser à nouveau, scannez-le en NFC.  
Une session démarrée sans compte ne peut revenir qu'à xDrip sur ce téléphone.

#### Copier les diagnostics {#copy-diagnostics}

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;COPY DIAGNOSTICS&emsp;</div>
:::

Copie les informations de diagnostic dans le presse-papiers. Collez-les lorsque vous demandez de l'aide.

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
