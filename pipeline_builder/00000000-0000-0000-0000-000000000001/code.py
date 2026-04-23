
from uuid import uuid4
import textwrap
function_string = config["code"]
func_name = f"__exec_{uuid4()}"
indented = textwrap.indent(function_string, "  ")
exec(f"async def {func_name}():\n{indented}")
output = await func_name()
return output
