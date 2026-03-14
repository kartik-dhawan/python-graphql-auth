import strawberry
# `merge_types` used to merge mutations written in different variables
from strawberry.tools import merge_types
from app.auth.mutations import AuthMutations
from app.auth.queries import AuthQueries


# A combination of all mutations, written separately for modularity
mutations = merge_types("Mutation", (AuthMutations,))

# A combination of all queries, written separately for modularity
# () -> is a tuple, hence when a single item is there, we put comma at the end to make it behave like a tuple
queries = merge_types("Query", (AuthQueries,))

# combines all queries & mutation in to schema, which is used by the graphql router
schema = strawberry.Schema(query=queries, mutation=mutations)
