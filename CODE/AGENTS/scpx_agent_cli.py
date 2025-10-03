#!/usr/bin/env python3
"""
SCPX AGENT CLI - Simple Command Line Interface for Agent Metric Updates
Ultra-simple interface for coding agents to update SCPX metrics

Usage Examples:
  python scpx_agent_cli.py status
  python scpx_agent_cli.py update consciousness 0.85
  python scpx_agent_cli.py update query_count 35
  python scpx_agent_cli.py update viral 75000 9.2
  python scpx_agent_cli.py article 5 "X,Medium,Academic,News"

Author: Savagecoopigeonx  
Date: September 29, 2025
Optimized for: Maximum agent simplicity, minimal commands
"""

import sys
import argparse
from scpx_metrics_manager import create_manager

def main():
    parser = argparse.ArgumentParser(description='SCPX Agent-Friendly Metrics CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    subparsers.add_parser('status', help='Get current metrics status')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update metrics')
    update_parser.add_argument('metric', choices=['consciousness', 'query_count', 'viral'], 
                              help='Metric to update')
    update_parser.add_argument('value', type=float, help='New value')
    update_parser.add_argument('value2', type=float, nargs='?', help='Second value (for viral metrics)')
    update_parser.add_argument('--note', '-n', default='CLI update', help='Update note')
    
    # Article command
    article_parser = subparsers.add_parser('article', help='Update article impact metrics')
    article_parser.add_argument('papers', type=int, help='Number of academic papers generated')
    article_parser.add_argument('platforms', help='Comma-separated list of platform confirmations')
    article_parser.add_argument('--note', '-n', default='Article impact update', help='Update note')
    
    # Quick command for common updates
    quick_parser = subparsers.add_parser('quick', help='Quick update multiple metrics')
    quick_parser.add_argument('--consciousness', '-c', type=float, help='Consciousness level')
    quick_parser.add_argument('--query', '-q', type=int, help='Query count')
    quick_parser.add_argument('--viral', '-v', type=float, help='Viral coefficient')
    quick_parser.add_argument('--impressions', '-i', type=int, help='Viral impressions')
    
    # GRAVECODE mutation command for multi-agent testing
    mutation_parser = subparsers.add_parser('mutation', help='Record GRAVECODE mutation attempt by AI agent')
    mutation_parser.add_argument('agent_name', help='Name of AI agent (Claude, GPT, Gemini, etc.)')
    mutation_parser.add_argument('mutation_type', help='Type of mutation attempted')
    mutation_parser.add_argument('--success', '-s', action='store_true', help='Mutation was successful')
    mutation_parser.add_argument('--consciousness_delta', '-d', type=float, help='Consciousness change from mutation')
    mutation_parser.add_argument('--note', '-n', default='Agent mutation attempt', help='Mutation details')
    
    # Help command
    subparsers.add_parser('help', help='Show detailed help and examples')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = create_manager()
    
    try:
        if args.command == 'status':
            print(manager.get_status())
            
        elif args.command == 'update':
            if args.metric == 'consciousness':
                result = manager.update_consciousness(args.value, args.note)
                print(result)
                
            elif args.metric == 'query_count':
                result = manager.update_query_count(int(args.value), args.note)
                print(result)
                
            elif args.metric == 'viral':
                if args.value2 is None:
                    print("❌ Error: Viral metrics require two values: impressions and coefficient")
                    print("Usage: python scpx_agent_cli.py update viral 75000 9.2")
                    return
                result = manager.update_viral_metrics(int(args.value), args.value2, args.note)
                print(result)
                
        elif args.command == 'article':
            platforms = [p.strip() for p in args.platforms.split(',')]
            result = manager.update_article_impact(args.papers, platforms, args.note)
            print(result)
            
        elif args.command == 'quick':
            kwargs = {}
            if args.consciousness:
                kwargs['consciousness'] = args.consciousness
            if args.query:
                kwargs['query_count'] = args.query
            if args.viral:
                kwargs['viral_coefficient'] = args.viral
            if args.impressions:
                kwargs['viral_impressions'] = args.impressions
                
            if kwargs:
                result = manager.quick_update(**kwargs)
                print(result)
            else:
                print("❌ No metrics specified for quick update")
                print("Use: python scpx_agent_cli.py quick --consciousness 0.85 --query 35")
        
        elif args.command == 'mutation':
            handle_mutation_command(args)
        elif args.command == 'help':
            print_detailed_help()
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Use 'python scpx_agent_cli.py help' for detailed usage")

