<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    ![H9FmR9bq_400x400](https://github.com/user-attachments/assets/83186047-819d-4fa6-bac6-5a4df81c8a8f)
    <h1>PARTI.COM Bot Metrics Tracker</h1>
    <p>This Python script tracks bot metrics by fetching data from the <strong>Parti API</strong> and calculates real viewers based on a specified botting behavior (either 12 users = 1 real user, or 8 users = 1 real user).</p>
    <h2>Features:</h2>
    <ul class="feature-list">
        <li>Fetches user profile data from the Parti API.</li>
        <li>Calculates real viewers based on a randomized botting ratio.</li>
        <li>Updates the bot metrics every 60 seconds.</li>
        <li>Outputs the metrics to a JSON file.</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li><strong>Clone this repository or download the Python script.</strong>
            <pre><code>git clone https://github.com/Riotcoke123/PARTI.COM-Bot-Metrics-Tracker</code></pre>
        </li>
        <li><strong>Install the required Python dependencies.</strong>
            <pre><code>pip install requests</code></pre>
        </li>
        <li><strong>Ensure your environment supports Python 3.</strong></li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li><strong>Run the Python script:</strong>
            <pre><code>python bot_metrics_tracker.py</code></pre>
        </li>
        <li><strong>Input the User ID:</strong> When prompted, enter the <strong>User ID</strong> whose bot metrics you want to track.
            <pre><code>Enter User ID: &lt;your_user_id&gt;</code></pre>
        </li>
        <li><strong>Wait for updates:</strong> The script will fetch bot metrics, calculate real viewers, and save them into a <code>bot_metrics.json</code> file. It will update the data every <strong>60 seconds</strong>.</li>
        <li><strong>Output:</strong> The JSON file will contain the following metrics:
            <ul>
                <li><code>username</code>: The username of the tracked user.</li>
                <li><code>unique_chatters</code>: Number of unique users participating in the chat.</li>
                <li><code>total_viewers</code>: Total viewers (bot + real users).</li>
                <li><code>real_viewers</code>: Number of real viewers calculated based on botting behavior.</li>
                <li><code>monitoring</code>: Whether the user is under monitoring (from the API response).</li>
            </ul>
        </li>
    </ol>
    <h2>Botting Behavior</h2>
    <p>The real viewers count is calculated using a random ratio:</p>
    <ul>
        <li><strong>12 users = 1 real user</strong></li>
        <li><strong>8 users = 1 real user</strong></li>
    </ul>
    <p>Every time the script updates, it randomly chooses between these two ratios to calculate the <code>real_viewers</code> value.</p>
<h2>License</h2>
<p>This project is licensed under the <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">GNU General Public License v3.0</a>. It is open-source and available for personal and educational use. Please ensure it is not used for any malicious activities. By using this tool, you agree to comply with the Parti.com Terms of Service. Please note that this open-source project is currently in beta testing.</p>
</body>
</html>
