using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Text.Json;
using System.Windows;
using System.Windows.Media;
using System.Windows.Threading;
using Microsoft.Kiota.Abstractions;
using Microsoft.Win32;
using SpaceGassApi;
using SpaceGassApi.Models;


namespace Example.AnalysisMonitor;

public partial class MainWindow : Window
{
    private SpaceGassApiClient? _client;
    private bool _isConnected;
    private bool _isProjectOpen;
    private readonly DispatcherTimer _pollTimer;
    private readonly ObservableCollection<RunItem> _runs = new();

    public MainWindow()
    {
        InitializeComponent();
        QueueGrid.ItemsSource = _runs;

        _pollTimer = new DispatcherTimer { Interval = TimeSpan.FromMilliseconds(500) };
        _pollTimer.Tick += PollTimer_Tick;
    }

    // =================================================================
    //  CONNECTION
    // =================================================================

    private async void BtnConnect_Click(object sender, RoutedEventArgs e)
    {
        if (_isConnected)
        {
            Disconnect();
            return;
        }

        var baseUrl = TxtServiceUrl.Text.TrimEnd('/');
        if (!baseUrl.EndsWith("/api/v1"))
            baseUrl += "/api/v1";

        ConnDot.Fill = (SolidColorBrush)FindResource("Orange");
        ConnText.Text = "Connecting...";
        TxtApiStatus.Text = "Checking...";
        TxtApiStatus.Foreground = (SolidColorBrush)FindResource("Orange");
        BtnConnect.IsEnabled = false;

        try
        {
            _client = SpaceGassApiClient.CreateClient(baseUrl);
            var info = await _client.Service.Info.GetAsync();

            _isConnected = true;
            ConnDot.Fill = (SolidColorBrush)FindResource("Green");
            ConnText.Text = "Connected";
            BtnConnect.Content = "Disconnect";

            var version = info?.SpaceGassVersion ?? "unknown";
            TxtApiStatus.Text = $"SPACE GASS {version} — Ready";
            TxtApiStatus.Foreground = (SolidColorBrush)FindResource("Green");

            UpdateButtonStates();
        }
        catch (Exception ex)
        {
            _client = null;
            ConnDot.Fill = (SolidColorBrush)FindResource("Red");
            ConnText.Text = "Failed";
            TxtApiStatus.Text = ex.Message;
            TxtApiStatus.Foreground = (SolidColorBrush)FindResource("Red");
        }
        finally
        {
            BtnConnect.IsEnabled = true;
        }
    }

    private void Disconnect()
    {
        _client = null;
        _isConnected = false;
        _isProjectOpen = false;
        ConnDot.Fill = (SolidColorBrush)FindResource("Red");
        ConnText.Text = "Disconnected";
        BtnConnect.Content = "Connect";
        TxtApiStatus.Text = "—";
        TxtApiStatus.Foreground = (SolidColorBrush)FindResource("TextDim");
        BtnOpenClose.Content = "Open";
        UpdateButtonStates();
    }

    // =================================================================
    //  PROJECT
    // =================================================================

    private void BtnBrowse_Click(object sender, RoutedEventArgs e)
    {
        var dlg = new OpenFileDialog
        {
            Filter = "SPACE GASS Files (*.sg)|*.sg|All Files (*.*)|*.*",
            Title = "Select a SPACE GASS project"
        };
        if (dlg.ShowDialog() == true)
        {
            TxtProjectPath.Tag = dlg.FileName;
            TxtProjectPath.Text = System.IO.Path.GetFileName(dlg.FileName);
            TxtProjectPath.ToolTip = dlg.FileName;
        }
    }

    private async void BtnOpenClose_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;

