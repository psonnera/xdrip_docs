---
source_hash: 29d4533605
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;CareLink Follower
:::

<br>

::: warning Attention
Les serveurs CareLink font l'objet de modifications fréquentes qui peuvent casser cette fonction.  
**En cas de problème, utilisez la [dernière pré-version](./download#pre-release).**  
Envisagez plutôt d'utiliser [Companion App](./companion) sur le téléphone principal, et xDrip [Sync](./xdripfollower) ou Nightscout pour partager les données.  
L'authentification de l'application CarePartner est valable 1 semaine : même si xDrip ne peut pas se connecter à CareLink pendant quelques jours (par exemple faute de connexion Internet), il pourra renouveler la connexion (actualiser le jeton) automatiquement en arrière-plan dès qu'il pourra de nouveau joindre CareLink, sans que vous ayez à vous reconnecter manuellement dans le navigateur. La restriction sur le compte utilisateur s'applique aussi à ce processus d'authentification :   
**xDrip doit utiliser un compte abonné dédié, vous ne pouvez pas utiliser le même abonné pour d'autres applications ou d'autres téléphones.**
:::

<br>

Cela fonctionne aussi pour un CGM Simplera autonome (utilisé sans pompe associée) qui envoie ses données vers CareLink.

Sélectionnez le pays dans lequel vous avez enregistré votre utilisateur CareLink.

::: xdripitem Pays CareLink
&ensp;Sélectionner votre pays CareLink.
:::

Indiquez le nom d'utilisateur du patient si vous utilisez un compte de care partner avec plusieurs patients.

::: xdripitem Nom d'utilisateur du patient CareLink
&ensp;Nom d'utilisateur du patient CareLink (facultatif)
:::

xDrip ouvre le site d'authentification CareLink : saisissez vos identifiants pour vous connecter.  

::: xdripitem Connexion
&ensp;Se connecter avec le navigateur
:::

Le délai de grâce est un temps d'attente supplémentaire après la réception de la dernière valeur + 5 minutes.  
Il sert à éviter un blocage par le serveur si xDrip envoie des requêtes trop fréquentes.

::: xdripitem Délai de grâce
&ensp;Délai de grâce pour la demande de données en secondes
:::

L'intervalle de collecte des données manquées est un temps d'attente supplémentaire après la réception de la dernière valeur + 5 minutes + délai de grâce.  
Il sert à éviter un blocage par le serveur si xDrip envoie des requêtes trop fréquentes.

::: xdripitem Intervalle de collecte de données manquées
&ensp;Intervalle de collecte après les données manquées en minutes
:::

<br>

#### Traitements {#treatments}

Vous pouvez télécharger les traitements et recevoir les notifications.

::: xdripitem Glycémies capillaires <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger les glycémies capillaires depuis CareLink  
:::

::: xdripitem Bolus <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger les bolus depuis CareLink
:::

::: xdripitem Repas <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger les repas depuis CareLink
:::

::: xdripitem Notifications <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger les notifications de CareLink
:::

<br>

#### Ligne d'état {#status-line}

L'état du capteur et l'état de la pompe peuvent être activés dans l'option [Ligne d'état supplémentaire](../use/lesscommon#extra-status-line).

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;&ensp;Paramètres moins courants  
&emsp;&emsp;Ligne d'état supplémentaire
:::

::: xdripitem Statut externe <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;État de l'affichage d'autres applications comme AndroidAPS
:::

::: xdripitem État de la pompe <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Afficher les informations d’état de pompe si disponible
:::

Les informations de la pompe (état, basal) sont <u>uniquement visibles</u> dans la ligne d'état et **ne peuvent pas être envoyées vers Nightscout/Tidepool**.

<img src="./images/M-S-HDS-CF6.png" style="zoom:75%;" />

<br>

Si aucune donnée n'apparaît et qu'aucun message d'erreur ne s'affiche, vous devrez peut-être [Démarrer le capteur](../use/startsensor#followers-and-companion-apps).

[*Dernière modification le 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
