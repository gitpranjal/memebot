# an enum class for recording different api responses

import enum


class ApiResponse(enum.Enum):
    SUCCESS_WITH_DATA = 1
    SUCCESS_NO_DATA = 2
    NOT_SUCCESS_200 = 3
    NOT_200 = 4
    NO_DATA_400 = 5
    NOT_SUCCESS_400 = 6
