import pandapower.networks
import pandapower
import pandas as pd


def getCostObjective(net):
    df_gen = pd.DataFrame()
    df_ext_grid = pd.DataFrame()
    # Generators
    df_gen['PP Network Index'] = net.res_gen.index.to_list()
    df_gen['PP Bus Type'] = 'gen'
    df_gen['p_mw'] = net.res_gen['p_mw']
    # External Grid
    df_ext_grid['PP Network Index'] = net.res_ext_grid.index.to_list()
    df_ext_grid['PP Bus Type'] = 'ext_grid'
    df_ext_grid['p_mw'] = net.res_ext_grid['p_mw']
    # Combine
    df_p = pd.concat([df_gen, df_ext_grid])
    df_p = df_p.reset_index()
    cost_df = net.poly_cost.merge(df_p, left_on=['element', 'et'], right_on=['PP Network Index', 'PP Bus Type'])
    # Manually Computing Cost Objective
    cost_obj = (cost_df['cp0_eur'] + cost_df['cp1_eur_per_mw'] * cost_df['p_mw'] + cost_df['cp2_eur_per_mw2'] * cost_df[
        'p_mw'] ** 2).sum()
    return cost_obj


# Example with 30 Case
net = pandapower.networks.case30()
pandapower.runopp(net)
print('case30')
print('Pandapower Cost: ', net.res_cost)
print('Cost from my function: ', getCostObjective(net))
# Example with 118 Case
net = pandapower.networks.case118()
pandapower.runopp(net)
print('case118')
print('Pandapower Cost: ', net.res_cost)
print('Cost from my function: ', getCostObjective(net))