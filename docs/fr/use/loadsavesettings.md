---
source_hash: 12c86ae746
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" /> 
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_content_save_grey600_48dp.png" style="width:5%;" />&ensp;Charger / Enregistrer les paramètres
:::

Vous pouvez aussi y accéder depuis le menu à trois points : `Fonctionnalités Import / Export` puis `Charger/Sauver les paramètres`

<img src="../images/3dots_menu.png" style="zoom:75%;" /> 

::: xdripitem Fonctionnalités Import / Export >
:::

::: xdripitem Charger/Sauver les paramètres
:::

Vous trouverez toutes les options dans cet écran.

::: xdripitem Charger/Sauver les paramètres
Ici, vous pouvez enregistrer les paramètres vers la mémoire interne (Download/xDrip-export/com.eveningoutpost.dexdrip_preferences.xml).  
Une fois enregistrés dans le fichier, il est possible pour toute application de lire les paramètres qui pourraient contenir des informations sensibles.  
Il est conseillé de supprimer les paramètres une fois que vous les avez importés à nouveau si vous êtes préoccupé par cela.  
:::
    

### Enregistrer les paramètres {#save-settings}

<div style="background-color: gray; color: white; text-align: center;">  &emsp;Enregistrer tous les paramètres dans le fichier&emsp;</div> 

Vos paramètres seront enregistrés dans `/storage/emulated/0/Download/xDrip-Export` pour les anciennes versions (export vers la carte SD) ou dans le dossier `Download/xDrip-export` pour les versions récentes.   
Vous devez autoriser xDrip à accéder à la mémoire de votre téléphone.  

::: warning Le fichier de sauvegarde existant sera écrasé
:::

<img src="./images/M-S-LSSe.png" style="zoom:75%;" />

Si vous voulez en conserver une copie en lieu sûr, envoyez-vous le fichier par e-mail, enregistrez-le sur un stockage cloud ou copiez-le sur un ordinateur via USB.

### Charger les paramètres {#load-settings}

<div style="background-color: gray; color: white; text-align: center;">  &emsp;Charger tous les paramètres depuis le fichier&emsp;</div> 

::: warning Les paramètres existants seront écrasés
:::

Vous devrez peut-être redémarrer votre téléphone pour terminer l'opération.

### Supprimer les paramètres {#delete-settings}

<div style="background-color: gray; color: white; text-align: center;">  &emsp;Supprimer le dossier de paramètres (Download/xDrip-export)&emsp;</div> 

Les paramètres exportés contiennent des informations privées : une fois transférés vers un autre téléphone ou un emplacement sûr, vous voudrez peut-être supprimer la sauvegarde.

<br>

[*Dernière modification le 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