        if (_isProjectOpen)
        {
            try
            {
                await _client.Job.Close.PostAsync();
                _isProjectOpen = false;
                BtnOpenClose.Content = "Open";
                TxtApiStatus.Text = TxtApiStatus.Text?.Replace("Job open", "Ready") ?? "Ready";
                UpdateButtonStates();
            }
            catch (Exception ex)
            {
                ShowApiError("close project", ex);
            }
        }
        else
        {
            var path = TxtProjectPath.Tag as string ?? TxtProjectPath.Text;
            if (string.IsNullOrWhiteSpace(path))
            {
                MessageBox.Show("Please select a project file first.", "No file selected",
                    MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }

            BtnOpenClose.IsEnabled = false;
            try
            {
                await _client.Job.Open.PostAsync(new OpenJobRequest { FilePath = path });
                _isProjectOpen = true;
                BtnOpenClose.Content = "Close";

                var fileName = System.IO.Path.GetFileName(path);
                TxtApiStatus.Text = TxtApiStatus.Text?.Replace("Ready", $"Job open — {fileName}") ?? $"Job open — {fileName}";

                UpdateButtonStates();
            }
            catch (Exception ex)
            {
                ShowApiError("open project", ex);
            }
            finally
            {
                BtnOpenClose.IsEnabled = true;
            }
        }
    }

    // =================================================================
    //  ANALYSIS — RUN
    // =================================================================

