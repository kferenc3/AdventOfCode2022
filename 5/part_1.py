import pandas as pd
import numpy as np
import os
os.chdir(os.getcwd()+'/5')
def df_creator(s):
    ln = []
    df = []
    spaces = 0
    for x in range(len(s)):
        for y in s[x]:
            if y != ' ':
                ln.append(y.strip())
                spaces = 0
            else:
                spaces +=1
                if spaces == 4:
                    ln.append(' ')
                    spaces = 0
        df.append(ln)
        spaces = 0
        ln = []
    return pd.DataFrame(df).replace(' ', np.nan)

def data_process(f):
    data = [x.replace('\n','') for x in open(f)]
    c = [int(x.split()[1]) for x in data[data.index('')+1:]]
    s_f = [int(x.split()[3])-1 for x in data[data.index('')+1:]]
    s_t = [int(x.split()[5])-1 for x in data[data.index('')+1:]]
    stcks = [x.replace('[','').replace(']','') for x in data[:data.index('')-1]]
    return c, s_f, s_t, df_creator(stcks)

def part_1(flnm):
    crates, stack_from, stack_to, stacks = data_process(flnm)
    for x in range(len(crates)):
        for y in range(crates[x]):
            try:
                stacks.iloc[max(pd.isnull(stacks.iloc[:,stack_to[x]]).to_numpy().nonzero()[0]),stack_to[x]] = stacks.iat[stacks.iloc[:,stack_from[x]].first_valid_index(),stack_from[x]]
                stacks.iat[stacks.iloc[:,stack_from[x]].first_valid_index(),stack_from[x]] = np.nan
            except ValueError:
                df = pd.DataFrame(index=np.arange(1),columns=np.arange(3))
                stacks = pd.concat([df,stacks.loc[:]]).reset_index(drop=True)
                stacks.iloc[max(pd.isnull(stacks.iloc[:,stack_to[x]]).to_numpy().nonzero()[0]),stack_to[x]] = stacks.iat[stacks.iloc[:,stack_from[x]].first_valid_index(),stack_from[x]]
                stacks.iat[stacks.iloc[:,stack_from[x]].first_valid_index(),stack_from[x]] = np.nan
    ans = []
    for x in stacks:
        ans.append(stacks.iat[stacks.iloc[:,x].first_valid_index(),x])
    return ans


if __name__ == '__main__':
    #Part I answer:
    print(part_1('day_5_test.data'))