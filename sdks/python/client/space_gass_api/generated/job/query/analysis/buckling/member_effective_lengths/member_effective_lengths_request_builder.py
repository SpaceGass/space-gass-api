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
    from ......models.buckling_effective_length_query_result import BucklingEffectiveLengthQueryResult
    from ......models.error_response import ErrorResponse
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberEffectiveLengthsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/buckling/member-effective-lengths
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberEffectiveLengthsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/buckling/member-effective-lengths{?limit*,loadCases*,members*,modes*,offset*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        members: Optional[str] = None,
        modes: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Optional[BucklingEffectiveLengthQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None) -> Optional[BucklingEffectiveLengthQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[BucklingEffectiveLengthQueryResult]:
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BucklingEffectiveLengthQueryResult]
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
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.buckling_effective_length_query_result import BucklingEffectiveLengthQueryResult

        return await self.request_adapter.send_async(request_info, BucklingEffectiveLengthQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MemberEffectiveLengthsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberEffectiveLengthsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberEffectiveLengthsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberEffectiveLengthsRequestBuilderGetQueryParameters():
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
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
            if original_name == "limit":
                return "limit"
            if original_name == "members":
                return "members"
            if original_name == "modes":
                return "modes"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Member Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        members: Optional[str] = None

        # Buckling mode numbers in SG list format (e.g. `"1-3"`). Omit to return all.
        modes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class MemberEffectiveLengthsRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

