---
source_hash: bb1a1f1faf
source_commit: 7a18e7c
---
Les algorithmes hors processus (Out of process algorithms) sont des applications externes chargées d'effectuer des traitements de données que xDrip ne fournit pas directement.

Ils ne sont plus utilisés aujourd'hui que pour les capteurs Libre et les transmetteurs.

Il existe deux familles différentes d'algorithmes hors processus (OOP) :

### OOP1 {#oop1}

<img src="./images/OOP_1.png" style="zoom:75%;" />

::: warning Anciennes versions d'Android UNIQUEMENT
La version d'Android maximale prise en charge est la 9.  
Quelques téléphones sous Android 10 et plus ont été signalés comme fonctionnant avec OOP1new/OOP1us.
:::

| Version OOP                                 | Date de version | Capteurs pris en charge    | Taille du fichier |
| ------------------------------------------- | --------------- | -------------------------- | ----------------- |
| OOP1 (2bb9458)                              | 2018-08-26      | Libre                      | 17.1MB            |
| OOP1new (fa218ef)                           | 2019-11-22      | Libre, Libre 2 EU          | 25.3MB            |
| OOP1us (e901151) - **ne pas utiliser : utilisez OOP2** | 2019-09-13 | Libre 14 jours US (ancien) | 27.8MB     |

OOP1 fournit des valeurs similaires à celles du lecteur du fabricant, sans étalonnage. Vous avez besoin d'un [transmetteur compatible](../install/libreBT) si vous en utilisez un. OOP1 s'applique aussi aux résultats des scans NFC.

::: warning Aucun étalonnage possible
Les étalonnages sont ignorés lorsque vous utilisez OOP1.  
C'est une mesure de sécurité, car xDrip ne peut pas vérifier la cohérence des données fournies par OOP1.
:::

Deux versions sont disponibles : [Libre 1 et Libre 2 EU](https://drive.google.com/open?id=13ERWcSVSFMLy9rhpbv5rArFrnDuAzriM) ou [Libre 14 jours US](https://drive.google.com/open?id=172whZZYTyE_ZEuN0T-zhdMKhucy6jP-a). 
*Remarque : vous devez être connecté à votre compte Google pour accéder aux liens ci-dessus*

L'algorithme hors processus doit être [activé](./misc#out-of-process-algorithm) lorsque vous utilisez OOP1.

### OOP2 {#oop2}

<img src="./images/OOP_2.png" style="zoom:75%;" />

OOP2 assure le décodage des capteurs Libre 14 jours US et Libre 2 EU, soit en connexion directe (Libre 2 EU uniquement), soit avec un [transmetteur compatible](../install/libreBT).

::: info L'étalonnage est facultatif
Vous pouvez soit étalonner à partir des données brutes, soit ne pas étalonner, soit ajouter un étalonnage aux données natives.  
Consultez les [paramètres OOP2](./misc#oop2).
:::

**N'utilisez que la dernière application OOP2 avec la dernière version de xDrip.**

**<u><big>[→ Téléchargez la dernière version d'OOP2 ici. ←](https://drive.google.com/file/d/1106h2s12b3Ev9gKCTU2G75q8h9ChHjcz/view?usp=sharing)</big></u>**

*Remarque : vous devez être connecté à votre compte Google pour accéder au lien ci-dessus.* 

::: warning Attention
*Algorithme Libre hors processus* (OOP1) doit être [désactivé dans xDrip](./misc#out-of-process-algorithm) lorsque vous utilisez OOP2.
:::

| Version OOP                         | Date de version | Capteurs pris en charge                       | Taille du fichier |
| ----------------------------------- | --------------- | --------------------------------------------- | ----------------- |
| OOP2 (70129ac) - **ne pas utiliser**     | 2021-12-04 | Libre 2 EU                                    | 2.63MB            |
| OOP2new (93e5cac) - **ne pas utiliser**  | 2020-12-08 | Libre 14 jours US, Libre 2 EU                 | 2.65MB            |
| OOP2 1.2 (8a0ee8f) - **ne pas utiliser** | 2022-06-10 | Libre 14 jours US (ancien), Libre 2 EU        | 2.66MB            |
| OOP2_e6 (6de6678) - **ne pas utiliser**  | 2023-01-10 | Libre 14 jours US (nouveau), Libre 2 EU       | 2.66MB            |
| OOP2_more (27da3f5)                 | 2023-05-25      | Libre 14 jours US (nouveau), Libre 2 EU (nouveau) | 2.66MB        |
| OOP2_c6_09_31 (27da3f5)             | 2024-05-31      | Libre 14 jours US, Libre 2/2+ EU              | 2.7MB             |
| OOP2-7f0e31 (27da3f5)               | 2025-06-12      | Libre 14 jours US, Libre 2/2+ EU              | 2.73MB            |
| **OOP2-21_9_25 (05d1989)**          | **2025-09-21**  | **Libre 14 jours US, Libre 2/2+ EU**          | **2.73MB**        |

### Détection automatique {#auto-detection}

Certaines anciennes versions de xDrip détectent la présence ou la nécessité de l'algorithme hors processus.

Activez-le <u>uniquement</u> pour OOP1.  
**Ne l'activez pas pour OOP2**. Si vous l'avez activé par erreur : [désactivez](./misc#out-of-process-algorithm) OOP1.

<img src="./images/OOP_AD.png" style="zoom:75%;" />

### Paramètres {#settings}

Use service correspond à l'activation ou la désactivation de l'application OOP. Si vous voulez l'utiliser, cette option doit être activée.

<img src="./images/OOP_UI1.png" style="zoom:75%;" />

Foreground service est un complément qui réduit le risque que l'application soit mise en veille par le téléphone. Cela n'empêchera pas Google Play Protect de l'arrêter.  
Activez-le si vous perdez des données (**recommandé**).

<img src="./images/OOP_UI2.png" style="zoom:75%;" />

Direct intent peut être activé si votre montre Wear OS autonome le nécessite (transmetteur nécessaire).

<img src="./images/OOP_UI4.png" style="zoom:75%;" />

Vous pouvez choisir la période à laquelle OOP vérifie qu'il est disponible.  
En cas de perte de données, vous pouvez réduire l'intervalle. Plus l'intervalle est court, plus la consommation de batterie est élevée.

<img src="./images/OOP_UI3.png" style="zoom:75%;" />

<br>

[*Dernière modification le 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
