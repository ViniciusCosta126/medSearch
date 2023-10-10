from medicSearch.models import *


class City(models.Model):
    state = models.ForeignKey(
        State, null=True, related_name='state', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.state.name}'
