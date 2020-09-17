import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from blog.models import BlogPost


class PostType(DjangoObjectType):
    """Defines a graphql type for our blogpost."""
    class Meta:
        model = BlogPost
        filter_fields = ['author', 'title']
        interfaces = (graphene.Node, )


class Query(graphene.ObjectType):
    """Create the main query interface."""
    posts = DjangoFilterConnectionField(PostType)

    def resolve_posts(self, info, **kwargs):
        return BlogPost.objects.all()