    private async void BtnRunStatic_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            AnalysisRun? run;
            string typeName;
            if (RadioLinear.IsChecked == true)
            {
                run = await _client.Job.Analysis.Static.RunLinear.PostAsync(new StaticSettingsUpdate());
                typeName = "Linear Static";
            }
            else
            {
                run = await _client.Job.Analysis.Static.RunNonLinear.PostAsync(new StaticSettingsUpdate());
                typeName = "Non-Linear Static";
            }
            if (run?.RunId != null)
                AddRun(typeName, run.RunId.Value, run);
        }
        catch (Exception ex) { ShowApiError("run static analysis", ex); }
    }

    private async void BtnRunBuckling_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            var run = await _client.Job.Analysis.Buckling.Run.PostAsync(new BucklingSettingsUpdate());
            if (run?.RunId != null)
                AddRun("Buckling", run.RunId.Value, run);
        }
        catch (Exception ex) { ShowApiError("run buckling analysis", ex); }
    }

    private async void BtnRunDynamic_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            var run = await _client.Job.Analysis.DynamicFrequency.Run.PostAsync(new DynamicFrequencySettingsUpdate());
            if (run?.RunId != null)
                AddRun("Dynamic Frequency", run.RunId.Value, run);
        }
        catch (Exception ex) { ShowApiError("run dynamic frequency analysis", ex); }
    }

    private void AddRun(string typeName, Guid runId, AnalysisRun run)
    {
        var item = new RunItem
        {
            RunId = runId,
            TypeName = typeName,
            StatusText = run.Status?.ToString() ?? "Queued",
            ElapsedText = "—"
        };
        _runs.Add(item);

        if (!_pollTimer.IsEnabled)
            _pollTimer.Start();
    }

    // =================================================================
    //  ANALYSIS — CANCEL (from queue grid row)
    // =================================================================

    private async void BtnCancelRun_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        if (sender is not FrameworkElement { Tag: RunItem item }) return;
        if (item.IsTerminal) return;

        try
        {
            await _client.Job.Analysis.Runs[item.RunId].DeleteAsync();
        }
        catch (Exception ex) { ShowApiError("cancel analysis", ex); }
    }

    // =================================================================
    //  ANALYSIS — SETTINGS
    // =================================================================

    private async void BtnSettingsStatic_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            var isLinear = RadioLinear.IsChecked == true;
            var title = isLinear ? "Linear Static Settings" : "Non-Linear Static Settings";
            var settings = await _client.Job.Analysis.Static.Settings.GetAsync();
            var json = JsonSerializer.Serialize(settings, new JsonSerializerOptions { WriteIndented = true });

            var dlg = new SettingsDialog(title, json) { Owner = this };
            if (dlg.ShowDialog() == true)
            {
                var update = JsonSerializer.Deserialize<StaticSettingsUpdate>(dlg.ResultJson);
                if (update != null)
                    await _client.Job.Analysis.Static.Settings.PatchAsync(update);
            }
        }
        catch (Exception ex) { ShowApiError("load static settings", ex); }
    }

    private async void BtnSettingsBuckling_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            var settings = await _client.Job.Analysis.Buckling.Settings.GetAsync();
            var json = JsonSerializer.Serialize(settings, new JsonSerializerOptions { WriteIndented = true });

            var dlg = new SettingsDialog("Buckling Settings", json) { Owner = this };
            if (dlg.ShowDialog() == true)
            {
                var update = JsonSerializer.Deserialize<BucklingSettingsUpdate>(dlg.ResultJson);
                if (update != null)
                    await _client.Job.Analysis.Buckling.Settings.PatchAsync(update);
            }
        }
        catch (Exception ex) { ShowApiError("load buckling settings", ex); }
    }

    private async void BtnSettingsDynamic_Click(object sender, RoutedEventArgs e)
    {
        if (_client == null) return;
        try
        {
            var settings = await _client.Job.Analysis.DynamicFrequency.Settings.GetAsync();
            var json = JsonSerializer.Serialize(settings, new JsonSerializerOptions { WriteIndented = true });

            var dlg = new SettingsDialog("Dynamic Frequency Settings", json) { Owner = this };
            if (dlg.ShowDialog() == true)
            {
                var update = JsonSerializer.Deserialize<DynamicFrequencySettingsUpdate>(dlg.ResultJson);
                if (update != null)
                    await _client.Job.Analysis.DynamicFrequency.Settings.PatchAsync(update);
            }
        }
        catch (Exception ex) { ShowApiError("load dynamic frequency settings", ex); }
    }

    // =================================================================
    //  POLLING
    // =================================================================

    private async void PollTimer_Tick(object? sender, EventArgs e)
    {
        if (_client == null) return;

        var anyActive = false;

        foreach (var item in _runs.ToList())
        {
            if (item.IsTerminal) continue;
            anyActive = true;

            try
            {
                var run = await _client.Job.Analysis.Runs[item.RunId].GetAsync();
                if (run == null) continue;

                item.StatusText = run.Status?.ToString() ?? "Unknown";

                if (run.Progress != null)
                {
                    var p = run.Progress;
                    var totalSteps = p.TotalSteps ?? 1;
                    var currentStep = p.CurrentStep ?? 0;
                    var iterPct = p.IterationPercentage ?? 0;

                    // Step label
                    var stepLabel = "";
                    if (p.StepLabels != null && currentStep < p.StepLabels.Count)
                        stepLabel = p.StepLabels[currentStep] ?? "";

                    item.CurrentStepText = $"{currentStep + 1} / {totalSteps} — {stepLabel}";
                    item.LoadCaseText = p.LoadCaseStatus ?? "—";
                    item.StatusDetailText = p.StatusText ?? "";

                    // Overall progress for detail bar
                    var stepWeight = 100.0 / Math.Max(totalSteps, 1);
                    item.OverallProgressPercent = (int)Math.Min(99,
                        currentStep * stepWeight + (iterPct / 100.0) * stepWeight);
                    item.StepProgressPercent = iterPct;
                }

                // Format elapsed as mm:ss
                item.ElapsedText = FormatElapsed(run.ElapsedTime);

                // Terminal states
                if (run.Status is AnalysisRunStatus.Completed or AnalysisRunStatus.Failed or AnalysisRunStatus.Cancelled)
                {
                    item.IsTerminal = true;
                    item.CancelVisible = Visibility.Collapsed;

                    // Capture error and warnings
                    item.ErrorMessage = run.ErrorMessage;
                    item.Warnings = run.Warnings;
                }
            }
            catch
            {
                // Polling errors are non-fatal — just skip this tick
            }
        }

        UpdateDetailPanel();

        if (!anyActive)
            _pollTimer.Stop();
    }

    /// <summary>
    /// Converts "00:01:23.456" to "1:23" (mm:ss). Falls back to raw string.
    /// </summary>
    private static string FormatElapsed(string? elapsed)
    {
        if (string.IsNullOrEmpty(elapsed)) return "—";
        if (TimeSpan.TryParse(elapsed, out var ts))
        {
            var totalMinutes = (int)ts.TotalMinutes;
            return $"{totalMinutes}:{ts.Seconds:D2}";
        }
        return elapsed;
    }

    // =================================================================
    //  DETAIL PANEL
    // =================================================================

    private void QueueGrid_SelectionChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
    {
        UpdateDetailPanel();
    }

    private void UpdateDetailPanel()
    {
        // Prefer selected row, fall back to first running, fall back to last completed
        var item = QueueGrid.SelectedItem as RunItem
            ?? _runs.FirstOrDefault(r => !r.IsTerminal)
            ?? _runs.LastOrDefault(r => r.IsTerminal);

        if (item == null)
        {
            DetailGrid.Visibility = Visibility.Collapsed;
            DetailEmpty.Visibility = Visibility.Visible;
            DetailErrorBorder.Visibility = Visibility.Collapsed;
            DetailWarningBorder.Visibility = Visibility.Collapsed;
            return;
        }

        DetailGrid.Visibility = Visibility.Visible;
        DetailEmpty.Visibility = Visibility.Collapsed;

        DetailType.Text = item.TypeName;
        DetailStep.Text = item.CurrentStepText ?? "—";
        DetailLoadCases.Text = item.LoadCaseText ?? "—";
        DetailStatus.Text = item.StatusDetailText ?? item.StatusText;
        DetailElapsed.Text = item.ElapsedText;
        DetailProgressBar.Value = item.StepProgressPercent;
        DetailProgressText.Text = $"Step progress: {item.StepProgressPercent}%";

        // Error display
        if (!string.IsNullOrEmpty(item.ErrorMessage))
        {
            DetailErrorBorder.Visibility = Visibility.Visible;
            DetailErrorHeader.Text = "Error";
            DetailErrorText.Text = item.ErrorMessage;
        }
        else
        {
            DetailErrorBorder.Visibility = Visibility.Collapsed;
        }

        // Warnings display
        if (item.Warnings is { Count: > 0 })
        {
            DetailWarningBorder.Visibility = Visibility.Visible;
            DetailWarningText.Text = string.Join("\n", item.Warnings);
        }
        else
        {
            DetailWarningBorder.Visibility = Visibility.Collapsed;
        }
    }

    // =================================================================
    //  HELPERS
    // =================================================================

    private void UpdateButtonStates()
    {
        var canRun = _isConnected && _isProjectOpen;
        BtnRunStatic.IsEnabled = canRun;
        BtnRunBuckling.IsEnabled = canRun;
        BtnRunDynamic.IsEnabled = canRun;
        BtnOpenClose.IsEnabled = _isConnected;
    }

    private static void ShowApiError(string action, Exception ex)
    {
        var message = ex.Message;
        if (ex is ApiException apiEx)
            message = $"API Error ({apiEx.ResponseStatusCode}): {apiEx.Message}";
        MessageBox.Show(message, $"Error: {action}", MessageBoxButton.OK, MessageBoxImage.Error);
    }
}

