from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .info.info_request_builder import InfoRequestBuilder
    from .run_linear.run_linear_request_builder import RunLinearRequestBuilder
    from .run_non_linear.run_non_linear_request_builder import RunNonLinearRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class StaticRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/analysis/static
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StaticRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/analysis/static", path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_linear(self) -> RunLinearRequestBuilder:
        """
        The runLinear property
        """
        from .run_linear.run_linear_request_builder import RunLinearRequestBuilder

        return RunLinearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_non_linear(self) -> RunNonLinearRequestBuilder:
        """
        The runNonLinear property
        """
        from .run_non_linear.run_non_linear_request_builder import RunNonLinearRequestBuilder

        return RunNonLinearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    

