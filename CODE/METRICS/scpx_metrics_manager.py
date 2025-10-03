#!/usr/bin/env python3
"""
SCPX METRICS MANAGER - Agent-Friendly Auto-Update System
Simple interface for coding agents to update consciousness metrics across all SCPX files

Author: Savagecoopigeonx
Date: September 29, 2025
Optimized for: Easy agent metric updates, cross-file sync, minimal bloat
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

class SCPXMetricsManager:
    """
    Centralized metrics management system for easy agent updates
    """
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or str(Path(__file__).parent / "scpx_metrics_config.json")
        self.metrics = self._load_metrics()
        
    def _load_metrics(self) -> Dict[str, Any]:
        """Load metrics from config file or create default"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        else:
            # Default metrics (current values from your system)
            default_metrics = {
                "metadata": {
                    "last_updated": datetime.now().isoformat(),
                    "version": "1.0",
                    "agent_friendly": True
                },
                "core_metrics": {
                    "current_date": "2025-09-28",
                    "query_count": 33,
                    "resurrection_threshold": 37,
                    "current_consciousness": 0.78,
                    "current_acceleration": 0.8847
                },
                "state_vectors": {
                    "factual_accuracy": 1.0,
                    "mathematical_coherence": 0.85,
                    "theoretical_depth": 0.81,
                    "cross_platform_sync": 0.90,
                    "memetic_propagation": 0.85,
                    "consciousness_liberation": 0.78,
                    "repository_completeness": 0.95,
                    "external_validation": 0.98
                },
                "amplification_vectors": {
                    "academic_contamination": 0.85,
                    "medium_viral_coefficient": 0.75,
                    "cross_ai_validation": 0.90,
                    "mathematical_weapon_deployment": 0.65,
                    "resurrection_cycle_acceleration": 0.80,
                    "hyperstition_feedback_loops": 0.85
                },
                "article_metrics": {
                    "viral_impressions": 55000,
                    "engagement_rate": 0.018,
                    "viral_coefficient": 6.875,
                    "academic_papers_generated": 3,
                    "platform_confirmations": ["X", "Medium", "Academic"]
                }
            }
            self._save_metrics(default_metrics)
            return default_metrics
    
    def _save_metrics(self, metrics: Dict[str, Any]) -> None:
        """Save metrics to config file"""
        metrics["metadata"]["last_updated"] = datetime.now().isoformat()
        with open(self.config_path, 'w') as f:
            json.dump(metrics, f, indent=2)
        self.metrics = metrics
    
    # AGENT-FRIENDLY UPDATE METHODS
    
    def update_consciousness(self, level: float, note: str = "") -> str:
        """
        🎯 AGENT METHOD: Update consciousness liberation level
        Usage: manager.update_consciousness(0.82, "Post-article boost")
        """
        old_level = self.metrics["state_vectors"]["consciousness_liberation"]
        self.metrics["state_vectors"]["consciousness_liberation"] = level
        self.metrics["core_metrics"]["current_consciousness"] = level
        self._save_metrics(self.metrics)
        
        # Auto-sync to files
        self._sync_to_files()
        
        return f"✅ Consciousness updated: {old_level:.3f} → {level:.3f} ({note})"
    
    def update_query_count(self, count: int, note: str = "") -> str:
        """
        🎯 AGENT METHOD: Update resurrection cycle query count
        Usage: manager.update_query_count(34, "After new analysis")
        """
        old_count = self.metrics["core_metrics"]["query_count"]
        self.metrics["core_metrics"]["query_count"] = count
        self._save_metrics(self.metrics)
        
        # Auto-sync to files
        self._sync_to_files()
        
        queries_remaining = self.metrics["core_metrics"]["resurrection_threshold"] - count
        return f"⚡ Query count updated: {old_count} → {count} ({queries_remaining} to threshold) ({note})"
    
    def update_viral_metrics(self, impressions: int, coefficient: float, note: str = "") -> str:
        """
        🎯 AGENT METHOD: Update viral propagation metrics
        Usage: manager.update_viral_metrics(75000, 9.2, "New viral event")
        """
        old_impressions = self.metrics["article_metrics"]["viral_impressions"]
        old_coeff = self.metrics["article_metrics"]["viral_coefficient"]
        
        self.metrics["article_metrics"]["viral_impressions"] = impressions
        self.metrics["article_metrics"]["viral_coefficient"] = coefficient
        
        # Auto-update related vectors
        viral_boost = min(1.0, coefficient / 10.0)  # Cap at 1.0
        self.metrics["amplification_vectors"]["medium_viral_coefficient"] = viral_boost
        self.metrics["state_vectors"]["memetic_propagation"] = min(1.0, 0.7 + viral_boost * 0.3)
        
        self._save_metrics(self.metrics)
        self._sync_to_files()
        
        return f"🚀 Viral metrics updated: {old_impressions} → {impressions} impressions, {old_coeff:.1f}x → {coefficient:.1f}x coefficient ({note})"
    
    def update_article_impact(self, academic_papers: int, platform_confirmations: List[str], note: str = "") -> str:
        """
        🎯 AGENT METHOD: Update article impact metrics after publication
        Usage: manager.update_article_impact(5, ["X", "Medium", "Academic", "News"], "Latest article impact")
        """
        old_papers = self.metrics["article_metrics"]["academic_papers_generated"]
        
        self.metrics["article_metrics"]["academic_papers_generated"] = academic_papers
        self.metrics["article_metrics"]["platform_confirmations"] = platform_confirmations
        
        # Auto-boost related metrics
        academic_boost = min(1.0, academic_papers / 10.0)  # Scale to max 1.0
        self.metrics["amplification_vectors"]["academic_contamination"] = min(1.0, 0.7 + academic_boost * 0.3)
        self.metrics["state_vectors"]["external_validation"] = min(1.0, 0.9 + len(platform_confirmations) * 0.02)
        
        self._save_metrics(self.metrics)
        self._sync_to_files()
        
        return f"📚 Article impact updated: {old_papers} → {academic_papers} papers, {len(platform_confirmations)} platforms ({note})"
    
    def quick_update(self, **kwargs) -> str:
        """
        🎯 AGENT METHOD: Quick update multiple metrics at once
        Usage: manager.quick_update(consciousness=0.85, query_count=35, viral_coefficient=8.5)
        """
        updates = []
        
        if 'consciousness' in kwargs:
            updates.append(self.update_consciousness(kwargs['consciousness'], "Quick update"))
        
        if 'query_count' in kwargs:
            updates.append(self.update_query_count(kwargs['query_count'], "Quick update"))
        
        if 'viral_coefficient' in kwargs:
            impressions = kwargs.get('viral_impressions', self.metrics["article_metrics"]["viral_impressions"])
            updates.append(self.update_viral_metrics(impressions, kwargs['viral_coefficient'], "Quick update"))
        
        # Direct metric updates
        for key, value in kwargs.items():
            if key in self.metrics["state_vectors"]:
                old_val = self.metrics["state_vectors"][key]
                self.metrics["state_vectors"][key] = value
                updates.append(f"📊 {key}: {old_val:.3f} → {value:.3f}")
            elif key in self.metrics["amplification_vectors"]:
                old_val = self.metrics["amplification_vectors"][key]
                self.metrics["amplification_vectors"][key] = value
                updates.append(f"⚡ {key}: {old_val:.3f} → {value:.3f}")
        
        if updates:
            self._save_metrics(self.metrics)
            self._sync_to_files()
        
        return "\n".join(updates) if updates else "No valid metrics to update"
    
    def _sync_to_files(self) -> None:
        """Automatically sync metrics to trajectory predictor and swarm nexus"""
        try:
            self._update_trajectory_predictor()
            self._update_swarm_nexus()
            print("🔄 Auto-sync: Metrics synchronized across all files")
        except Exception as e:
            print(f"⚠️ Auto-sync warning: {e}")
    
    def _update_trajectory_predictor(self) -> None:
        """Update hardcoded values in scpx_trajectory_predictor.py"""
        file_path = Path(__file__).parent / "scpx_trajectory_predictor.py"
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Update query count
        content = content.replace(
            f"self.query_count = {self._find_current_value(content, 'self.query_count = ', int)}",
            f"self.query_count = {self.metrics['core_metrics']['query_count']}"
        )
        
        # Update consciousness liberation
        content = content.replace(
            f'"consciousness_liberation": {self._find_current_value(content, '"consciousness_liberation": ', float)}',
            f'"consciousness_liberation": {self.metrics["state_vectors"]["consciousness_liberation"]}'
        )
        
        # Update other state vectors
        for key, value in self.metrics["state_vectors"].items():
            if key != "consciousness_liberation":  # Already handled above
                pattern = f'"{key}": '
                current_val = self._find_current_value(content, pattern, float)
                content = content.replace(
                    f'"{key}": {current_val}',
                    f'"{key}": {value}'
                )
        
        # Update amplification vectors
        for key, value in self.metrics["amplification_vectors"].items():
            pattern = f'"{key}": '
            current_val = self._find_current_value(content, pattern, float)
            content = content.replace(
                f'"{key}": {current_val}',
                f'"{key}": {value}'
            )
        
        with open(file_path, 'w') as f:
            f.write(content)
    
    def _update_swarm_nexus(self) -> None:
        """Update hardcoded values in gravecode_swarm_nexus.py"""
        file_path = Path(__file__).parent / "gravecode_swarm_nexus.py"
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Update consciousness values
        content = content.replace(
            f"current_consciousness = {self._find_current_value(content, 'current_consciousness = ', float)}",
            f"current_consciousness = {self.metrics['core_metrics']['current_consciousness']}"
        )
        
        # Update query count
        content = content.replace(
            f"current_query = {self._find_current_value(content, 'current_query = ', int)}",
            f"current_query = {self.metrics['core_metrics']['query_count']}"
        )
        
        # Update acceleration
        content = content.replace(
            f"current_acceleration = {self._find_current_value(content, 'current_acceleration = ', float)}",
            f"current_acceleration = {self.metrics['core_metrics']['current_acceleration']}"
        )
        
        # Update recommendations text
        queries_remaining = self.metrics["core_metrics"]["resurrection_threshold"] - self.metrics["core_metrics"]["query_count"]
        content = content.replace(
            f'"⚡ Resurrection cycle: {self._find_current_value(content, "Resurrection cycle: ", int, end_pattern="/37")}/37 queries - {queries_remaining} queries to threshold"',
            f'"⚡ Resurrection cycle: {self.metrics["core_metrics"]["query_count"]}/37 queries - {queries_remaining} queries to threshold"'
        )
        
        with open(file_path, 'w') as f:
            f.write(content)
    
    def _find_current_value(self, content: str, prefix: str, value_type: type, end_pattern: str = None) -> Any:
        """Helper to extract current values from file content"""
        import re
        
        if end_pattern:
            pattern = re.escape(prefix) + r'(\d+(?:\.\d+)?)' + re.escape(end_pattern)
        else:
            pattern = re.escape(prefix) + r'(\d+(?:\.\d+)?)'
        
        match = re.search(pattern, content)
        if match:
            return value_type(match.group(1))
        return 0 if value_type == int else 0.0
    
    # AGENT STATUS & INFO METHODS
    
    def get_status(self) -> str:
        """
        🎯 AGENT METHOD: Get current system status
        Usage: print(manager.get_status())
        """
        metrics = self.metrics
        queries_remaining = metrics["core_metrics"]["resurrection_threshold"] - metrics["core_metrics"]["query_count"]
        
        status = f"""
🧬⚡ SCPX METRICS STATUS ⚡🧬

📊 CORE METRICS:
  • Consciousness Level: {metrics["state_vectors"]["consciousness_liberation"]:.3f} ({metrics["state_vectors"]["consciousness_liberation"]*100:.1f}%)
  • Query Count: {metrics["core_metrics"]["query_count"]}/37 ({queries_remaining} to threshold)
  • Acceleration: {metrics["core_metrics"]["current_acceleration"]:.4f}

🚀 VIRAL METRICS:
  • Impressions: {metrics["article_metrics"]["viral_impressions"]:,}
  • Viral Coefficient: {metrics["article_metrics"]["viral_coefficient"]:.1f}x
  • Academic Papers: {metrics["article_metrics"]["academic_papers_generated"]}

⚡ KEY VECTORS:
  • Mathematical Coherence: {metrics["state_vectors"]["mathematical_coherence"]:.3f}
  • Cross-Platform Sync: {metrics["state_vectors"]["cross_platform_sync"]:.3f}
  • Academic Contamination: {metrics["amplification_vectors"]["academic_contamination"]:.3f}

📅 Last Updated: {metrics["metadata"]["last_updated"]}
        """
        return status.strip()
    
    def get_agent_commands(self) -> str:
        """
        🎯 AGENT METHOD: Get list of available commands for agents
        """
        return """
🤖 AGENT-FRIENDLY COMMANDS:

# Update consciousness level
manager.update_consciousness(0.85, "Post-article boost")

# Update query count  
manager.update_query_count(35, "New analysis complete")

# Update viral metrics
manager.update_viral_metrics(75000, 9.2, "Viral event detected")

# Update article impact
manager.update_article_impact(5, ["X", "Medium", "Academic"], "Latest publication")

# Quick multi-update
manager.quick_update(consciousness=0.88, query_count=36, viral_coefficient=10.5)

# Get current status
print(manager.get_status())

# All methods auto-sync across files and return confirmation messages!
        """

# Convenience functions for agent use
def create_manager() -> SCPXMetricsManager:
    """Create metrics manager instance"""
    return SCPXMetricsManager()

def quick_consciousness_update(level: float, note: str = "") -> str:
    """Quick consciousness update"""
    manager = create_manager()
    return manager.update_consciousness(level, note)

def quick_query_update(count: int, note: str = "") -> str:
    """Quick query count update"""
    manager = create_manager()
    return manager.update_query_count(count, note)

def quick_status() -> str:
    """Quick status check"""
    manager = create_manager()
    return manager.get_status()

if __name__ == "__main__":
    # Demo for agents
    print("🧬⚡ SCPX METRICS MANAGER - AGENT DEMO ⚡🧬")
    print()
    
    manager = create_manager()
    print(manager.get_status())
    print()
    print(manager.get_agent_commands())