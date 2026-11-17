using System;
using System.Threading;
using System.Threading.Tasks;
using SpaceGassApi.Job.Design.SteelMember;
using SpaceGassApi.Job.Design.SteelMember.Item;
using SpaceGassApi.Job.Design.SteelMember.Item.Settings;
using SpaceGassApi.Models;

namespace SpaceGassApi
{
    /// <summary>
    /// Conveniences for steel member design (<c>/job/design/steel-member/...</c>).
    /// </summary>
    /// <remarks>
    /// <para>
    /// Every design code (AS 4100, NZS 3404, Eurocode 3, AISC, ...) has its own settings
    /// classes, all deriving from <see cref="SteelMemberDesignSettingsBase"/> /
    /// <see cref="SteelMemberDesignSettingsBaseUpdate"/>. The generated client already
    /// accepts and returns those base types, so a code's own object can be passed anywhere
    /// settings are taken:
    /// </para>
    /// <code>
    /// var as4100 = client.Job.Design.SteelMember.ForCode(DesignCode.As4100);
    ///
    /// await as4100.RunCheck.PostAsync(new SteelMemberDesignRunCheckRequest
    /// {
    ///     CodeSettings = new SteelMemberDesignSettingsAs4100Update { SlendernessRatioCheck = true },
    /// });
    ///
    /// var settings = await as4100.Settings.GetAsync&lt;SteelMemberDesignSettingsAs4100&gt;();
    /// settings = await as4100.Settings.PatchAsync&lt;SteelMemberDesignSettingsAs4100&gt;(
    ///     new SteelMemberDesignSettingsAs4100Update { UseKtFactorForTension = true });
    /// </code>
    /// <para>
    /// These helpers add the <see cref="DesignCode"/> enum in place of the string indexer,
    /// and typed reads so the result does not need casting from the base class.
    /// Lives in Utils/ so it survives Kiota's --clean-output.
    /// </para>
    /// </remarks>
    public static class SteelMemberDesignExtensions
    {
        /// <summary>
        /// The endpoints for one design code — <c>RunCheck</c>, <c>RunDesign</c>, <c>Settings</c>.
        /// Equivalent to <c>SteelMember["As4100"]</c> but with the <see cref="DesignCode"/> enum.
        /// </summary>
        public static WithCodeItemRequestBuilder ForCode(this SteelMemberRequestBuilder builder, DesignCode code)
            => builder[code.ToString()];

        /// <summary>
        /// Reads the design code's stored settings as its own type, e.g.
        /// <c>Settings.GetAsync&lt;SteelMemberDesignSettingsAs4100&gt;()</c>.
        /// The untyped <c>GetAsync()</c> returns the same object as <see cref="SteelMemberDesignSettingsBase"/>.
        /// </summary>
        /// <exception cref="InvalidCastException">
        /// The route's design code returned a different settings type than <typeparamref name="TSettings"/>.
        /// </exception>
        public static async Task<TSettings?> GetAsync<TSettings>(
            this SettingsRequestBuilder builder, CancellationToken cancellationToken = default)
            where TSettings : SteelMemberDesignSettingsBase
            => As<TSettings>(await builder.GetAsync(cancellationToken: cancellationToken).ConfigureAwait(false));

        /// <summary>
        /// Partially updates the design code's stored settings and returns them as their own type, e.g.
        /// <c>Settings.PatchAsync&lt;SteelMemberDesignSettingsAs4100&gt;(new SteelMemberDesignSettingsAs4100Update { ... })</c>.
        /// </summary>
        /// <exception cref="InvalidCastException">
        /// The route's design code returned a different settings type than <typeparamref name="TSettings"/>.
        /// </exception>
        public static async Task<TSettings?> PatchAsync<TSettings>(
            this SettingsRequestBuilder builder, SteelMemberDesignSettingsBaseUpdate settings, CancellationToken cancellationToken = default)
            where TSettings : SteelMemberDesignSettingsBase
            => As<TSettings>(await builder.PatchAsync(settings, cancellationToken: cancellationToken).ConfigureAwait(false));

        private static TSettings? As<TSettings>(SteelMemberDesignSettingsBase? value)
            where TSettings : SteelMemberDesignSettingsBase
        {
            if (value == null) return null;
            return value as TSettings
                ?? throw new InvalidCastException(
                    $"The design code returned {value.GetType().Name}, not {typeof(TSettings).Name}.");
        }
    }
}
