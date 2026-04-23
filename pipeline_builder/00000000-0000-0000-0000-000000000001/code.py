from uuid import uuid4
import textwrap
function_string = config["code"]
func_name = f"__exec_{uuid4().hex}"
indented = textwrap.indent(function_string, "  ")
namespace = {}
exec(f"async def {func_name}():
{indented}", namespace)
output = await namespace[func_name]()
return output
