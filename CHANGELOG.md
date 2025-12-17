# Changelog

All notable changes to The Graph Protocol Metrics Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Two square stats cards (250x250px) displaying metrics side by side
- Total Subgraphs (Top 20 Chains) card with percentage of total networks
- Total Subgraphs (All Networks) card showing complete network count
- Percentage calculation showing top 20 chains vs all networks

### Changed
- Replaced single rectangular stats card with two square cards
- Optimized font sizes for square card format
- Updated footer to display dynamic generation timestamp instead of static text
- Removed "Top 20 Networks by Subgraph Count" subtitle from header
- Improved responsive design for mobile devices with stacked cards

### Technical
- Added calculation for total subgraphs across all networks (not just top 20)
- Implemented percentage calculation (top 20 / total * 100)
- Enhanced CSS with flex layout for stats cards
- Added mobile breakpoint for card stacking

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
