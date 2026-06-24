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
    from ....models.error_response import ErrorResponse
    from ....models.node_constraint import NodeConstraint
    from ....models.node_constraint_create import NodeConstraintCreate
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_node_item_request_builder import WithNodeItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class NodeConstraintsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/node-constraints
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NodeConstraintsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/node-constraints{?limit*,masterNode*,offset*,slaves*}", path_parameters)
    
    def by_node_id(self,node_id: int) -> WithNodeItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.structure.nodeConstraints.item collection
        param node_id: The slave node Id
        Returns: WithNodeItemRequestBuilder
        """
        if node_id is None:
            raise TypeError("node_id cannot be null.")
        from .item.with_node_item_request_builder import WithNodeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["nodeId"] = node_id
        return WithNodeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        master_node: Optional[int] = None,
        offset: Optional[int] = None,
        slaves: Optional[str] = None,
    ) -> Optional[list[NodeConstraint]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[NodeConstraintsRequestBuilderGetQueryParameters]] = None) -> Optional[list[NodeConstraint]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[NodeConstraintsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[NodeConstraint]]:
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[NodeConstraint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.node_constraint import NodeConstraint

        return await self.request_adapter.send_collection_async(request_info, NodeConstraint, error_mapping)
    
    async def post(self,body: NodeConstraintCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NodeConstraint]:
        """
        Creates a new attribute row. The body must include the parent Id (e.g. `node`, `member`).Returns 409 if a row already exists for the supplied parent — PATCH instead, or DELETE first.Returns 404 if the parent does not exist.
        param body: DTO for creating a node constraint. POST is entity-style: 409 if a constraint already existsfor the supplied slave node — caller must DELETE first or PATCH instead.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeConstraint]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.node_constraint import NodeConstraint

        return await self.request_adapter.send_async(request_info, NodeConstraint, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NodeConstraintsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: NodeConstraintCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new attribute row. The body must include the parent Id (e.g. `node`, `member`).Returns 409 if a row already exists for the supplied parent — PATCH instead, or DELETE first.Returns 404 if the parent does not exist.
        param body: DTO for creating a node constraint. POST is entity-style: 409 if a constraint already existsfor the supplied slave node — caller must DELETE first or PATCH instead.
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
    
    def with_url(self,raw_url: str) -> NodeConstraintsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NodeConstraintsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NodeConstraintsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NodeConstraintsRequestBuilderGetQueryParameters():
        """
        Returns all attribute rows for this resource type, with optional filtering.Sorted by parent Id ascending. Pagination metadata is returned in responseheaders (Total-Count, Offset, Limit).
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "master_node":
                return "masterNode"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            if original_name == "slaves":
                return "slaves"
            return original_name
        
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by master node number — returns only constraints whose master node matches.Omit to return constraints regardless of master.
        master_node: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Slave node Ids to filter by, in SG list format (e.g. `"1,5-10,15"`).Omit to return all constraints.
        slaves: Optional[str] = None

    
    @dataclass
    class NodeConstraintsRequestBuilderGetRequestConfiguration(RequestConfiguration[NodeConstraintsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NodeConstraintsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