// =================================================================
//  RUN ITEM — simple bindable model for the DataGrid
// =================================================================

public class RunItem : INotifyPropertyChanged
{
    public Guid RunId { get; set; }
    public string TypeName { get; set; } = "";
    public bool IsTerminal { get; set; }

    // For detail panel
    public string? CurrentStepText { get; set; }
    public string? LoadCaseText { get; set; }
    public string? StatusDetailText { get; set; }
    public int StepProgressPercent { get; set; }
    public int OverallProgressPercent { get; set; }

    // Error/warning info captured at completion
    public string? ErrorMessage { get; set; }
    public List<string>? Warnings { get; set; }

    private string _statusText = "Queued";
    public string StatusText
    {
        get => _statusText;
        set { _statusText = value; OnPropertyChanged(); }
    }

    private string _elapsedText = "—";
    public string ElapsedText
    {
        get => _elapsedText;
        set { _elapsedText = value; OnPropertyChanged(); }
    }

    private Visibility _cancelVisible = Visibility.Visible;
    public Visibility CancelVisible
    {
        get => _cancelVisible;
        set { _cancelVisible = value; OnPropertyChanged(); }
    }

    public event PropertyChangedEventHandler? PropertyChanged;
    private void OnPropertyChanged([CallerMemberName] string? name = null)
        => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
}
