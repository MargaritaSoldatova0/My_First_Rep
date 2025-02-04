'''
It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child.
Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose)
versus those who were vaccinated but did not contract chicken pox. Return results by sex.
'''
#Задание 1
import pandas as pd 
df=pd.read_csv('NISPUF17.csv',index_col=0) 
df.head() 
def chickenpox_by_sex(): 
    male_df=df[df['SEX']==1]            
    vac_m=male_df[male_df['P_NUMVRC']>=1]   
    cp_m=vac_m[vac_m['HAD_CPOX']==1]        
    counts_cp_m=cp_m['SEX'].count() 
    ncp_m=vac_m[vac_m['HAD_CPOX']==2] 
    counts_ncp_m=ncp_m['SEX'].count() 
    male=counts_cp_m/counts_ncp_m 
    female_df=df[df['SEX']==2]                
    vac_f=female_df[female_df['P_NUMVRC']>=1]   
    cp_f=vac_f[vac_f['HAD_CPOX']==1]        
    counts_cp_f=cp_f['SEX'].count() 
    ncp_f=vac_f[vac_f['HAD_CPOX']==2] 
    counts_ncp_f=ncp_f['SEX'].count() 
    female=counts_cp_f/counts_ncp_f 
    ratio_dict={"male":male,"female":female} 
    return ratio_dict 
    raise NotImplementedError() 
print(chickenpox_by_sex()) 
print(chickenpox_by_sex()['female'])