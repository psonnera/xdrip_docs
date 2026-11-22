<script setup lang="ts">
// Shown above the content of /fr/ and /it/ pages that are not translated yet (fallback routes)
// or whose English page changed after translation (source_hash mismatch, set in config.mts).
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'

const { frontmatter, page, lang } = useData()

const text = {
  fr: {
    missing: ['Page pas encore traduite', "Cette page n'est pas encore disponible en français : vous lisez la version anglaise."],
    outdated: ['Traduction à mettre à jour', 'La version anglaise de cette page a été modifiée depuis sa traduction. Consultez', 'la version anglaise', 'pour les dernières informations.'],
  },
  it: {
    missing: ['Pagina non ancora tradotta', 'Questa pagina non è ancora disponibile in italiano: stai leggendo la versione inglese.'],
    outdated: ['Traduzione da aggiornare', 'La versione inglese di questa pagina è stata modificata dopo la traduzione. Consulta', 'la versione inglese', 'per le informazioni più recenti.'],
  },
} as const

const t = computed(() => text[lang.value as keyof typeof text])
const kind = computed(() =>
  !t.value || page.value.relativePath.endsWith('changelog.md') ? null
  : frontmatter.value.i18n_fallback ? 'missing'
  : frontmatter.value.i18n_outdated ? 'outdated'
  : null)
const englishUrl = computed(() =>
  withBase('/' + page.value.relativePath.replace(/^(fr|it)\//, '').replace(/\.md$/, '.html')))
</script>

<template>
  <div v-if="kind === 'missing'" class="custom-block info i18n-notice">
    <p class="custom-block-title">{{ t.missing[0] }}</p>
    <p>{{ t.missing[1] }}</p>
  </div>
  <div v-else-if="kind === 'outdated'" class="custom-block warning i18n-notice">
    <p class="custom-block-title">{{ t.outdated[0] }}</p>
    <p>{{ t.outdated[1] }} <a :href="englishUrl">{{ t.outdated[2] }}</a> {{ t.outdated[3] }}</p>
  </div>
</template>
