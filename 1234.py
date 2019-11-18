from jinja2 import Template

temp = """  {
    "pk": "{{num}}",
    "model": "ping.HostAddress",
    "fields": {
      "host_addr": "10.55.195.{{host_id}}",
      "description": ""     
    }
  },\n
"""

full_text = "[\n"
for i in range(1, 254):
    param = {
        "num": i,
        "host_id": i
    }
    template = Template(temp)
    text = template.render(**param)
    full_text += text
full_text += "]"
print(full_text)