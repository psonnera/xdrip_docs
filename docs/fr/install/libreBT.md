---
source_hash: dc2943a1ef
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Source de données matérielle  
&ensp;&emsp;Libre Bluetooth
:::

De nombreux transmetteurs NFC vers Bluetooth pour capteurs Libre sont disponibles sur le marché.

Le projet d'origine a été développé par Joern : [LimiTTer](https://github.com/JoernL/LimiTTer). Retenez ce nom, car il apparaît comme nom de transmetteur par défaut lorsque l'appareil réel n'est pas identifié. À moins que vous ayez réellement un LimiTTer (ou que vous connectiez directement un Libre 2), voir ce nom signifie que votre transmetteur n'est pas connecté à xDrip.

xDrip prend en charge certains d'entre eux pour certains capteurs.  
**Les Libre H et Libre 2/2+ US/CA/AUS ne sont pas pris en charge.**  
Vous pouvez utiliser Diabox ou Juggluco en mode [Libre (patched app)](./libre2patch).

Voici ci-dessous un tableau de compatibilité des transmetteurs pris en charge ; pour les capteurs compatibles, la version **minimale** du firmware est indiquée.

| Transmetteur | - Libre 1 / Pro - | - 14 jours US - | - Libre 2/2+ EU - |
| :---------: | :---------------: | :------------: | :---------------: |
|  MiaoMiao   |       `Oui`       |     `39*`      |       `39*`       |
| MiaoMiao 2  |       `Oui`       |      `7*`      |       `7*`        |
| MiaoMiao 3  |       `Oui`       |     `3A*`      |       `3A*`       |
|    Atom     |       `Oui`       |                |                   |

*Remarque :*  
*`*` [module externe OOP nécessaire](../use/OOP)*  
*Bubble et Bubble mini ne sont plus pris en charge depuis la version 2026.11.20.*

<br>

## Paramètres du transmetteur {#bridge-settings}

Si ce n'est pas encore fait, [vérifiez que xDrip ne sera pas mis en veille](./install#make-sure-xdrip-will-not-be-put-to-sleep).

Avant d'essayer de connecter votre transmetteur, vérifiez que vos paramètres sont corrects afin d'éviter des déconnexions fréquentes.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Paramètres moins courants  
&ensp;&emsp;Paramètres Bluetooth  
:::

Pour commencer, utilisez les paramètres indiqués ci-dessous.

Le Bluetooth doit être allumé. **Activez** `Activer le Bluetooth`.

::: xdripitem Activer le Bluetooth <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Activer automatiquement bluetooth s'il est éteint lorsqu'on tente de se connecter à un périphérique bluetooth
:::

**Activez** le garde-fou, mais lisez l'information ci-dessous.

::: xdripitem Garde-fou Bluetooth <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Réinitialiser Bluetooth en le désactivant puis réactivant si nous n’obtenons rien pendant 20 minutes
:::

**Activez** le garde-fou Dex, mais lisez l'information ci-dessous.

::: xdripitem Chien de garde Bluetooth Dex <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Réinitialiser Bluetooth en le désactivant et reactivant pour continuer de faire marcher la source de données. Sans cela, le collecteur peut échouer.
:::

::: info Remarque
Attention : le Garde-fou Bluetooth et le Chien de garde Bluetooth Dex éteignent puis rallument le Bluetooth du téléphone, ce qui provoque une déconnexion Bluetooth temporaire de tous les appareils connectés. Vous voudrez peut-être désactiver cette fonction si vous utilisez AAPS et que votre transmetteur ou votre pompe ne rétablit pas automatiquement la connexion Bluetooth.
:::

**Désactivez** Fermer GATT.

::: xdripitem Fermer GATT sur déconnexion BLE <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Si le garde-fou Bluetooth s'active souvent alors vous pouvez essayer de décocher cette option pour voir si ça aide
:::

Si votre transmetteur perd la connexion et qu'un scan Bluetooth permet de la rétablir, vous pouvez essayer d'activer `Utiliser le scan`. Laissez-le **désactivé** pour commencer.

::: xdripitem Utiliser le scan <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Scanner avant de se connecter sur xBridge et Bluetooth Libre
:::

