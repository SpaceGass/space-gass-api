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
from typing import Any, Optional, TYPE_CHECKING, Union, overload
from warnings import warn

if TYPE_CHECKING:
    from ....models.error_response import ErrorResponse
    from ....models.member_offset import MemberOffset
    from ....models.member_offset_create import MemberOffsetCreate
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_member_item_request_builder import WithMemberItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberOffsetsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/member-offsets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberOffsetsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/member-offsets{?Limit*,Members*,Offset*}", path_parameters)
    
    def by_member_id(self,member_id: int) -> WithMemberItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.structure.memberOffsets.item collection
        param member_id: The member Id
        Returns: WithMemberItemRequestBuilder
        """
        if member_id is None:
            raise TypeError("member_id cannot be null.")
        from .item.with_member_item_request_builder import WithMemberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["memberId"] = member_id
        return WithMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        members: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Optional[list[MemberOffset]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberOffsetsRequestBuilderGetQueryParameters]] = None) -> Optional[list[MemberOffset]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberOffsetsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[MemberOffset]]:
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[MemberOffset]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.member_offset import MemberOffset

        return await self.request_adapter.send_collection_async(request_info, MemberOffset, error_mapping)
    
    async def post(self,body: MemberOffsetCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MemberOffset]:
        """
        Creates a new attribute row. The body must include the parent Id (e.g. `node`, `member`).Returns 409 if a row already exists for the supplied parent — PATCH instead, or DELETE first.Returns 404 if the parent does not exist.
        param body: DTO for creating member offsets. POST is entity-style: 409 if offsets already existfor the supplied member — caller must DELETE first or PATCH instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberOffset]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.member_offset import MemberOffset

        return await self.request_adapter.send_async(request_info, MemberOffset, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberOffsetsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: MemberOffsetCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new attribute row. The body must include the parent Id (e.g. `node`, `member`).Returns 409 if a row already exists for the supplied parent — PATCH instead, or DELETE first.Returns 404 if the parent does not exist.
        param body: DTO for creating member offsets. POST is entity-style: 409 if offsets already existfor the supplied member — caller must DELETE first or PATCH instead.
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
    
    def with_url(self,raw_url: str) -> MemberOffsetsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberOffsetsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberOffsetsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberOffsetsRequestBuilderGetQueryParameters():
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "limit":
                return "Limit"
            if original_name == "members":
                return "Members"
            if original_name == "offset":
                return "Offset"
            return original_name
        
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Member Ids to filter offsets by, in SG list format (e.g. `"1,5-10,15"`).Omit to return all offsets.
        members: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class MemberOffsetsRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberOffsetsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MemberOffsetsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

