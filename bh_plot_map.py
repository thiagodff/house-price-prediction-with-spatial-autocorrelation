import pandas as pd
import folium
from folium.plugins import BeautifyIcon

# Coordenadas dos limites da cidade https://github.com/tbrugz/geodata-br
belo_horizonte = { "type": "Feature", "properties": {"id": "3106200", "name": "Belo Horizonte", "description": "Belo Horizonte"}, "geometry": { "type": "Polygon", "coordinates": [[[-43.9457849746, -19.7767903180], [-43.9473367812, -19.7922741594], [-43.9431934105, -19.7976070923], [-43.9335019999, -19.7951499673], [-43.9203343492, -19.8027086680], [-43.9137467105, -19.7971376791], [-43.9021947661, -19.8043937653], [-43.8987660252, -19.8019361296], [-43.8983642722, -19.8085357087], [-43.8893407662, -19.8154139510], [-43.8766748813, -19.8133675339], [-43.8758125388, -19.8185084301], [-43.8693632930, -19.8194726409], [-43.8683577746, -19.8249918439], [-43.8618362861, -19.8269137404], [-43.8655802740, -19.8308811375], [-43.8630895852, -19.8370800438], [-43.8675217470, -19.8394894108], [-43.8663248483, -19.8471943017], [-43.8568973205, -19.8573286857], [-43.8625333326, -19.8554425194], [-43.8767780032, -19.8670147148], [-43.8821343649, -19.8613448250], [-43.8961957994, -19.8635972175], [-43.8989222895, -19.8745305173], [-43.9091314428, -19.8757588514], [-43.9055579824, -19.8855614428], [-43.8912261009, -19.8848567318], [-43.8899157716, -19.8918801234], [-43.8865126972, -19.8919730736], [-43.8813337589, -19.9011748014], [-43.8817007269, -19.9054118579], [-43.8690044303, -19.9242842047], [-43.8706677729, -19.9278319329], [-43.8752967904, -19.9320311931], [-43.8915387061, -19.9467641590], [-43.9095956803, -19.9596795873], [-43.9160669178, -19.9635927934], [-43.9393950615, -19.9744521356], [-43.9653466009, -20.0043246495], [-43.9749707319, -20.0084383290], [-43.9921342511, -20.0288102543], [-44.0017993710, -20.0569179764], [-44.0122183078, -20.0593041937], [-44.0171105899, -20.0533886737], [-44.0098884566, -20.0415750489], [-44.0227223059, -20.0305116431], [-44.0359205516, -20.0197794642], [-44.0482550695, -19.9979031437], [-44.0537954119, -19.9955235539], [-44.0561339217, -19.9810429030], [-44.0619669836, -19.9743133955], [-44.0452479624, -19.9731980690], [-44.0340780876, -19.9827905782], [-44.0303343456, -19.9760289363], [-44.0123962295, -19.9676849436], [-44.0135597039, -19.9556319164], [-44.0053652817, -19.9545255611], [-44.0085899740, -19.9528013190], [-44.0084393526, -19.9505340778], [-44.0101098830, -19.9483564328], [-44.0236722601, -19.9429085938], [-44.0267212581, -19.9369446046], [-44.0219784108, -19.9245333459], [-44.0263816397, -19.9176470135], [-44.0288571549, -19.9149519731], [-44.0245819525, -19.9082053074], [-44.0263084446, -19.8984160715], [-44.0149735419, -19.8899937729], [-44.0129240682, -19.8805876470], [-44.0203362865, -19.8670036590], [-44.0183646097, -19.8596099247], [-44.0133877831, -19.8600122313], [-44.0128667569, -19.8542898597], [-44.0087277223, -19.8536813550], [-44.0198118978, -19.8395993630], [-44.0168325354, -19.8311831927], [-44.0127576729, -19.8295669830], [-44.0135824102, -19.8258171921], [-44.0097538743, -19.8255422001], [-44.0053392294, -19.8209055263], [-44.0075553152, -19.8130178038], [-44.0019136544, -19.8018451474], [-43.9918908664, -19.7952335256], [-43.9901098910, -19.7853887276], [-43.9757802428, -19.7811918934], [-43.9652509981, -19.7912141110], [-43.9657764050, -19.7848451737], [-43.9591085350, -19.7780025727], [-43.9483213766, -19.7767704160], [-43.9457849746, -19.7767903180]]] }}

geojson_bh = folium.GeoJson(
    belo_horizonte,
    name='Belo Horizonte',
    style_function=lambda x: {'color': 'black', 'fillOpacity': 0},
)

# lat long de BH
mapa_bh = folium.Map(location=[-19.9166813, -43.9344931], zoom_start=12)

folium.TileLayer('cartodbpositron').add_to(mapa_bh)
geojson_bh.add_to(mapa_bh)

df = pd.read_csv('novo_arquivo_ord_lat_lng.csv')
df_schools = pd.read_csv('ranking_escolas.csv')

def plot_places(row, color):
    id = row['id']
    preco = row['preco']
    lat = row['lat']
    lon = row['lng']

    icon_circle = BeautifyIcon(icon_shape='circle-dot', border_color=color, border_width=5)
    folium.Marker([lat, lon],
        tooltip=preco,
        popup=id,
        icon=icon_circle).add_to(mapa_bh)

# Adicionar marcadores para cada casa
for i, row in df.iterrows():
    if (row['preco'] < 300000):
        plot_places(row, 'orange');
    elif (row['preco'] < 600000):
        plot_places(row, 'red');
    else:
        plot_places(row, '#800020');

# Adicionar marcadores para cada escola
#for i, row in df_schools.iterrows():
#    plot_places(row, 'red');
# Criar um objeto de legenda personalizado
legend_html = '''
<div style="position: fixed;
     bottom: 50px; left: 50px; width: 150px; height: 110px;
     border: 2px solid grey; z-index: 9999; font-size: 14px;
     background-color: white;">
     &nbsp;<b>Legenda</b><br>
     &nbsp;<svg width="15" height="15">
     <rect width="15" height="15" style="fill: orange" />
     </svg>&nbsp; < R$300k<br>
     &nbsp;<svg width="15" height="15">
     <rect width="15" height="15" style="fill: red" />
     </svg>&nbsp;R$300k - R$600k<br>
     &nbsp;<svg width="15" height="15">
     <rect width="15" height="15" style="fill: #800020" />
     </svg>&nbsp;> R$600k<br>
     &nbsp;<svg width="15" height="15">
     <rect width="15" height="15" style="stroke: black; fill: white; stroke-width: 3px;" />
     </svg>&nbsp;Belo Horizonte<br>
</div>
'''

# Adicionar a legenda personalizada ao mapa
mapa_bh.get_root().html.add_child(folium.Element(legend_html))

# Exibir o mapa
mapa_bh.show_in_browser()
