from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .elements_to_load.elements_to_load_request_builder import ElementsToLoadRequestBuilder
    from .generate.generate_request_builder import GenerateRequestBuilder
    from .pressures.pressures_request_builder import PressuresRequestBuilder
    from .scenarios.scenarios_request_builder import ScenariosRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .travel_paths.travel_paths_request_builder import TravelPathsRequestBuilder
    from .vehicles.vehicles_request_builder import VehiclesRequestBuilder

class MovingLoadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MovingLoadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads", path_parameters)
    
    @property
    def elements_to_load(self) -> ElementsToLoadRequestBuilder:
        """
        The elementsToLoad property
        """
        from .elements_to_load.elements_to_load_request_builder import ElementsToLoadRequestBuilder

        return ElementsToLoadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generate(self) -> GenerateRequestBuilder:
        """
        The generate property
        """
        from .generate.generate_request_builder import GenerateRequestBuilder

        return GenerateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pressures(self) -> PressuresRequestBuilder:
        """
        The pressures property
        """
        from .pressures.pressures_request_builder import PressuresRequestBuilder

        return PressuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scenarios(self) -> ScenariosRequestBuilder:
        """
        The scenarios property
        """
        from .scenarios.scenarios_request_builder import ScenariosRequestBuilder

        return ScenariosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def travel_paths(self) -> TravelPathsRequestBuilder:
        """
        The travelPaths property
        """
        from .travel_paths.travel_paths_request_builder import TravelPathsRequestBuilder

        return TravelPathsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vehicles(self) -> VehiclesRequestBuilder:
        """
        The vehicles property
        """
        from .vehicles.vehicles_request_builder import VehiclesRequestBuilder

        return VehiclesRequestBuilder(self.request_adapter, self.path_parameters)
    

