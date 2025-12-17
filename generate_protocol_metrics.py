#!/usr/bin/env python3
"""
The Graph Protocol Metrics Dashboard Generator

This script generates a static HTML dashboard showing network metrics
for The Graph Protocol, including subgraph counts and unique indexers
per network (top 20 networks by subgraph count).

Version: v0.0.1
Date: December 17, 2025
Author: Paolo Diomede
"""

import os
import json
import requests
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

# Version of the dashboard generator
VERSION = "0.0.1"

# Data class for network subgraph and unique indexer counts
@dataclass
class NetworkIndexerData:
    network_name: str
    subgraph_count: int
    unique_indexer_count: int


# Mapping of network names to local logo image paths
NETWORK_LOGOS = {
    "abstract": "images/abstract.png",
    "arbitrum-nova": "images/arbitrum-nova.png",
    "arbitrum-one": "images/arbitrum.png",
    "aurora": "images/aurora.png",
    "avalanche": "images/avalanche.png",
    "base": "images/base.png",
    "berachain": "images/berachain.png",
    "blast": "images/blast.png",
    "boba": "images/boba.png",
    "bsc": "images/bsc.png",
    "celo": "images/celo.png",
    "chiliz": "images/chiliz.png",
    "corn": "images/corn.png",
    "eos": "images/eos.png",
    "etherlink": "images/etherlink.png",
    "fantom": "images/fantom.png",
    "fraxtal": "images/fraxtal.png",
    "fuji": "images/fuji.png",
    "fuse": "images/fuse.png",
    "gnosis": "images/gnosis.png",
    "harmony": "images/harmony.png",
    "hemi": "images/hemi.png",
    "injective": "images/injective.png",
    "ink": "images/ink.png",
    "iotex": "images/iotex.png",
    "kaia": "images/kaia.png",
    "kroma": "images/kroma.png",
    "kylin": "images/kylin.png",
    "lens": "images/lens.png",
    "lens-2": "images/lens-2.png",
    "linea": "images/linea.png",
    "mainnet": "images/ethereum.png",
    "mantle": "images/mantle.png",
    "matic": "images/polygon.png",
    "monad": "images/monad.png",
    "moonbeam": "images/moonbeam.png",
    "near": "images/near.png",
    "optimism": "images/optimism.png",
    "polygon-zkevm": "images/polygon-zkevm.png",
    "redstone": "images/redstone.png",
    "rootstock": "images/rootstock.png",
    "scroll": "images/scroll.png",
    "sei": "images/sei.png",
    "sepolia": "images/sepolia.png",
    "soneium": "images/soneium.png",
    "sonic": "images/abstract.png",
    "unichain": "images/unichain.png",
    "vana": "images/vana.png",
    "wax": "images/wax.png",
    "zkfair": "images/zkfair.png",
    "zksync-era": "images/zksync-era.png",
    "zetachain": "images/zetachain.png"
}


def log_message(message: str):
    """Log a timestamped message to console."""
    timestamped = f"[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] {message}"
    print(timestamped)


def fetch_network_subgraph_counts(api_key: str) -> List[NetworkIndexerData]:
    """
    Fetch network names and count subgraphs and unique indexers per network.
    
    Args:
        api_key: The Graph API key
        
    Returns:
        List of NetworkIndexerData objects
    """
    url = f"https://gateway.thegraph.com/api/{api_key}/subgraphs/id/DZz4kDTdmzWLWsV373w2bSmoar3umKKH9y82SUKr5qmp"
    headers = {"Content-Type": "application/json"}
    counts = {}
    indexers_by_network = {}
    skip = 0
    page_size = 1000

    log_message("Fetching network subgraph counts...")
    
    while True:
        query = f"""{{
            subgraphs(first: {page_size}, skip: {skip}, where: {{ currentVersion_not: null }}) {{
                id
                currentVersion {{
                    subgraphDeployment {{
                        manifest {{
                            network
                        }}
                        indexerAllocations(first: 1000, where: {{ status: Active }}) {{
                            indexer {{
                                id
                            }}
                        }}
                    }}
                }}
            }}
        }}"""

        response = requests.post(url, json={"query": query}, headers=headers)

        if response.status_code != 200:
            log_message(f"Failed to fetch data: {response.status_code}")
            break

        batch = response.json().get("data", {}).get("subgraphs", [])
        if not batch:
            break

        for item in batch:
            deployment = item.get("currentVersion", {}).get("subgraphDeployment", {})
            manifest = deployment.get("manifest")
            if not manifest:
                continue
            network = manifest.get("network")
            if not network:
                continue
            counts[network] = counts.get(network, 0) + 1
            
            # Process indexer allocations
            allocations = deployment.get("indexerAllocations", [])
            if network not in indexers_by_network:
                indexers_by_network[network] = set()
            for alloc in allocations:
                indexer = alloc.get("indexer")
                if indexer and "id" in indexer:
                    indexers_by_network[network].add(indexer["id"])

        skip += page_size

    result = []
    for network, subgraph_count in counts.items():
        unique_indexer_count = len(indexers_by_network.get(network, set()))
        result.append(NetworkIndexerData(
            network_name=network,
            subgraph_count=subgraph_count,
            unique_indexer_count=unique_indexer_count
        ))
    
    log_message(f"Fetched subgraph and indexer counts for {len(result)} networks.")
    return result


