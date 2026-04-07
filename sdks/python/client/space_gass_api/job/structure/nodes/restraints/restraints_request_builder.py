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
    from .....models.node_restraint import NodeRestraint
    from .....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder

class RestraintsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/nodes/restraints
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RestraintsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/nodes/restraints{?nodes*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RestraintsRequestBuilderGetQueryParameters]] = None) -> Optional[list[NodeRestraint]]:
        """
        Returns all nodes that have explicit restraint rows defined.Nodes without a restraint row use default values (all DOFs free, no spring stiffness).Use GET /{key}/restraint to retrieve defaults for any node.Optionally filter by node numbers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[NodeRestraint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node_restraint import NodeRestraint

        return await self.request_adapter.send_collection_async(request_info, NodeRestraint, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RestraintsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all nodes that have explicit restraint rows defined.Nodes without a restraint row use default values (all DOFs free, no spring stiffness).Use GET /{key}/restraint to retrieve defaults for any node.Optionally filter by node numbers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> RestraintsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RestraintsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RestraintsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RestraintsRequestBuilderGetQueryParameters():
        """
        Returns all nodes that have explicit restraint rows defined.Nodes without a restraint row use default values (all DOFs free, no spring stiffness).Use GET /{key}/restraint to retrieve defaults for any node.Optionally filter by node numbers.
        """
        # Comma-separated list of node numbers to filter by (e.g., "1,5,10"). Omit to return all.
        nodes: Optional[str] = None

    
    @dataclass
    class RestraintsRequestBuilderGetRequestConfiguration(RequestConfiguration[RestraintsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

