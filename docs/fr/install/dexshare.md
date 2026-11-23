---
source_hash: 5e151bd537
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Dex Share Follower
:::

### Prérequis {#prerequisites}

Pour que xDrip reçoive les données des serveurs Share, il vous faut :

1. un nom d'utilisateur qui **n'est pas un numéro de téléphone** : créez un [compte dépendant](https://www.dexcom.com/faqs/how-do-i-create-a-dependent-account) pour en obtenir un. Une fois le nouveau compte dépendant créé, vérifiez que vous êtes connecté avec ce compte dans vos applications Dexcom et recréez tous les abonnés
2. le partage activé dans l'application Dex connectée au capteur
3. l'invitation acceptée dans l'application Dex Follow (vous pourrez la désinstaller ensuite)

<img src="./images/M-S-HDS-DexSh1.png" style="zoom:75%;" />

Saisissez les identifiants que vous utilisez pour vous connecter à Clarity.

::: xdripitem Share Username
&ensp;Login username for Dex Share Following
:::

::: xdripitem Share Password
&ensp;Login password for Dex Share following
:::

N'activez les serveurs US que si votre compte est aux États-Unis.

::: xdripitem US Servers
&ensp;Your account and follower app are from the USA
:::

::: warning Verrouillage du compte
Laisser xDrip tourner avec un mot de passe erroné verrouillera votre compte.  
Pour débloquer un compte verrouillé, supprimez vos identifiants, [désactivez la collecte xDrip](./datasource#changing-data-source) et attendez 15 à 20 minutes.  
xDrip, comme toute autre application tierce qui tente de se connecter avec un mauvais mot de passe, maintiendra le verrouillage.
:::

Si aucune donnée n'apparaît et qu'aucun message d'erreur ne s'affiche, vous devrez peut-être [Démarrer le capteur](../use/startsensor#followers-and-companion-apps).

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
