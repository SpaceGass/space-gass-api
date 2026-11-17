"""
Hand-maintained conveniences for steel member design
(``/job/design/steel-member/...``) — parity with the C# SDK's
``Utils/SteelMemberDesignExtensions.cs``.

Every design code (AS 4100, NZS 3404, Eurocode 3, AISC, ...) has its own
settings classes, all deriving from ``SteelMemberDesignSettingsBase`` /
``SteelMemberDesignSettingsBaseUpdate``. The generated client already accepts
and returns those base types, so a code's own object can be passed anywhere
settings are taken::

    from space_gass_api import steel_member
    import space_gass_api.models as models

    as4100 = client.job.design.steel_member.by_code(models.DesignCode.As4100.value)

    run = await as4100.run_check.post(models.SteelMemberDesignRunCheckRequest(
        code_settings=models.SteelMemberDesignSettingsAs4100Update(slenderness_ratio_check=True)))

    settings = await steel_member.get_settings(as4100, models.SteelMemberDesignSettingsAs4100)
    settings = await steel_member.patch_settings(
        as4100, models.SteelMemberDesignSettingsAs4100Update(use_kt_factor_for_tension=True),
        models.SteelMemberDesignSettingsAs4100)

These helpers add typed reads so IntelliSense knows the result's class.

Lives outside ``generated/`` so it survives Kiota's ``--clean-output``.
"""

from __future__ import annotations

from typing import Optional, TypeVar, overload

from .generated.job.design.steel_member.item.with_code_item_request_builder import (
    WithCodeItemRequestBuilder,
)
from .generated.models.steel_member_design_settings_base import SteelMemberDesignSettingsBase
from .generated.models.steel_member_design_settings_base_update import (
    SteelMemberDesignSettingsBaseUpdate,
)

__all__ = ["get_settings", "patch_settings"]

TSettings = TypeVar("TSettings", bound=SteelMemberDesignSettingsBase)


def _expect(value: Optional[SteelMemberDesignSettingsBase], expect: Optional[type]):
    if value is not None and expect is not None and not isinstance(value, expect):
        raise TypeError(f"The design code returned {type(value).__name__}, not {expect.__name__}.")
    return value


@overload
async def get_settings(code: WithCodeItemRequestBuilder) -> Optional[SteelMemberDesignSettingsBase]: ...
@overload
async def get_settings(code: WithCodeItemRequestBuilder, expect: type[TSettings]) -> Optional[TSettings]: ...


async def get_settings(code, expect=None):
    """Reads a design code's stored settings.

    ``code`` is ``client.job.design.steel_member.by_code("As4100")``. Pass ``expect`` (e.g.
    ``models.SteelMemberDesignSettingsAs4100``) to get a typed result; a different
    type coming back raises ``TypeError``. Without it this is ``code.settings.get()``.
    """
    return _expect(await code.settings.get(), expect)


@overload
async def patch_settings(
    code: WithCodeItemRequestBuilder, update: SteelMemberDesignSettingsBaseUpdate
) -> Optional[SteelMemberDesignSettingsBase]: ...
@overload
async def patch_settings(
    code: WithCodeItemRequestBuilder, update: SteelMemberDesignSettingsBaseUpdate, expect: type[TSettings]
) -> Optional[TSettings]: ...


async def patch_settings(code, update, expect=None):
    """Partially updates a design code's stored settings and returns the updated settings."""
    return _expect(await code.settings.patch(update), expect)
