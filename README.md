# PyVPN
Automates the connection to VPN. Use either the Python or the Batch scripts I wrote here to connect to VPN. Wrote it since VPN gets disconnected after a while by design. I run it as on Task Scheduler (Windows Scheduler) so it doesn't need to be run every time VPN is disconnected.

# Setting Up Python / BAT Script in Windows Task Scheduler

This guide will help you schedule the script to run automatically using Windows Task Scheduler.

## Step 1: Open Task Scheduler
1. Press `Windows + R` to open the Run dialog.
2. Type `taskschd.msc` and hit Enter. This will open the Task Scheduler.

## Step 2: Create a New Task
1. In the Task Scheduler, click on **"Create Basic Task..."** in the right-hand pane.
2. Give your task a name (e.g., **"VPN Reconnect Script"**) and a description if you like. Click **Next**.

## Step 3: Set the Trigger
1. Choose how often you want the task to run (e.g., **Daily**, **Weekly**, or **One Time**). Click **Next**.
2. Set the specific time and frequency according to your preference. Click **Next**.

## Step 4: Set the Action
1. Select **"Start a program"** and click **Next**.
2. In the **Program/script** field, enter the path to your Python executable. This is usually something like:

C:\Python39\python.exe [skip this step if you use my bat script instead of py]

(Adjust the path based on your Python installation.)

3. In the **Add arguments (optional)** field, enter the path to your script:

“C:\path\to\your\AutoConnectToVPN.py”

Make sure to include the quotes if there are spaces in the path.

4. In the **Start in (optional)** field, specify the directory where your script is located:

C:\path\to\your\


## Step 5: Finish the Setup
1. Review your settings and click **Finish** to create the task.

## Step 6: Test the Task
1. You can manually run the task by right-clicking it in the Task Scheduler and selecting **Run**. Check the output to ensure it works as expected.

## Additional Considerations
- **Permissions**: Ensure that the user account running the task has the necessary permissions to execute the script and connect to the VPN.
- **Logging**: If you want to log the output of your script, consider modifying your Python script to write to a log file.

