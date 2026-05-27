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
    from .....models.node_restraint import NodeRestraint
    from .....models.set_general_restraint_request import SetGeneralRestraintRequest

class SetGeneralRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/node-restraints/set-general
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SetGeneralRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/node-restraints/set-general", path_parameters)
    
    async def post(self,body: SetGeneralRestraintRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NodeRestraint]:
        """
        Promotes a single node as the general restraint and atomically demotes every other row.Pass `node = N` to set node N as the general restraint;pass `node = null` to clear the flag from every node so no general restraint is set.            At most one node can be the general restraint at any time. The target node must alreadyhave a restraint row — use `POST /node-restraints` to create one first.            To observe which node (if any) is currently the general restraint, read`generalRestraint` on the node restraint DTO via `GET /node-restraints` or`GET /node-restraints/{nodeId}`.
        param body: Request body for `POST job/structure/node-restraints/set-general`.Provide a node Id to promote that node as the general restraint(demoting every other row); pass `null` to clear the flag from every node.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeRestraint]
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
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.node_restraint import NodeRestraint

        return await self.request_adapter.send_async(request_info, NodeRestraint, error_mapping)
    
    def to_post_request_information(self,body: SetGeneralRestraintRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Promotes a single node as the general restraint and atomically demotes every other row.Pass `node = N` to set node N as the general restraint;pass `node = null` to clear the flag from every node so no general restraint is set.            At most one node can be the general restraint at any time. The target node must alreadyhave a restraint row — use `POST /node-restraints` to create one first.            To observe which node (if any) is currently the general restraint, read`generalRestraint` on the node restraint DTO via `GET /node-restraints` or`GET /node-restraints/{nodeId}`.
        param body: Request body for `POST job/structure/node-restraints/set-general`.Provide a node Id to promote that node as the general restraint(demoting every other row); pass `null` to clear the flag from every node.
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
    
    def with_url(self,raw_url: str) -> SetGeneralRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SetGeneralRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SetGeneralRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SetGeneralRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

