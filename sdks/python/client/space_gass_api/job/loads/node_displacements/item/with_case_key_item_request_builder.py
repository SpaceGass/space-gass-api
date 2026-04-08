from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_node_key_item_request_builder import WithNodeKeyItemRequestBuilder

class WithCaseKeyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/node-displacements/{caseKey}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCaseKeyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/node-displacements/{caseKey}", path_parameters)
    
    def by_node_key(self,node_key: int) -> WithNodeKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.nodeDisplacements.item.item collection
        param node_key: The node number
        Returns: WithNodeKeyItemRequestBuilder
        """
        if node_key is None:
            raise TypeError("node_key cannot be null.")
        from .item.with_node_key_item_request_builder import WithNodeKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["nodeKey"] = node_key
        return WithNodeKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

