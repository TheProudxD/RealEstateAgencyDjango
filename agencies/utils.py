
menu = [{'title': "О сайте", 'url_name': 'about'},
{'title': "Клиенты", 'url_name': 'clients'},
{'title': "Агенты", 'url_name': 'agents'}]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context