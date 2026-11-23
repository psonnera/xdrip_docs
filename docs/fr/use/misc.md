---
source_hash: 87f439d0b6
source_commit: 7a18e7c
---
D'autres options sont disponibles dans ce menu.  
Si elles sont cachées ici, c'est sans doute parce que vous n'aurez pas besoin de les modifier tous les jours, ou que vous devriez les laisser telles quelles sauf indication contraire.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;&ensp;Paramètres moins courants  
&emsp;&emsp;&emsp;Autres options diverses
:::

##### Exécutez Collector au premier plan {#run-collector-in-foreground}

::: info Remarque
Depuis l'abandon de la prise en charge d'Android 7 ([12 juil. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)), ce n'est plus une option que vous pouvez désactiver.
:::

Sous Android 8.0 et plus (version minimale prise en charge), xDrip exécute toujours son collecteur en tant que service au premier plan pour éviter qu'Android ne le mette en veille. Un graphique de notification persistante est donc toujours affiché, visible sur l'écran de verrouillage.

Si vous préférez ne pas afficher le graphique, l'option `Notification persistante compacte` du même menu n'affiche que la glycémie actuelle.

::: xdripitem Notification persistante compacte <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Activer pour masquer le graphique dans la notification et afficher uniquement la valeur de glucose actuelle.
:::

<img src="./images/M-S-LCS15a2.png" style="zoom:75%;" />

##### Mode développeur {#engineering-mode}

Active des fonctions potentiellement dangereuses ou non testées. Il n'est pas nécessaire de l'activer pour redémarrer un émetteur G5 ou un ancien émetteur G6 (les nouveaux, appelés Firefly, ne peuvent pas être redémarrés). En pratique, vous n'avez pas besoin de l'activer.

::: xdripitem Mode développeur <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Permet de changer les paramètres les plus dangereux qui pourraient tout casser !
:::

Pour activer l'Engineering mode, saisissez ou prononcez le traitement `enable engineering mode`.

Un rappel mensuel vous signalera que l'Engineering mode est activé. Assurez-vous d'en avoir vraiment besoin, sinon laissez-le désactivé.

<img src="./images/M-S-LCS15b3.png" style="zoom:52%;" />

##### Invité pour l’optimisation de la batterie {#battery-optimization-prompt}

