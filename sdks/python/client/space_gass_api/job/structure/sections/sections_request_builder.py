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
    from ....models.problem_details import ProblemDetails
    from ....models.section import Section
    from ....models.section_create import SectionCreate
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_key_item_request_builder import WithKeyItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class SectionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/sections
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SectionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/sections{?Limit*,Offset*,Sections*}", path_parameters)
    
    def by_key(self,key: int) -> WithKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.structure.sections.item collection
        param key: The entity key
        Returns: WithKeyItemRequestBuilder
        """
        if key is None:
            raise TypeError("key cannot be null.")
        from .item.with_key_item_request_builder import WithKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["key"] = key
        return WithKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SectionsRequestBuilderGetQueryParameters]] = None) -> Optional[list[Section]]:
        """
        Gets all items with optional filtering and pagination.Results are always sorted by Key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Section]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.section import Section

        return await self.request_adapter.send_collection_async(request_info, Section, error_mapping)
    
    async def post(self,body: SectionCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Section]:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new user-defined section.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Section]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.section import Section

        return await self.request_adapter.send_async(request_info, Section, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SectionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all items with optional filtering and pagination.Results are always sorted by Key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SectionCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new user-defined section.
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
    
    def with_url(self,raw_url: str) -> SectionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SectionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SectionsRequestBuilder(self.request_adapter, raw_url)
    
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
    
    @property
    def next(self) -> NextRequestBuilder:
        """
        The next property
        """
        from .next.next_request_builder import NextRequestBuilder

        return NextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SectionsRequestBuilderGetQueryParameters():
        """
        Gets all items with optional filtering and pagination.Results are always sorted by Key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
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
            if original_name == "offset":
                return "Offset"
            if original_name == "sections":
                return "Sections"
            return original_name
        
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Comma-separated list of specific section numbers (e.g., "1,5,10").
        sections: Optional[str] = None

    
    @dataclass
    class SectionsRequestBuilderGetRequestConfiguration(RequestConfiguration[SectionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SectionsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

