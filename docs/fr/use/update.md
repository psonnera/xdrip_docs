---
source_hash: 874eaebd13
source_commit: 7a18e7c
---
Vous pouvez mettre à jour xDrip en installant une autre version par-dessus la version actuelle, sans la désinstaller, de la même façon que lors de votre [installation](../install/download) d'origine.

Vous pouvez aussi utiliser le mécanisme de mise à jour interne de xDrip.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_briefcase_download_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Mises à jour
:::

Les paramètres de mise à jour vous permettent de choisir quelles versions de xDrip vous sont proposées en mise à jour.

::: warning NE DÉSINSTALLEZ PAS xDRIP+
Vous pouvez passer à une version plus récente ou plus ancienne de xDrip simplement en l'installant par-dessus la version actuelle.  
Désinstaller xDrip peut entraîner une perte de données complète et irrécupérable si vous n'avez pas fait de [sauvegarde](../troubleshoot/reinstall#reinstall-xdrip).
:::

Seules les versions officielles de xDrip peuvent utiliser cette fonction.  
Si vous avez installé une [version dérivée (fork)](../install/download#forked-versions), seul son auteur peut fournir des mises à jour. 

::: info Remarque
La mise à jour de xDrip est totalement transparente et ne nécessite aucune action particulière sur votre capteur en cours.  
Vos paramètres sont conservés, sauf si une modification importante a été apportée à un paramètre particulier.  
Par précaution, il vaut mieux garder un œil sur xDrip si vous avez choisi une version alpha ou nightly.
:::

Vous devriez activer la vérification automatique des mises à jour.

::: xdripitem Vérification automatique de mise à jour <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Être informé des nouvelles versions disponibles  
:::

Si vous la laissez désactivée, xDrip vous rappellera de faire la mise à jour tous les 60 jours.

::: xdripitem Hé Fam...
&ensp;Vous avez les contrôles de mise à jour désactivé!  
&ensp;Nous essayons de corriger les bugs et ajouter de nouvelles fonctionnalités à xDrip+ au fil du temps.  
&ensp;Tous les 60 jours ce rappel s'affichera pour vous demander d'activer le contrôle de mises à jour.  
:::

Il existe trois canaux de mise à jour :

- Stable : versions publiées dont la stabilité et la fiabilité ont été éprouvées
- Beta : versions candidates à une publication stable
- Alpha : versions en cours de développement

Un quatrième n'apparaît qu'une fois Alpha sélectionné (voir [ci-dessous](#getting-the-nightlies-on-automatic-update)) :

- Nightly : prototypes destinés aux tests

Les versions les plus testées n'incluent pas les dernières fonctionnalités et corrections.

Les versions moins testées peuvent contenir des bugs, mais incluent aussi les dernières fonctionnalités et corrections.

::: xdripitem Mise à jour du Canal
&ensp;Choisir version Stable, Bêta ou Alpha
:::

::: xdripitem Mise à jour du Canal
&ensp;Stable - tried and tested versions (versions éprouvées)  
&ensp;Beta - new features but not fully tested (nouvelles fonctions, pas entièrement testées)  
&ensp;Alpha - versions for early testing (versions pour les premiers tests)  
&ensp;Nightly - untested raw code - experts only! (code brut non testé, experts uniquement !)
:::

### Recevoir les nightlies par mise à jour automatique {#getting-the-nightlies-on-automatic-update}

Le canal Nightly est masqué tant que vous n'avez pas sélectionné Alpha une première fois.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_briefcase_download_grey600_48dp.png" style="width:5%;" />&ensp;xDrip+ Mises à jour  
&ensp;&emsp;Mise à jour du Canal
:::

1. Ouvrez Mise à jour du Canal. Si Nightly figure dans la liste, sélectionnez-le et c'est terminé.
2. Si Nightly n'apparaît pas, sélectionnez Alpha, revenez à l'écran d'accueil de xDrip, puis rouvrez xDrip+ Mises à jour et Mise à jour du Canal. Nightly est maintenant visible : sélectionnez-le.

::: warning Nightly est le canal le moins testé
Les versions Nightly contiennent le code le plus récent et le moins testé. Elles sont les premières à recevoir les nouvelles fonctions, mais c'est aussi là que les bugs sont généralement découverts. Surveillez xDrip après chaque mise à jour et soyez prêt à [revenir à une version antérieure](#downgrade) en installant une version plus ancienne par-dessus.
:::

Les vérifications de mise à jour ont lieu environ toutes les 24 heures. Pour vérifier immédiatement, utilisez [Vérifier les mises à jour](./3dotsmenu#check-for-updated-version) dans le menu à 3 points.

Dans le [dépôt officiel](https://github.com/NightscoutFoundation/xDrip/releases), vous pouvez identifier la dernière version publiée grâce à l'étiquette Latest.    
Vous pouvez télécharger la dernière version publiée [ici](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk).  
Toutes les autres portent l'étiquette Pre-release.

<img src="./images/M-S-US2b.png" style="zoom:75%;" />

Les fonctions de rapport ne sont plus utilisées. Si vous avez besoin d'aide, utilisez les [discussions](https://github.com/NightscoutFoundation/xDrip/discussions) ou [Facebook](https://www.facebook.com/groups/xDripG5).

::: xdripitem Rapport d'erreurs automatique
:::

::: xdripitem Activer la télémétrie
:::

Les commentaires ne sont plus utilisés. Ne vous en servez que pour envoyer des compliments.

::: xdripitem Envoyer des commentaires
:::

### Mise à jour {#update}

Vous pouvez mettre à jour xDrip en installant une autre version par-dessus la version actuelle, sans la désinstaller, de la même façon que lors de votre [installation](../install/download) d'origine.

Vous pouvez aussi utiliser le mécanisme de mise à jour interne de xDrip.

Les notifications de mise à jour disponible se déclenchent selon le canal choisi.  
Si vous avez désactivé la vérification automatique des mises à jour, vous pouvez lancer une vérification manuellement depuis le [menu à 3 points](./3dotsmenu#check-for-updated-version).

1. Le canal de mise à jour actuel est affiché
2. Versions actuelle et plus récente (disponible)
3. Télécharger maintenant lance le téléchargement de la mise à jour ; Android demandera l'autorisation d'installer une fois le téléchargement terminé.
4. Vous pouvez désactiver les mises à jour automatiques. Cela a le même effet que le bouton de vérification automatique des mises à jour ci-dessus.
5. Si vous n'utilisez pas le téléchargeur interne, votre appareil utilisera l'application par défaut pour télécharger les fichiers depuis Internet.
6. Quitter sans rien faire.

<img src="./images/M-S-US5.png" style="zoom:75%;" />

Si vous choisissez le téléchargeur interne, une barre de progression s'affiche et, une fois le téléchargement terminé, l'installation démarre automatiquement.

<img src="./images/M-S-US6.png" style="zoom:75%;" />

Si vous n'avez pas choisi le téléchargeur interne, votre téléphone télécharge le paquet depuis [GitHub](https://github.com/NightscoutFoundation/xDrip/releases) et lance l'installation une fois le téléchargement terminé.

Aucune nouvelle autorisation ne devrait être nécessaire.

 <img src="./images/M-S-US6a.png" style="zoom:75%;" />

Une fois la mise à jour effectuée, vous pouvez vérifier la version actuelle dans l'[état du système](../troubleshoot/systemstatus).

### Revenir à une version antérieure {#downgrade}

Vous n'avez pas besoin de désinstaller xDrip pour revenir à une version plus ancienne (sauf pour [passer d'une version officielle à une version dérivée](../troubleshoot/reinstall) ou inversement) : installez simplement la version voulue par-dessus la version actuelle, [comme lors de la première installation](../install/download).

<br>

[*Dernière modification le 6/9/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
