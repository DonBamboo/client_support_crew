from pydantic import BaseModel, Field


class ClientCommunicationResult(BaseModel):
    client_reply: str = Field(
        ...,
        description="The email or message to send to the client, in non-technical language.",
    )
    debugging_findings: str = Field(
        ..., description="A summary of the technical findings and debugging details."
    )
