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
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_login = graphql_jwt.Verify.Field()
    refresh_login_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
