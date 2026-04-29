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
    from ........models.problem_details import ProblemDetails
    from ........models.table import Table

class WithDirectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/nodes/{id}/restraint/table/{direction}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithDirectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/nodes/{id}/restraint/table/{direction}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Clears the variable-stiffness table for one DOF on a node restraint(writes Count = 0 — the binary field stays allocated but holds no points).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Table]:
        """
        Returns the variable-stiffness table for one DOF on a node restraint.404 if the node has no restraint row, or if the table for that DOF is empty.Schema metadata (axis labels, units, bounds) is available atGET nodes/restraint/table/{direction}/metadata.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Table]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.table import Table

        return await self.request_adapter.send_async(request_info, Table, error_mapping)
    
    async def post(self,body: Table, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Table]:
        """
        Creates or replaces the variable-stiffness table for one DOF on a node restraint.The node must already have a restraint row (POST /{id}/restraint to create one),and the corresponding character of restraintCode must be 'V'.            Body is a TableDto whose `points` field is a list of 1–15 (x, y) pairs.X is deflection (translational) or rotation (rotational), Y is the spring stiffness.The first point's X must be 0 (the base stiffness anchor); X values must be unique;X and Y must be ≥ 0.            Any `metadata` on the request body is ignored — metadata is server-derivedand exposed via GET /restraint/table/{direction}/metadata.
        param body: A generic 2D data table — row-major, where each row is an array of column values.Reused across the API for any tabular (X, Y, …) data such as restraintvariable-stiffness curves, derived force-vs-deflection views, material curves, etc.Schema (column names, types, units, bounds) is returned by the resource's dedicatedtable-metadata endpoint and is not embedded here.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Table]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ........models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.table import Table

        return await self.request_adapter.send_async(request_info, Table, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Clears the variable-stiffness table for one DOF on a node restraint(writes Count = 0 — the binary field stays allocated but holds no points).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the variable-stiffness table for one DOF on a node restraint.404 if the node has no restraint row, or if the table for that DOF is empty.Schema metadata (axis labels, units, bounds) is available atGET nodes/restraint/table/{direction}/metadata.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Table, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates or replaces the variable-stiffness table for one DOF on a node restraint.The node must already have a restraint row (POST /{id}/restraint to create one),and the corresponding character of restraintCode must be 'V'.            Body is a TableDto whose `points` field is a list of 1–15 (x, y) pairs.X is deflection (translational) or rotation (rotational), Y is the spring stiffness.The first point's X must be 0 (the base stiffness anchor); X values must be unique;X and Y must be ≥ 0.            Any `metadata` on the request body is ignored — metadata is server-derivedand exposed via GET /restraint/table/{direction}/metadata.
        param body: A generic 2D data table — row-major, where each row is an array of column values.Reused across the API for any tabular (X, Y, …) data such as restraintvariable-stiffness curves, derived force-vs-deflection views, material curves, etc.Schema (column names, types, units, bounds) is returned by the resource's dedicatedtable-metadata endpoint and is not embedded here.
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
    
    def with_url(self,raw_url: str) -> WithDirectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithDirectionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithDirectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithDirectionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDirectionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithDirectionItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

