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
    from .....models.error_response import ErrorResponse
    from .....models.moving_load_generate_request import MovingLoadGenerateRequest
    from .....models.moving_load_generation_result import MovingLoadGenerationResult

class GenerateRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads/generate
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GenerateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads/generate", path_parameters)
    
    async def post(self,body: MovingLoadGenerateRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MovingLoadGenerationResult]:
        """
        Validates the moving-load data and runs the generator synchronously, returning thegenerated load cases and selection groups. Validation runs as part of the call (there isno separate validate endpoint); a request whose data fails validation — or that suppliesan unknown `loadCategory` — is rejected with `400` before the engine runs.Generation is selective by each scenario's `include` flag — included scenarios are(re)generated and excluded scenarios keep their previously-generated results.            Generation serializes against analysis through the shared engine: a request is rejectedwith `409` while another generation run or an analysis is already in progress. Thegenerated load cases are also readable through `GET /job/loads/load-cases`.            Supply `loadCategory` in the request body to tag every generated load case with anexisting load category (create it first via `POST /job/loads/load-categories`). Thebody is optional — omit it (or omit `loadCategory`) and the API reuses or creates adefault "Moving loads" category.
        param body: Optional request body for `POST moving-loads/generate`. The body itself is optional —omit it entirely to generate with the default load category.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadGenerationResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.moving_load_generation_result import MovingLoadGenerationResult

        return await self.request_adapter.send_async(request_info, MovingLoadGenerationResult, error_mapping)
    
    def to_post_request_information(self,body: MovingLoadGenerateRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Validates the moving-load data and runs the generator synchronously, returning thegenerated load cases and selection groups. Validation runs as part of the call (there isno separate validate endpoint); a request whose data fails validation — or that suppliesan unknown `loadCategory` — is rejected with `400` before the engine runs.Generation is selective by each scenario's `include` flag — included scenarios are(re)generated and excluded scenarios keep their previously-generated results.            Generation serializes against analysis through the shared engine: a request is rejectedwith `409` while another generation run or an analysis is already in progress. Thegenerated load cases are also readable through `GET /job/loads/load-cases`.            Supply `loadCategory` in the request body to tag every generated load case with anexisting load category (create it first via `POST /job/loads/load-categories`). Thebody is optional — omit it (or omit `loadCategory`) and the API reuses or creates adefault "Moving loads" category.
        param body: Optional request body for `POST moving-loads/generate`. The body itself is optional —omit it entirely to generate with the default load category.
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
    
    def with_url(self,raw_url: str) -> GenerateRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GenerateRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GenerateRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GenerateRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

