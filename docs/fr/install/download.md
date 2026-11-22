---
source_hash: 932cfecc51
source_commit: 298bb92
---
## Laquelle installer ? {#which-one-to-install}

xDrip n'est pas disponible sur le Google Play Store. Vous trouverez toutes les versions sur [Github](https://github.com/NightscoutFoundation/xDrip/releases).  
Vous avez deux choix principaux pour installer xDrip : la **dernière version stable** (Latest release) ou une **pré-version** (Pre-release).

::: info Remarque
Si xDrip est déjà installé sur votre téléphone, vous n'avez pas besoin de le désinstaller avant d'installer une mise à jour.  
Si vous utilisez une version dérivée (fork) et voulez passer à une version officielle de xDrip, ou l'inverse, suivez [ceci](../troubleshoot/reinstall).
:::

::: info Plusieurs installations de xDrip
Si vous devez installer plus d'un xDrip sur le même téléphone, il vous faut une [variante](#variants).
:::

### Dernière version stable {#latest-release}

La dernière version stable (Latest release) est une version stable de xDrip. Elle n'a pas toutes les fonctions les plus récentes, mais sa stabilité est éprouvée et elle ne souffre pas de bugs graves. C'est une version sûre pour commencer, sauf si vous avez besoin d'une fonction particulière (consultez le [journal des modifications](../changelog) pour le vérifier).

Vous pouvez la télécharger [ici](https://xdrip-plus-updates.appspot.com/stable/xdrip-plus-latest.apk) ou avec ce QR code :

<img src="https://jamorham.github.io/images/download-xdrip-plus-qr-code-120.png" />

Vous la trouverez aussi dans le [dépôt principal](https://github.com/NightscoutFoundation/xDrip) en sélectionnant Latest.

<img src="./images/GitHubReleaseLatest.png" style="zoom:50%;" />

<br>

#### Avertissement au téléchargement {#download-warning}

xDrip téléchargé depuis [https://github.com/NightscoutFoundation/xDrip/releases](https://github.com/NightscoutFoundation/xDrip/releases) est sûr.

<img src="./images/Install46.png" style="zoom:75%;" />

<br>

Une fois le téléchargement terminé, [passez à l'installation de xDrip](./install)

<br>

### Pré-version {#pre-release}

Les pré-versions (Pre-release) contiennent les développements les plus récents de xDrip, comme les traductions, les nouvelles fonctions et les corrections de bugs. Elles peuvent aussi contenir quelques bugs... C'est pourtant la version à utiliser pour profiter des dernières améliorations.

Toutes les versions de xDrip sont disponibles [ici](https://github.com/NightscoutFoundation/xDrip/releases).

Dépliez les fichiers (Assets) et sélectionnez le fichier `.apk`. Vous le trouverez dans le dossier `Téléchargements` de votre téléphone.

<img src="./images/GitHubReleaseAssets.png" style="zoom:50%;" />

::: info Remarque
N'utilisez **pas** les liens Facebook pour télécharger xDrip, mais **copiez et collez le lien** dans un navigateur (comme Chrome).
:::

<br>

#### Avertissement au téléchargement {#download-warning-1}

xDrip téléchargé depuis [https://github.com/NightscoutFoundation/xDrip/releases](https://github.com/NightscoutFoundation/xDrip/releases) est sûr.

<img src="./images/Install46.png" style="zoom:75%;" />

<br>

Une fois le téléchargement terminé, [passez à l'installation de xDrip](./install)

<br>

## Versions dérivées {#forked-versions}

Certains développeurs ajoutent des fonctions et des personnalisations qui ne sont pas disponibles dans les pré-versions officielles, tant que leur auteur n'a pas créé une Pull Request dans xDrip et qu'elle n'a pas été intégrée au projet principal.

::: warning Mise à jour des versions dérivées
Vous pouvez utiliser ces versions, mais sachez qu'elles ne sont parfois prises en charge que par leur créateur.  
**Les mises à jour automatiques de xDrip ne fonctionnent pas avec les versions dérivées.**  
Gardez aussi à l'esprit que vous ne pouvez pas installer une version dérivée si une version officielle est installée sur votre téléphone :  
vous devrez d'abord la [désinstaller](../troubleshoot/reinstall).  
Il en va de même dans l'autre sens (d'une version dérivée vers une version officielle).
:::

<br>

## Variantes {#variants}

Quatre variantes sont publiées régulièrement, ce qui permet d'installer jusqu'à 5 xDrip sur votre téléphone. Cela peut être particulièrement utile pour suivre plusieurs personnes à la fois.

::: warning Attention
Il est déconseillé d'utiliser une variante connectée à votre capteur : utilisez uniquement la version principale.  
N'utilisez les variantes que comme abonnés.  
Certaines anciennes versions de xDrip laissaient fuir des valeurs avec AAPS/NSClient. Utilisez les dernières variantes.
:::

Vous pouvez télécharger les variantes [ici](https://drive.google.com/drive/folders/0B6mvYVNVC-fOWkxnVF80dlFabjQ?resourcekey=0-ebguuiPuB1wUI9Rp2zjMNg).

Triez-les par date de modification, les plus récentes en premier, et choisissez la variante à télécharger.

<img src="./images/Variant.png" style="zoom:90%;" />

Les variantes sont aussi fournies comme fichiers (assets), à côté de l'apk habituel, dans la dernière version stable sur [GitHub](https://github.com/NightscoutFoundation/xDrip/releases).

<img src="./images/GitHubReleaseLatest.png" style="zoom:50%;" />

Une fois la variante téléchargée, procédez comme pour une installation normale de xDrip.

**Les variantes ne se mettent pas à jour automatiquement.** Vous devez télécharger les mises à jour et les installer par-dessus la version actuelle de la variante (sans avoir besoin de la désinstaller) : veillez simplement à sélectionner la même variante (1 à 4).

<br>

[*Dernière modification le 3/2/2023*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2023.02.26)