def generate_html_dashboard(data: List[NetworkIndexerData], output_path: str = "index.html"):
    """
    Generate HTML dashboard with network metrics.
    
    Args:
        data: List of NetworkIndexerData objects
        output_path: Path to save the HTML file
    """
    # Calculate total across all networks
    total_all_networks = sum(entry.subgraph_count for entry in data)
    
    # Sort by subgraph count and get top 20
    sorted_data = sorted(data, key=lambda x: x.subgraph_count, reverse=True)[:20]
    total_top_20 = sum(entry.subgraph_count for entry in sorted_data)
    
    # Calculate percentage
    percentage = (total_top_20 / total_all_networks * 100) if total_all_networks > 0 else 0
    
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Real-time dashboard showing The Graph Protocol metrics across the top 20 blockchain networks.">
    <meta name="robots" content="index, follow">
    
    <meta property="og:title" content="The Graph Protocol Metrics Dashboard">
    <meta property="og:description" content="Explore network metrics for The Graph Protocol's top 20 networks including subgraph counts and unique indexers.">
    <meta property="og:type" content="website">
    
    <title>The Graph Protocol Metrics</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0C0A1D;
            min-height: 100vh;
            padding: 20px;
            color: #F8F6FF;
        }}
        
        .breadcrumb {{
            max-width: 1200px;
            margin: 0 auto 15px auto;
            padding: 12px 20px;
            background: rgba(12, 10, 29, 0.6);
            border-radius: 8px;
            border: 1px solid #9CA3AF;
            color: #F8F6FF;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .breadcrumb a {{
            color: #9CA3AF;
            text-decoration: none;
            transition: color 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        
        .breadcrumb a:hover {{
            color: #F8F6FF;
        }}
        
        .breadcrumb-separator {{
            color: #9CA3AF;
            margin: 0 4px;
            font-weight: 300;
        }}
        
        .home-icon {{
            width: 16px;
            height: 16px;
            display: inline-block;
            position: relative;
        }}
        
        .home-icon::before {{
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-bottom: 8px solid currentColor;
        }}
        
        .home-icon::after {{
            content: '';
            position: absolute;
            left: 2px;
            bottom: 0;
            width: 12px;
            height: 9px;
            background-color: currentColor;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: #0C0A1D;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            overflow: hidden;
            border: 1px solid #9CA3AF;
        }}
        
        .header {{
            background: #0C0A1D;
            color: #F8F6FF;
            padding: 30px;
            border-bottom: 1px solid #9CA3AF;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.2em;
            margin: 0 0 10px 0;
            font-weight: 500;
        }}
        
        .header .subtitle {{
            font-size: 0.95em;
            opacity: 0.8;
            font-weight: 300;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .stats-container {{
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            justify-content: flex-start;
            flex-wrap: wrap;
        }}
        
        .stats-card {{
            background: rgba(12, 10, 29, 0.6);
            border: 1px solid #9CA3AF;
            border-radius: 10px;
            padding: 15px 20px;
            text-align: center;
            flex: 0 0 200px;
            height: 180px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        .stats-card h2 {{
            font-size: 0.95em;
            margin: 0 0 20px 0;
            padding-top: 5px;
            color: #F8F6FF;
            font-weight: 400;
            line-height: 1.2;
            min-height: 2.4em;
            display: flex;
            align-items: flex-start;
            justify-content: center;
        }}
        
        .stats-card .total {{
            font-size: 2em;
            color: #4CAF50;
            font-weight: 600;
            margin: 0 0 20px 0;
            line-height: 1;
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .stats-card .percentage {{
            font-size: 0.85em;
            color: #9CA3AF;
            margin: 0;
            padding-bottom: 5px;
            min-height: 1.5em;
            display: flex;
            align-items: flex-end;
            justify-content: center;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: rgba(12, 10, 29, 0.4);
            border: 1px solid #9CA3AF;
            border-radius: 10px;
            overflow: hidden;
        }}
        
        th {{
            background: rgba(12, 10, 29, 0.8);
            color: #F8F6FF;
            padding: 15px;
            text-align: left;
            font-weight: 500;
            border-bottom: 1px solid #9CA3AF;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid rgba(156, 163, 175, 0.3);
        }}
        
        tr:last-child td {{
            border-bottom: none;
        }}
        
        tr:hover {{
            background: rgba(248, 246, 255, 0.05);
        }}
        
        .network-name {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .network-logo {{
            width: 24px;
            height: 24px;
            object-fit: contain;
        }}
        
        .rank {{
            background: rgba(156, 163, 175, 0.3);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
            min-width: 35px;
            text-align: center;
            display: inline-block;
        }}
        
        .footer {{
            padding: 20px 30px;
            background: #0C0A1D;
            color: #9CA3AF;
            margin-top: 30px;
            border-top: 1px solid #9CA3AF;
        }}
        
        .footer-content {{
            max-width: 1140px;
            margin: 0 auto;
        }}
        
        .footer-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            flex-wrap: wrap;
            gap: 15px;
        }}
        
        .footer-left {{
            text-align: left;
            flex: 0 0 auto;
        }}
        
        .footer-right {{
            text-align: right;
            flex: 0 0 auto;
        }}
        
        .footer a {{
            color: #9CA3AF;
            text-decoration: none;
            transition: color 0.3s ease;
        }}
        
        .footer a:hover {{
            color: #F8F6FF;
            text-decoration: underline;
        }}
        
        .version {{
            font-size: 0.9em;
            opacity: 0.8;
        }}
        
        .footer-separator {{
            color: #9CA3AF;
        }}
        
        .github-icon {{
            width: 16px;
            height: 16px;
            vertical-align: middle;
            margin-right: 4px;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.5em;
            }}
            
            .stats-container {{
                flex-direction: column;
                align-items: center;
            }}
            
            .stats-card {{
                width: 100%;
                max-width: 300px;
            }}
            
            .footer-top {{
                flex-direction: column;
                align-items: flex-start;
                gap: 12px;
            }}
            
            .footer-left,
            .footer-right {{
                text-align: left;
                width: 100%;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            th, td {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="breadcrumb">
        <a href="../index.html">
            <span class="home-icon"></span>
            <b>Home</b>
        </a>
        <span class="breadcrumb-separator">>></span>
        <span>The Graph Protocol Metrics</span>
    </div>
    
    <div class="container">
        <div class="header">
            <h1>The Graph Protocol Metrics</h1>
        </div>
        
        <div class="content">
            <div class="stats-container">
                <div class="stats-card">
                    <h2>Total Subgraphs<br/>(Top 20 Chains)</h2>
                    <div class="total">{total_top_20:,}</div>
                    <div class="percentage">{percentage:.1f}% of total</div>
                </div>
                <div class="stats-card">
                    <h2>Total Subgraphs<br/>(All Networks)</h2>
                    <div class="total">{total_all_networks:,}</div>
                </div>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th style="width: 10%;">Rank</th>
                        <th style="width: 40%;">Network</th>
                        <th style="width: 25%;">Subgraph Count</th>
                        <th style="width: 25%;">Unique Indexers</th>
                    </tr>
                </thead>
                <tbody>
"""
    
    # Add table rows
    for idx, entry in enumerate(sorted_data, 1):
        logo = NETWORK_LOGOS.get(entry.network_name.lower(), "")
        logo_html = f'<img src="{logo}" alt="{entry.network_name}" class="network-logo" onerror="this.style.display=\'none\'" />' if logo else ""
        
        # Format network name
        if entry.network_name.lower() == "mainnet":
            name = "Ethereum (Mainnet)"
        elif entry.network_name.lower() == "matic":
            name = "Polygon (Matic)"
        else:
            name = entry.network_name.title()
        
        html_content += f"""
                    <tr>
                        <td><span class="rank">#{idx}</span></td>
                        <td>
                            <div class="network-name">
                                {logo_html}
                                <a href="https://thegraph.com/explorer?indexedNetwork={entry.network_name}&orderBy=Query+Count&orderDirection=desc" 
                                   target="_blank" style="color: #F8F6FF; text-decoration: none;">
                                    {name}
                                </a>
                            </div>
                        </td>
                        <td>{entry.subgraph_count:,}</td>
                        <td>{entry.unique_indexer_count}</td>
                    </tr>
"""
    
    html_content += f"""
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <div class="footer-content">
                <div class="footer-top">
                    <div class="footer-left">
                        Generated on: {timestamp}
                    </div>
                    <div class="footer-right">
                        <span class="version">v{VERSION}</span>
                        <span class="footer-separator">-</span>
                        <svg class="github-icon" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg><a href="https://github.com/pdiomede/metrics" target="_blank">View repo on GitHub</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    log_message(f"Dashboard saved to {output_path}")


def main():
    """Main execution function."""
    log_message("Starting The Graph Protocol Metrics Dashboard Generator...")
    log_message(f"Version: v{VERSION}")
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GRAPH_API_KEY")
    
    if not api_key:
        log_message("ERROR: GRAPH_API_KEY not found in environment variables")
        log_message("Please create a .env file with GRAPH_API_KEY=your_api_key")
        return
    
    # Fetch network data
    network_data = fetch_network_subgraph_counts(api_key)
    
    if not network_data:
        log_message("ERROR: No data retrieved")
        return
    
    # Generate HTML dashboard
    generate_html_dashboard(network_data)
    
    log_message("Dashboard generation completed successfully!")


if __name__ == "__main__":
    main()
