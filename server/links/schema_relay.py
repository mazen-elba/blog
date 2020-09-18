import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link, Vote

# Relay QUERIES


class LinkFilter(django_filters.FilterSet):
    # 1) define a FilterSet
    class Meta:
        model = Link
        fields = ['url', 'description']


class LinkNode(DjangoObjectType):
    # 2) create nodes from exposed data
    class Meta:
        model = Link
        # 3) each node implementats an interface w/unique ID
        interfaces = (graphene.relay.Node, )


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
    # 4) use nodes w/relay_link field inside new query
    relay_link = graphene.relay.Node.Field(LinkNode)
    # 5) implement pagination structure -> defines multiple relay links field as a connection
    relay_links = DjangoFilterConnectionField(
        LinkNode, filterset_class=LinkFilter)

# Relay MUTATIONS


class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get('url'),
            description=input.get('description'),
            posted_by=user,
        )
        link.save()

        return RelayCreateLink(link=link)


class RelayMutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()
