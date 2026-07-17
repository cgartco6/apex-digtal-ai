import os
from dotenv import load_dotenv
from rich.console import Console
from orchestrator.orchestrator import ApexOrchestrator

load_dotenv()
console = Console()

def main():
    console.print("[bold green]🚀 Apex Digital AI Orchestrator Started[/bold green]")
    orchestrator = ApexOrchestrator()
    brief = "Build complete brand, website and marketing strategy for AI SaaS product called NovaFlow."
    result = orchestrator.run_full_project(brief)
    console.print("[bold blue]🎉 Project Complete[/bold blue]")

if __name__ == "__main__":
    main()
