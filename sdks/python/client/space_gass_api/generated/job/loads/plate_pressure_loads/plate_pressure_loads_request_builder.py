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
    from ....models.plate_pressure_load import PlatePressureLoad
    from ....models.plate_pressure_load_create import PlatePressureLoadCreate
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_case_item_request_builder import WithCaseItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class PlatePressureLoadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/plate-pressure-loads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlatePressureLoadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/plate-pressure-loads{?Cases*,Limit*,LoadCategory*,Offset*,Plates*}", path_parameters)
    
    def by_case_id(self,case_id: int) -> WithCaseItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.platePressureLoads.item collection
        param case_id: The load case number
        Returns: WithCaseItemRequestBuilder
        """
        if case_id is None:
            raise TypeError("case_id cannot be null.")
        from .item.with_case_item_request_builder import WithCaseItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseId"] = case_id
        return WithCaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        cases: Optional[str] = None,
        limit: Optional[int] = None,
        load_category: Optional[int] = None,
        offset: Optional[int] = None,
        plates: Optional[str] = None,
    ) -> Optional[list[PlatePressureLoad]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PlatePressureLoadsRequestBuilderGetQueryParameters]] = None) -> Optional[list[PlatePressureLoad]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PlatePressureLoadsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[PlatePressureLoad]]:
        """
        Gets all loads with optional filtering and pagination.Use the `cases` query parameter to filter by load cases — accepts SG list format(e.g. `"1,3-7,10"`). Omit any list filter to match all.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[PlatePressureLoad]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error_response import ErrorResponse
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.plate_pressure_load import PlatePressureLoad

        return await self.request_adapter.send_collection_async(request_info, PlatePressureLoad, error_mapping)
    
    async def post(self,body: PlatePressureLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new plate pressure load.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error_response import ErrorResponse
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlatePressureLoadsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all loads with optional filtering and pagination.Use the `cases` query parameter to filter by load cases — accepts SG list format(e.g. `"1,3-7,10"`). Omit any list filter to match all.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: PlatePressureLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new plate pressure load.
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
    
    def with_url(self,raw_url: str) -> PlatePressureLoadsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlatePressureLoadsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlatePressureLoadsRequestBuilder(self.request_adapter, raw_url)
    
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
    class PlatePressureLoadsRequestBuilderGetQueryParameters():
        """
        Gets all loads with optional filtering and pagination.Use the `cases` query parameter to filter by load cases — accepts SG list format(e.g. `"1,3-7,10"`). Omit any list filter to match all.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
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
            if original_name == "offset":
                return "Offset"
            if original_name == "plates":
                return "Plates"
            return original_name
        
        # Load cases to filter by, in SG list format (e.g. `"1,3-7,10"`).Returns only loads belonging to the specified cases.Omit to return loads for all cases.
        cases: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by load category number.Returns only loads assigned to the specified category.
        load_category: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Plate Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Returns only pressure loads applied to the specified plates.Omit to return pressure loads for all plates.
        plates: Optional[str] = None

    
    @dataclass
    class PlatePressureLoadsRequestBuilderGetRequestConfiguration(RequestConfiguration[PlatePressureLoadsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlatePressureLoadsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

