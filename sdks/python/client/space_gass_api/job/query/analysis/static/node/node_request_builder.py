from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .displacements.displacements_request_builder import DisplacementsRequestBuilder
    from .reactions.reactions_request_builder import ReactionsRequestBuilder

class NodeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/node
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NodeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/node", path_parameters)
    
    @property
    def displacements(self) -> DisplacementsRequestBuilder:
        """
        The displacements property
        """
        from .displacements.displacements_request_builder import DisplacementsRequestBuilder

        return DisplacementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reactions(self) -> ReactionsRequestBuilder:
        """
        The reactions property
        """
        from .reactions.reactions_request_builder import ReactionsRequestBuilder

        return ReactionsRequestBuilder(self.request_adapter, self.path_parameters)
    

