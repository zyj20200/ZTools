# -*- coding: utf-8 -*-
"""
@author: zyj
@time: 2023/1/5 15:48
"""

import pandas as pd

def parseExcel2json(path:str) -> str:
    try:
        df = pd.read_csv(path, encoding="GBK")
        if not set(df.columns.tolist()) & {'ID', 'id'}:
            df.insert(0, "id", df.index)


        res = ""
        for i in df.to_dict(orient="records"):
            for k, v in i.items():
                res = res + f'{k}: {v} \n'
            res = res + "---------------------------------- \n"
        return res
    except Exception as e:
        return str(e)