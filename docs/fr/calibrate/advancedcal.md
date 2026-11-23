---
source_hash: d8b53e5b65
source_commit: 7a18e7c
---
Ce menu propose des paramètres et des mécanismes importants pour l'étalonnage.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;"/>
&ensp;Paramètres  
&emsp;Paramètres moins courants  
&emsp;&ensp;Calibration avancée
:::

##### Utiliser les valeurs BG des traitements {#use-treatment-bg-values}

Vous pouvez choisir d'utiliser les [traitements](../use/mainUI#treatments) de glycémie (tests sanguins) comme calibrations.

::: xdripitem Utiliser les valeurs BG des traitements
&ensp;Indiquer si vous voulez calibrer avec la valeur de glycémie dans une saisie de Traitement  
:::

::: warning Attention
Utiliser systématiquement les traitements comme calibrations **n'est pas recommandé**.
:::

Le mode automatique ne vous propose d'utiliser le traitement comme calibration que si xDrip détecte que les conditions actuelles sont bonnes pour étalonner (glycémie stable depuis 20 minutes, faible bruit...).

::: xdripitem Utiliser les valeurs BG des traitements
&emsp;Automatic mode (best)<span style="float: right;">●&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Ask me every time<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Never use them<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Always use them<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp; 
:::

Il peut aussi vous proposer d'activer la calibration automatique.  

**Il n'est pas recommandé d'utiliser cette fonction avec les capteurs G6/G7/ONE/ONE+.**

::: xdripitem Activer la calibration automatique
&emsp;Les tests sanguins réalisés durant les périodes stables peuvent être utilisés pour recalibrer automatiquement 20 minutes après leur entrée. Ceci devrait être la méthode de calibration la plus précise.  


&ensp;Voulez-vous activer cette fonctionnalité ?  

&emsp;<span style="background-color: white; color: black;">&ensp;NON&ensp;</span>&emsp;&emsp;&emsp;&emsp;OUI, ACTIVER
:::

Ask me every time vous posera exactement cette question à chaque saisie d'un traitement de glycémie.

::: xdripitem Utiliser les glycémies capilaires pour la calibration?
&emsp;Voulez-vous utiliser ce résultat de test de glycémie capillaire pour calibrer ?  
:::

Never use them n'utilisera jamais les traitements pour étalonner (et vous empêchera de transformer un [traitement](../use/mainUI#treatments) en calibration).

##### Calibration automatique {#automatic-calibration}

Il est recommandé de **la désactiver pour les capteurs G6/G7/ONE/ONE+**.

La calibration automatique accepte un traitement comme calibration s'il remplit la condition d'une tendance plate pendant 20 minutes.

::: xdripitem Calibration automatique <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Calibrer en utilisant les nouvelles valeurs de glycémies si les conditions semblent pouvoir le faire, sans demander confirmation (expérimental)  
:::

### Plugins {#plugins}

Des plugins de calibration sont disponibles dans xDrip, la plupart ne sont plus utilisés. Lorsqu'il est activé, un plugin remplace la calibration standard de xDrip. L'idée était de permettre de choisir un algorithme de calibration personnalisé, mais elle n'a jamais été entièrement mise en œuvre. En règle générale, un capteur qui a besoin d'un plugin pour être étalonné devrait être remplacé, par sécurité.

::: warning **SÉCURITÉ**
**Les mécanismes de sécurité de la calibration ne s'appliquent pas aux plugins. Utiliser un plugin pour contourner un échec de calibration est dangereux.**
:::

::: xdripitem Plugin de Calibration
&ensp;Plugin de calibration secondaire expérimental  
:::

::: warning Extension Wear
Les plugins ne sont pas entièrement implémentés dans Wear. Vous pourriez voir des valeurs différentes sur votre montre.
:::

::: xdripitem Plugin de Calibration
&emsp;None  
&emsp;Datricsae - pronounced: da-trix-ee - highly experimental  
&emsp;Fixed Slope Example - never use for real data  
&emsp;xDrip Original - classic algorithm  
&emsp;Last7Ua - Unweighted last 7 calibrations. Example only
:::

**`None`** : par défaut, l'algorithme de xDrip est utilisé. **Recommandé**

**`Datricsae`** était apprécié de ceux qui avaient des difficultés avec l'algorithme par défaut de xDrip. Il nécessite 8 points de calibration (en dessous de 4, l'algorithme d'origine de xDrip est utilisé) et limite la pente entre 0,5 et 1,7. Son principal atout est d'écarter les valeurs aberrantes (mauvais points de calibration) trop éloignées de la droite de calibration. Après ce filtrage, si le nombre de points de calibration tombe sous 4 ou si la pente sort des limites, l'algorithme classique de xDrip est utilisé.  
Soyez prudent : des calibrations bruitées peuvent donner des résultats incohérents.

