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
    from ....models.member_prestress_load import MemberPrestressLoad
    from ....models.member_prestress_load_create import MemberPrestressLoadCreate
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_case_item_request_builder import WithCaseItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberPrestressLoadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/member-prestress-loads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberPrestressLoadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/member-prestress-loads{?Cases*,Limit*,LoadCategory*,Members*,Offset*}", path_parameters)
    
    def by_case_id(self,case_id: int) -> WithCaseItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.memberPrestressLoads.item collection
        param case_id: The load case number
        Returns: WithCaseItemRequestBuilder
        """
        if case_id is None:
            raise TypeError("case_id cannot be null.")
        from .item.with_case_item_request_builder import WithCaseItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseId"] = case_id
        return WithCaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberPrestressLoadsRequestBuilderGetQueryParameters]] = None) -> Optional[list[MemberPrestressLoad]]:
        """
        Gets all loads with optional filtering and pagination.Use the `cases` query parameter to filter by load cases — accepts SG list format(e.g. `"1,3-7,10"`). Omit any list filter to match all.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[MemberPrestressLoad]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.member_prestress_load import MemberPrestressLoad

        return await self.request_adapter.send_collection_async(request_info, MemberPrestressLoad, error_mapping)
    
    async def post(self,body: MemberPrestressLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new member prestress load.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberPrestressLoadsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all loads with optional filtering and pagination.Use the `cases` query parameter to filter by load cases — accepts SG list format(e.g. `"1,3-7,10"`). Omit any list filter to match all.Returns an empty array when no loads match the filter — never 404.Results are sorted by Case ascending, then by entity Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: MemberPrestressLoadCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new load. The load case must exist and be a Primary load case.
        param body: DTO for creating a new member prestress load.
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
    
    def with_url(self,raw_url: str) -> MemberPrestressLoadsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberPrestressLoadsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberPrestressLoadsRequestBuilder(self.request_adapter, raw_url)
    
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
    class MemberPrestressLoadsRequestBuilderGetQueryParameters():
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
            if original_name == "members":
                return "Members"
            if original_name == "offset":
                return "Offset"
            return original_name
        
        # Load cases to filter by, in SG list format (e.g. `"1,3-7,10"`).Returns only loads belonging to the specified cases.Omit to return loads for all cases.
        cases: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by load category number.Returns only loads assigned to the specified category.
        load_category: Optional[int] = None

        # Member Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Returns only prestress loads applied to the specified members.Omit to return prestress loads for all members.
        members: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class MemberPrestressLoadsRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberPrestressLoadsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MemberPrestressLoadsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

