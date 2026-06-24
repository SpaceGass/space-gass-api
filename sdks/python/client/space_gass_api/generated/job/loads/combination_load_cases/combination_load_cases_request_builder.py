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
    from ....models.combination_load_case_create import CombinationLoadCaseCreate
    from ....models.error_response import ErrorResponse
    from ....models.expand_option import ExpandOption
    from ....models.load_case import LoadCase
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.combination_case_item_request_builder import CombinationCaseItemRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class CombinationLoadCasesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/combination-load-cases
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CombinationLoadCasesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/combination-load-cases{?expand*,limit*,loadCases*,offset*,titleSearch*}", path_parameters)
    
    def by_combination_case_id(self,combination_case_id: int) -> CombinationCaseItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.combinationLoadCases.item collection
        param combination_case_id: The combination load case Id
        Returns: CombinationCaseItemRequestBuilder
        """
        if combination_case_id is None:
            raise TypeError("combination_case_id cannot be null.")
        from .item.combination_case_item_request_builder import CombinationCaseItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["combinationCase%2Did"] = combination_case_id
        return CombinationCaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        offset: Optional[int] = None,
        title_search: Optional[str] = None,
    ) -> Optional[list[LoadCase]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[CombinationLoadCasesRequestBuilderGetQueryParameters]] = None) -> Optional[list[LoadCase]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[CombinationLoadCasesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[LoadCase]]:
        """
        Returns all combination load cases (load cases of type `Combination`) in the open job.Filter by case-Id list or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).`Expand` defaults to `none` on this list endpoint; pass `Expand=all` to hydrateeach case's `combinationItems` array (otherwise `hasCombinationItems` is populatedbut the array is omitted from the wire).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LoadCase]]
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
        from ....models.load_case import LoadCase

        return await self.request_adapter.send_collection_async(request_info, LoadCase, error_mapping)
    
    async def post(self,body: CombinationLoadCaseCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LoadCase]:
        """
        Creates a combination load case (case + items) in a single atomic call. The`combinationItems` list is required and must contain at least one item; onfailure during item creation the parent case row is rolled back so the operation isall-or-nothing. Each component case must exist and be of type Primary, Combinationor Unused (Step cases are rejected); no item may reference the parent case(self-reference); item `case` values must be unique within the request.
        param body: Request payload for creating a combination load case in a single call.Inherits Id, Guid, Title and Notes from SpaceGassApi.Models.Dtos.Entity.Loads.LoadCaseCreateDto and addsa required, non-empty list of combination items.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
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
        from ....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CombinationLoadCasesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all combination load cases (load cases of type `Combination`) in the open job.Filter by case-Id list or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).`Expand` defaults to `none` on this list endpoint; pass `Expand=all` to hydrateeach case's `combinationItems` array (otherwise `hasCombinationItems` is populatedbut the array is omitted from the wire).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CombinationLoadCaseCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a combination load case (case + items) in a single atomic call. The`combinationItems` list is required and must contain at least one item; onfailure during item creation the parent case row is rolled back so the operation isall-or-nothing. Each component case must exist and be of type Primary, Combinationor Unused (Step cases are rejected); no item may reference the parent case(self-reference); item `case` values must be unique within the request.
        param body: Request payload for creating a combination load case in a single call.Inherits Id, Guid, Title and Notes from SpaceGassApi.Models.Dtos.Entity.Loads.LoadCaseCreateDto and addsa required, non-empty list of combination items.
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
    
    def with_url(self,raw_url: str) -> CombinationLoadCasesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CombinationLoadCasesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CombinationLoadCasesRequestBuilder(self.request_adapter, raw_url)
    
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
    class CombinationLoadCasesRequestBuilderGetQueryParameters():
        """
        Returns all combination load cases (load cases of type `Combination`) in the open job.Filter by case-Id list or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).`Expand` defaults to `none` on this list endpoint; pass `Expand=all` to hydrateeach case's `combinationItems` array (otherwise `hasCombinationItems` is populatedbut the array is omitted from the wire).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "load_cases":
                return "loadCases"
            if original_name == "title_search":
                return "titleSearch"
            if original_name == "expand":
                return "expand"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Sub-resource expansion. Defaults to `none`; pass `all` to hydrate combination items.
        expand: Optional[ExpandOption] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Combination case Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all combination cases.
        load_cases: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Search text to filter by title (case-insensitive contains).
        title_search: Optional[str] = None

    
    @dataclass
    class CombinationLoadCasesRequestBuilderGetRequestConfiguration(RequestConfiguration[CombinationLoadCasesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CombinationLoadCasesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

