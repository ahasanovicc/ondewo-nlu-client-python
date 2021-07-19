# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from ondewo.nlu.session_pb2 import (
    DetectIntentResponse as ondewo___nlu___session_pb2___DetectIntentResponse,
    TextInput as ondewo___nlu___session_pb2___TextInput,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class GetAnswerRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    session_id = ... # type: typing___Text
    max_num_answers = ... # type: builtin___int
    threshold_reader = ... # type: builtin___float
    threshold_retriever = ... # type: builtin___float
    threshold_overall = ... # type: builtin___float
    reader_model_name = ... # type: typing___Text

    @property
    def text(self) -> ondewo___nlu___session_pb2___TextInput: ...

    @property
    def filters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___MetadataFilters]: ...

    def __init__(self,
        *,
        session_id : typing___Optional[typing___Text] = None,
        text : typing___Optional[ondewo___nlu___session_pb2___TextInput] = None,
        max_num_answers : typing___Optional[builtin___int] = None,
        threshold_reader : typing___Optional[builtin___float] = None,
        threshold_retriever : typing___Optional[builtin___float] = None,
        threshold_overall : typing___Optional[builtin___float] = None,
        reader_model_name : typing___Optional[typing___Text] = None,
        filters : typing___Optional[typing___Iterable[global___MetadataFilters]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAnswerRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAnswerRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"filters",b"filters",u"max_num_answers",b"max_num_answers",u"reader_model_name",b"reader_model_name",u"session_id",b"session_id",u"text",b"text",u"threshold_overall",b"threshold_overall",u"threshold_reader",b"threshold_reader",u"threshold_retriever",b"threshold_retriever"]) -> None: ...
global___GetAnswerRequest = GetAnswerRequest

class GetAnswerResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def query_result(self) -> ondewo___nlu___session_pb2___DetectIntentResponse: ...

    def __init__(self,
        *,
        query_result : typing___Optional[ondewo___nlu___session_pb2___DetectIntentResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAnswerResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAnswerResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"query_result",b"query_result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"query_result",b"query_result"]) -> None: ...
global___GetAnswerResponse = GetAnswerResponse

class RunScraperResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    container_name = ... # type: typing___Text
    container_id = ... # type: typing___Text

    def __init__(self,
        *,
        container_name : typing___Optional[typing___Text] = None,
        container_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RunScraperResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RunScraperResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"container_id",b"container_id",u"container_name",b"container_name"]) -> None: ...
global___RunScraperResponse = RunScraperResponse

class RunTrainingResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    f1 = ... # type: builtin___float
    accuracy = ... # type: builtin___float

    def __init__(self,
        *,
        f1 : typing___Optional[builtin___float] = None,
        accuracy : typing___Optional[builtin___float] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RunTrainingResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RunTrainingResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"accuracy",b"accuracy",u"f1",b"f1"]) -> None: ...
global___RunTrainingResponse = RunTrainingResponse

class MetadataFilters(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    metadata_field = ... # type: typing___Text
    filters = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    regex_filter = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        metadata_field : typing___Optional[typing___Text] = None,
        filters : typing___Optional[typing___Iterable[typing___Text]] = None,
        regex_filter : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MetadataFilters: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MetadataFilters: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"filters",b"filters",u"metadata_field",b"metadata_field",u"regex_filter",b"regex_filter"]) -> None: ...
global___MetadataFilters = MetadataFilters
