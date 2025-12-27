import logging
from zoautil_py.common import clean_shell_input as clean_shell_input, parse_universal_arguments as parse_universal_arguments
from zoautil_py.core import call_zoau_library as call_zoau_library
from zoautil_py.ztypes import DDStatement as DDStatement, ZOAUResponse as ZOAUResponse

logger: logging.Logger

def execute(pgm: str, pgm_args: str | None = None, dds: list[DDStatement] | None = None, json: bool = False, **kwargs) -> ZOAUResponse: ...
def execute_authorized(pgm: str, pgm_args: str | None = None, dds: list[DDStatement] | None = None, json: bool = False, **kwargs) -> ZOAUResponse: ...
