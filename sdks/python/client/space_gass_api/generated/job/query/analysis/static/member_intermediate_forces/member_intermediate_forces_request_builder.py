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
    from ......models.error_response import ErrorResponse
    from ......models.member_intermediate_force_query_result import MemberIntermediateForceQueryResult
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberIntermediateForcesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/member-intermediate-forces
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberIntermediateForcesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/member-intermediate-forces{?Limit*,Offset*,loadCases*,members*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        members: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Optional[MemberIntermediateForceQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberIntermediateForcesRequestBuilderGetQueryParameters]] = None) -> Optional[MemberIntermediateForceQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberIntermediateForcesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[MemberIntermediateForceQueryResult]:
        """
        Gets intermediate force results for members, grouped by load case and member.Each result contains force values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberIntermediateForceQueryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.member_intermediate_force_query_result import MemberIntermediateForceQueryResult

        return await self.request_adapter.send_async(request_info, MemberIntermediateForceQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberIntermediateForcesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets intermediate force results for members, grouped by load case and member.Each result contains force values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MemberIntermediateForcesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberIntermediateForcesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberIntermediateForcesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberIntermediateForcesRequestBuilderGetQueryParameters():
        """
        Gets intermediate force results for members, grouped by load case and member.Each result contains force values at stations along the member.
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
            if original_name == "load_cases":
                return "loadCases"
            if original_name == "offset":
                return "Offset"
            if original_name == "members":
                return "members"
            return original_name
        
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Member Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        members: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class MemberIntermediateForcesRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberIntermediateForcesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

