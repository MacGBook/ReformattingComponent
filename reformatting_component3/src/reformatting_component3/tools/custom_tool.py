from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai_tools import PDFSearchTool

#from crewai_tools import PDFSearchTool
import os

#from crewai_tools import PDFSearchTool


tool = PDFSearchTool(pdf='"/Users/madeleine/reformatting_component3/nws_training_document.pdf"')

os.environ["OpenAI_Key"] = "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"

rag_tool_config = {
    "embedder": {
        "provider": "OpenAI",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "model_kwargs": {
                "trust_remote_code": True
            }
        }
    }
}

pdf_search_tool = PDFSearchTool(
    pdf="/Users/madeleine/reformatting_component3/nws_training_document.pdf",
    config=rag_tool_config,
    summarize=False  # Default
)



# Initialize the tool with a specific PDF path for exclusive search within that document
#tool = PDFSearchTool(pdf='Users/madeleine/reformatting_component3/nws_training_document.pdf')

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."



