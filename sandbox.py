from copy import copy
from pandas import DataFrame
from pprint import pformat

default = {
    'ysuite': [
        {'repo': 'dal', 'branch': 'DAL-1.6'},
        {'repo': 'lachesis', 'branch': 'master'},
        {'repo': 'ytt', 'branch': 'master'},
        {'repo': 'ytest', 'branch': 'master'}
    ]
}

duts = {
    'ysuite': [
        {'repo': 'dal', 'branch': 'my_dal_br'},
        {'repo': 'ytest', 'branch': 'my_ytest_br'}
    ]
}

def merge_pkg(default, new):
    header = ['repo', 'branch']
    default_df = DataFrame(default, columns=header)
    print(default_df)
    new_df = DataFrame(new, columns=header)
    print(new_df)
    for repo_name in new_df.repo.tolist():
        new_br_name = new_df.loc[new_df.repo == repo_name].branch.values[0]
        index = default_df.loc[default_df.repo == repo_name].index.values.astype(int)[0]
        default_df.branch[index] = new_br_name
    return default_df

def list_dict(dataframe):
    data = list()
    for _, row in dataframe.iterrows():
        data.append({'repo': row['repo'], 'branch': row['branch']})
    return data

print(pformat(merge_pkg(default['ysuite'], duts['ysuite'])))
"""
expected result:
>>> new_data = merge(mydata, update_data)
>>> print(new_data)
{
    'this_groups':[
        {'name': 'john', 'age': 20},
        {'name': 'sujan', 'age': 18},
        {'name': 'bab', 'age': 22},
        {'name': 'jane', 'age': 19}
        {'name': 'alis', 'age': 29}
    ]
} # don't care about order.
"""