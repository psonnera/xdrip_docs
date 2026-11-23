---
source_hash: 05ada65eb5
source_commit: 7a18e7c
---
::: warning Sujet à des interruptions
Le fabricant n'ayant pas publié d'API, les mises à jour de son serveur et de son protocole casseront cette source de données.  
**En cas de problème, utilisez la [dernière pré-version](./download#pre-release).**
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Web Follower
:::

<br>

### Prérequis {#prerequisites}

1. Installez l'application LibreLink ou Libre 3, connectez-vous ou créez un compte (obligatoire) et vérifiez qu'elle affiche les valeurs du capteur en temps réel
2. Invitez un abonné  
   <img src="./images/M-S-HDS-WF3.png" style="zoom:76%;" />
3. Dans l'e-mail d'invitation, appuyez sur le lien Play Store pour installer l'[application d'abonné](https://play.google.com/store/apps/details?id=org.nativescript.LibreLinkUp)  
   Créez un autre compte pour l'application d'abonné.

::: warning Risque de verrouillage du compte
N'utilisez **pas** les identifiants de votre compte principal !
:::

Vérifiez que vous recevez bien des valeurs.   
Vous pouvez ensuite désinstaller l'application d'abonné. Vous devrez peut-être la réinstaller pour authentifier votre abonné si les données cessent de s'afficher dans xDrip.

### Configurer l'abonné web de xDrip {#configure-xdrip-web-follower}

::: xdripitem Web Follower Settings
&ensp;Configuration options for web follower data source
:::

Ne modifiez pas le nom du script de configuration. Il s'agit de `beonlabs`

::: xdripitem Configuration Script
&ensp;This is the community helper address or keyword
:::

Saisissez les identifiants utilisés dans l'application d'abonné.

::: xdripitem Service logon user name
&ensp;This is your registered user name or email address with the service
:::

::: xdripitem Service logon password
&ensp;This is your registered password with the service
:::

N'activez pas de serveur proxy à moins de savoir pourquoi vous le faites.

::: xdripitem Use proxy server (advanced) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<br>

Si aucune donnée n'apparaît et qu'aucun message d'erreur ne s'affiche, vous devrez peut-être [Démarrer le capteur](../use/startsensor#followers-and-companion-apps).

Consultez si nécessaire la page de [dépannage](../troubleshoot/webfollow).

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
