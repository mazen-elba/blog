import graphene
import blog.schema


QUERIES = (
    # Place all future query classes here.
    blog.schema.Query,
)


class Query(*QUERIES):
    """Top level query class that inherits from all others."""
    pass


schema = graphene.Schema(query=Query)
