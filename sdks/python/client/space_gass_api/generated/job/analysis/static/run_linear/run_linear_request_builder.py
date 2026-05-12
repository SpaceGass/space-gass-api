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
    from .....models.analysis_run import AnalysisRun
    from .....models.error_response import ErrorResponse
    from .....models.static_settings_update import StaticSettingsUpdate

class RunLinearRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/analysis/static/run-linear
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RunLinearRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/analysis/static/run-linear", path_parameters)
    
    async def post(self,body: StaticSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AnalysisRun]:
        """
        Starts a Linear Static Analysis run. The analysis executes asynchronously in the background.Poll the returned status URL to track progress. Only one analysis can run at a time.            The request body is optional. If provided, only fields included are applied as settingoverrides before the analysis starts; omitted fields remain unchanged.If omitted, the analysis runs with the current job settings as-is.            Once complete, results are available via the query endpoints(e.g., GET /api/v1/job/query/analysis/static/node-reactions).
        param body: Update request for Static Analysis settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /static/settings and the POST run endpoints.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AnalysisRun]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "409": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.analysis_run import AnalysisRun

        return await self.request_adapter.send_async(request_info, AnalysisRun, error_mapping)
    
    def to_post_request_information(self,body: StaticSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Starts a Linear Static Analysis run. The analysis executes asynchronously in the background.Poll the returned status URL to track progress. Only one analysis can run at a time.            The request body is optional. If provided, only fields included are applied as settingoverrides before the analysis starts; omitted fields remain unchanged.If omitted, the analysis runs with the current job settings as-is.            Once complete, results are available via the query endpoints(e.g., GET /api/v1/job/query/analysis/static/node-reactions).
        param body: Update request for Static Analysis settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /static/settings and the POST run endpoints.
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
    
    def with_url(self,raw_url: str) -> RunLinearRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RunLinearRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RunLinearRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RunLinearRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

