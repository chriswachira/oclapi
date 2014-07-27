from haystack import indexes
from users.models import UserProfile

__author__ = 'misternando'


class UserProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='user__username', indexed=True, stored=True)
    company = indexes.CharField(model_attr='company', null=True, indexed=True, stored=True)
    location = indexes.CharField(model_attr='location', null=True, indexed=True, stored=True)

    def get_model(self):
        return UserProfile