import base64
from ipywidgets import HTML


class StopExecution(Exception):
    def _render_traceback_(self):
        pass 

def alert(message):
    message = message.replace('\n', '\\n')
    return f"<script>alert('{message}');</script>"
        
def make_download_button(dialog_filename, raw_contents=''):
    b64 = base64.b64encode(raw_contents.encode())
    payload = b64.decode()
    return HTML(f'''<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<a download="{dialog_filename}" href="data:text/csv;base64,{payload}" download>
<button class="p-Widget jupyter-widgets jupyter-button widget-button mod-warning">Download File</button>
</a>
</body>
</html>
''')


# def make_network_download_button(graph_name):
#     filename = graph_name + '.png'
#     html = f'''<html>
# <head>
# <meta name="viewport" content="width=device-width, initial-scale=1">

# <META HTTP-EQUIV="Access-Control-Allow-Origin" CONTENT="http://localhost:8888">

# <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.3.3/html2canvas.min.js" integrity="sha512-adgfzougYIGhG3Tpb47fZLuMwaULLJQdujqOeWFoGc7vwFvBrFkhaPkJPId5swgdr122mghL/ysQk4oiabmRCQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
# <script src="https://cdn.jsdelivr.net/npm/file-saver@2.0.4/dist/FileSaver.min.js"></script>

# </head>
# <body>
# <button class="p-Widget jupyter-widgets jupyter-button widget-button mod-warning" onclick="capture()">Save as PNG</button>

# <script>
# function capture(){{
#     if(document.querySelector('#mynetwork') == null) {{
#         alert('Please use the "Draw inline" function first to get a picture of the graph.');
#         return;
#     }}
    
#     html2canvas(document.querySelector('#mynetwork')).then(function(canvas) {{
#         saveAs(canvas.toDataURL(), '{filename}');
#     }});
# }}
# </script>
# </body>
# </html>'''
#     return html


# def wait_message(message, duration):
#     html = f'''<html>
# <head>
# <meta name="viewport" content="width=device-width, initial-scale=1">
# </head>
# <body>
# <script>
# function tempAlert(msg,duration)
# {{
#  var el = document.createElement("div");
#  el.setAttribute("style","position:absolute;top:50%;left:50%;border:5px outset red;background-color: lightblue; text-align: center;font-size: 28px;border-radius: 10px;");
#  el.innerHTML = msg;
#  setTimeout(function(){{
#   el.parentNode.removeChild(el);
#  }},duration);
#  document.body.appendChild(el);
# }}

# tempAlert('{message}', {duration});
# </script>

# </body>
# </html>'''
#     return html

