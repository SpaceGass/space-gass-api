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
    from ..models.error_response import ErrorResponse
    from ..models.job import Job
    from .analysis.analysis_request_builder import AnalysisRequestBuilder
    from .close.close_request_builder import CloseRequestBuilder
    from .data.data_request_builder import DataRequestBuilder
    from .design.design_request_builder import DesignRequestBuilder
    from .errors.errors_request_builder import ErrorsRequestBuilder
    from .filters.filters_request_builder import FiltersRequestBuilder
    from .headings.headings_request_builder import HeadingsRequestBuilder
    from .import_.import_request_builder import ImportRequestBuilder
    from .loads.loads_request_builder import LoadsRequestBuilder
    from .new.new_request_builder import NewRequestBuilder
    from .new_from_template.new_from_template_request_builder import NewFromTemplateRequestBuilder
    from .open.open_request_builder import OpenRequestBuilder
    from .open_sample.open_sample_request_builder import OpenSampleRequestBuilder
    from .query.query_request_builder import QueryRequestBuilder
    from .save.save_request_builder import SaveRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .structure.structure_request_builder import StructureRequestBuilder
    from .units.units_request_builder import UnitsRequestBuilder

class JobRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JobRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Job]:
        """
        Gets the current job (there is only one).            Sub-resources are managed via their own endpoints:- Headings: GET/PATCH /job/headings- Settings: GET /job/settings- Units: GET/PATCH /job/units- Errors: GET/DELETE /job/errors- Model summary: GET /job/status
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Job]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.job import Job

        return await self.request_adapter.send_async(request_info, Job, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets the current job (there is only one).            Sub-resources are managed via their own endpoints:- Headings: GET/PATCH /job/headings- Settings: GET /job/settings- Units: GET/PATCH /job/units- Errors: GET/DELETE /job/errors- Model summary: GET /job/status
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> JobRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: JobRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return JobRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def analysis(self) -> AnalysisRequestBuilder:
        """
        The analysis property
        """
        from .analysis.analysis_request_builder import AnalysisRequestBuilder

        return AnalysisRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def close(self) -> CloseRequestBuilder:
        """
        The close property
        """
        from .close.close_request_builder import CloseRequestBuilder

        return CloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data(self) -> DataRequestBuilder:
        """
        The data property
        """
        from .data.data_request_builder import DataRequestBuilder

        return DataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def design(self) -> DesignRequestBuilder:
        """
        The design property
        """
        from .design.design_request_builder import DesignRequestBuilder

        return DesignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def errors(self) -> ErrorsRequestBuilder:
        """
        The errors property
        """
        from .errors.errors_request_builder import ErrorsRequestBuilder

        return ErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filters(self) -> FiltersRequestBuilder:
        """
        The filters property
        """
        from .filters.filters_request_builder import FiltersRequestBuilder

        return FiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def headings(self) -> HeadingsRequestBuilder:
        """
        The headings property
        """
        from .headings.headings_request_builder import HeadingsRequestBuilder

        return HeadingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def import_(self) -> ImportRequestBuilder:
        """
        The import property
        """
        from .import_.import_request_builder import ImportRequestBuilder

        return ImportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def loads(self) -> LoadsRequestBuilder:
        """
        The loads property
        """
        from .loads.loads_request_builder import LoadsRequestBuilder

        return LoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def new(self) -> NewRequestBuilder:
        """
        The new property
        """
        from .new.new_request_builder import NewRequestBuilder

        return NewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def new_from_template(self) -> NewFromTemplateRequestBuilder:
        """
        The newFromTemplate property
        """
        from .new_from_template.new_from_template_request_builder import NewFromTemplateRequestBuilder

        return NewFromTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def open(self) -> OpenRequestBuilder:
        """
        The open property
        """
        from .open.open_request_builder import OpenRequestBuilder

        return OpenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def open_sample(self) -> OpenSampleRequestBuilder:
        """
        The openSample property
        """
        from .open_sample.open_sample_request_builder import OpenSampleRequestBuilder

        return OpenSampleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def query(self) -> QueryRequestBuilder:
        """
        The query property
        """
        from .query.query_request_builder import QueryRequestBuilder

        return QueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def save(self) -> SaveRequestBuilder:
        """
        The save property
        """
        from .save.save_request_builder import SaveRequestBuilder

        return SaveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def structure(self) -> StructureRequestBuilder:
        """
        The structure property
        """
        from .structure.structure_request_builder import StructureRequestBuilder

        return StructureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def units(self) -> UnitsRequestBuilder:
        """
        The units property
        """
        from .units.units_request_builder import UnitsRequestBuilder

        return UnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class JobRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

