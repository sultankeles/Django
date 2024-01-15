from django.contrib import admin
from .models import Product, Review


from django.utils import timezone
from django.utils.safestring import mark_safe




admin.site.site_title = 'Cosmios Title'
admin.site.site_header = 'Cosmios Admin Portal'
admin.site.index_title = 'Welcome to Cosmios Admin Portal'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ('collapse',)


class ProductAdmin(admin.ModelAdmin):
    inlines = (ReviewInline,)
    list_display = ('name', 'create_date', 'is_in', 'update_date', 'added_days_go', 'how_many_review', 'bring_img_to_list')
    list_editable = ('is_in',)
    list_display_links = ('create_date',)
    list_filter = ('is_in', 'create_date')
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 25
    date_hierarchy = 'update_date'
    readonly_fields = ('bring_images',)

    # fields =(('name', 'slug'), 'description', 'is_in')

    fieldsets = (
        ('ÜRÜN BİLGİSİ',{
            'fields':(
                ('name', 'slug'), 'is_in'
            )
        }),
        ('Optionals Settings', {
            'classes': ('collapse',),
            'fields': ('description', 'bring_images', 'image'),
            'description': 'You can use this section for optionals settings.'
        })
    )

    actions = ('is_in',)

    def is_in(self, request, queryset):
        count = queryset.update(is_in=True)
        self.message_user(request, f'{count} çeşit ürün stoğa eklendi.')

    is_in.short_description = 'İşaretlenen ürünleri stoğa ekle'

    def added_days_go(self, product):
        fark = timezone.now() - product.create_date
        return fark.days

    def how_many_review(self, obj):
        count = obj.reviews.count()
        return count
    
    def bring_images(self, obj):
        if obj.images:
            return mark_safe(f'<img src={obj.image.url} width=450 height=600></img>')
        return mark_safe(f'<h3>{obj.name} has not image </h3>')
    
    def bring_img_to_list(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=35 height=50></img>')
        return mark_safe('********')
    
    bring_img_to_list.short_description = 'image'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)




admin.site.register(Product,ProductAdmin)
admin.site.register(Review)