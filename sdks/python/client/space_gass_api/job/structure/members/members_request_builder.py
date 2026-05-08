from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.expand_option import ExpandOption
    from ....models.member import Member
    from ....models.member_create import MemberCreate
    from ....models.member_type import MemberType
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .direction.direction_request_builder import DirectionRequestBuilder
    from .item.members_item_request_builder import MembersItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder
    from .releases.releases_request_builder import ReleasesRequestBuilder

class MembersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/members
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MembersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/members{?Expand*,Limit*,Material*,Members*,Offset*,Section*,Type*}", path_parameters)
    
    def by_id(self,id: int) -> MembersItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.structure.members.item collection
        param id: The entity Id
        Returns: MembersItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.members_item_request_builder import MembersItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return MembersItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MembersRequestBuilderGetQueryParameters]] = None) -> Optional[list[Member]]:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Member]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.member import Member

        return await self.request_adapter.send_collection_async(request_info, Member, None)
    
    async def post(self,body: MemberCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Member]:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new member.NodeA and NodeB are required; all other fields are optional.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Member]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.member import Member

        return await self.request_adapter.send_async(request_info, Member, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MembersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: MemberCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new member.NodeA and NodeB are required; all other fields are optional.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MembersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MembersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MembersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def direction(self) -> DirectionRequestBuilder:
        """
        The direction property
        """
        from .direction.direction_request_builder import DirectionRequestBuilder

        return DirectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def next(self) -> NextRequestBuilder:
        """
        The next property
        """
        from .next.next_request_builder import NextRequestBuilder

        return NextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def releases(self) -> ReleasesRequestBuilder:
        """
        The releases property
        """
        from .releases.releases_request_builder import ReleasesRequestBuilder

        return ReleasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MembersRequestBuilderGetQueryParameters():
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "Expand"
            if original_name == "limit":
                return "Limit"
            if original_name == "material":
                return "Material"
            if original_name == "members":
                return "Members"
            if original_name == "offset":
                return "Offset"
            if original_name == "section":
                return "Section"
            if original_name == "type":
                return "Type"
            return original_name
        
        # Sub-resource expansion. Defaults to `none`; pass `all` to hydrate sub-resources.
        expand: Optional[ExpandOption] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by material number.
        material: Optional[int] = None

        # Member Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all members.
        members: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Filter by section number.
        section: Optional[int] = None

        # Filter by member type (Normal, TensionOnly, CompressionOnly, Cable, Gap, BrittleFuse, PlasticFuse).
        type: Optional[MemberType] = None

    
    @dataclass
    class MembersRequestBuilderGetRequestConfiguration(RequestConfiguration[MembersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MembersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

