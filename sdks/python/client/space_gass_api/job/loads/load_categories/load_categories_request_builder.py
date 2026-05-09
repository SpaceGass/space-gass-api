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
    from ....models.expand_option import ExpandOption
    from ....models.load_category import LoadCategory
    from ....models.load_category_create import LoadCategoryCreate
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.load_categories_item_request_builder import LoadCategoriesItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class LoadCategoriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/load-categories
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LoadCategoriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/load-categories{?Categories*,Expand*,Limit*,Offset*,TitleSearch*}", path_parameters)
    
    def by_id(self,id: int) -> LoadCategoriesItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.loadCategories.item collection
        param id: The entity Id
        Returns: LoadCategoriesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.load_categories_item_request_builder import LoadCategoriesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return LoadCategoriesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        categories: Optional[str] = None,
        expand: Optional[ExpandOption] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        title_search: Optional[str] = None,
    ) -> Optional[list[LoadCategory]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[LoadCategoriesRequestBuilderGetQueryParameters]] = None) -> Optional[list[LoadCategory]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[LoadCategoriesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[LoadCategory]]:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LoadCategory]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.load_category import LoadCategory

        return await self.request_adapter.send_collection_async(request_info, LoadCategory, None)
    
    async def post(self,body: LoadCategoryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LoadCategory]:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new load category.Read-only fields (Source, Version, Username) are excluded.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCategory]
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
        from ....models.load_category import LoadCategory

        return await self.request_adapter.send_async(request_info, LoadCategory, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LoadCategoriesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LoadCategoryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new load category.Read-only fields (Source, Version, Username) are excluded.
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
    
    def with_url(self,raw_url: str) -> LoadCategoriesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LoadCategoriesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LoadCategoriesRequestBuilder(self.request_adapter, raw_url)
    
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
    class LoadCategoriesRequestBuilderGetQueryParameters():
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
            if original_name == "categories":
                return "Categories"
            if original_name == "expand":
                return "Expand"
            if original_name == "limit":
                return "Limit"
            if original_name == "offset":
                return "Offset"
            if original_name == "title_search":
                return "TitleSearch"
            return original_name
        
        # Category Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all categories.
        categories: Optional[str] = None

        # Sub-resource expansion. Defaults to `none`; pass `all` to hydrate sub-resources.
        expand: Optional[ExpandOption] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Search text to filter by title (case-insensitive contains).
        title_search: Optional[str] = None

    
    @dataclass
    class LoadCategoriesRequestBuilderGetRequestConfiguration(RequestConfiguration[LoadCategoriesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LoadCategoriesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

