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
    from .....models.node_restraint_update import NodeRestraintUpdate
    from .....models.problem_details import ProblemDetails
    from .table.table_request_builder import TableRequestBuilder

class WithNodeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/node-restraints/{nodeId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithNodeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/node-restraints/{nodeId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the restraint row for a specific node. After deletion the node has no explicitrestraint — it falls back to default behaviour (all DOFs free, no spring stiffness).Returns 404 if no restraint row exists.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NodeRestraint]:
        """
        Gets the restraint for a specific node — boundary conditions and spring stiffness.Returns 404 if no explicit restraint row exists for the node. Variable-stiffnesstables for V-type DOFs are inlined on the response when present.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeRestraint]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node_restraint import NodeRestraint

        return await self.request_adapter.send_async(request_info, NodeRestraint, error_mapping)
    
    async def patch(self,body: NodeRestraintUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NodeRestraint]:
        """
        Partially updates the restraint for a specific node.Only fields included in the request are changed; omitted fields keep their current value.The restraint must already exist — use `POST /node-restraints` to create one.Variable-stiffness tables can be supplied inline; the corresponding restraintCode positionmust be 'V' (after the update is applied).
        param body: DTO for partial updates to a node restraint.Only fields included in the request are updated; omit a field to keep its current value.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeRestraint]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node_restraint import NodeRestraint

        return await self.request_adapter.send_async(request_info, NodeRestraint, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the restraint row for a specific node. After deletion the node has no explicitrestraint — it falls back to default behaviour (all DOFs free, no spring stiffness).Returns 404 if no restraint row exists.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets the restraint for a specific node — boundary conditions and spring stiffness.Returns 404 if no explicit restraint row exists for the node. Variable-stiffnesstables for V-type DOFs are inlined on the response when present.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: NodeRestraintUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates the restraint for a specific node.Only fields included in the request are changed; omitted fields keep their current value.The restraint must already exist — use `POST /node-restraints` to create one.Variable-stiffness tables can be supplied inline; the corresponding restraintCode positionmust be 'V' (after the update is applied).
        param body: DTO for partial updates to a node restraint.Only fields included in the request are updated; omit a field to keep its current value.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithNodeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithNodeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithNodeItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def table(self) -> TableRequestBuilder:
        """
        The table property
        """
        from .table.table_request_builder import TableRequestBuilder

        return TableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithNodeItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithNodeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithNodeItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

