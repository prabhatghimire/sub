import graphene
import graphql_jwt

import Donor.schema
import accounts.schema


class Query(Donor.schema.Query,
            accounts.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(Donor.schema.Mutation,
               accounts.schema.Mutation,
               graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
