import pandas as pd


from collections import defaultdict



# load file
def df_mem(df):
	return '%.1f Mb' % (df.memory_usage(index=True, deep=True).values.sum() / 1024 / 1024)


def load_df(file_name, nrows=1000, header='infer', names=None):
	df = pd.read_csv(file_name, sep='|', nrows=nrows, low_memory=False, header=header, names=names)
	# print("loaded '%s', %d rows (%s)" % (file_name, len(df), df_mem(df)))
	return df


# Map Studies to Mesh
df_mesh_ct = load_df('asset/data/browse_conditions.txt', nrows=None)
df_mesh_ct = df_mesh_ct[['nct_id', 'downcase_mesh_term']]

## search mesh_term
nct_to_mesh_term = defaultdict(set)

for row in df_mesh_ct[['nct_id', 'downcase_mesh_term']].itertuples():
	nct_to_mesh_term[row[1]].add(row[2])

###==========================================================================================================

# # Map Mesh to Keywords
# df_mesh_kw = load_df('data/keywords.txt', nrows=None)
# df_mesh_kw = df_mesh_kw[['nct_id', 'downcase_name']]

# ## get mesh keywords
# nct_to_mesh_kywd = defaultdict(set)

# for row in df_mesh_kw[['nct_id','downcase_name']].itertuples():
#     nct_to_mesh_kywd[row[1]].add(row[2])

###==========================================================================================================
# original mesh fuction in creator py
###==========================================================================================================
# load mesh dataframe

df_mesh = pd.read_csv('asset/data/df_mesh.csv', encoding='unicode_escape')

# Map Mesh Term to ID
mesh_term_to_id = {}

for row in df_mesh[['name', 'ui']].itertuples():
	mesh_term_to_id[row[1]] = row[2]
