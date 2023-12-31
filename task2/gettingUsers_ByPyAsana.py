# pip install asana
import asana
import pandas as pd

f = open('token.txt', 'r')
token = f.readline()
f.close()

client = asana.Client.access_token(token)

workspaces = client.workspaces.get_workspaces({'param': 'value', 'param': 'value'}, opt_pretty=True) # returns a generator
ws_ids = []
for workspace in workspaces:
    ws_ids.append(workspace['gid'])

user_records = []
for ws_id in ws_ids:
    users = client.users.get_users({'param': 'value', 'param': 'value'}, workspace= ws_ids[0], opt_pretty=True)
    for user in users:
        id = user['gid']
        name = user['name']
        resType = user['resource_type']
    user_records.append([id, name, resType, ws_id])

df_userRecords = pd.DataFrame(user_records)

tableHeaders = ['gid', 'user_name', 'resourceType', 'workspace_gid']
df_userRecords.columns = tableHeaders

df_userRecords.to_csv('userRecords.csv', index=False)