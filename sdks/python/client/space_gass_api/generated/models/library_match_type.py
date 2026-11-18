from enum import Enum

class LibraryMatchType(str, Enum):
    Exact = "Exact",
    Prefix = "Prefix",
    Contains = "Contains",
    TokenSet = "TokenSet",
    Approximate = "Approximate",
    Fuzzy = "Fuzzy",

