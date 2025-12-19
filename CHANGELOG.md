# Changelog

All notable changes to The Graph Protocol Metrics Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Dual Repository Support**: Added graphprotocol/metrics repository as additional remote
  - Repository now syncs to both https://github.com/pdiomede/metrics and https://github.com/graphprotocol/metrics
  - Updated README.md to include links to both repositories

## [0.0.2] - 2025-12-17

### Added
- **All/90d/30d Period Toggle**: Toggle switch in breadcrumb row for selecting time period
  - Located in the first row (breadcrumb), aligned to the right
  - Three options: All (default), 90d, and 30d
  - Active state shows purple background (#6F4CFF) with white text
  - Inactive state shows gray text (#9CA3AF) with transparent background
  - Old-style toggle switch design matching dashboard theme
  - Real-time filtering of delegation data based on selected period
- **Period-based Data Filtering**: Dynamic filtering of delegation statistics by time period
  - "All" shows all available data (default)
  - "90d" filters to show statistics for the past 90 days
  - "30d" filters to show statistics for the past 30 days
  - Delegation cards (Total Delegated, Total Undelegated, Net) update dynamically
  - Delegation events table filters and updates based on selected period
  - Uses approximate day calculations for efficient filtering
- **Statistics JSON Export**: Automatic saving of all statistics to `last_stats_run.json`
  - Saves comprehensive metrics after each dashboard generation
  - JSON format for easy programmatic access
  - Includes:
    - Last run date (YYYY-MM-DD format)
    - Subgraph counts (all networks and top 20)
    - Delegation statistics (without transaction details)
    - GRT rewards distribution (per network and quarterly)
  - `save_stats_json()` function handles JSON file generation
- **Hardcoded Ethereum Network Data**: Ethereum statistics are now hardcoded
  - Ethereum network is inactive, data is static
  - Removes unnecessary API calls for Ethereum subgraph
  - Improves script execution speed
  - Hardcoded values: total_rewards: 827351728, indexer_rewards: 345569142, delegator_rewards: 481782586, delegator_count: 17387, active_delegators: 9018

### Changed
- **Period Toggle Options**: Changed from "30d / 90d" to "All / 90d / 30d"
  - Default period changed from "30d" to "All"
  - Added "All" option to show complete historical data
- **Statistics Export Format**: Changed from text file (`last_stats_run.txt`) to JSON file (`last_stats_run.json`)
  - More structured and machine-readable format
  - Includes all dashboard metrics in organized sections
  - Easier to parse and integrate with other tools
- **Breadcrumb Layout**: Updated to use flexbox with `justify-content: space-between`
  - Breadcrumb content wrapped in `.breadcrumb-left` div
  - Toggle button positioned on the right side
  - Maintains responsive design for mobile devices

### Technical
- **Period filtering implementation**:
  - Added `filterEventsByPeriod()` JavaScript function for time-based filtering
  - Added `calculateTotals()` function to recalculate statistics from filtered events
  - Added `updateDelegationDisplay()` and `updateDelegationTable()` for dynamic UI updates
  - Delegation events data embedded in JavaScript for client-side filtering
  - Approximate day calculations (90/30 days * 24 * 60 * 60 seconds)
- **JSON export implementation**:
  - `save_stats_json()` function creates structured JSON output
  - Includes subgraph data, delegation metrics, and rewards distribution
  - Proper JSON escaping for JavaScript embedding
- **Ethereum data hardcoding**:
  - Removed Ethereum subgraph API calls from `fetch_network_comparison_stats()`
  - Hardcoded Ethereum values in both `fetch_network_comparison_stats()` and `save_stats_json()`
  - Updated function documentation to reflect hardcoded data

## [Unreleased]

### Added
- **Arbitrum Quarterly Rewards Distribution table**: Historical quarterly rewards data
  - Shows 6 most recent quarters (Q3-2025 through Q2-2024)
  - Includes Q3-2025 (Jul-Sep 2025) - newly added quarter
  - Displays quarter, period, total rewards, indexer rewards, delegator rewards
  - Shows percentage breakdown of indexer vs delegator rewards per quarter
  - Real-time data from Arbitrum Analytics subgraph
  - Purple-themed styling with monospace numbers
  - Hover effects on table rows
  - Grouped with Network Comparison table in collapsible section
  - Both tables toggle together via "GRT Given to Delegators" arrow button
  - Removed emoji (📅) from heading for cleaner look
- `fetch_quarterly_arbitrum_data()` function to query quarterly data
  - Queries graphNetworkDailyDatas from Arbitrum Analytics subgraph
  - Calculates differences between quarter start and end dates
  - Timestamp to day number conversion (genesis: 2020-12-17)
  - Wei to GRT conversion for all reward values
  - Fallback data support for incomplete historical data
  - Real quarterly data: Q3-2025: 74.7M, Q2-2025: 73.8M, Q1-2025: 76.2M GRT
- **Network comparison table**: Expandable table comparing Arbitrum vs Ethereum networks
  - Triggered by arrow button on "GRT Given to Delegators" card
  - Shows side-by-side comparison of both networks
  - Columns: Arbitrum, Ethereum
  - Rows: Total Rewards, Indexer Rewards, Delegator Rewards, Total Delegators, Active Delegators
  - Active delegators marked with + to indicate first 1,000 count
  - Purple-themed headers matching arrow button styling
  - Table hidden by default, toggles on/off with arrow click
- `fetch_network_comparison_stats()` function to query both network subgraphs
  - Queries Arbitrum Network (DZz4kDTdmzWLWsV373w2bSmoar3umKKH9y82SUKr5qmp)
  - Queries Ethereum Network (9Co7EQe5PgW3ugCUJrJgRv4u9zdEuDJf8NvMWftNsBH8)
  - Fetches graphNetwork data and active delegators count for each
  - Returns dictionary with 'arbitrum' and 'ethereum' keys
- **Rewards distribution cards** (second row): Three new cards showing network-wide rewards metrics
  - Total Rewards Distributed - all indexing rewards on Arbitrum Network
  - GRT Kept by Indexers (red #FF6B6B) - indexer portion of rewards
  - GRT Given to Delegators (cyan #4ECDC4) - delegator portion of rewards
  - Data fetched from Arbitrum Network subgraph (DZz4kDTdmzWLWsV373w2bSmoar3umKKH9y82SUKr5qmp)
- `fetch_rewards_metrics()` function to query graphNetwork for rewards data
  - Queries totalIndexingRewards, totalIndexingIndexerRewards, totalIndexingDelegatorRewards
  - Converts values from wei to GRT (divides by 10^18)
- **Delegation table filtering**: Now shows only transactions ≥10,000 GRT
  - Removed 50-event limit, shows all qualifying transactions from 1,000 fetched
  - Updated tooltip text to reflect filter: "(table shows ≥10,000 GRT)"
- **Link styling** in delegation table
  - White links (#F8F6FF) with no underline by default
  - Underline appears on hover for better UX
- **Tooltips on delegation cards**: All three delegation cards now display tooltip on hover
  - Tooltip text: "Calculated for the last 1,000 transactions"
  - Appears on Total Delegated, Total Undelegated, and Net cards
  - Smooth fade-in/out animation with arrow pointer
- **Delegation events table**: Expandable table showing recent delegation activity
  - Triggered by clicking Net card arrow button (›/∨)
  - Displays 50 most recent events from 1,000 fetched
  - 6 columns: Event, GRT, Date, Indexer, Delegator, Tx
  - Event types: ✅ Delegation | ❌ Undelegation
  - Shortened addresses (first 8 + last 6 characters) for better readability
  - Direct links to The Graph Explorer (indexers/delegators) and Arbiscan (transactions)
  - Table hidden by default, toggles on/off with arrow click
- **Three delegation metrics cards** at the top of dashboard:
  - Total Delegated (green) - displays sum of all delegation events in GRT
  - Total Undelegated (red) - displays sum of all undelegation events in GRT
  - Net (dynamic color) - shows net delegation with arrow toggle button
- `fetch_delegation_metrics()` function enhanced to return full event details
  - Now returns tuple: (total_delegated, total_undelegated, net, events_list)
  - Each event includes: type, tokens, delegator, indexer, timestamp, tx_hash
- Queries `stakeDelegateds` and `stakeDelegatedLockeds` events (1000 most recent each)
- Dynamic color coding: green for positive net, red for negative net
- Two compact stats cards (200x180px) displaying subgraph metrics side by side
- Total Subgraphs (All Networks) card showing complete network count
- Total Subgraphs (Top 20 Chains) card with percentage of total networks
- Percentage calculation showing top 20 chains vs all networks
- Toggleable arrow button (›/∨) on Top 20 Chains card for table visibility
- Interactive table that shows/hides when clicking arrow button
- Smooth rotation animation for arrow button (0.3s transition)
- Hover effects on arrow button
- Two-row card layout: delegation metrics on top, subgraph metrics below

### Changed
- **Breadcrumb layout**: Updated to use flexbox with `justify-content: space-between`
  - Breadcrumb content wrapped in `.breadcrumb-left` div
  - Toggle button positioned on the right side
  - Maintains responsive design for mobile devices
- **Enhanced arrow button visibility and styling**:
  - Increased font size from 1.2em to 1.5em (25% larger)
  - Changed color from gray (#9CA3AF) to white (#F8F6FF)
  - Added bold font weight for better prominence
  - Added green background (rgba(76, 175, 80, 0.3)) and border (2px solid #4CAF50)
  - Increased padding from 2px 6px to 4px 8px (more clickable area)
  - Added 8px left margin for spacing
  - Enhanced hover effects: brighter background, scale animation (1.1x), lighter border
  - Expanded state shows visible background
  - Combined transforms for expanded hover state (rotation + scale)
- **Tooltip positioning**: Adjusted from 125% to 105% for closer proximity to cards
- **Footer font size**: Reduced to 0.8em with smaller GitHub icon (14px)
- **Number font size in cards**: Reduced from 2em to 1.5em to fit square boxes
- Replaced single rectangular stats card with two compact cards
- Made stats cards smaller (200x180px instead of 250x250px)
- Aligned stats cards to the left instead of center
- Swapped card order: All Networks first, Top 20 Chains second
- Switched from Flexbox to CSS Grid for precise vertical alignment
- Table hidden by default on page load (click arrow to reveal)
- Updated footer to display dynamic generation timestamp
- Removed "Top 20 Networks by Subgraph Count" subtitle from header
- Removed timestamp and version from header subtitle
- Changed breadcrumb home link from graphtools.pro to local ../index.html
- Improved responsive design for mobile devices with stacked cards
- Reduced padding and gaps for more efficient space usage

### Fixed
- **GRT font size consistency in Net card**: Fixed font-size styling inconsistency
  - Moved `font-size: 0.75em` from inner span to percentage div
  - Now matches styling of Total Delegated and Total Undelegated cards
  - GRT text displays at same size across all delegation cards
- **f-string formatting for subgraph cards**: Fixed missing 'f' prefix on line 775
  - Variables now properly interpolate (total_all_networks, total_top_20, percentage)
  - Cards display actual numbers instead of template strings
- Perfect vertical text alignment across both stats cards using CSS Grid
- Fixed heights for title (45px), number section (flexible), and percentage (35px)
- Ensured green numbers align at exactly the same vertical position

### Technical
- **Period toggle implementation**:
  - Added `.period-toggle` CSS with old-style toggle switch design
  - `.period-toggle-option` styling for active/inactive states
  - Purple theme (#6F4CFF) for active state matching dashboard accent color
  - `togglePeriod()` JavaScript function handles click events
  - Stores current period in `currentPeriod` variable for future use
- **Delegation stats file generation**:
  - `save_delegation_stats()` function creates formatted text file
  - Called automatically in `main()` after fetching delegation metrics
  - File saved as `last_stats_run.txt` in script directory
  - Uses UTF-8 encoding for proper character support
  - Includes formatted columns for easy reading
  - Timestamp conversion from Unix timestamp to UTC datetime format
- **Network comparison table implementation**:
  - Added `toggleNetworkComparison()` JavaScript function to control table visibility
  - Added `#networkComparisonTable` CSS with purple-themed styling
  - Network headers: `rgba(111, 76, 255, 0.2/0.3)` background
  - Row labels left-aligned with gray color (#9CA3AF)
  - Responsive table layout with proper column widths (40%, 30%, 30%)
  - Wei to GRT conversion for all reward values
  - Pagination for active delegators (first 1000 for performance)
- **Arrow button CSS enhancements**:
  - Added background and border styling with green theme
  - Scale transform (1.1x) on hover for interactive feedback
  - Combined transforms for expanded state: `rotate(90deg) scale(1.1)`
  - Increased border-radius from 4px to 6px
- **Link styling in delegation table**: Added `#delegationTable a` CSS rules
  - White color (#F8F6FF), no underline by default
  - Underline on hover only
- Added rewards metrics fetching from Arbitrum Network subgraph
- Query uses graphNetwork(id: "1") to get total rewards, indexer rewards, delegator rewards
- Wei to GRT conversion (division by 10^18) for all reward values
- Second stats-container added for rewards cards layout
- Delegation table filter logic: `if event["tokens"] < 10000: continue`
- Added tooltip CSS styling with hover effects and arrow pointer
- Tooltip positioned absolute with bottom: 105% (appears above cards)
- Enhanced `fetch_delegation_metrics()` to fetch full event details (delegator, indexer, timestamp, tx_hash)
- Added `#delegationTable` with responsive styling
- Updated `toggleNetExpand()` JavaScript function to control delegation table visibility
- Table includes datetime conversion from Unix timestamp to UTC format
- Added delegation metrics data fetching from subgraph `9wzatP4KXm4WinEhB31MdKST949wCH8ZnkGe8o3DLTwp`
- Fetches delegation events via GraphQL queries with extended fields
- Converts token values from wei to GRT (divides by 10^18)
- Events sorted by timestamp in descending order (most recent first)
- Added calculation for total subgraphs across all networks (not just top 20)
- Implemented percentage calculation (top 20 / total * 100)
- Changed layout system from Flexbox to CSS Grid (3 rows: 45px, 1fr, 35px)
- Added JavaScript toggle function for table visibility
- Table ID added for DOM manipulation
- Arrow button CSS with rotation transform on toggle
- Two separate `stats-container` divs for organizing card rows

## [0.0.1] - 2025-12-17

### Added
- Initial release of The Graph Protocol Metrics Dashboard
- Python script (`generate_protocol_metrics.py`) to generate HTML dashboard
- Display of top 20 networks by subgraph count
- Network metrics including:
  - Subgraph count per network
  - Unique indexers per network
- REO-inspired dark theme design with Poppins font
- Breadcrumb navigation
- Responsive design for mobile and desktop
- Link to GitHub repository in footer
- MIT License
- Comprehensive installation guides:
  - `INSTALL_LOCAL.md` for local development setup
  - `INSTALL_VPS.md` for production VPS deployment
- Environment configuration with `.env` file support
- `.gitignore` and `.env.example` for security

### Features
- Real-time data fetching from The Graph Network
- Sortable table display
- Network logos with fallback handling
- Clean and modern UI with dark purple/blue theme (#0C0A1D)
- Direct links to The Graph Explorer for each network
- Automated deployment script for VPS (in installation guide)
