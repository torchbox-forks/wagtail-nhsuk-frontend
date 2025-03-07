from django import template
from wagtailnhsukfrontend.settings.models import HeaderSettings, FooterSettings, FooterSettingsColumns

from wagtail.models import Site

register = template.Library()


@register.inclusion_tag('wagtailnhsukfrontend/header.html', takes_context=True)
def header(context, **kwargs):
    request = context['request']
    site = Site.find_for_request(request)
    header = HeaderSettings.for_site(site)

    return {
        'service_name': header.service_name,
        'service_href': header.service_link.relative_url(site) if header.service_link else '',
        'service_long_name': header.service_long_name,
        'transactional': header.transactional,
        'organisation_name': header.organisation_name,
        'organisation_split_name': header.organisation_split_name,
        'organisation_descriptor': header.organisation_descriptor,
        'organisation_white': header.organisation_white,
        'logo_href': header.logo_link.relative_url(site) if header.logo_link else '',
        'logo_aria': header.logo_aria,
        'logo_custom': header.logo_custom,
        'show_search': header.show_search,
        'search_action': kwargs.get('search_action', None),
        'search_field_name': kwargs.get('search_field_name', None),
        'primary_links': [
            {
                'label': link.label,
                'url': link.page.relative_url(site)
            }
            for link in header.navigation_links.all()
        ],
    }


@register.inclusion_tag("wagtailnhsukfrontend/footer.html", takes_context=True)
def footer(context):
    request = context['request']
    site = Site.find_for_request(request)
    footer = FooterSettings.for_site(site)
    footer_columns = FooterSettingsColumns.for_site(site)

    # Organize column links by column number
    column_links = {1: [], 2: [], 3: [], 4: []}
    if footer_columns.enable_column_footer:
        for link in footer_columns.column_links.all():
            column_links[link.column].append({
                'label': link.link_label,
                'url': link.link_page.url if link.link_page else link.link_url
            })

    return {
        'enable_column_footer': footer_columns.enable_column_footer,
        'primary_links': [
            {
                'label': link.link_label,
                'url': link.link_url
            }
            for link in footer.footer_links.all()
        ],
        'column_links': column_links,
    }
