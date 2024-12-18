#!/usr/bin/env python3

"""
Script to plot the locations of the Educause annual meetings on a map of the US.

Usage:
    python educause_meetings_map.py --output filename --format pdf
"""

import argparse
import os
import sys
from typing import List, Tuple

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Data for Educause annual meetings
meetings: List[Tuple[int, str]] = [
    (1999, 'Long Beach, California'),
    (2000, 'Nashville, Tennessee'),
    (2001, 'Indianapolis, Indiana'),
    (2002, 'Atlanta, Georgia'),
    (2003, 'Anaheim, California'),
    (2004, 'Denver, Colorado'),
    (2005, 'Orlando, Florida'),
    (2006, 'Dallas, Texas'),
    (2007, 'Seattle, Washington'),
    (2008, 'Orlando, Florida'),
    (2009, 'Denver, Colorado'),
    (2010, 'Anaheim, California'),
    (2011, 'Philadelphia, Pennsylvania'),
    (2012, 'Denver, Colorado'),
    (2013, 'Anaheim, California'),
    (2014, 'Orlando, Florida'),
    (2015, 'Indianapolis, Indiana'),
    (2016, 'Anaheim, California'),
    (2017, 'Philadelphia, Pennsylvania'),
    (2018, 'Denver, Colorado'),
    (2019, 'Chicago, Illinois'),
    # Skip 2020 as it was virtual due to COVID-19
    (2021, 'Philadelphia, Pennsylvania'),
    (2022, 'Denver, Colorado'),
    (2023, 'Chicago, Illinois'),
    (2024, 'San Antonio, Texas'),
]

# Mapping of cities to their latitude and longitude
city_coords = {
    'Long Beach, California': (33.7701, -118.1937),
    'Nashville, Tennessee': (36.1627, -86.7816),
    'Indianapolis, Indiana': (39.7684, -86.1581),
    'Atlanta, Georgia': (33.7490, -84.3880),
    'Anaheim, California': (33.8366, -117.9143),
    'Denver, Colorado': (39.7392, -104.9903),
    'Orlando, Florida': (28.5383, -81.3792),
    'Dallas, Texas': (32.7767, -96.7970),
    'Seattle, Washington': (47.6062, -122.3321),
    'Philadelphia, Pennsylvania': (39.9526, -75.1652),
    'Chicago, Illinois': (41.8781, -87.6298),
    'San Antonio, Texas': (29.4241, -98.4936),
}

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Plot the locations of the Educause annual meetings on a US map.'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='educause_meetings_map',
        help='Output filename without extension (default: educause_meetings_map)'
    )
    parser.add_argument(
        '--format', '-f',
        type=str,
        choices=['pdf', 'png', 'jpg'],
        default='pdf',
        help='Output file format (default: pdf)'
    )
    return parser.parse_args()

def confirm_overwrite(filepath: str) -> bool:
    """
    Ask for confirmation before overwriting an existing file.

    Args:
        filepath (str): Path to the file.

    Returns:
        bool: True if overwrite is confirmed, False otherwise.
    """
    if os.path.exists(filepath):
        response = input(f'File "{filepath}" exists. Overwrite? (y/n): ').lower()
        return response == 'y'
    return True

def get_coordinates(meetings: List[Tuple[int, str]]) -> Tuple[List[float], List[float], List[int], List[str]]:
    """
    Get the latitude and longitude for each meeting location.

    Args:
        meetings (List[Tuple[int, str]]): List of meetings with year and location.

    Returns:
        Tuple containing lists of latitudes, longitudes, years, and locations.
    """
    lats = []
    lons = []
    years = []
    locations = []

    for year, location in meetings:
        if location == 'Virtual due to COVID-19':
            continue
        coords = city_coords.get(location)
        if coords:
            lat, lon = coords
            lats.append(lat)
            lons.append(lon)
            years.append(year)
            locations.append(location)
        else:
            print(f'Coordinates for {location} not found.')
    return lats, lons, years, locations

def plot_meetings(lats: List[float], lons: List[float], years: List[int], locations: List[str]) -> None:
    """
    Plot the meeting locations on the map with annotations and arrows.

    Args:
        lats (List[float]): List of latitudes.
        lons (List[float]): List of longitudes.
        years (List[int]): List of years.
        locations (List[str]): List of locations.
    """
    plt.figure(figsize=(15, 10))
    ax = plt.axes(projection=ccrs.LambertConformal())
    ax.set_extent([-125, -66.5, 20, 50], crs=ccrs.Geodetic())

    # Add features
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)
    ax.coastlines(resolution='50m')

    # Plot the points and annotations
    for i in range(len(lats)):
        ax.plot(lons[i], lats[i], 'ro', markersize=5, transform=ccrs.Geodetic())
        ax.text(
            lons[i] + 0.5,
            lats[i] + 0.5,
            f'{years[i]}: {locations[i]}',
            transform=ccrs.Geodetic()
        )

        # Draw arrows between points
        if i > 0:
            ax.annotate(
                '',
                xy=(lons[i], lats[i]),
                xytext=(lons[i-1], lats[i-1]),
                arrowprops=dict(arrowstyle='->', color='blue'),
                transform=ccrs.Geodetic()
            )

    plt.title('Educause Annual Meeting Locations (1999-2024)')
    plt.show()

def main() -> None:
    """
    Main function to execute the script.
    """
    args = parse_arguments()
    output_file = f'{args.output}.{args.format}'

    if not confirm_overwrite(output_file):
        print('Operation cancelled by the user.')
        sys.exit(0)

    lats, lons, years, locations = get_coordinates(meetings)

    # Create the plot
    plt.figure(figsize=(15, 10))
    ax = plt.axes(projection=ccrs.LambertConformal())
    ax.set_extent([-125, -66.5, 20, 50], crs=ccrs.Geodetic())

    # Add features
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)
    ax.coastlines(resolution='50m')

    # Plot the points and annotations
    for i in range(len(lats)):
        ax.plot(lons[i], lats[i], 'ro', markersize=5, transform=ccrs.Geodetic())
        ax.text(
            lons[i] + 0.5,
            lats[i] + 0.5,
            f'{years[i]}: {locations[i]}',
            transform=ccrs.Geodetic()
        )

        # Draw arrows between points
        if i > 0:
            ax.annotate(
                '',
                xy=(lons[i], lats[i]),
                xytext=(lons[i-1], lats[i-1]),
                arrowprops=dict(arrowstyle='->', color='blue'),
                transform=ccrs.Geodetic()
            )

    plt.title('Educause Annual Meeting Locations (1999-2024)')
    plt.savefig(output_file, format=args.format)
    print(f'Map saved to {output_file}')

if __name__ == '__main__':
    main()
