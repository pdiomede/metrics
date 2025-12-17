# Changelog

All notable changes to The Graph Protocol Metrics Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
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
