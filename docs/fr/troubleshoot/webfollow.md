---
source_hash: 8c757f2bd2
source_commit: 7a18e7c
---
# Libre Web Follower {#libre-web-follower}

## Configuration du système {#system-setup}

Avec cette source de données, vous devez vous assurer que votre système est correctement configuré avec les applications du fabricant.

**L'application principale (connectée au capteur Libre) doit envoyer les données vers le [serveur](https://www.libreview.com/) du fabricant.**  

Déconnectez-vous puis reconnectez-vous au serveur pour vérifier que vous utilisez les bons identifiants.

Vérifiez que le serveur contient bien des données.

**L'application [abonné](https://play.google.com/store/search?q=librelinkup&c=apps) du fabricant doit recevoir les données partagées.**  

Essayez de supprimer puis de renvoyer une invitation vers l'application abonné du fabricant (depuis l'application principale du fabricant).

Essayez de désinstaller puis de réinstaller l'application abonné du fabricant.

- Utilisez de préférence les identifiants de l'invitation pour vous connecter.
- Si cela ne fonctionne pas, utilisez les identifiants de l'application principale (serveur) et renvoyez l'invitation.

<br>

## Configuration de xDrip {#xdrip-setup}

Une fois que le système fonctionne avec les applications du fabricant, vous pouvez dépanner xDrip.

1. Vérifiez que la source de données est [Web follower](../install/webfollower).
2. Utilisez les identifiants de l'abonné que vous avez invité depuis l'application principale du fabricant.
3. Si cela ne fonctionne pas, vous pouvez essayer les identifiants du serveur pour le dépannage, mais soyez prudent afin de limiter le risque de blocage du compte.

<br>

## Mises à jour des serveurs du fabricant {#vendor-servers-updates}

Les mises à jour du serveur peuvent casser le mécanisme.

**Une fois xDrip corrigé**, il peut être nécessaire de le réinitialiser en suivant cette séquence :

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Web Follower
:::

Modifiez le `Configuration script`

::: xdripitem Configuration Script
&ensp;This is the community helper address or keyword
:::

Ajoutez une espace après `beonlabs`, sélectionnez `Ok`

<img src="./images/M-S-HDS-WF-Scr.png" style="zoom:75%;" />

Modifiez à nouveau le `Configuration script`, **supprimez l'espace** après `beonlabs` et sélectionnez `Ok`.

Attendez jusqu'à une minute que les données s'affichent de nouveau.

<br>

Si le problème persiste, installez l'application abonné du fabricant sur le même téléphone et vérifiez qu'elle reçoit les données avec les mêmes identifiants.

<br>

[*Dernière modification le 8/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
