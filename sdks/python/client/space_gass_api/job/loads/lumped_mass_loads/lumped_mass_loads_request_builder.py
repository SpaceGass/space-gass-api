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
    from ....models.lumped_mass_load import LumpedMassLoad
    from ....models.lumped_mass_load_create import LumpedMassLoadCreate
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_case_key_item_request_builder import WithCaseKeyItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class LumpedMassLoadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/lumped-mass-loads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LumpedMassLoadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/lumped-mass-loads{?Cases*,Limit*,LoadCategory*,Nodes*,Offset*}", path_parameters)
    
    def by_case_key(self,case_key: int) -> WithCaseKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.lumpedMassLoads.item collection
        param case_key: The load case number
        Returns: WithCaseKeyItemRequestBuilder
        """
        if case_key is None:
            raise TypeError("case_key cannot be null.")
        from .item.with_case_key_item_request_builder import WithCaseKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseKey"] = case_key
        return WithCaseKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LumpedMassLoadsRequestBuilderGetQueryParameters]] = None) -> Optional[list[LumpedMassLoad]]:
        """
        Gets all loads with optional filtering and pagination.Use the 'cases' query parameter to filter by specific load cases.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LumpedMassLoad]]
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
        from ....models.lumped_mass_load import LumpedMassLoad

        return await self.request_adapter.send_collection_async(request_info, LumpedMassLoad, error_mapping)
    
    async def post(self,body: LumpedMassLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LumpedMassLoad]:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new lumped mass load.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LumpedMassLoad]
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
            "404": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.lumped_mass_load import LumpedMassLoad

        return await self.request_adapter.send_async(request_info, LumpedMassLoad, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LumpedMassLoadsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all loads with optional filtering and pagination.Use the 'cases' query parameter to filter by specific load cases.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LumpedMassLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new lumped mass load.
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
    
    def with_url(self,raw_url: str) -> LumpedMassLoadsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LumpedMassLoadsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LumpedMassLoadsRequestBuilder(self.request_adapter, raw_url)
    
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
    class LumpedMassLoadsRequestBuilderGetQueryParameters():
        """
        Gets all loads with optional filtering and pagination.Use the 'cases' query parameter to filter by specific load cases.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity key ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
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
            if original_name == "limit":
                return "Limit"
            if original_name == "load_category":
                return "LoadCategory"
            if original_name == "nodes":
                return "Nodes"
            if original_name == "offset":
                return "Offset"
            return original_name
        
        # Load case numbers to filter by (e.g., ?cases=1&cases=5&cases=10).Returns only loads belonging to the specified cases.Omit to return loads for all cases.
        cases: Optional[list[int]] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by load category number.Returns only loads assigned to the specified category.
        load_category: Optional[int] = None

        # Node numbers to filter by (e.g., ?nodes=1&nodes=5&nodes=10).Returns only lumped masses applied to the specified nodes.Omit to return lumped masses for all nodes.
        nodes: Optional[list[int]] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class LumpedMassLoadsRequestBuilderGetRequestConfiguration(RequestConfiguration[LumpedMassLoadsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LumpedMassLoadsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

