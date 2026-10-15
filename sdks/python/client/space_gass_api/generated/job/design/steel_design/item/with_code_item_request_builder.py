from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run_check.run_check_request_builder import RunCheckRequestBuilder
    from .run_design.run_design_request_builder import RunDesignRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class WithCodeItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design/steel-design/{code}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCodeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design/steel-design/{code}", path_parameters)
    
    @property
    def run_check(self) -> RunCheckRequestBuilder:
        """
        The runCheck property
        """
        from .run_check.run_check_request_builder import RunCheckRequestBuilder

        return RunCheckRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_design(self) -> RunDesignRequestBuilder:
        """
        The runDesign property
        """
        from .run_design.run_design_request_builder import RunDesignRequestBuilder

        return RunDesignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    

