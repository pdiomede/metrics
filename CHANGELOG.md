# Changelog

All notable changes to The Graph Protocol Metrics Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Two compact stats cards (200x180px) displaying metrics side by side
- Total Subgraphs (All Networks) card showing complete network count
- Total Subgraphs (Top 20 Chains) card with percentage of total networks
- Percentage calculation showing top 20 chains vs all networks
- Toggleable arrow button (›/∨) on Top 20 Chains card
- Interactive table that shows/hides when clicking arrow button
- Smooth rotation animation for arrow button (0.3s transition)
- Hover effects on arrow button

### Changed
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
- Perfect vertical text alignment across both stats cards using CSS Grid
- Fixed heights for title (45px), number section (flexible), and percentage (35px)
- Ensured green numbers align at exactly the same vertical position

### Technical
- Added calculation for total subgraphs across all networks (not just top 20)
- Implemented percentage calculation (top 20 / total * 100)
- Changed layout system from Flexbox to CSS Grid (3 rows: 45px, 1fr, 35px)
- Added JavaScript toggle function for table visibility
- Table ID added for DOM manipulation
- Arrow button CSS with rotation transform on toggle

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
