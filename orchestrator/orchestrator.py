from crewai import Crew, Process
from design_studio.crew import create_design_crew
from branding_studio.crew import create_branding_crew
from web_dev_studio.crew import create_webdev_crew
from marketing_studio.crew import create_marketing_crew

class ApexOrchestrator:
    def __init__(self):
        self.design_crew = create_design_crew()
        self.branding_crew = create_branding_crew()
        self.web_crew = create_webdev_crew()
        self.marketing_crew = create_marketing_crew()

    def run_full_project(self, brief: str):
        print(f"Starting project: {brief}")
        
        design_result = self.design_crew.kickoff(inputs={"brief": brief})
        print("Design Studio Complete")
        
        branding_result = self.branding_crew.kickoff(inputs={"brief": brief})
        print("Branding Studio Complete")
        
        web_result = self.web_crew.kickoff(inputs={"brief": brief})
        print("Web Development Studio Complete")
        
        marketing_result = self.marketing_crew.kickoff(inputs={"brief": brief})
        print("Marketing Studio Complete")
        
        return "All studios completed successfully."
