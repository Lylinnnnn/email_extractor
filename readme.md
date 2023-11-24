# GitHub Email Extractor

This script is designed to extract email addresses associated with GitHub user accounts. It reads an input Excel file containing a list of GitHub usernames and uses the GitHub API to retrieve their email addresses. The results are then saved to an output Excel file.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system
- Required Python packages: pandas, requests

## Getting Started

1. Clone the repository:

```
git clone https://github.com/Lylinnnnn/email_extractor.git
```

2. Install the required packages using pip:
```
pip install pandas requests
```

3. Obtain a personal access token from GitHub:

- Go to your GitHub **Settings**.
- Navigate to **Developer settings** > **Personal access tokens**.
- Click on **Generate new token**.
- Provide a suitable description and select the necessary scopes (e.g., `user` and `user:email`).
- Click on **Generate token** and copy the generated token.

4. Update the script:

- Replace `'your_token'` in the script with your personal access token obtained from GitHub.

5. Prepare the input file:

- Create an Excel file with a column header `'github ID'`.
- Fill in the GitHub usernames in the respective rows.

6. Run the script:
```
python email_extractor.py
```

7. View the results:

- The script will create an output Excel file named `'output.xlsx'` containing the extracted email addresses.

## License

This project is licensed under the [MIT License](LICENSE).

