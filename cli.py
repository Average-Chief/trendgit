import argparse
import sys

from utils import print_repos
from api import fetch_repos

def main():
    parser = argparse.ArgumentParser(description="🔥 GitHub Trending Repositories CLI")

    parser.add_argument(
        "--duration", 
        choices=["day","week","month","year"],
        default = "week",
        help = "Time range for trending repositories"
    )

    parser.add_argument(
        "--limit",
        type = int,
        default = 10,
        help = "Number of repositories to display"
    )

    args = parser.parse_args()

    if args.limit <= 0:
        print("❌ Limit must be a positive number")
        sys.exit(1)
    
    try:
        repos = fetch_repos(args.duration,args.limit)
        print_repos(repos)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()