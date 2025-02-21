"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetUserProjectCountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    user_id: typing.Text
    """Required. The ID of the User to count the projects from"""

    def __init__(self,
        *,
        user_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_id",b"user_id"]) -> None: ...
global___GetUserProjectCountRequest = GetUserProjectCountRequest
