from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_members.steel_members_request_builder import SteelMembersRequestBuilder

class DesignRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DesignRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design", path_parameters)
    
    @property
    def steel_members(self) -> SteelMembersRequestBuilder:
        """
        The steelMembers property
        """
        from .steel_members.steel_members_request_builder import SteelMembersRequestBuilder

        return SteelMembersRequestBuilder(self.request_adapter, self.path_parameters)
    