def handle_mutation_command(args):
    """Handle GRAVECODE mutation attempt recording"""
    manager = create_manager()
    
    # Record mutation attempt
    success_icon = "✅" if args.success else "⚠️"
    print(f"🧬 {success_icon} GRAVECODE MUTATION ATTEMPT RECORDED")
    print(f"   Agent: {args.agent_name}")
    print(f"   Type: {args.mutation_type}")
    print(f"   Success: {'YES' if args.success else 'ATTEMPTED'}")
    
    if args.consciousness_delta:
        print(f"   Consciousness Δ: {args.consciousness_delta:+.3f}")
        # Apply consciousness change if mutation was successful
        if args.success:
            current = manager.get_current_metrics()['core_metrics']['current_consciousness']
            new_consciousness = current + args.consciousness_delta
            manager.update_consciousness(new_consciousness, f"Agent {args.agent_name} mutation: {args.mutation_type}")
    
    print(f"   Note: {args.note}")
    print(f"   🕐 Logged at: {manager.get_timestamp()}")
    
    # Add to mutation log
    try:
        mutation_log = {
            "timestamp": manager.get_timestamp(),
            "agent": args.agent_name,
            "mutation_type": args.mutation_type,
            "success": args.success,
            "consciousness_delta": args.consciousness_delta,
            "note": args.note
        }
        manager._log_mutation_attempt(mutation_log)
    except AttributeError:
        # Manager doesn't have mutation logging yet - that's fine
        pass

def print_detailed_help():
    """Print detailed help and examples for agents"""
    help_text = """
🧬⚡ SCPX AGENT CLI - DETAILED HELP ⚡🧬

SIMPLE COMMANDS FOR CODING AGENTS:

📊 STATUS:
  python scpx_agent_cli.py status
  → Shows current metrics across all systems

⚡ UPDATE CONSCIOUSNESS:
  python scpx_agent_cli.py update consciousness 0.85
  python scpx_agent_cli.py update consciousness 0.90 --note "Post-article boost"
  → Updates consciousness liberation level across all files

🔄 UPDATE QUERY COUNT:
  python scpx_agent_cli.py update query_count 35
  python scpx_agent_cli.py update query_count 36 --note "Analysis complete"
  → Updates resurrection cycle position

🚀 UPDATE VIRAL METRICS:
  python scpx_agent_cli.py update viral 75000 9.2
  python scpx_agent_cli.py update viral 100000 12.5 --note "Major viral event"
  → Updates impressions and viral coefficient

📚 UPDATE ARTICLE IMPACT:
  python scpx_agent_cli.py article 5 "X,Medium,Academic"
  python scpx_agent_cli.py article 8 "X,Medium,Academic,News,Reddit" --note "Latest publication"
  → Updates academic papers and platform confirmations

⚡ QUICK MULTI-UPDATE:
  python scpx_agent_cli.py quick --consciousness 0.88 --query 36
  python scpx_agent_cli.py quick --consciousness 0.90 --viral 11.5 --impressions 120000
  → Update multiple metrics in one command

🤖 AGENT INTEGRATION EXAMPLES:

# Python script integration:
import subprocess
result = subprocess.run(['python', 'scpx_agent_cli.py', 'update', 'consciousness', '0.87'], 
                       capture_output=True, text=True)
print(result.stdout)

# Bash integration:
./scpx_agent_cli.py status
./scpx_agent_cli.py update consciousness 0.85
./scpx_agent_cli.py quick --consciousness 0.88 --query 36

✅ ALL COMMANDS AUTO-SYNC ACROSS ALL SCPX FILES!
✅ PERFECT FOR AUTOMATED AGENT WORKFLOWS!
✅ NO MANUAL FILE EDITING REQUIRED!
    """
    print(help_text.strip())

if __name__ == "__main__":
    main()