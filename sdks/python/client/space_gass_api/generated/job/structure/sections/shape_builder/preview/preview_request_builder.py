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
    from ......models.error_response import ErrorResponse
    from ......models.section_shape_builder_create import SectionShapeBuilderCreate
    from ......models.section_shape_builder_preview import SectionShapeBuilderPreview

class PreviewRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/sections/shape-builder/preview
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PreviewRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/sections/shape-builder/preview", path_parameters)
    
    async def post(self,body: SectionShapeBuilderCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SectionShapeBuilderPreview]:
        """
        Computes the geometry of the section that `POST /sections/shape-builder` wouldcreate from the same body, without writing anything to the job. Returns the geometry`GET /job/query/geometry/sections/{id}` would return for it — the extent of thewhole section and the outlines of each shape, in the member's local Y-Z plane with theorigin at the section centroid and in the job's section-properties unit, the unit theshapes' dimensions and translations are given in — with each shape's extent(`bounds`) and numbered `referencePoints` added, the points an`anchorPosition` refers to.`section` is 0. Library shapes and anchor positions are resolvedexactly as a create resolves them, and a body a create would reject is rejected here withthe same error.
        param body: DTO for creating a shape-builder (multi-shape) section. The section's structuralproperties (A, J, Iy, Iz, …) are computed by SPACE GASS from the supplied shapes —they are not asserted by the caller.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SectionShapeBuilderPreview]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.section_shape_builder_preview import SectionShapeBuilderPreview

        return await self.request_adapter.send_async(request_info, SectionShapeBuilderPreview, error_mapping)
    
    def to_post_request_information(self,body: SectionShapeBuilderCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Computes the geometry of the section that `POST /sections/shape-builder` wouldcreate from the same body, without writing anything to the job. Returns the geometry`GET /job/query/geometry/sections/{id}` would return for it — the extent of thewhole section and the outlines of each shape, in the member's local Y-Z plane with theorigin at the section centroid and in the job's section-properties unit, the unit theshapes' dimensions and translations are given in — with each shape's extent(`bounds`) and numbered `referencePoints` added, the points an`anchorPosition` refers to.`section` is 0. Library shapes and anchor positions are resolvedexactly as a create resolves them, and a body a create would reject is rejected here withthe same error.
        param body: DTO for creating a shape-builder (multi-shape) section. The section's structuralproperties (A, J, Iy, Iz, …) are computed by SPACE GASS from the supplied shapes —they are not asserted by the caller.
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
    
    def with_url(self,raw_url: str) -> PreviewRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PreviewRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PreviewRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PreviewRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

