from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .codes.codes_request_builder import CodesRequestBuilder
    from .design_iteration_settings.design_iteration_settings_request_builder import DesignIterationSettingsRequestBuilder
    from .item.with_code_item_request_builder import WithCodeItemRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class SteelDesignRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design/steel-design
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SteelDesignRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design/steel-design", path_parameters)
    
    def by_code(self,code: str) -> WithCodeItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.design.steelDesign.item collection
        param code: The design code
        Returns: WithCodeItemRequestBuilder
        """
        if code is None:
            raise TypeError("code cannot be null.")
        from .item.with_code_item_request_builder import WithCodeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["code"] = code
        return WithCodeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def codes(self) -> CodesRequestBuilder:
        """
        The codes property
        """
        from .codes.codes_request_builder import CodesRequestBuilder

        return CodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def design_iteration_settings(self) -> DesignIterationSettingsRequestBuilder:
        """
        The designIterationSettings property
        """
        from .design_iteration_settings.design_iteration_settings_request_builder import DesignIterationSettingsRequestBuilder

        return DesignIterationSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    

