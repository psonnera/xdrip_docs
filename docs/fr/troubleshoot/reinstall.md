---
source_hash: 59290c3e55
source_commit: 7a18e7c
---
## Désinstaller xDrip {#uninstall-xdrip}

::: warning Données historiques
Désinstaller xDrip supprime aussi toutes les données et tous les paramètres, sans récupération possible.  
Veillez à **[sauvegarder](#backup)** la base de données et/ou tous les paramètres au préalable.  
Il est recommandé d'envoyer les données vers [Nightscout](https://nightscout.github.io/).
:::

<br>

Cela ne devrait normalement pas être nécessaire, mais vous pouvez avoir besoin de désinstaller xDrip pour un dépannage, ou pour passer à une version dérivée (fork) ou en revenir. Vous pouvez désinstaller xDrip comme n'importe quelle autre application Android, par un appui long sur l'icône ou depuis Paramètres Android -> Applications.

## Réinstaller xDrip {#reinstall-xdrip}

Suivez cette séquence :

1. Sauvegardez (localement ou dans le cloud)
2. Désinstallez xDrip
3. Installez xDrip
4. Restaurez (depuis la sauvegarde locale ou dans le cloud)
5. Vérifiez tous vos paramètres et recréez vos alarmes

## Sauvegarde {#backup}

Vous pouvez sauvegarder la base de données localement ou dans votre [Google Drive](#cloud-backup).

### Sauvegarder la base de données {#backup-the-database}

La base de données contient toutes les valeurs de glycémie, les traitements et les notes. Il est fortement recommandé de sauvegarder votre base de données et d'en garder une copie sur un autre appareil si vous voulez conserver vos données existantes, et par précaution en cas de perte du téléphone, de panne...  
L'envoi vers [Nightscout](https://nightscout.github.io/) est aussi fortement recommandé.

L'exportation de la base de données [enregistre aussi les paramètres](../use/loadsavesettings#save-settings).

Depuis l'écran principal de xDrip, sélectionnez le menu à 3 points en haut à droite, Fonctionnalités Import / Export, Exporter la base de données.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Fonctionnalités Import / Export ►  
&emsp;Exporter la base de données
:::

<br>

La base de données actuelle sera enregistrée dans `/storage/emulated/0/xdrip` ou `Internal Storage/xdrip`
Vous devez autoriser xDrip à accéder à la mémoire de votre téléphone.  
Vous pouvez faire autant de sauvegardes que votre mémoire peut en contenir.

Si vous êtes assez rapide pour appuyer sur `PARTAGER` avant qu'il disparaisse, vous pouvez utiliser les options de partage de votre téléphone pour envoyer la base de données vers un autre appareil ou la copier à un autre emplacement.

<img src="./images/3DM-IE-ExpDB.png" style="zoom:75%;" />

Votre sauvegarde sera nommée `exportYYYYMMDD-HHMMSS.zip`, avec `YYYY` l'année en cours, `MM` le mois, `DD` le jour et `HHMMSS` les heures, minutes et secondes. Vous pouvez ainsi avoir plusieurs sauvegardes identifiées par un horodatage unique.

Si vous voulez en garder une copie en lieu sûr, envoyez-vous le fichier par e-mail, enregistrez-le sur un stockage en ligne ou copiez-le par USB sur un ordinateur.

C'est une base de données SQLite que vous pouvez parcourir avec divers utilitaires comme [SQLite Browser](https://sqlitebrowser.org/).

<br>

## Restauration {#restore}

Vous pouvez restaurer la base de données depuis une copie locale ou depuis votre [Google Drive](#cloud-backup).

### Restaurer les paramètres {#restore-settings}

Une fois l'installation de xDrip terminée, si une sauvegarde est disponible, xDrip proposera de la restaurer automatiquement.   
Sélectionnez RÉTABLIR LES PARAMÈTRES

::: xdripitem Sauvegarde détectée
&emsp;Il semble que vous ayez peut-être une sauvegarde des paramètres, devons-nous essayer de la restaurer?  


&emsp;NON&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;RÉTABLIR LES PARAMÈTRES&ensp;</span>
:::

Si vous ne voyez pas ce message, [restaurez-les manuellement](../use/loadsavesettings#load-settings).

### Restaurer une base de données {#restore-a-database}

::: warning Perte de données
Restaurer une base de données **supprime toutes les données actuelles**.  
Restaurez une base de données avec **la même version de xDrip que celle utilisée pour l'exporter**.  
Veillez à sauvegarder la base de données actuelle avant d'en restaurer une. 
:::

Une fois l'installation de xDrip terminée, si une sauvegarde de base de données est disponible, xDrip peut proposer de la restaurer automatiquement.

Vérifiez qu'il s'agit bien de la base de données que vous voulez restaurer, puis sélectionnez RESTAURER.

::: xdripitem Restaurer la sauvegarde ?
&emsp;Voulez-vous restaurer le fichier de sauvegarde : export20210328-085436.zip  


&emsp;NON&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;RESTAURER&ensp;</span>
:::

xDrip confirmera que la base de données a bien été restaurée.

::: xdripitem Import Result
&emsp;Successfully imported database
:::

*Remarque : par sécurité, la base de données actuelle est d'abord exportée ; vous la trouverez dans la liste sous le nom `b4import` suivi de la date et de l'heure de l'importation. Vous pourrez ainsi la récupérer si nécessaire.*

<br>

Si vous voulez restaurer une sauvegarde précise, depuis l'écran principal de xDrip, sélectionnez le menu à 3 points en haut à droite, Fonctionnalités Import / Export, Importer la base de données.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Fonctionnalités Import / Export ►  
&emsp;Importer la base de données
:::

Des instructions s'affichent. Vous n'avez pas besoin de déplacer le fichier de sauvegarde si vous ne l'avez pas apporté d'un autre appareil, ni de le décompresser. Soyez prudent si vous restaurez une base de données avec une autre version de xDrip : il est recommandé d'installer la [version de xDrip](../install/install#verify-which-version-is-installed) qui a servi à l'exportation avant d'importer, puis de mettre à jour xDrip ensuite.

::: xdripitem Restore Instructions
&emsp;WARNING: Database restore is rarely necessary and may cause SEVERE DATA LOSS.

Protect your data by uploading to Nightscout or Tidepool.

When switching phones, importing settings (alerts, colors, etc.) is usually sufficient. Restoring the database is typically unnecessary unless you need short-term access to historical data (for example, before a medical visit).

Instructions:

\- Place the database in the 'xdrip' folder. If it doesn't exist, perform an export once to create it.

\- Restart this restore routine.

\- Select the correct database and follow the on-screen instructions.
:::

Sélectionnez la base de données à importer ; regardez la date et la taille (avec le gestionnaire de fichiers du téléphone) pour être sûr de choisir la bonne.

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Restaurer la base de données
export20220129-184625.zip  
export20220129-184615.zip  
b4import20220129-194141.zip
:::

Une fois certain de restaurer la bonne sauvegarde, `D'accord`

::: xdripitem Confirm Import
&emsp;Do you really want to import  
&emsp;'export20220129-184615.zip'?  
&emsp;This may negatively affect the data integrity of your system!  

&emsp;ANNULER&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;D'ACCORD&ensp;</span>
:::

xDrip confirmera que la base de données a bien été restaurée.

::: xdripitem Import Result
&emsp;Successfully imported database
:::

Si vous avez restauré la mauvaise base de données, refaites simplement les mêmes étapes et sélectionnez la dernière version `b4import` pour revenir en arrière.

::: info Android 11 et versions ultérieures
Un problème avec les versions récentes d'Android vous oblige à restaurer la base de données plusieurs fois (3 à 4) avant de voir l'intégralité de son contenu.
:::

<br>

## Sauvegarde dans le cloud {#cloud-backup}

La sauvegarde dans le cloud vous permet d'enregistrer dans votre Google Drive un fichier compressé contenant à la fois la base de données et les paramètres.  
Vous devez être connecté à votre compte Google pour utiliser cette fonction.

Sélectionnez Sauvegarde dans le Cloud.

::: xdrip <img src="../images/3dots_menu.png" style="zoom:75%;" />
&ensp;Fonctionnalités Import / Export ►  
&emsp;Sauvegarde dans le Cloud
:::

::: xdripitem Sauvegarde dans le Cloud
&emsp;&emsp;Vous pouvez utiliser Google Drive pour la sauvegarde  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Prêt
:::

Pour utiliser cette fonction, vous devez d'abord sélectionner un emplacement de sauvegarde.

### Sélectionner l'emplacement de la sauvegarde {#select-backup-location}

::: xdrip <span style="background-color: white; color: black;">&ensp;Sélectionner l'emplacement de la sauvegarde&ensp;</span>
:::

::: xdripitem Choisir le fichier de sauvegarde
&emsp;&emsp;Sélectionner Automatique pour que xDrip gère les fichiers dans Google Drive ou sélectionner un autre fichier spécifique à utiliser si vous devez restaurer à partir d'ailleurs.  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;SAUVEGARDE GÉRÉE AUTOMATIQUEMENT&ensp;</span>  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;UTILISER UN FICHIER ALTERNATIF&ensp;</span>
:::

- Utiliser un fichier alternatif vous permet de choisir un autre dossier et un autre fichier de sauvegarde lors d'une **restauration**. 
- Pour votre **première sauvegarde**, ou pour récupérer après **une réinstallation de xDrip** sur le même téléphone, sélectionnez Sauvegarde gérée automatiquement.

Vous devez autoriser xDrip à accéder à votre compte Google. xDrip se contentera d'enregistrer et de récupérer le fichier de sauvegarde dans votre Google Drive. **Rien d'autre.**

<img src="./images/3DM-BR-CB3.png" style="zoom:75%;" />

Une fois cela fait, xDrip confirmera l'accès :

<img src="./images/3DM-BR-CB4.png" style="zoom:75%;" />

xDrip créera un nouveau dossier nommé xDrip-Backups à la racine de votre Google Drive.

<img src="./images/3DM-BR-CB6.png" style="zoom:75%;" />

### Sauvegarder maintenant {#do-backup-now}

Une fois l'emplacement de sauvegarde sélectionné, vous pouvez lancer une sauvegarde. Le fichier de sauvegarde est créé sur votre appareil puis envoyé vers votre Google Drive.

::: xdrip <span style="background-color: white; color: black;">&ensp;Sauvegarder Maintenant&ensp;</span>
:::

<img src="./images/3DM-BR-CB5.png" style="zoom:75%;" />

Vous pouvez vérifier l'état de la sauvegarde dans le cloud en haut de l'écran.

<img src="./images/3DM-BR-CB7.png" style="zoom:75%;" />

Vous pouvez faire exécuter automatiquement la sauvegarde dans le cloud chaque jour.  
Ne l'activez pas si votre forfait de données mobiles est limité.

::: xdripitem <img src="../images/DIS.png" style="zoom:75%;" />&emsp;Sauvegarde journalière automatique
:::

### Restaurer depuis la sauvegarde {#restore-from-backup}

::: xdrip <span style="background-color: white; color: black;">&ensp;Restaurer depuis la sauvegarde&ensp;</span>
:::

::: warning Perte de données
Restaurer une base de données supprime toutes les données actuelles.  
Restaurez une base de données avec **la même version de xDrip que celle utilisée pour l'exporter**.  
Veillez à sauvegarder la base de données actuelle avant d'en restaurer une.
:::

::: xdripitem Êtes-vous vraiment sûr ?
&emsp;Restaurer une sauvegarde effacera vos paramètres et données actuelles de la sauvegarde.  

&emsp;Êtes-vous absolument sûr de vouloir le faire ?  

&emsp;NON&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;OUI&ensp;</span>
:::

La restauration copie localement la base de données du cloud et remplace la base de données actuelle.

Une fois l'opération terminée, xDrip redémarre.

<br>

## Migration vers un nouveau téléphone {#new-phone-migration}

Effectuez les opérations suivantes :

Sur l'ancien téléphone :

1. [Sauvegardez la base de données localement](#backup-the-database) ou dans votre [Google Drive](#do-backup-now).
   - Si vous n'utilisez pas la sauvegarde Google dans le cloud, envoyez-vous la sauvegarde de la base de données ou copiez-la sur un ordinateur.

2. Si cet ancien téléphone est connecté à un capteur ou à un transmetteur, veillez à [désactiver la collecte](../install/datasource#changing-data-source) pour qu'il n'interfère pas lorsque vous commencerez à utiliser votre nouveau téléphone.
3. Si cet ancien téléphone était principal pour des abonnés xDrip Sync, [retirez-lui le rôle de principal](../use/sync#be-master-for-followers).

Sur le nouveau téléphone :

1. [Installez](../install/download#which-one-to-install) la [même version](../install/install#verify-which-version-is-installed) de xDrip que celle de l'ancien téléphone.
   - Si vous n'avez pas utilisé la sauvegarde Google dans le cloud :  
     [Sauvegardez la base de données](#backup-the-database) (uniquement pour créer les bons dossiers).  
     Copiez dans le bon dossier le fichier de base de données que vous vous êtes envoyé par e-mail, ou depuis un ordinateur.

2. [Restaurez la base de données depuis la sauvegarde locale](#restore-a-database) ou depuis votre [Google Drive](#restore-from-backup).  
3. Si le nouveau téléphone doit être connecté à un capteur ou à un transmetteur, [connectez-le maintenant](../install/datasource#sensor-selection). (Votre source de données sera correcte, mais vous devrez rétablir la connexion.)

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
