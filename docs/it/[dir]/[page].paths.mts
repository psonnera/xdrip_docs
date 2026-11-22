// English pages not yet translated: served under /it/ with a notice (see theme/I18nNotice.vue).
import { englishBody, untranslated } from '../../.vitepress/i18n.mts'

export default {
  paths: () =>
    untranslated('it')
      .filter(([dir]) => dir !== '' && !dir.includes('/'))
      .map(([dir, page]) => ({ params: { dir, page }, content: englishBody(`${dir}/${page}.md`) })),
}
