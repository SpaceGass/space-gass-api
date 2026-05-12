using System.Net.Http;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;
using Microsoft.Kiota.Http.HttpClientLibrary.Middleware.Options;

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
    /// Use <c>https://</c> for HTTPS connections.
    /// </param>
    /// <returns>A configured client ready to make API calls.</returns>
    /// <remarks>
    /// The local SPACE GASS API may serve HTTPS with a self-signed
    /// certificate, so SSL verification is disabled by default.
    /// HTTP-to-HTTPS redirects are also allowed so either scheme
    /// works for the same port.
    /// </remarks>
    public static SpaceGassApiClient CreateClient(string baseUrl = DefaultBaseUrl)
    {
        // Accept self-signed certificates from the local API.
        var handler = new HttpClientHandler
        {
            ServerCertificateCustomValidationCallback =
                HttpClientHandler.DangerousAcceptAnyServerCertificateValidator,
        };

        // Allow HTTP ↔ HTTPS redirects (the local API may redirect).
        var httpClient = KiotaClientFactory.Create(
            handler,
            [
                new RedirectHandlerOption
                {
                    AllowRedirectOnSchemeChange = true,
                },
            ]);

        var adapter = new HttpClientRequestAdapter(
            new AnonymousAuthenticationProvider(),
            httpClient: httpClient);
        adapter.BaseUrl = baseUrl;
        return new SpaceGassApiClient(adapter);
    }
}
