# This is a PowerShell script that sends a request to a Streamlit app URL to keep it awake.
# This script will be scheduled to run periodically using Windows Task Scheduler.

# URL of the Streamlit app
$url = "https://cricket-t20-score-predictor.streamlit.app/"

# Send a request to the URL
try {
    Invoke-WebRequest -Uri $url -UseBasicParsing
    Write-Output "Visited Streamlit app at $(Get-Date)"
} catch {
    Write-Output "Failed to visit Streamlit app: $_"
}