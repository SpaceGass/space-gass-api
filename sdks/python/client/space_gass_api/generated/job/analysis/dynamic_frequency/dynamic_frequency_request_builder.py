from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .info.info_request_builder import InfoRequestBuilder
    from .run.run_request_builder import RunRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class DynamicFrequencyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/analysis/dynamic-frequency
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DynamicFrequencyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/analysis/dynamic-frequency", path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run(self) -> RunRequestBuilder:
        """
        The run property
        """
        from .run.run_request_builder import RunRequestBuilder

        return RunRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    

