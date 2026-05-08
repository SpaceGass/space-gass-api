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
    from ....models.expand_option import ExpandOption
    from ....models.node import Node
    from ....models.node_create import NodeCreate
    from ....models.node_type_filter import NodeTypeFilter
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .exists.exists_request_builder import ExistsRequestBuilder
    from .item.nodes_item_request_builder import NodesItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .next.next_request_builder import NextRequestBuilder

class NodesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/nodes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NodesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/nodes{?Expand*,Limit*,MaxX*,MaxY*,MaxZ*,MinX*,MinY*,MinZ*,NodeType*,Nodes*,Offset*}", path_parameters)
    
    def by_id(self,id: int) -> NodesItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.structure.nodes.item collection
        param id: The entity Id
        Returns: NodesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.nodes_item_request_builder import NodesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return NodesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[NodesRequestBuilderGetQueryParameters]] = None) -> Optional[list[Node]]:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Node]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.node import Node

        return await self.request_adapter.send_collection_async(request_info, Node, None)
    
    async def post(self,body: NodeCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Node]:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new nodeNode number may be auto-assigned if not provided
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Node]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.node import Node

        return await self.request_adapter.send_async(request_info, Node, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NodesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: NodeCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new item. If a validator is registered, the item is validated before creation.
        param body: DTO for creating a new nodeNode number may be auto-assigned if not provided
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
    
    def with_url(self,raw_url: str) -> NodesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NodesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NodesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exists(self) -> ExistsRequestBuilder:
        """
        The exists property
        """
        from .exists.exists_request_builder import ExistsRequestBuilder

        return ExistsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def next(self) -> NextRequestBuilder:
        """
        The next property
        """
        from .next.next_request_builder import NextRequestBuilder

        return NextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NodesRequestBuilderGetQueryParameters():
        """
        Gets all items with optional filtering, pagination and sub-resource expansion.Results are always sorted by Id ascending.Pagination metadata is returned in response headers (Total-Count, Offset, Limit).`Expand` defaults to `none` on list endpoints so payloads stay lean;pass `Expand=all` to hydrate sub-resources. Sub-resource expansion isopt-in per resource type — resources that don't define sub-resources ignore the parameter.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "Expand"
            if original_name == "limit":
                return "Limit"
            if original_name == "max_x":
                return "MaxX"
            if original_name == "max_y":
                return "MaxY"
            if original_name == "max_z":
                return "MaxZ"
            if original_name == "min_x":
                return "MinX"
            if original_name == "min_y":
                return "MinY"
            if original_name == "min_z":
                return "MinZ"
            if original_name == "nodes":
                return "Nodes"
            if original_name == "node_type":
                return "NodeType"
            if original_name == "offset":
                return "Offset"
            return original_name
        
        # Sub-resource expansion. Defaults to `none`; pass `all` to hydrate sub-resources.
        expand: Optional[ExpandOption] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Maximum X coordinate filter. Unit: Length (see GET /job/units).
        max_x: Optional[float] = None

        # Maximum Y coordinate filter. Unit: Length (see GET /job/units).
        max_y: Optional[float] = None

        # Maximum Z coordinate filter. Unit: Length (see GET /job/units).
        max_z: Optional[float] = None

        # Minimum X coordinate filter. Unit: Length (see GET /job/units).
        min_x: Optional[float] = None

        # Minimum Y coordinate filter. Unit: Length (see GET /job/units).
        min_y: Optional[float] = None

        # Minimum Z coordinate filter. Unit: Length (see GET /job/units).
        min_z: Optional[float] = None

        # Filter by node type (e.g., Restrained). Default is All_Types.
        node_type: Optional[NodeTypeFilter] = None

        # Node Ids to filter by, in SG list format (e.g. `"1,5-10,15"`).Omit to return all nodes.
        nodes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

    
    @dataclass
    class NodesRequestBuilderGetRequestConfiguration(RequestConfiguration[NodesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NodesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

