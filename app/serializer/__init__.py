from app.serializer.namespace import ns
from app.serializer.di.bootstrap import bootstrap_di

bootstrap_di()

from app.serializer.dto.serializer_request_dto import serializerRequestDto
from app.serializer.dto.serializer_response_dto import serializerResponseDto
from app.serializer.dto.serialized_record_dto import serializedRecordDto
from app.serializer.dto.serializer_result_dto import serializerResultDto
from app.serializer.dto.bank_record_dto import bankRecordDto

ns.models[serializerRequestDto.name] = serializerRequestDto
ns.models[serializerResponseDto.name] = serializerResponseDto
ns.models[serializedRecordDto.name] = serializedRecordDto
ns.models[serializerResultDto.name] = serializerResultDto
ns.models[bankRecordDto.name] = bankRecordDto


