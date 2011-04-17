from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True, unique=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))

    class Meta:
        db_table = 'wiki_page'
        verbose_name = _('wiki page')
        verbose_name_plural = _('wiki pages')
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url
