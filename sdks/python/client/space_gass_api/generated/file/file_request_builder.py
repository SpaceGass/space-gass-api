from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .preview.preview_request_builder import PreviewRequestBuilder
    from .samples.samples_request_builder import SamplesRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder

class FileRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /file
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FileRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/file", path_parameters)
    
    @property
    def preview(self) -> PreviewRequestBuilder:
        """
        The preview property
        """
        from .preview.preview_request_builder import PreviewRequestBuilder

        return PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def samples(self) -> SamplesRequestBuilder:
        """
        The samples property
        """
        from .samples.samples_request_builder import SamplesRequestBuilder

        return SamplesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    

