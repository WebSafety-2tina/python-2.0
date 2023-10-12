pd.set_option( 'display.unicode.east_asian_width ' ,True)
df=pd.read_excel('工作簿pandas.xlsx ')
df1=df[['物料编码",'需求量’,'销售单价']]
df1=df1.groupby(['物料编码','销售单价'])
for (k1,k2),group in df1.groupby(['物料编码','销售单价']):
    print(k1,k2)
    print(group)
    print( ' ------- ')