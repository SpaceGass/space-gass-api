from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .materials.materials_request_builder import MaterialsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .nodes.nodes_request_builder import NodesRequestBuilder
    from .plates.plates_request_builder import PlatesRequestBuilder
    from .plate_cuts.plate_cuts_request_builder import PlateCutsRequestBuilder
    from .plate_strips.plate_strips_request_builder import PlateStripsRequestBuilder
    from .sections.sections_request_builder import SectionsRequestBuilder

class StructureRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StructureRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure", path_parameters)
    
    @property
    def materials(self) -> MaterialsRequestBuilder:
        """
        The materials property
        """
        from .materials.materials_request_builder import MaterialsRequestBuilder

        return MaterialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        The members property
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nodes(self) -> NodesRequestBuilder:
        """
        The nodes property
        """
        from .nodes.nodes_request_builder import NodesRequestBuilder

        return NodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_cuts(self) -> PlateCutsRequestBuilder:
        """
        The plateCuts property
        """
        from .plate_cuts.plate_cuts_request_builder import PlateCutsRequestBuilder

        return PlateCutsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_strips(self) -> PlateStripsRequestBuilder:
        """
        The plateStrips property
        """
        from .plate_strips.plate_strips_request_builder import PlateStripsRequestBuilder

        return PlateStripsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plates(self) -> PlatesRequestBuilder:
        """
        The plates property
        """
        from .plates.plates_request_builder import PlatesRequestBuilder

        return PlatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> SectionsRequestBuilder:
        """
        The sections property
        """
        from .sections.sections_request_builder import SectionsRequestBuilder

        return SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    

