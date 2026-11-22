---
source_hash: 4b874be737
source_commit: 0bbdbd2
---
Une fois le téléchargement terminé, installez l'apk de xDrip.

<img src="./images/InstallConfirm.png" style="zoom:50%;" />

Sur les versions récentes d'Android, vous verrez un avertissement de Google Play Protect indiquant que l'application n'est pas sûre et a été conçue pour d'anciennes versions d'Android. Ignorez-le avec Plus de détails, puis Installer quand même.

<img src="./images/PlayProtectWarning.png" style="zoom:50%;" />

**Vous devez [autoriser l'installation d'applications de sources inconnues](https://developer.android.com/distribute/marketing-tools/alternative-distribution#unknown-sources) dans les paramètres de sécurité d'Android.**  
Les versions officielles de xDrip sont exemptes de virus et de logiciels malveillants : comme le code est open source et contrôlé par le développeur principal, sa distribution est sûre si vous le téléchargez depuis GitHub.

<img src="./images/AllowUnknownSources.png" style="zoom:50%;" />

Appuyez sur `Paramètres` puis activez `Autoriser cette source`.

<img src="./images/AllowFromThisSource.png" style="zoom:50%;" />

Une fois l'installation terminée, ouvrez xDrip.

<img src="./images/Install03.png" style="zoom:75%;" />

### Comprendre ce qu'est xDrip {#understand-what-is-xdrip}

::: warning **Lisez** l'avertissement important
:::

::: xdrip <img src="./images/ImportantWarning.png" style="zoom:50%;" />
<img src="./images/WarningAgree.png" style="zoom:50%;" />  
Do NOT use or rely on this software or any associated materials for any medical purpose or decision.  
Do NOT rely on this system for any real-time alarms or time critical data.  
Do NOT use or rely on this system for treatment decisions or use as a substitute for professional healthcare judgement.  
All software and materials have been provided for informational purposes only as a proof of concept to assist possibilities for further research.  
No claims at all are made about fitness for any purpose and everything is provided **AS IS**. Any part of the system can fail at any time.  
Always seek the advice of a qualified healthcare professional for any medical questions.  
Always follow your glucose-sensor or other device manufacturers' instructions when using any equipment; do not discontinue use of accompanying reader or receiver, other than as advised by your doctor.  
This software is not associated with or endorsed by any equipment manufacturer and all trademarks are those of their respective owners.  
Your use of this software is entirely at your own risk.  
No charge has been made by the developers for the use of this software.  
This is an open-source project which has been created by volunteers. The source code is published free and open-source for you to inspect and evaluate.  
By using this software and/or website you agree that you are over 18 years of age and have read, understood and agree to all of the above.
:::

<br>

**Lisez** le CLUF (EULA).  

::: warning Assurez-vous de bien le comprendre avant d'enregistrer.
:::

::: xdrip <img src="./images/EULA.png" style="zoom:50%;" />
xDrip MUST NOT BE USED TO MAKE MEDICAL DECISIONS.  
IT IS A RESEARCH TOOL ONLY AND IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  
THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
:::



<br>

### Autoriser l'activité en arrière-plan {#authorize-background-activity}

xDrip doit avoir le droit de fonctionner en arrière-plan : il doit être exclu de l'optimisation de la batterie (liste blanche). C'est indispensable à son bon fonctionnement. Il devrait vous demander cette autorisation. S'il ne le fait pas, ou si vous devez le vérifier plus tard, vous devrez le contrôler dans `Paramètres` - `Applications` - `xDrip` de votre téléphone. Consultez le manuel de votre téléphone, car cela dépend de la version d'Android et du fabricant.

::: xdripitem Veuillez autoriser les permissions
&emsp;xDrip+ a besoin d'être sur liste blanche pour des performances correctes  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;D'accord&ensp;</span>
:::

<img src="./images/AllowRunInBackground.png" style="zoom:75%;" />

*Remarque : à partir d'Android 12, vous ne verrez plus la mention **liste blanche** (whitelisting).*

Plus d'informations [ici](../troubleshoot/savings#apps-battery-savings).

<br>

### Autoriser les notifications {#authorize-notifications}

xDrip doit avoir accès aux notifications du téléphone pour fonctionner comme prévu.

<img src="./images/Install47.png" style="zoom:75%;" />

<br>

## Vérifier la version installée {#verify-which-version-is-installed}

Appuyez sur le bouton retour de votre téléphone jusqu'à revenir à l'écran principal. Sélectionnez le menu hamburger en haut à gauche, puis `État du système`.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;  État du système
:::

La version actuelle s'affiche après `Version`. Dans l'exemple ci-dessous, le 28 janvier 2022.

<img src="../images/M-SS-Ver.png" style="zoom:75%;" />

Sur les versions les plus récentes, vous la trouverez sur toutes les pages de l'état du système.

<img src="../images/M-SS-Ver2.png" style="zoom:76%;" />

Consultez [cette page](../use/update) pour mettre à jour ou revenir à une version antérieure.

<br>

## Empêcher la mise en veille de xDrip {#make-sure-xdrip-will-not-be-put-to-sleep}

Ces réglages sont ceux par défaut, mais vérifiez quand même qu'ils sont exactement comme ci-dessous. À chaque mise à jour de votre téléphone, revenez les vérifier : désactivez puis réactivez les cases qui doivent être cochées pour forcer les réglages.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Paramètres moins courants  
&ensp;&emsp;Autres options diverses  
&ensp;&emsp;&emsp;Exécutez Collector au premier plan
:::

Depuis le retrait de la prise en charge d'Android 7 ([12 juillet 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)), le collecteur fonctionne toujours au premier plan sur Android 8.0 et plus récent : il n'y a plus d'interrupteur pour cela. Le graphique de la notification persistante, dans le volet déroulant de votre téléphone, est indispensable pour maintenir l'application active et s'affiche toujours.

::: xdripitem Notification persistante compacte <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Activer pour masquer le graphique dans la notification et afficher uniquement la valeur de glucose actuelle.
:::

Si vous préférez ne pas afficher le graphique dans la notification persistante, activez `Notification persistante compacte` pour n'afficher que la valeur de glucose actuelle.

::: xdripitem Invité pour l’optimisation de la batterie <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Sur Android 6+ s'assurer que l'optimisation de la batterie est désactivée (recommandé).
:::

`Invité pour l’optimisation de la batterie` doit être **désactivé**, car vous devriez avoir accepté la [liste blanche de la batterie](#authorize-background-activity) pendant l'installation. Sinon, excluez xDrip de l'optimisation de la batterie dans les paramètres Android.

::: xdripitem Solutions de contournement Wake <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utiliser des contournements pour éviter le comportement Android non standard de certains terminaux. Sans cela, les collecteurs ne peuvent pas obtenir les données.
:::

Anciennement « Samsung workaround », cette option corrige le non-respect des spécifications Android par certains fabricants. Elle devrait s'activer automatiquement sur certains smartphones. Recommandé.

### Activer la localisation {#enable-location}

Sur les versions récentes d'Android (6 et plus), la localisation est [obligatoire](https://developer.android.com/training/location/permissions) pour permettre la connexion Bluetooth Low Energy.  
Si vous utilisez xDrip avec un capteur ou un transmetteur Bluetooth, vous **devez** activer la localisation (Paramètres Android -> [Localisation](https://support.google.com/android/answer/3467281)) et autoriser xDrip à y accéder. Consultez le manuel de votre téléphone, car cela dépend de la version d'Android et du fabricant.

Veillez à sélectionner Toujours autoriser dans les paramètres.

<img src="./images/Install17a.png" style="zoom:75%;" />

<img src="./images/Install17.png" style="zoom:75%;" />

<br>

Passez à la [sélection de la source de données](./datasource)

<br>

[*Dernière modification le 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.15)