<img src="./images/M-S-LCS-AC3d.png" style="zoom:75%;" />

**`Fixed slope`** est un plugin vide qui renvoie une pente de 1,08 et une ordonnée à l'origine de -5. **Ne l'utilisez pas pour une glycémie réelle.**

**`xDrip Original`** était l'équivalent en plugin de l'algorithme de xDrip. Il ne fait rien de plus que l'algorithme de xDrip. **L'utiliser n'apporte rien.**

**`Last 7 unweighted`** était une première tentative d'amélioration de l'algorithme d'origine. Il nécessite au moins 4 calibrations (il utilise jusqu'aux 7 dernières ; en dessous de 4, l'algorithme actuel de xDrip est utilisé). **Non recommandé.**

::: xdripitem Tracés du Plugin sur le graphique <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Afficher les résultats de glycémie du plugin sur le graphique principal  
:::

Activez cette option si vous voulez que xDrip trace les résultats du plugin.

<img src="../use/images/M-S-DS2l2.png" style="zoom:75%;" />

::: xdripitem Utiliser la Glycémie du Plugin <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;L'affichage des chiffres principaux de glucides proviennent du plugin !  
:::

Activez cette option si vous voulez que la valeur de glycémie principale provienne des résultats du plugin. Un P entouré s'affiche alors.

<img src="./images/M-S-LCS-AC5a.png" style="zoom:75%;" />

::: xdripitem Plugin surpasse tous les autres <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Toutes les nouvelles données de glycémie seront calculées et enregistrées du plugin sélectionné et non à partir de l'algorithme standard xDrip. Ce n'est pas testé et peut être inexacte et pleins de bug. Utiliser avec une extrême prudence.  
:::

Non implémenté.

### Calibrations {#calibrations}

::: xdripitem Calibrations doubles <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Demander un second test sanguin optionnel pour la calibration initiale  
:::

Si vous ne faites pas réellement deux tests sanguins distincts pour la calibration initiale, désactivez cette option.

L'ancienne méthode de calibration rétablit la plage d'origine, plus étroite, des pentes autorisées dans l'algorithme de calibration classique de xDrip (avant 2017), ce qui rend les pentes par défaut plus probables. Visible uniquement lorsque le Mode développeur est activé.

::: xdripitem Ancienne méthode de calibration <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Plage plus étroite originale de pentes autorisées dans l'algorithme de calibration classique xDrip (avant 2017). Les pentes par défaut sont plus probables !
:::

::: xdripitem Calibrations peu fréquentes <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Si besoin, utiliser des calibrations plus anciennes, par exemple si les calibrations sont rarement saisies.  
:::

Les calibrations trop anciennes sont ignorées : si vous étalonnez rarement et voulez que des mesures de calibration plus anciennes pèsent sur la courbe de calibration actuelle, activez cette option. 

### Spécifique au Libre {#libre-specific}

##### Pentes du Libre non fixées {#non-fixed-libre-slopes}

::: xdripitem Pentes du Libre non fixées <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Activer pour permettre les pentes variables avec les méthodes de collection Libre  
:::

Les capteurs Libre peuvent être difficiles à étalonner. Si vous n'arrivez pas à obtenir une bonne précision sur toute la plage, ou si vous n'étalonnez jamais dans la plage haute, désactivez cette option pour fixer la pente à 1. C'est recommandé pour les débutants.

**Par sécurité, étalonnez toujours à glycémie stable, dans le bas de la plage normale.**

::: xdripitem Check Libre Serial <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Automatically stop if Libre Serial changes unexpectedly  
:::

Reporter les calibrations de l'ancien capteur sur un nouveau est dangereux. **Laissez cette option activée.**

### Ignorer la vérification de qualité {#bypass-quality-check}

::: xdripitem Ignorer la vérification de qualité <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Permettre la calibration initiale même si nous n'avons pas assez de bonnes données. Attention peut entraîner une calibration inexacte !  
:::

Lors des mesures préliminaires avant la première calibration, 3 mesures valides sont nécessaires. Si elles manquent ou ne respectent pas les valeurs de sécurité, xDrip attend. Activer cette option permet de calibrer sans vérification. **Non recommandé.**

::: xdripitem Collecte des premières lectures
&ensp;✔ Collecteur de données en cours d'exécution  
&ensp;✔ Réception des données du Collecteur MiaoMiao  
&ensp;✔ Reçu quelques données récentes  
&ensp;⧖ Reçu assez de bonnes données pour calibrer  
&ensp;**Need 3 recent readings, got only 1 so far**  
&ensp;Next reading expected in 1 minute 
:::

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
