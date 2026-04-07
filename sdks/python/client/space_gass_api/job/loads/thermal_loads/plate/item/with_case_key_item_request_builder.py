from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_plate_key_item_request_builder import WithPlateKeyItemRequestBuilder

class WithCaseKeyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/thermal-loads/plate/{caseKey}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCaseKeyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/thermal-loads/plate/{caseKey}", path_parameters)
    
    def by_plate_key(self,plate_key: int) -> WithPlateKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.thermalLoads.plate.item.item collection
        param plate_key: The plate number
        Returns: WithPlateKeyItemRequestBuilder
        """
        if plate_key is None:
            raise TypeError("plate_key cannot be null.")
        from .item.with_plate_key_item_request_builder import WithPlateKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plateKey"] = plate_key
        return WithPlateKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

