import jinja2

_interface = "Gi1/0/4"
_vlan = 30
_description = "Cabeza Fria"

loader = jinja2.FileSystemLoader(searchpath="templates/")
env = jinja2.Environment(loader=loader)
File = "access.jinja"
template = env.get_template(File)
out_text = template.render(
    interface = _interface,
    vlan = _vlan,
    description = _description,
)

print(out_text)
    

