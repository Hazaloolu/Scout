# Scout

Scout fetches job listings from the Adzuna API and automatically adds them to a specified Notion database. It's designed to streamline the job search process by aggregating listings from multiple countries and job types into a single, organized Notion database.

## Features

- Fetches job listings from Adzuna API
- Supports multiple job stacks and countries
- Adds job listings to a Notion database

## Prerequisites

- Python 3.7 or higher installed
- Adzuna API key and app ID
- Notion API key
- Notion database ID for storing job listings

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Hazaloolu/NotionRecruiter.git
   cd job_finder
   ```

2. Install the required packages:
   ```
   pip install requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys:
   ```
   ADZUNA_APP_ID=your_adzuna_app_id
   ADZUNA_API_KEY=your_adzuna_api_key
   NOTION_API_KEY=your_notion_api_key
   DATABASE_ID=your_notion_database_id
   ```

## Usage

1. Modify the `stacks` and `countries` lists in the `main()` function to match your job search criteria.

2. Run the script:
   ```
   python main.py
   ```

The script will fetch job listings based on your specified stacks and countries, and add them to your Notion database.

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Adzuna API](https://developer.adzuna.com/) for providing job listing data
- [Notion API](https://developers.notion.com/) for enabling database integration
