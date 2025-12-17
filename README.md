# The Graph Protocol Metrics Dashboard

A Python-generated static HTML dashboard displaying key metrics for The Graph Protocol's top 20 networks, including subgraph counts and unique indexer statistics.

## Features

- 📊 **Dual Stats Cards**: Two compact cards showing Total Subgraphs (All Networks) and Top 20 Chains
- 📈 **Percentage Analysis**: Shows what percentage of total subgraphs the top 20 chains represent
- 🔽 **Collapsible Table**: Interactive arrow button to show/hide the detailed network table
- 🔢 **Subgraph Counts**: Total number of subgraphs deployed on each network
- 👥 **Unique Indexers**: Number of unique indexers actively allocating to each network
- 🎨 **Modern UI**: Clean, responsive design with dark theme inspired by REO dashboard
- 🔗 **Explorer Links**: Direct links to The Graph Explorer for each network
- 📱 **Responsive**: Works on desktop and mobile devices
- ⚡ **Interactive**: Click arrow button to expand/collapse network details

## Prerequisites

- Python 3.7+
- The Graph API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pdiomede/metrics.git
cd metrics
```

2. Install required dependencies:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root:
```bash
GRAPH_API_KEY=your_api_key_here
```

You can obtain a Graph API key from [The Graph Studio](https://thegraph.com/studio/).

## Usage

Run the dashboard generator:

```bash
python generate_protocol_metrics.py
```

This will generate an `index.html` file in the same directory. Open it in your web browser to view the dashboard.

## Dashboard Components

### Stats Cards
- **Card 1**: Total Subgraphs (All Networks) - Shows complete count across all 150+ networks
- **Card 2**: Total Subgraphs (Top 20 Chains) - Shows top 20 count with percentage of total
- **Arrow Button**: Click to expand/collapse the detailed network table

### Network Metrics Table (Collapsible)
- **Rank**: Network ranking by subgraph count
- **Network**: Network name with logo and link to Graph Explorer
- **Subgraph Count**: Total number of subgraphs on the network
- **Unique Indexers**: Number of unique indexers serving the network
- **Toggle**: Click the arrow (›) on the Top 20 card to show/hide this table

## Project Structure

```
metrics/
├── generate_protocol_metrics.py   # Main dashboard generator script
├── index.html                      # Generated dashboard (output)
├── README.md                       # This file
├── CHANGELOG.md                    # Version history (see CHANGELOG.md)
├── LICENSE                         # MIT License (see LICENSE)
├── .env                            # Environment variables (not in repo)
├── .env.example                    # Environment template
└── .gitignore                      # Git ignore rules
```

## Styling

The dashboard uses a dark theme with the following color palette:
- **Background**: #0C0A1D (dark purple/blue)
- **Text**: #F8F6FF (off-white)
- **Borders**: #9CA3AF (gray)
- **Accent**: #4CAF50 (green for stats)
- **Font**: Poppins (Google Fonts)

## Version

Current version: **v0.0.1** (December 17, 2025)

For detailed version history and changes, see [CHANGELOG.md](CHANGELOG.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Paolo Diomede**

## Links

- [GitHub Repository](https://github.com/pdiomede/metrics)
- [The Graph Protocol](https://thegraph.com)
- [The Graph Explorer](https://thegraph.com/explorer)

## Acknowledgments

- Design inspired by the REO Eligibility Dashboard
- Data sourced from The Graph Network
- Built for The Graph Protocol community
