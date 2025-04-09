import os 
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field, ConfigDict
from groundx import Document, Groundx
from dotenv import load_dotenv

load_dotenv()

class DocuementSearchToolInput(BaseModel):
    """Input schema for DocumentSearchTool"""
    query: str = Field(..., description= "Query to search the document")

class DocumentSearchTool(BaseModel):
    name: str = "DocumentSearchTool"
    description: str = "Search the document for the given query"
    args_schema: Type[BaseModel] = DocuementSearchToolInput

    model_config = ConfigDict(extra='allow')

    