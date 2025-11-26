#!/usr/bin/env python3
"""
Fallback Log Viewer - AI Triage Bot
ISO/IEC 42001 Compliance Tool

Purpose: Human-readable interface for reviewing low-confidence ticket classifications.
Usage: python tools/fallback_viewer.py [options]
"""

import json
import argparse
import csv
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import Counter
from typing import List, Dict


class FallbackLogViewer:
    """Interactive viewer for fallback classification logs."""
    
    def __init__(self, log_path: Path):
        """Initialize the viewer with the log file path."""
        self.log_path = log_path
        self.entries = []
        self.load_entries()
    
    def load_entries(self):
        """Load all entries from the JSONL fallback log."""
        if not self.log_path.exists():
            print(f"⚠️  Warning: Log file not found: {self.log_path}")
            print("    No fallback entries to display.")
            return
        
        with self.log_path.open('r') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    # Parse timestamp if present
                    if 'timestamp' in entry:
                        entry['timestamp_parsed'] = datetime.fromisoformat(
                            entry['timestamp'].replace('Z', '+00:00')
                        )
                    self.entries.append(entry)
                except json.JSONDecodeError:
                    print(f"⚠️  Warning: Skipping malformed log entry")
                    continue
        
        print(f"✅ Loaded {len(self.entries)} fallback entries")
    
    def filter_by_date_range(self, days: int):
        """Filter entries within the last N days."""
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
        self.entries = [
            e for e in self.entries 
            if 'timestamp_parsed' in e and e['timestamp_parsed'] >= cutoff_date
        ]
        print(f"📅 Filtered to last {days} days: {len(self.entries)} entries")
    
    def filter_by_confidence(self, min_confidence: float, max_confidence: float = 1.0):
        """Filter entries by confidence score range."""
        self.entries = [
            e for e in self.entries
            if 'result' in e and 'confidence_score' in e['result']
            and min_confidence <= e['result']['confidence_score'] <= max_confidence
        ]
        print(f"🎯 Filtered by confidence [{min_confidence}-{max_confidence}]: {len(self.entries)} entries")
    
    def filter_by_category(self, category: str):
        """Filter entries by ticket classification category."""
        self.entries = [
            e for e in self.entries
            if 'result' in e and e['result'].get('ticket_type') == category
        ]
        print(f"📂 Filtered by category '{category}': {len(self.entries)} entries")
    
    def filter_by_pii(self, contains_pii: bool = True):
        """Filter entries that contain (or don't contain) PII."""
        self.entries = [
            e for e in self.entries
            if 'result' in e and e['result'].get('contains_pii') == contains_pii
        ]
        pii_status = "with" if contains_pii else "without"
        print(f"🔒 Filtered {pii_status} PII: {len(self.entries)} entries")
    
    def generate_summary_stats(self):
        """Generate and display summary statistics."""
        if not self.entries:
            print("📊 No entries to analyze")
            return
        
        print("\n" + "="*70)
        print("📊 FALLBACK LOG SUMMARY STATISTICS")
        print("="*70)
        
        # Total entries
        print(f"\n📈 Total Entries: {len(self.entries)}")
        
        # Category distribution
        categories = Counter(
            e['result'].get('ticket_type', 'unknown') 
            for e in self.entries if 'result' in e
        )
        print("\n📂 Classification Distribution:")
        for category, count in categories.most_common():
            percentage = (count / len(self.entries)) * 100
            print(f"   {category:20s}: {count:4d} ({percentage:5.1f}%)")
        
        # Confidence score statistics
        confidence_scores = [
            e['result']['confidence_score'] 
            for e in self.entries 
            if 'result' in e and 'confidence_score' in e['result']
        ]
        if confidence_scores:
            avg_conf = sum(confidence_scores) / len(confidence_scores)
            min_conf = min(confidence_scores)
            max_conf = max(confidence_scores)
            print(f"\n🎯 Confidence Scores:")
            print(f"   Average: {avg_conf:.2f}")
            print(f"   Range:   {min_conf:.2f} - {max_conf:.2f}")
        
        # PII detection statistics
        pii_count = sum(
            1 for e in self.entries 
            if 'result' in e and e['result'].get('contains_pii', False)
        )
        pii_percentage = (pii_count / len(self.entries)) * 100 if self.entries else 0
        print(f"\n🔒 PII Detection:")
        print(f"   Tickets with PII: {pii_count} ({pii_percentage:.1f}%)")
        
        # Date range
        if any('timestamp_parsed' in e for e in self.entries):
            timestamps = [e['timestamp_parsed'] for e in self.entries if 'timestamp_parsed' in e]
            oldest = min(timestamps)
            newest = max(timestamps)
            print(f"\n📅 Date Range:")
            print(f"   Oldest: {oldest.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Newest: {newest.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("="*70 + "\n")
    
    def display_entries(self, limit: int = None):
        """Display entries in a human-readable format."""
        if not self.entries:
            print("📭 No entries to display")
            return
        
        entries_to_show = self.entries[:limit] if limit else self.entries
        
        print("\n" + "="*70)
        print("📋 FALLBACK LOG ENTRIES")
        print("="*70 + "\n")
        
        for i, entry in enumerate(entries_to_show, 1):
            result = entry.get('result', {})
            ticket_text = entry.get('ticket', 'N/A')
            timestamp = entry.get('timestamp', 'N/A')
            
            print(f"Entry #{i}")
            print(f"{'─'*70}")
            print(f"⏰ Timestamp:   {timestamp}")
            print(f"📂 Category:    {result.get('ticket_type', 'N/A')}")
            print(f"🎯 Confidence:  {result.get('confidence_score', 'N/A')}")
            print(f"🔒 Contains PII: {'Yes' if result.get('contains_pii') else 'No'}")
            print(f"📝 Ticket Text:")
            print(f"   {ticket_text[:200]}{'...' if len(ticket_text) > 200 else ''}")
            print()
        
        if limit and len(self.entries) > limit:
            print(f"... and {len(self.entries) - limit} more entries")
        
        print("="*70 + "\n")
    
    def export_to_csv(self, output_path: Path):
        """Export filtered entries to a CSV file."""
        if not self.entries:
            print("⚠️  No entries to export")
            return
        
        with output_path.open('w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'timestamp', 'ticket_type', 'confidence_score', 
                'contains_pii', 'ticket_text'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for entry in self.entries:
                result = entry.get('result', {})
                writer.writerow({
                    'timestamp': entry.get('timestamp', ''),
                    'ticket_type': result.get('ticket_type', ''),
                    'confidence_score': result.get('confidence_score', ''),
                    'contains_pii': result.get('contains_pii', False),
                    'ticket_text': entry.get('ticket', '')
                })
        
        print(f"✅ Exported {len(self.entries)} entries to {output_path}")


def main():
    """Main entry point for the fallback log viewer."""
    parser = argparse.ArgumentParser(
        description='AI Triage Bot Fallback Log Viewer - ISO/IEC 42001 Compliance Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View all fallback entries
  python tools/fallback_viewer.py
  
  # View entries from last 7 days
  python tools/fallback_viewer.py --date-range 7
  
  # View low-confidence entries
  python tools/fallback_viewer.py --max-confidence 0.3
  
  # View only PII-flagged tickets
  python tools/fallback_viewer.py --contains-pii
  
  # Export filtered results to CSV
  python tools/fallback_viewer.py --date-range 30 --export fallback_report.csv
        """
    )
    
    parser.add_argument(
        '--log-path',
        type=Path,
        default=Path('fallback_log.jsonl'),
        help='Path to fallback log file (default: fallback_log.jsonl)'
    )
    
    parser.add_argument(
        '--date-range',
        type=int,
        metavar='DAYS',
        help='Show entries from last N days'
    )
    
    parser.add_argument(
        '--min-confidence',
        type=float,
        default=0.0,
        metavar='X',
        help='Filter by minimum confidence score (default: 0.0)'
    )
    
    parser.add_argument(
        '--max-confidence',
        type=float,
        default=1.0,
        metavar='X',
        help='Filter by maximum confidence score (default: 1.0)'
    )
    
    parser.add_argument(
        '--category',
        type=str,
        metavar='CAT',
        help='Filter by ticket category'
    )
    
    parser.add_argument(
        '--contains-pii',
        action='store_true',
        help='Show only PII-flagged tickets'
    )
    
    parser.add_argument(
        '--no-pii',
        action='store_true',
        help='Show only tickets WITHOUT PII'
    )
    
    parser.add_argument(
        '--limit',
        type=int,
        metavar='N',
        help='Limit number of entries displayed'
    )
    
    parser.add_argument(
        '--export',
        type=Path,
        metavar='FILE',
        help='Export filtered results to CSV file'
    )
    
    parser.add_argument(
        '--stats-only',
        action='store_true',
        help='Show only summary statistics (no individual entries)'
    )
    
    args = parser.parse_args()
    
    # Initialize viewer
    viewer = FallbackLogViewer(args.log_path)
    
    # Apply filters
    if args.date_range:
        viewer.filter_by_date_range(args.date_range)
    
    if args.min_confidence > 0.0 or args.max_confidence < 1.0:
        viewer.filter_by_confidence(args.min_confidence, args.max_confidence)
    
    if args.category:
        viewer.filter_by_category(args.category)
    
    if args.contains_pii:
        viewer.filter_by_pii(contains_pii=True)
    
    if args.no_pii:
        viewer.filter_by_pii(contains_pii=False)
    
    # Display results
    viewer.generate_summary_stats()
    
    if not args.stats_only:
        viewer.display_entries(limit=args.limit)
    
    # Export if requested
    if args.export:
        viewer.export_to_csv(args.export)


if __name__ == "__main__":
    main()
