import pandas as pd
import numpy as np
import folium
import glob
from folium import plugins
import matplotlib.pyplot as plt


list_of_files = glob.glob(r'G:\My Drive\IC Files\Extracted Files\*')


# For latest files
def map_generator(path, year):
    if year <= 1993:
        pass

    if 1993 < year <= 2001:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)
        map = folium.Map(location=[-14.356625, -50.343006], zoom_start=4)
        map.add_child(plugins.HeatMap(merged_df[['latitude', 'longitude', 'City Count']], radius=6))
        map.save('{}_.html'.format(year))

    if 2002 <= year <= 2009:
        df = pd.read_csv(path, encoding='latin-1', delimiter='|', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)
        map = folium.Map(location=[-14.356625, -50.343006], zoom_start=4)
        map.add_child(plugins.HeatMap(merged_df[['latitude', 'longitude', 'City Count']], radius=6))
        map.save('{}_.html'.format(year))

    if year == 2010:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        map = folium.Map(location=[-14.356625, -50.343006], zoom_start=4)
        map.add_child(plugins.HeatMap(merged_df[['latitude', 'longitude', 'City Count']], radius=8))
        map.save('{}.html'.format(year))

    if year > 2010:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', usecols=['Município', 'CNAE 2.0 Classe'])
        df = df[df['CNAE 2.0 Classe'] == 23303]
        df = df.groupby(['Município']).count()
        df.columns = ['City Count']

        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        map = folium.Map(location=[-14.356625, -50.343006], zoom_start=4)
        map.add_child(plugins.HeatMap(merged_df[['latitude', 'longitude', 'City Count']], radius=8))
        map.save('{}.html'.format(year))

def map_generator_matplot(path, year):


    bbox = (-73.5932, -34.4730, -33.4507, 05.1619)
    img = plt.imread('brazil_map.png')

    if year <= 1993:
        pass

    if 1993 < year <= 2001:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        fig, ax = plt.subplots(figsize=(20,8))
        ax.scatter(merged_df.longitude, merged_df.latitude, zorder=1, alpha=0.2, c='b', s=10)
        ax.set_title('Concreteiras no Brasil - {}'.format(year))
        ax.set_xlim(bbox[0], bbox[1])
        ax.set_ylim(bbox[2], bbox[3])
        ax.imshow(img, zorder=0, extent=bbox, aspect='equal')
        plt.savefig('{}.png'.format(year))

    if 2002 <= year <= 2009:
        df = pd.read_csv(path, encoding='latin-1', delimiter='|', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        fig, ax = plt.subplots(figsize=(20,8))
        ax.scatter(merged_df.longitude, merged_df.latitude, zorder=1, alpha=0.2, c='b', s=10)
        ax.set_title('Concreteiras no Brasil - {}'.format(year))
        ax.set_xlim(bbox[0], bbox[1])
        ax.set_ylim(bbox[2], bbox[3])
        ax.imshow(img, zorder=0, extent=bbox, aspect='equal')
        plt.savefig('{}.png'.format(year))


    if year == 2010:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', error_bad_lines=False, usecols=['MUNICIPIO', 'CLAS CNAE 95'])
        df = df[df['CLAS CNAE 95'] == 26301]
        df = df.groupby(['MUNICIPIO']).count()
        df.columns = ['City Count']
        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        fig, ax = plt.subplots(figsize=(20,8))
        ax.scatter(merged_df.longitude, merged_df.latitude, zorder=1, alpha=0.2, c='b', s=10)
        ax.set_title('Concreteiras no Brasil - {}'.format(year))
        ax.set_xlim(bbox[0], bbox[1])
        ax.set_ylim(bbox[2], bbox[3])
        ax.imshow(img, zorder=0, extent=bbox, aspect='equal')
        plt.savefig('{}.png'.format(year))


    if year > 2010:
        df = pd.read_csv(path, encoding='latin-1', delimiter=';', usecols=['Município', 'CNAE 2.0 Classe'])
        df = df[df['CNAE 2.0 Classe'] == 23303]
        df = df.groupby(['Município']).count()
        df.columns = ['City Count']

        municipios = pd.read_csv('municipios.csv', index_col='codigo_ibge')
        municipios = municipios[['latitude', 'longitude']]
        municipios.index = [int(str(i)[:-1]) for i in municipios.index]

        merged_df = pd.merge(municipios, df, left_index=True, right_index=True)

        fig, ax = plt.subplots(figsize=(20,8))
        ax.scatter(merged_df.longitude, merged_df.latitude, zorder=1, alpha=0.2, c='b', s=10)
        ax.set_title('Concreteiras no Brasil - {}'.format(year))
        ax.set_xlim(bbox[0], bbox[1])
        ax.set_ylim(bbox[2], bbox[3])
        ax.imshow(img, zorder=0, extent=bbox, aspect='equal')
        plt.savefig('{}.png'.format(year))





for i in list_of_files:
    year = int(i[-10:-6])
    map_generator_matplot(i, year)
    print(year, 'done')



