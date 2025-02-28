APP_SITE_HEADER='Demo Django Admin'
APP_STATIC_JS=('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')
APP_STATIC_CSS={'all': ('my_admin/css/custom.css',)}
APP_STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
APP_LAYOUT_CHOICE = (
        ('list', 'List'),
        ('gird', 'Gird')
    )