Sur les téléphones Samsung et de nombreux téléphones chinois, vous **devez désactiver `Faire confiance à Auto-Connect`** ! Si votre téléphone perd la connexion, **désactivez-le**.

::: xdripitem Faire confiance à Auto-Connect <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utiliser et faire confiance à la fonctionnalité de connexion auto Bluetooth d'Android
:::

À partir d'Android 8, vous pouvez activer `Utiliser les scans en arrière-plan`. Si vous perdez la connexion, **laissez-le désactivé**.

::: xdripitem Utiliser les scans en arrière-plan <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Utiliser la fonction de scan en arrière-plan d'Android 8+
:::

Laissez les deux options ci-dessous **désactivées**.

::: xdripitem Wakelocks Bluetooth <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Anciens wakelocks Bluetooth qui peuvent drainer la batterie un peu plus, mais pourraient être nécessaire pour la réception bluetooth  
:::

::: xdripitem Redémarrer le Bluetooth en permanence <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Réinitialiser le Bluetooth en le désactivant en en le réactivant après quelques minutes ! À sélectionner uniquement pour test. Cela peut perturber les autres utilisations du Bluetooth.
:::

Si votre transmetteur est un Transmitter_T ou un Droplet, activez cette option ; sinon laissez-la **désactivée**.

::: xdripitem Support de Transmitter (PL) <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Support expérimental du périphérique 'Transmitter' de @FPV-UAV - test uniquement
:::

En cas de pertes de connexion, vous pouvez **activer** le mode de sondage. Il ne fait rien d'utile en soi, mais garde le Bluetooth du téléphone éveillé.

::: xdripitem Mode de sondage xBridge+ <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Support expérimental pour la fonction de sondage xBridge+
:::

Si votre transmetteur est un ancien BluCon compatible, vous pouvez activer cette option ; si vous avez plusieurs demandes d'appairage par jour, laissez-la **désactivée**.   
*Remarque : seul le BluCon s'appaire (bond) avec Android, les autres transmetteurs non.*

::: xdripitem Permettre la dissociation du BluCon <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Disponible uniquement pour les téléphones qui supportent l'association automatique
:::

<br>

Redémarrez votre téléphone pour vous assurer que tous les paramètres sont pris en compte.

<br>

## Connecter le transmetteur Bluetooth {#connect-bluetooth-bridge}

Vérifiez que votre transmetteur n'est connecté à rien d'autre : ni à un autre appareil, ni à une autre application.  
Lancez un scan Bluetooth.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Scan Bluetooth  
:::

Si le scan ne démarre pas automatiquement, sélectionnez `BALAYAGE`.

<img src="../images/M-BTscan.png" style="zoom:75%;" />

Si votre transmetteur n'apparaît pas, vérifiez qu'il est complètement chargé (ou qu'il a une pile neuve) et réinitialisez-le.

Une fois visible, sélectionnez-le.

Si votre transmetteur est un BluCon, saisissez le code inscrit sur le côté. 

<img src="./images/M-BT-BK.png" style="zoom:55%;" />

Positionnez-le correctement sur votre capteur. Certains transmetteurs tolèrent très peu d'écart d'angle et de distance par rapport au capteur.

::: info Module externe
Si votre capteur nécessite un [algorithme hors processus (OOP)](../use/OOP), assurez-vous qu'il est installé dès maintenant.
:::

<br>

Passez ensuite à [Démarrer le capteur](../use/startsensor#libre)

## Arrêter le capteur Libre {#stop-libre-sensor}

xDrip ne peut pas arrêter physiquement un capteur Libre ; celui-ci s'arrête de lui-même après 14 jours et 12 heures et continue d'afficher la dernière valeur.

Néanmoins, lors d'un changement de capteur, il est vivement recommandé d'informer xDrip du changement en arrêtant le capteur.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Arrêter le capteur  
:::

Confirmez que vous voulez vraiment arrêter le capteur.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Arrêt du capteur <span class='symbol'></span>
  &emsp;N'arrêtez votre capteur que lorsque vous planifiez de l'enlever, sinon laissez fonctionner!  


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;ARRÊTER LE CAPTEUR&ensp;</span>
:::

Cela réinitialise toutes les calibrations et permet à xDrip de démarrer un nouveau capteur.

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
