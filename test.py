import jinja2

_interface = "Gi1/0/4"
_native_vlan = 30
_description = "Cabeza Fria"
_allowed_vlan = "10-50"

loader = jinja2.FileSystemLoader(searchpath="templates/")
env = jinja2.Environment(loader=loader)
File = "trunk.jinja"
template = env.get_template(File)
out_text = template.render(
    interface = _interface,
    description = _description,
    native_vlan = _native_vlan,
    allowed_vlan = _allowed_vlan
)

print(out_text)
    

