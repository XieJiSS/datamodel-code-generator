# generated by datamodel-codegen:
#   filename:  schema.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from pydantic import BaseModel, Field

from . import type_1


class Response(BaseModel):
    inner: type_1.Type1 = Field(..., discriminator='type_', title='Inner')