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
    from .....models.expand_option import ExpandOption
    from .....models.node import Node
    from .....models.node_update import NodeUpdate
    from .....models.problem_details import ProblemDetails
    from .constraint.constraint_request_builder import ConstraintRequestBuilder
    from .restraint.restraint_request_builder import RestraintRequestBuilder

class NodesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/nodes/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NodesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/nodes/{id}{?Expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[NodesItemRequestBuilderGetQueryParameters]] = None) -> Optional[Node]:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Entities without sub-resources ignore the parameter            — overriding M:SpaceGassApi.Controllers.Entity.EntityControllerBase`4.HydrateSingle(`0,SpaceGassApi.Models.Enums.ExpandOption) opts in.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Node]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node import Node

        return await self.request_adapter.send_async(request_info, Node, error_mapping)
    
    async def patch(self,body: NodeUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Node]:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for updating an existing node.All coordinate fields are optional to support partial updates.Id is inherited from EntityUpdateBaseDto - nullable because single updatesreceive the Id from the route, while batch updates include it in the body.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Node]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node import Node

        return await self.request_adapter.send_async(request_info, Node, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NodesItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Entities without sub-resources ignore the parameter            — overriding M:SpaceGassApi.Controllers.Entity.EntityControllerBase`4.HydrateSingle(`0,SpaceGassApi.Models.Enums.ExpandOption) opts in.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: NodeUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for updating an existing node.All coordinate fields are optional to support partial updates.Id is inherited from EntityUpdateBaseDto - nullable because single updatesreceive the Id from the route, while batch updates include it in the body.
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
    
    def with_url(self,raw_url: str) -> NodesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NodesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NodesItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def constraint(self) -> ConstraintRequestBuilder:
        """
        The constraint property
        """
        from .constraint.constraint_request_builder import ConstraintRequestBuilder

        return ConstraintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restraint(self) -> RestraintRequestBuilder:
        """
        The restraint property
        """
        from .restraint.restraint_request_builder import RestraintRequestBuilder

        return RestraintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NodesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NodesItemRequestBuilderGetQueryParameters():
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Entities without sub-resources ignore the parameter            — overriding M:SpaceGassApi.Controllers.Entity.EntityControllerBase`4.HydrateSingle(`0,SpaceGassApi.Models.Enums.ExpandOption) opts in.
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
            return original_name
        
        # Sub-resource expansion. Defaults to `all`; pass `none` to suppress sub-resource hydration.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class NodesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[NodesItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NodesItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

