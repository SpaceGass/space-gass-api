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
    from ...models.error_response import ErrorResponse
    from ...models.expand_option import ExpandOption
    from ...models.filter import Filter
    from ...models.filter_create import FilterCreate
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.filters_item_request_builder import FiltersItemRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class FiltersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/filters
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FiltersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/filters{?Expand*,Filters*,Limit*,Offset*,Search*}", path_parameters)
    
    def by_id(self,id: int) -> FiltersItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.filters.item collection
        param id: The filter Id (1..200).
        Returns: FiltersItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.filters_item_request_builder import FiltersItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return FiltersItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
        filters: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        search: Optional[str] = None,
    ) -> Optional[list[Filter]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[FiltersRequestBuilderGetQueryParameters]] = None) -> Optional[list[Filter]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[FiltersRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[Filter]]:
        """
        Returns all named filters in the open job. Filter by Id list or byname substring (`search`). Results are sorted by Id ascending.Pagination metadata is returned in response headers(`Total-Count`, `Offset`, `Limit`).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Filter]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.filter import Filter

        return await self.request_adapter.send_collection_async(request_info, Filter, error_mapping)
    
    async def post(self,body: FilterCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Filter]:
        """
        Creates a new named filter. At least one sub-filter must beactive (or carry a non-default value) for the filter to be persisted.If `id` is omitted, the next available slot (1..200) is assigned.
        param body: DTO for creating a new filter.At least one sub-filter must be active — a filter with no rows in thedatasheet has no persisted state and cannot be retrieved by Id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Filter]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.filter import Filter

        return await self.request_adapter.send_async(request_info, Filter, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FiltersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all named filters in the open job. Filter by Id list or byname substring (`search`). Results are sorted by Id ascending.Pagination metadata is returned in response headers(`Total-Count`, `Offset`, `Limit`).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: FilterCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new named filter. At least one sub-filter must beactive (or carry a non-default value) for the filter to be persisted.If `id` is omitted, the next available slot (1..200) is assigned.
        param body: DTO for creating a new filter.At least one sub-filter must be active — a filter with no rows in thedatasheet has no persisted state and cannot be retrieved by Id.
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
    
    def with_url(self,raw_url: str) -> FiltersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FiltersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FiltersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        The items property
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class FiltersRequestBuilderGetQueryParameters():
        """
        Returns all named filters in the open job. Filter by Id list or byname substring (`search`). Results are sorted by Id ascending.Pagination metadata is returned in response headers(`Total-Count`, `Offset`, `Limit`).
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
            if original_name == "filters":
                return "Filters"
            if original_name == "limit":
                return "Limit"
            if original_name == "offset":
                return "Offset"
            if original_name == "search":
                return "Search"
            return original_name
        
        # Sub-resource expansion. Filters have no expandable sub-resources in v1; the parameter is accepted for API consistency.
        expand: Optional[ExpandOption] = None

        # Filter Ids to return, in SG list format (e.g. `"1,3-7,10"`).Omit to return all filters.
        filters: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Search text matched case-insensitively against the filter `name`.
        search: Optional[str] = None

    
    @dataclass
    class FiltersRequestBuilderGetRequestConfiguration(RequestConfiguration[FiltersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FiltersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

