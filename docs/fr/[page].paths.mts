// English pages at the docs root not yet translated: served under /fr/ with a notice.
import { englishBody, untranslated } from '../.vitepress/i18n.mts'

export default {
  paths: () =>
    untranslated('fr')
      .filter(([dir, page]) => dir === '' && page !== 'index')
      .map(([, page]) => ({ params: { page }, content: englishBody(`${page}.md`) })),
}
