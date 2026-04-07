using System.Windows;

namespace Example.AnalysisMonitor;

public partial class SettingsDialog : Window
{
    public string ResultJson { get; private set; } = "";

    public SettingsDialog(string title, string json)
    {
        InitializeComponent();
        Title = title;
        TitleText.Text = title;
        TxtJson.Text = json;
    }

    private void BtnSave_Click(object sender, RoutedEventArgs e)
    {
        ResultJson = TxtJson.Text;
        DialogResult = true;
    }
}
