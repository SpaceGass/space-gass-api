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
    from ...models.job_status import JobStatus
    from ...models.open_job_request import OpenJobRequest
    from ...models.problem_details import ProblemDetails

class OpenRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/open
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OpenRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/open", path_parameters)
    
    async def post(self,body: OpenJobRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[JobStatus]:
        """
        Opens a job from a local .sg file.            If a job is currently open, returns 409 Conflict — close the current job firstusing POST /job/close.            For normal open, omit forceOption (or set to null).If the file has unsaved temporary files from a previous session, provide a forceOption:- OpenPreviousSaved: Discard unsaved changes, open last saved version- OpenUnsavedMostRecent: Preserve unsaved changes, recover from abnormal shutdown            Example request to recover unsaved work:                POST /api/v1/job/open    {      "filePath": "C://path//to//job.sg",      "forceOption": "OpenUnsavedMostRecent"    }
        param body: Request DTO for opening a job file.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[JobStatus]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.job_status import JobStatus

        return await self.request_adapter.send_async(request_info, JobStatus, error_mapping)
    
    def to_post_request_information(self,body: OpenJobRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Opens a job from a local .sg file.            If a job is currently open, returns 409 Conflict — close the current job firstusing POST /job/close.            For normal open, omit forceOption (or set to null).If the file has unsaved temporary files from a previous session, provide a forceOption:- OpenPreviousSaved: Discard unsaved changes, open last saved version- OpenUnsavedMostRecent: Preserve unsaved changes, recover from abnormal shutdown            Example request to recover unsaved work:                POST /api/v1/job/open    {      "filePath": "C://path//to//job.sg",      "forceOption": "OpenUnsavedMostRecent"    }
        param body: Request DTO for opening a job file.
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
    
    def with_url(self,raw_url: str) -> OpenRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OpenRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OpenRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class OpenRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

