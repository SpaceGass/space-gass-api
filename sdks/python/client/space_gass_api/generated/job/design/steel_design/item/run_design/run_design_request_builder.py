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
    from ......models.design_run import DesignRun
    from ......models.error_response import ErrorResponse
    from ......models.steel_design_run_design_request import SteelDesignRunDesignRequest

class RunDesignRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design/steel-design/{code}/run-design
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RunDesignRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design/steel-design/{code}/run-design", path_parameters)
    
    async def post(self,body: SteelDesignRunDesignRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DesignRun]:
        """
        Starts a steel member DESIGN run for a design code — selects sections for themembers from the candidate sections and section libraries in the designsettings. The run executes asynchronously; poll GET /job/design/runs/{runId}.            By default (updateSections true) the run then updates the members' analysissections to the selected sizes and, as the design iteration settings(GET /job/design/steel-design/design-iteration-settings) direct, re-runs the static andbuckling analyses and the design, iterating until the analysis and designsections match. The run's iterations, analysisRerun and warnings report whathappened. With updateSections false the run designs only.            When the job has buckling results and the run re-runs the static analysis,the run re-runs the buckling analysis as well (the re-design needs currentbuckling results); rerunBucklingAnalysis is stored as true for it. Theanalyses re-run with the job's analysis settings, so their solver must beone the API supports (see POST /job/analysis/static/run-linear).            Requires static analysis results and at least one steel member designgroup. The request body is optional; supplied settings, codeSettings anddesignIterationSettings are written to the job's stored settings before therun starts, and remain stored after it.
        param body: Request body for POST /job/design/steel-design/{code}/run-design.The body is optional. Supplied settings are written to the job's storedsettings before the run starts, and remain stored after it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DesignRun]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
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
        from ......models.design_run import DesignRun

        return await self.request_adapter.send_async(request_info, DesignRun, error_mapping)
    
    def to_post_request_information(self,body: SteelDesignRunDesignRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Starts a steel member DESIGN run for a design code — selects sections for themembers from the candidate sections and section libraries in the designsettings. The run executes asynchronously; poll GET /job/design/runs/{runId}.            By default (updateSections true) the run then updates the members' analysissections to the selected sizes and, as the design iteration settings(GET /job/design/steel-design/design-iteration-settings) direct, re-runs the static andbuckling analyses and the design, iterating until the analysis and designsections match. The run's iterations, analysisRerun and warnings report whathappened. With updateSections false the run designs only.            When the job has buckling results and the run re-runs the static analysis,the run re-runs the buckling analysis as well (the re-design needs currentbuckling results); rerunBucklingAnalysis is stored as true for it. Theanalyses re-run with the job's analysis settings, so their solver must beone the API supports (see POST /job/analysis/static/run-linear).            Requires static analysis results and at least one steel member designgroup. The request body is optional; supplied settings, codeSettings anddesignIterationSettings are written to the job's stored settings before therun starts, and remain stored after it.
        param body: Request body for POST /job/design/steel-design/{code}/run-design.The body is optional. Supplied settings are written to the job's storedsettings before the run starts, and remain stored after it.
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
    
    def with_url(self,raw_url: str) -> RunDesignRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RunDesignRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RunDesignRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RunDesignRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

