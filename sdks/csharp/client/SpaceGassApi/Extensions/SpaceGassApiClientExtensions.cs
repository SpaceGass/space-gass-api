using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace SpaceGassApi;

/// <summary>
/// Hand-maintained convenience methods added to the Kiota-generated client.
/// This file lives outside the generated SpaceGassApi/ folder and is safe
/// from <c>--clean-output</c> during regeneration.
/// </summary>
public partial class SpaceGassApiClient
{
    /// <summary>
    /// Default base URL for the SPACE GASS API running locally.
    /// </summary>
    public const string DefaultBaseUrl = "http://localhost:34560/api/v1";

    /// <summary>
    /// Create a <see cref="SpaceGassApiClient"/> with default settings.
    /// </summary>
    /// <param name="baseUrl">
    /// Base URL of the SPACE GASS API.
    /// Defaults to <c>http://localhost:34560/api/v1</c>.
    /// </param>
    /// <returns>A configured client ready to make API calls.</returns>
    public static SpaceGassApiClient CreateClient(string baseUrl = DefaultBaseUrl)
    {
        var adapter = new HttpClientRequestAdapter(
            new AnonymousAuthenticationProvider());
        adapter.BaseUrl = baseUrl;
        return new SpaceGassApiClient(adapter);
    }
}
