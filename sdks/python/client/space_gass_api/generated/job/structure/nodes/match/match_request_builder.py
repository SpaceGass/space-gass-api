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
    from .....models.node_match_request import NodeMatchRequest
    from .....models.node_match_result import NodeMatchResult

class MatchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/nodes/match
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MatchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/nodes/match", path_parameters)
    
    async def post(self,body: NodeMatchRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NodeMatchResult]:
        """
        Finds the node in the job at each of a list of positions, so geometry can be built by positionwithout creating a node on top of an existing one. For each position the response gives thenearest node closer than the tolerance, or none. A position with no node that repeats anearlier position in the same request is reported against that earlier position, so creating onenode for each position that is null in both `node` and `sameAs` adds no coincidentnodes. A position matches here exactly when the SPACE GASS Clean Up tool would merge a node atit with the same tolerance. Writes nothing.
        param body: Positions to match against the nodes in the job.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeMatchResult]
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
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node_match_result import NodeMatchResult

        return await self.request_adapter.send_async(request_info, NodeMatchResult, error_mapping)
    
    def to_post_request_information(self,body: NodeMatchRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Finds the node in the job at each of a list of positions, so geometry can be built by positionwithout creating a node on top of an existing one. For each position the response gives thenearest node closer than the tolerance, or none. A position with no node that repeats anearlier position in the same request is reported against that earlier position, so creating onenode for each position that is null in both `node` and `sameAs` adds no coincidentnodes. A position matches here exactly when the SPACE GASS Clean Up tool would merge a node atit with the same tolerance. Writes nothing.
        param body: Positions to match against the nodes in the job.
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
    
    def with_url(self,raw_url: str) -> MatchRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MatchRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MatchRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MatchRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

