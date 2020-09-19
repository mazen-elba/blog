import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Link, Vote
from users.schema import UserType

# Adding QUERIES -> fetch data from server


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    # to filter -> add serach parameter inside links field
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        # use pagination to slice queryset
        qs = Link.objects.all()

        # to filter -> value send w/search parameter will be args variable
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        # return Link.objects.filter(filter)
        return qs

        # return Link.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


# Add MUTATIONS -> send data to server


class CreateLink(graphene.Mutation):
    # 1) defines a mutation class
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    # 2) defines data to send to server
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # 3) creates a link in DB (using data sent by user) thru parameters
    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(url=url, description=description, posted_by=user)
        link.save()

        # verifies data matches parameters set
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


class Mutation(graphene.ObjectType):
    # 4) creates a mutation class (w/fields to be resolved)
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
