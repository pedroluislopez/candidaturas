from django.contrib import admin
from candidatos.models import Candidato
from django.utils.translation import ugettext as _

# Register your models here.
class CandidatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'imagen']}),
        ('Datos personales', {'fields': ['nif', 'telefono']}),
        ('Candidatura', {'fields': ['secretario', 'consejo', 'biografia', 'motivacion', 'youtube']}),
    ]
    list_display = ('get_username', 'get_first_name', 'get_last_name', 'get_email', 'secretario', 'consejo', 'get_date_joined', 'get_is_active')
    list_filter = ['secretario', 'consejo']
    seach_fields = ['get_first_name', 'get_last_name', 'get_email']
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = _('username')
    get_username.admin_order_field = 'user__username'
    
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = _('first name')
    get_first_name.admin_order_field = 'user__first_name'
    
    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = _('last name')
    get_last_name.admin_order_field = 'user__last_name'
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = _('email')
    get_email.admin_order_field = 'user__email'
    
    def get_date_joined(self, obj):
        return obj.user.date_joined
    get_date_joined.short_description = _('date joined')
    get_date_joined.admin_order_field = 'user__date_joined'
    
    def get_is_active(self, obj):
        return obj.user.is_active
    get_is_active.short_description = _('active')
    get_is_active.admin_order_field = 'user__is_active'

admin.site.register(Candidato, CandidatoAdmin)
