---
source_hash: 247aedba5a
source_commit: 7a18e7c
---
::: warning Anciens certificats Android
Vous ne pourrez peut-être pas utiliser cette fonction sur les téléphones sous une version d'Android antérieure à 9 s'ils dépendent de certificats expirés ([exemple](https://community.letsencrypt.org/t/support-for-android-7-and-older-from-oct-2024/216446)).  
Il n'existe pas de solution de contournement.
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Nightscout Follower
:::

### Nightscout {#nightscout}

Pour utiliser xDrip avec les données provenant de votre site [Nightscout](https://nightscout.github.io/), il vous suffit de saisir l'URL de votre site.

::: xdripitem URL Abonnés Nightscout
&ensp;Adresse Web pour les abonnés 
:::

Avec un Nightscout DIY classique, l'URL ressemble à ceci : `https://sitename.yourprovider.com`  
N'ajoutez pas `/api/v1`  
Veillez à utiliser `https` et non `http`

Si vous utilisez un service hébergé, contactez le fournisseur pour plus d'informations.

Si votre site Nightscout est [sécurisé](https://nightscout.github.io/nightscout/security/), vous devez ajouter l'API_SECRET ou le jeton d'accès.

`https://API_SECRET@sitename.yourprovider.com`

`https://access_token@sitename.yourprovider.com`

::: xdripitem Télécharger les traitements
:::

Vous pouvez aussi télécharger depuis Nightscout les traitements compatibles (glycémies, calibrations, traitements, notes).

::: xdripitem Télécharger les traitements <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Télécharger également les traitements de Nightscout comme Abonné
:::

Pour éviter le risque de données en double (important pour AAPS), vous pouvez empêcher xDrip de télécharger les données qu'il a lui-même envoyées vers Nightscout.

::: xdripitem Ignorer les éléments de xDrip <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Éviter de télécharger les éléments chargés par xDrip
:::

Si vous constatez des retards importants dans xDrip, vous pouvez définir un délai fixe pour le resynchroniser avec Nightscout. Laissez la valeur par défaut.

::: xdripitem Délai pour l'Abonné Nightscout
&ensp;0>
:::

::: info Remarque
xDrip ne récupère depuis Nightscout qu'un historique limité (24 heures).
:::

Si votre site Nightscout publie l'état des appareils (batterie de l'uploader, batterie de la pompe), xDrip l'affichera dans État du système.

::: info Remarque
Les émulateurs Nightscout locaux tels que [Juggluco](https://github.com/j-kaltes/Juggluco) sont également pris en charge comme source pour l'abonné.
:::

<br>

### Diabox {#diabox}

Vous pouvez recevoir les données de [Diabox](https://sirius.thetaphi.de/diabox/) en activant la diffusion http dans l'application et en faisant de xDrip un abonné local.

::: warning Attention
Vous ne pouvez pas utiliser cette fonction si xDrip exécute un [service web](../use/interapp#web-service).
:::

<img src="./images/Diabox1.png" style="zoom:75%;" />

<img src="./images/Diabox2.png" style="zoom:75%;" />

Une fois cela fait, réglez xDrip en abonné Nightscout (voir ci-dessus) avec l'adresse :

`http://localhost:17580`

<img src="./images/Diabox3.png" style="zoom:75%;" />

<br>

[*Dernière modification le 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
