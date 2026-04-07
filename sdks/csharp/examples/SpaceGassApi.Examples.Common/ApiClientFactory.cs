using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;
using SpaceGassApi;

namespace SpaceGassApi.Examples.Common;

/// <summary>
/// Shared helper for creating a configured SpaceGass API client.
/// </summary>
public static class ApiClientFactory
{
    private const string DefaultBaseUrl = "https://localhost:53483/api/v1";
    private const string DefaultApiKey = "local";

    /// <summary>
    /// Creates a <see cref="SpaceGassApiClient"/> configured with API key
    /// authentication and a development SSL bypass handler.
    /// </summary>
    /// <param name="baseUrl">Base URL of the SpaceGass API (default: https://localhost:53483).</param>
    /// <param name="apiKey">API key for authentication (default: "local").</param>
    public static SpaceGassApiClient Create(
        string baseUrl = DefaultBaseUrl,
        string apiKey = DefaultApiKey)
    {
        var authProvider = new ApiKeyAuthenticationProvider(
            apiKey,
            "X-API-KEY",
            ApiKeyAuthenticationProvider.KeyLocation.Header);

        // Bypass SSL validation for local development with self-signed certificates.
        var handler = new HttpClientHandler
        {
            ServerCertificateCustomValidationCallback =
                HttpClientHandler.DangerousAcceptAnyServerCertificateValidator
        };
        var httpClient = new HttpClient(handler);

        var adapter = new HttpClientRequestAdapter(authProvider, httpClient: httpClient);
        adapter.BaseUrl = baseUrl;

        return new SpaceGassApiClient(adapter);
    }
}
