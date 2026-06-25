import re, datetime

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

now = datetime.datetime.utcnow()
fecha = now.strftime('%d %b %Y %H:%M UTC')

if 'id="lastUpdate"' in c:
    c = re.sub(r'id="lastUpdate">[^<]*<', 'id="lastUpdate">' + fecha + '<', c)
    print("Actualizado:", fecha)
else:
    print("id=lastUpdate no encontrado")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