Doit rester **désactivé**. xDrip doit être [exclu de l'optimisation de la batterie](../install/install#authorize-background-activity) et ne doit pas y être soumis. 

::: xdripitem Invité pour l’optimisation de la batterie <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Sur Android 6+ s'assurer que l'optimisation de la batterie est désactivée (recommandé).
:::

##### Samsung Workarounds {#samsung-workarounds}

Renommé en Solutions de contournement Wake, car d'autres appareils ne sont pas conformes.

##### Solutions de contournement Wake {#wake-workarounds}

Corrige une non-conformité de certains appareils Android ; activé désormais par défaut pour Samsung, Xiaomi, OnePlus, Oppo et Huawei.   
Doit rester **activé**.

::: xdripitem Solutions de contournement Wake <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utiliser des contournements pour éviter le comportement Android non standard de certains terminaux. Sans cela, les collecteurs ne peuvent pas obtenir les données.
:::

Utilisation Wakelocks excessive n'est pas nécessaire. Il s'agit de messages de "réveil" supplémentaires envoyés par xDrip à votre appareil Android pour l'empêcher de passer en mode veille. 

::: xdripitem Utilisation Wakelocks excessive <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Wakelocks anciennes qui peuvent drainer la batterie, mais pourraient être nécessaires pour NightWatch ou Android Wear
:::

Afficher les valeurs prédictives (ancienne méthode) est obsolète. Utilisez la [simulation prédictive](./predictions).

::: xdripitem Afficher les valeurs prédictives <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Vieille méthode - non recommandée !
:::

Proper Ongoing est indispensable pour les appareils sous Android 8 et plus. Visible uniquement lorsque l'Engineering mode (Mode développeur) est activé.

::: xdripitem Proper Ongoing <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Use proper ongoing notification. Disabling this causes collector problems on Android 8+ (utiliser une notification permanente correcte ; la désactiver cause des problèmes de collecteur sous Android 8+)
:::

##### Algorithme hors processus {#out-of-process-algorithm}

L'[algorithme hors processus](./OOP) (Out Of Process Algorithm) permet d'intégrer un plugin externe qui fournit des glycémies semblables à celles du fabricant pour les capteurs Libre, ou qui décode les informations du capteur Libre 2 EU.  
Si l'application externe n'est pas présente sur votre téléphone ou ne fournit pas les informations, xDrip n'affichera pas de glycémie.

::: warning Attention
Cette option ne doit être activée que si vous utilisez un algorithme hors processus de version 1 (OOP1).  
Elle doit être désactivée pour OOP2.
:::

::: xdripitem Algorithme Libre hors processus. <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utiliser un algorithme Libre hors processus.(BluCon/NFC/LibreAlarm)
:::

##### OOP2 {#oop2}

OOP2 est indispensable pour traiter les données des Libre 14 jours US et Libre 2/2+ EU.

::: xdripitem Calibration par algorithme OOP2.
&ensp;Apply xDrip calibration method on OOP2 data (appliquer la méthode d'étalonnage de xDrip aux données OOP2)
:::

Vous pouvez utiliser OOP2 de différentes façons :

- No calibration génère des valeurs semblables à celles du fabricant (mode natif) sans avoir besoin d'étalonner. Cela ne signifie pas que les résultats sont non étalonnés (bruts) : un algorithme semblable à celui du fabricant est appliqué (comme le lecteur Libre 1).
- Calibrate based on raw utilise les données brutes du capteur (sans correction de température), comme le Libre 1. Vous utiliserez l'algorithme d'étalonnage de xDrip. **Réglage par défaut.**
- Calibrate based on glucose vous permet d'appliquer l'étalonnage xDrip aux valeurs natives. Les données brutes sont transformées par l'algorithme semblable à celui du fabricant, puis transmises à l'algorithme d'étalonnage de xDrip.

::: xdripitem Calibration par algorithme OOP2.
&emsp;No calibration&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;○  
&emsp;Calibrate based on raw&emsp;&emsp;&emsp;●  
&emsp;Calibrate based on glucose&nbsp;&emsp;○
:::

Lissage des données Libre fait la moyenne sur 5 mesures. Cela retarde aussi les valeurs.  
Si cette option n'apporte pas l'amélioration attendue, essayez aussi [Smooth Sensor Noise](./display#smooth-sensor-noise).

::: xdripitem Lissage des données Libre. <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utiliser une moyenne de 5 points pour obtenir des données Libre plus lisses.
:::

Récupérer l'historique du Freestyle Libre est nécessaire pour les transmetteurs BluCon. Les autres transmetteurs récupèrent automatiquement les données manquantes.

::: xdripitem Récupérer l'historique du Freestyle Libre <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
Extraire l'historique manqué du périphérique BluCon lors de la reconnexion au capteur.
:::

L'affichage Libre one minute est encore en développement. xDrip affiche les glycémies toutes les 5 minutes. Avec la source de données [Li3](../install/li3), les valeurs sont enregistrées chaque minute lorsque cette option est activée.

::: xdripitem Libre one minute <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

##### Li3 {#li3}

Les paramètres Li3 (Account ID, Official app, Smooth Li3 readings) sont expliqués sur la page [Li3](../install/li3#li3-settings).

##### 1-min Inter-app broadcast {#1-min-inter-app-broadcast}

::: xdripitem 1-min Inter-app broadcast <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Accept data at one-minute intervals from Inter-app broadcast. Reboot your phone for changes to take effect. (accepter les données à intervalles d'une minute depuis Inter-app broadcast ; redémarrez votre téléphone pour que les modifications prennent effet)
:::

Accepte des valeurs toutes les minutes au lieu de toutes les 5 minutes depuis la source de données [Inter-app broadcast](../install/640_670). Redémarrez le téléphone après avoir modifié ce réglage. Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), il ne nécessite plus l'Engineering mode (il s'appelait auparavant "640G/Eversense 1-minute").

L'option ci-dessous est toujours grisée dans l'application : elle ne peut pas être activée.

::: xdripitem NE PAS UTILISER EN PRODUCTION <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
:::

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
