import graphene
import graphql_jwt

import links.schema
import users.schema


class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    # fetches data from server
    pass


class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    # sends data to server
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
