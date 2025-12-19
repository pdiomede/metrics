# The Graph Protocol Metrics Dashboard

A Python-generated static HTML dashboard displaying key metrics for The Graph Protocol, including delegation metrics, subgraph counts across the top 20 networks, and unique indexer statistics.

## Features

- ⏱️ **Period Toggle**: 30d/90d toggle switch in breadcrumb row for selecting time period (default: 30d)
- 💰 **Delegation Metrics** (First Row): Three cards showing Total Delegated, Total Undelegated, and Net (in GRT)
  - Real-time data from delegation events on The Graph Network
  - Color-coded: green for delegations, red for undelegations, dynamic for net
  - Tooltips on hover showing "Calculated for the last 1,000 transactions (table shows ≥10,000 GRT)"
  - Interactive arrow button on Net card to expand/collapse delegation events table
- 🎁 **Rewards Distribution** (Second Row): Three cards showing rewards metrics from Arbitrum Network
  - Total Rewards Distributed across The Graph Network
  - GRT Kept by Indexers (red) - portion retained by indexers
  - GRT Given to Delegators (cyan) - portion distributed to delegators
  - Real-time data from Arbitrum Network subgraph
- 📊 **Dual Subgraph Cards**: Two compact cards showing Total Subgraphs (All Networks) and Top 20 Chains
- 📈 **Percentage Analysis**: Shows what percentage of total subgraphs the top 20 chains represent
- 🔽 **Collapsible Table**: Interactive arrow button to show/hide the detailed network table
- 🔢 **Subgraph Counts**: Total number of subgraphs deployed on each network
- 👥 **Unique Indexers**: Number of unique indexers actively allocating to each network
- 🎨 **Modern UI**: Clean, responsive design with dark theme inspired by REO dashboard
- 🔗 **Explorer Links**: Direct links to The Graph Explorer for each network
- 📱 **Responsive**: Works on desktop and mobile devices
- ⚡ **Interactive**: Click arrow buttons to expand/collapse sections

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

The script also automatically saves delegation statistics to `last_stats_run.txt` after each run, containing all delegation event details for reference.

## Dashboard Components

### Period Toggle (Breadcrumb Row)
- **30d/90d Toggle**: Toggle switch located in the breadcrumb row, aligned to the right
  - Default: 30d enabled (purple background, white text)
  - Click to switch between 30d and 90d periods
  - Active period highlighted with purple background (#6F4CFF)
  - Inactive period shown in gray (#9CA3AF)
  - Old-style toggle switch design matching dashboard theme

### Delegation Metrics (Top Row)
- **Card 1**: Total Delegated - Total GRT delegated across all delegation events (green)
  - Hover to see tooltip: "Calculated for the last 1,000 transactions"
- **Card 2**: Total Undelegated - Total GRT undelegated across all undelegation events (red)
  - Hover to see tooltip: "Calculated for the last 1,000 transactions"
- **Card 3**: Net - Net delegation (Delegated - Undelegated) with dynamic color
  - Green if positive, red if negative
  - Hover to see tooltip: "Calculated for the last 1,000 transactions"
  - Arrow button (›/∨) to expand/collapse delegation events table

### Delegation Events Table (Collapsible)
Accessible by clicking the arrow on the Net card:
- **Event**: Type of transaction (✅ Delegation or ❌ Undelegation)
- **GRT**: Amount of GRT tokens in the transaction (only shows ≥10,000 GRT)
- **Date**: Transaction timestamp in UTC (YYYY-MM-DD HH:MM format)
- **Indexer**: Indexer address (linked to Graph Explorer, shortened display)
- **Delegator**: Delegator address (linked to Graph Explorer, shortened display)
- **Tx**: Link to view transaction on Arbiscan
- **Filter**: Only displays transactions of 10,000 GRT or more
- **Default**: Hidden (click arrow to reveal)

### Rewards Distribution (Second Row)
- **Card 1**: Total Rewards Distributed - Complete sum of all indexing rewards on Arbitrum
- **Card 2**: GRT Kept by Indexers - Portion of rewards retained by indexers (red)
- **Card 3**: GRT Given to Delegators - Portion of rewards distributed to delegators (cyan)
  - Interactive arrow button (›/∨) to expand/collapse network comparison table

### Network Comparison & Quarterly Data (Collapsible)
Accessible by clicking the arrow on the "GRT Given to Delegators" card:

**Network Comparison Table:**
- **Columns**: Arbitrum Network vs Ethereum Network side-by-side comparison
- **Rows**:
  - Total Rewards (in GRT)
  - Indexer Rewards (in GRT)
  - Delegator Rewards (in GRT)
  - Total Delegators (historical count)
  - Active Delegators (with GRT) - shows 1,000+ as approximation

**Arbitrum Quarterly Rewards Distribution:**
- Historical quarterly data showing rewards distribution
- **Quarters Displayed**: 6 most recent quarters (Q3-2025 to Q2-2024)
- **Columns**:
  - Quarter (e.g., Q3-2025)
  - Period (date range)
  - Total Rewards (GRT)
  - Indexer Rewards (GRT) with percentage
  - Delegator Rewards (GRT) with percentage
- **Data Source**: Real-time from Arbitrum Analytics subgraph
- **Purple Theme**: Matches overall dashboard styling
- **Default**: Hidden (click arrow on "GRT Given to Delegators" card to reveal both tables)

### Subgraph Metrics (Second Row)
- **Card 1**: Total Subgraphs (All Networks) - Shows complete count across all 150+ networks
- **Card 2**: Total Subgraphs (Top 20 Chains) - Shows top 20 count with percentage of total
- **Arrow Button**: Click to expand/collapse the detailed network table

### Network Metrics Table (Collapsible)
- **Rank**: Network ranking by subgraph count
- **Network**: Network name with logo and link to Graph Explorer
- **Subgraph Count**: Total number of subgraphs on the network
- **Unique Indexers**: Number of unique indexers serving the network
- **Toggle**: Click the arrow (›) on the Top 20 Chains card to show/hide this table

## Project Structure

```
metrics/
├── generate_protocol_metrics.py   # Main dashboard generator script
├── index.html                      # Generated dashboard (output)
├── last_stats_run.txt              # Delegation statistics export (generated)
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

Current version: **v0.0.2** (December 17, 2025)

For detailed version history and changes, see [CHANGELOG.md](CHANGELOG.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Paolo Diomede**

## Links

- [GitHub Repository (pdiomede)](https://github.com/pdiomede/metrics)
- [GitHub Repository (graphprotocol)](https://github.com/graphprotocol/metrics)
- [The Graph Protocol](https://thegraph.com)
- [The Graph Explorer](https://thegraph.com/explorer)

## Acknowledgments

- Design inspired by the REO Eligibility Dashboard
- Data sourced from The Graph Network
- Built for The Graph Protocol community
