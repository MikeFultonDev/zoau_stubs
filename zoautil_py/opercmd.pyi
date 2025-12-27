import logging
from zoautil_py.common import parse_universal_arguments as parse_universal_arguments
from zoautil_py.core import call_zoau_library as call_zoau_library
from zoautil_py.exceptions import ZOAUException as ZOAUException
from zoautil_py.ztypes import ZOAUResponse as ZOAUResponse

logger: logging.Logger

def execute(command: str, timeout: int = 0, json: bool = False, **kwargs) -> ZOAUResponse: ...
