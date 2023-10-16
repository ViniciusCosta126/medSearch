from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth',
                    'specialitiesList', 'addressesList')
    empty_value_display = 'Vazio'
    list_filter = ('user__is_active',)
    search_fields = ('user__username',)

    fieldsets = (
        ('Usuario', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialities', 'addresses')
        })
    )

    def birth(self, obj):
        if (obj.birthday):
            return obj.birthday.strftime("%d/%m/%Y")
    birth.empty_value_display = '___/___/_____'

    def specialitiesList(self, obj):
        return [i.name for i in obj.specialities.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]
    
    class Media:
        css = {
            'all':('css/custom.css',)
        }
        js = ('js/custom.js')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
