import pandas as pd
import numpy as np
def main():
   df = pd.DataFrame({ '类别': ['文具','文具', '文具','服装','服装','鞋袜', '鞋袜'],
                     '产地': ['晋江','厦门', '厦门','厦门','晋江','晋江', '晋江'],
                      '名称': ['文具盒','钢笔', '订书机','上衣','裤子','棉袜', '丝袜'],
                      '单价': [15.0,np.nan,18.0,50.0,35.0,np.nan,12.0]})
   df["单价"] = df.groupby("产地").transform(lambda x: x.fillna(x.mean()))
   print(df)
if __name__ == "__main__":
main()
