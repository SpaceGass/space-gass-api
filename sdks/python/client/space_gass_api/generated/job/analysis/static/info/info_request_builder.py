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
    from .....models.analysis_info import AnalysisInfo
    from .....models.error_response import ErrorResponse

class InfoRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/analysis/static/info
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InfoRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/analysis/static/info{?loadCases*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        load_cases: Optional[str] = None,
    ) -> Optional[AnalysisInfo]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[InfoRequestBuilderGetQueryParameters]] = None) -> Optional[AnalysisInfo]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[InfoRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[AnalysisInfo]:
        """
        Returns a lightweight pre-flight summary describing whether static analysisresults are stored for this job and which load cases they cover.Use this before issuing a static results query to decide whether the queryis worth issuing, and to derive a follow-up `POST /static/run-*` bodyfor the cases that still need to be analysed.            `hasResults` is sourced from the result file's header — no datasheet load.Linear and Non-Linear Static share the same result files, so this endpointcovers both modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AnalysisInfo]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.analysis_info import AnalysisInfo

        return await self.request_adapter.send_async(request_info, AnalysisInfo, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InfoRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a lightweight pre-flight summary describing whether static analysisresults are stored for this job and which load cases they cover.Use this before issuing a static results query to decide whether the queryis worth issuing, and to derive a follow-up `POST /static/run-*` bodyfor the cases that still need to be analysed.            `hasResults` is sourced from the result file's header — no datasheet load.Linear and Non-Linear Static share the same result files, so this endpointcovers both modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> InfoRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InfoRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InfoRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InfoRequestBuilderGetQueryParameters():
        """
        Returns a lightweight pre-flight summary describing whether static analysisresults are stored for this job and which load cases they cover.Use this before issuing a static results query to decide whether the queryis worth issuing, and to derive a follow-up `POST /static/run-*` bodyfor the cases that still need to be analysed.            `hasResults` is sourced from the result file's header — no datasheet load.Linear and Non-Linear Static share the same result files, so this endpointcovers both modes.
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
            return original_name
        
        # Optional load case filter in SG list format (e.g. `"1,3-7,10"`).Omit to query against every load case in the model.
        load_cases: Optional[str] = None

    
    @dataclass
    class InfoRequestBuilderGetRequestConfiguration(RequestConfiguration[InfoRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

