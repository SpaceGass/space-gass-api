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
    from ....models.load_case import LoadCase
    from ....models.load_case_create import LoadCaseCreate
    from ....models.load_case_type import LoadCaseType
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.load_cases_item_request_builder import LoadCasesItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class LoadCasesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/load-cases
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LoadCasesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/load-cases{?Cases*,Expand*,Limit*,Offset*,TitleSearch*,Type*}", path_parameters)
    
    def by_id(self,id: int) -> LoadCasesItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.loadCases.item collection
        param id: The load case Id
        Returns: LoadCasesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.load_cases_item_request_builder import LoadCasesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return LoadCasesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        cases: Optional[str] = None,
        expand: Optional[ExpandOption] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        title_search: Optional[str] = None,
        type: Optional[LoadCaseType] = None,
    ) -> Optional[list[LoadCase]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[LoadCasesRequestBuilderGetQueryParameters]] = None) -> Optional[list[LoadCase]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[LoadCasesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[LoadCase]]:
        """
        Returns all load cases in the open job. Type is read-only and computed by SPACE GASSbased on assigned loads (Primary, Combination, Step, Unused). Filter by type, bycase-Id list, or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).Pass `Expand=all` to hydrate `combinationItems` on combination cases (otherwise the`hasCombinationItems` indicator is populated but the array is omitted from the wire).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LoadCase]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.load_case import LoadCase

        return await self.request_adapter.send_collection_async(request_info, LoadCase, None)
    
    async def post(self,body: LoadCaseCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LoadCase]:
        """
        Creates a new load case. The case is initially type `Unused` until loads areassigned to it (or until combination items are added via `POST /combination-load-cases`,which creates the case as type `Combination`).
        param body: DTO for creating a new load case.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
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
        from ....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LoadCasesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all load cases in the open job. Type is read-only and computed by SPACE GASSbased on assigned loads (Primary, Combination, Step, Unused). Filter by type, bycase-Id list, or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).Pass `Expand=all` to hydrate `combinationItems` on combination cases (otherwise the`hasCombinationItems` indicator is populated but the array is omitted from the wire).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LoadCaseCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new load case. The case is initially type `Unused` until loads areassigned to it (or until combination items are added via `POST /combination-load-cases`,which creates the case as type `Combination`).
        param body: DTO for creating a new load case.
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
    
    def with_url(self,raw_url: str) -> LoadCasesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LoadCasesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LoadCasesRequestBuilder(self.request_adapter, raw_url)
    
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
    class LoadCasesRequestBuilderGetQueryParameters():
        """
        Returns all load cases in the open job. Type is read-only and computed by SPACE GASSbased on assigned loads (Primary, Combination, Step, Unused). Filter by type, bycase-Id list, or by title substring. Results are sorted by Id ascending.Pagination metadata is returned in response headers (`Total-Count`, `Offset`, `Limit`).Pass `Expand=all` to hydrate `combinationItems` on combination cases (otherwise the`hasCombinationItems` indicator is populated but the array is omitted from the wire).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "cases":
                return "Cases"
            if original_name == "expand":
                return "Expand"
            if original_name == "limit":
                return "Limit"
            if original_name == "offset":
                return "Offset"
            if original_name == "title_search":
                return "TitleSearch"
            if original_name == "type":
                return "Type"
            return original_name
        
        # Load case Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all load cases.
        cases: Optional[str] = None

        # Sub-resource expansion. Defaults to `none`; pass `all` to hydrate combination items on combination cases.
        expand: Optional[ExpandOption] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Search text to filter by title (case-insensitive contains).
        title_search: Optional[str] = None

        # Filter by load case type (Primary, Combination, Step, Unused).
        type: Optional[LoadCaseType] = None

    
    @dataclass
    class LoadCasesRequestBuilderGetRequestConfiguration(RequestConfiguration[LoadCasesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LoadCasesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

