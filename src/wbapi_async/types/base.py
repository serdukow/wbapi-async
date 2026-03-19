from pydantic import BaseModel, ConfigDict


class BaseType(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)
