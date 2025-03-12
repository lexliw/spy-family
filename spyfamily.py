
#%%
mangaList = [
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-103-pt-br/",
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-102-pt-br/",
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-101-pt-br/",
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-100-pt-br/",
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-99-pt-br/",
    "https://mangaonline.blog/manga/spy-x-family-manga/capitulo-98-pt-br/",
]
#%%
# capitura do site https://mangaonline.blog/manga/spy-x-family-manga/
import requests
import os
def folderName(url):
    folder = url.split('/')[5].replace('.html','')
    num = folder.split('-')[1]
    znum = num.zfill(4)
    return znum

def fileName(url):
    file = url.replace('download-(','').replace(')','').split('/')[9]
    num = file.split('.')[0]
    znum = num.zfill(4)
    result = file.replace(f'{num}',f'{znum}')
    if 'https://mangaonline.biz/wp-content/uploads/' in url:
        result = url.split('/')[7]
    print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print(f'pasta criada {newpath}')
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    imagesRaw = response.text.split('"')
    listRawImages = []
    for chunk in imagesRaw:
        if 'https://mangaonline.blog/wp-content/uploads/WP-manga' in chunk or 'https://mangaonline.blog/wp-content/uploads/WP-manga' in chunk:
            listRawImages.append(chunk.replace("	",''))
        
    # baixar imagens
    for image in listRawImages:
        print(f'imagens: {image}')
        img_data = requests.get(image).content
        file = fileName(image)
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)



#%%
mangaList = [
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-89/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-88/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-87/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-86/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-85/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-84/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-83/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-82/",
    "https://mangaonline.biz/capitulo/spy-x-family-capitulo-81/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-80/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-79/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-78-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-78/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-77/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-76/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-75/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-74/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-73/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-72/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-71/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-70/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-69/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-68-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-68/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-67-2/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-67/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-66/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-65/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-64/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-63/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-62-4/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-62-3/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-62-2/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-62-1/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-61/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-60/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-59/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-58-3/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-58-2/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-58-1/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-57/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-56/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-55/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-54/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-53/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-52/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-51-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-51/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-50/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-49/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-48/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-47/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-46/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-45/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-44/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-43/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-42/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-41/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-40-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-40/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-39/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-38/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-37/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-36/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-35/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-34/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-33/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-32/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-31/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-30/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-29/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-28/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-27-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-27/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-26/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-25/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-24-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-24/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-23/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-22/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-21/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-20/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-19/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-18-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-18/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-17/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-16/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-15-6/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-15-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-15/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-14/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-13/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-12/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-11/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-10/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-9/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-8-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-8/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-7/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-6/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-5/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-4/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-3/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-2/",
    # "https://mangaonline.biz/capitulo/spy-x-family-capitulo-1/",
]
#%%
# capitura do site https://mangaonline.blog/manga/spy-x-family-manga/
import requests
import os
def folderName(url):
    folder = url.split('/')[4].replace('.html','')
    num = folder.split('-')[4]
    znum = num.zfill(4)
    return znum

def fileName(url):
    # https://mangaonline.biz/wp-content/uploads/2023/05/img_or2805231927_0005.png"
    # file = url.replace('download-(','').replace(')','').split('/')[9]
    # num = file.split('.')[0]
    # znum = num.zfill(4)
    # result = file.replace(f'{num}',f'{znum}')
    if 'https://mangaonline.biz/wp-content/uploads/' in url:
        result = url.split('/')[7]
    print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print(f'pasta criada {newpath}')
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    imagesRaw = response.text.split('"')
    listRawImages = []
    for chunk in imagesRaw:
        if 'https://mangaonline.biz/wp-content/uploads' in chunk or 'https://mangaonline.biz/wp-content/uploads' in chunk:
            listRawImages.append(chunk)
    # tirar duplicados
    listRawImages = list(set(listRawImages))
    listRawImages.sort()
    # baixar imagens
    for image in listRawImages:
        print(f'imagens: {image}')
        img_data = requests.get(image).content
        file = fileName(image)
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)

#%%

for manga in mangaList:
    getManga(manga)

# print(response.text) "https://meo.comick.pictures/1-Pt0kp13YjAfKd.jpg",
#%%


import requests

url = "https://content.manganyaa.com/file/mnyaaa/spyfamily/pt/2/17.jpg"

payload = '6fc6f15dd7269bd9fd085ca2ac02924c224c52772432445c0a4c0425a8d75cdf=U2g4NrXTLv6EP7zMPtc_.6GfKJkiWgZal5RWzfu0axI-1741738138-1.2.1.1-LMueVPaIscCcR6IDggEFqRapmQ4JmshTWdbF21jq0Fhqg3eDq.O2oJX3T_vlplIOjOooatIQuPVVjz2ACo8XqezY09vhBlrnc3uz6njeH.VZeu7CLzYdYPbf3yx2GxeG3EZMpUnkah574Ha1T05u.Befl1CwmoZcXJ_MO47c.NgDgKgeQC4XbrlN6kxHFIDoC6ccpBGBlA1vR0OZkzR0Zow4vMYMAidAb4CoD7qJgadjEkNhhRcr674Xoo2ar08fhCOOorlCd0QdRIQCNp.TIngVg5VyxDEfjZ_XBzR0UcY9kTbwIteu.USCVFKmqdgxQ3BtB0axLBDxcc3l0kKM4e341HGldBdZu1gOQW2_YE86NNQKQNQ23LvNwwgx1xk7JnM0xID8fGDjbV7NU6Cl_RwA51spDYYaNXh1ZhZFyOxPYOZSGT_uxzlQ85gTogzD1p9VLU0zRp5OEfP1eNo6zt2FgHXmwfR.BCK5kanHmz0en7JYgJrNmUXKmYeuoaTv3RhHZnmhQHu__Sqc66WyukiqWti3c9MZCvxWH8bBYBaFkkPGtLXvXyNjgGVPO43G2MZJaEx5Z3EW3urojEnUK5X4aJwoSvSNbt5I9TCR37L.DCswbhRvds3iNb2ATa9ZlmgibQ1FQBEFYmrNAhAHZTHZ3mlHNrEpXygHuyPP64xEP6fy3XrJpgLZa0e.1CRbRPuR61fE0eUMuRE.7xflhskltictnPS67YEP3OJPOfGlwPBmQxaOnLKWOF1i.N35HtylNyXshE0tuVcT2JXnu8YHUExk454DZj6KM83WIPuLH5nv_tCuimDW8iMhPDaxoBvLVuGJBldLu7Z1Vp1OJRuzrd_PdY.xR1UcTiglqaUFbpqvGXS14Kn3PCirNOgejhHof6ZuBTUNkgDDNI3GGheGaA.0tteEE93pJ459.93n8k71vw3Geb_EaJPeitoRcRWNLbtbstpBIx5PxYpgofTBIv79IcXBn_WJtrNRu5l1jMLoGDrtJy5PX.VwjSzd5XvmHk.U_0pKr8ozR7EjJIPOpg1TVK.pN22aqQw4s3tWyIVdHPJJiiQWhazmrwcqKEm646Vp7tXlezy.z8j__tsuE9OtX_oYDqIngvgJVUW037eI8o4P1FSOqaME1BVTQ6QUCn_AbCt6.CxA7wXOOIBW4qeGHOzme7mcmptHQvA&53bd8e37490c45835ccba5dd1a276cdd5637481a82128af4771d0cd6e2a6368d=j28WVhHCBLz0EZ6BBREwcAeAUmNAv.8FYErkm5uZhmY-1741738138-1.2.1.1-E4WCu6NU9geoRkeEn5OujY7EmNNr27deY54k1AsXKvnyuURjEPXUmrV0VElXCxWU1t4DyKM5SlRnnUVofk.NofCErSZ8ZfCuXnynx1utKu8.hg4Ug7Q728qiXPID05kdHGMwHG6253CQ2cu_.F3OUXKcTR9YJF6EGIWhxXU.ANbk5TYOiEk3pW2wer4MT_X2WoWVWv68OD7Pl26L7Mvq.q31HU54yYyN4zN7TP0CZpGIVw4TPRB8lvWsEosZ.c0YOk2bv.Rd7feV6lOL2ws98l30.vn8ccqIdQRgiUHBPR8awGMUkeLNSA3pdOrIzpDJJOUtPn0Ku7Zz0qAQfjxNq5Hd.EFsK2pj.MBpzt84JdtlriyitUaghIaGL42QVMvJaaasuNtP3KZyZ3McNaOHNtWIlJ9r5TK7PQrZfuM3YHGnP.EU1o7dNOd081DoPgSNQyXmed13btf3owj3iaSfIE2cmhNvXBZXnZoDmmVWj97o6JRycnzRs8i_gtixj06SCVAosp5fayEK.IGI40X2SSrs4GPJRhClZGq3tv8fEzEGaNdjxvmUCYRQDWaCT8mkn9VEZEvhz2zVlKDJQWIAPDT5HSDnGc99IrAM6AZIoPyPL1yv4rcsLmV5PP1FiZg0JVdm2iGCS4q7w1n.0gcEImAPyRm4AOoChiKyBsKxW1WXAeec8rlKbMETT4qWAZx0XgP4zMH._XAwUWhDrs8VMWUhRaf0K3j6nLLERz3cZeOt.KiR3Fit.mUB3gZ.5aS.k2KGZiQTszRTpg5jSncjBUR6wX8N9Kr6EK3QVLlepS_st43S4XSBvQ0viXEq9DRBNi9zx5fuWrTwyKvif9KVprFN_8_rDskjuA2_07YtUD2EXwGO8odRIUZdxjiuncRIfTm6ypOVkhrk5OqwbIb3GErdLtrN.sEIB7BYjmVmqtsc1T9s03wilDMiBQ_0mnXkaqcaj0f72QUqnwRnLA5NAYkcOPJy5lvphFKRBLaVOYuVS6f2u700sbgokkcolyzOdqm9yXl75Tc4ZYP6vZDkWA7yCBAM8qLYuvjz_n2UKl0jpUhM1FoTGEd5YV70_b_Prg2oxi.GRhb.BlaKVTzcqydFruKsIsb5z2CExHcXsu0Oe_2G0CUM0_H.C7RZCMnUbuE8Bsj1EjP_bZNPa0fGV7C0nssY47f9trS9Gsx7n99n0uSK0rJTxQMzWYHh7Ms74h.Y9cbI1zeS1yDLPh3gXyeZi4djMBZoV5DiJvkNPHeQ8zx1IigGHeb0VXjecR70sjgoZrmGpE4FK0Mndbu5QDbM6jd2ABFQ1j5emS.wOwDg4osLO6giuLq8NInXOStxAXl9jG3.3913CQOqbhmqCgp_ssFxkZmsQB2K7zJ0S6mOZaryvS2nl7YoDiEjB_QVh0YxWJwep08ZJcR0ctaazA8Q8Yq77UH95NqBnOG57g6Jq_iU0hQNPCdG21BlzGkY2R1iQKoxrMoFIP8huTPAdTEGyWCawrtQCXlNAsE0MPXxcJsw.DOtRtp9iGd7top16ZUplXVfi0MQbCprkoqtGTvwGvO4jT17FSLKLb5aLumfohoADmsmNrzvvCI4IHnSzR96HUOMZaKIw5qSsj7eedtqFiF_79zOsRceiH_5jFf7uV6uLyBLKtYjGg4i9F.Dn6g90z_n3mjQLmWN8WnoR1WcLTjtWTAsoyI0i6jYecWVzVwqU2xOl8Pv.zt9nmbh2g6vFei_.ANsEqjMhrePyFc3nuLA1adGqVUAAACYS5aefVpMErBs0yDRxMeLr0Zz1NfPMuWs7BNxudjcoT2g52xSmSYGcTwvBx5Vy1xNGiu4kYjc.RABcRMZUls1HdgNgBnhyidlv9kbw87VjdyzlrCLHRvVDdkSoziRTPItur6SrbkhE_q.QkrzrjBhIa7aTxdodSBBh78jHOvNmwjyjy.QhVnPZfadR3ui_8n4Ed6BOSl3IA_2nzSASVYUg3EzX4H.FI5qmvkNnUbKLBceu78B.7Jey720wlNoKrFYm8wS4aCXMVF6qZXHES4rYliiCws3S70z4slEJhzKv.mCtEOAsdKqf5M3HQv_8grya0CBgC_CyWZS9IaBpQM_PddqfvYzyLg90GYa5pUXsDkQgWN.vDiqetk0ZlmAgbZaZp6kmjCrzTRSOkgSwwNdi5YSVLLde2eGYLEY6vXViKATykgMJdaOUPE.00cz5SAR7YNsg.B2hLk.IxIG.YoRde9xZy1n87.RqsBnbQ5hd6bfzvhAbh2O6rAeJWM8sNG8rT9jwGS.Rr_8aunv0CoH.RGLUnDWU5mcYn6dmdwZGHBMB5EMDuO6yed5HB4uYwpGtIoH5fMaZmJlFJh1Qb5HP8wF2zhxJ1VOXVZA54owyCjRc9YRGxtxv8rdbqWoUMMkT6EktoKlSFqClZit0JoKIJCpUQg.Y6Uy8OvM_YkGarbXH44_GQ77elDE7LhQJooyHhZes598FngdFXnnQ7gtc9zJZWzN8L42M3OpgV6V8VLqitARc2FcEQUtZgCmsRxeJ1FKs0w1MhJDFZHjyjqC9W4Xccl9szXWaYdVECNF6sT1qZ88wgvYQTwthWas1Va1uKVwWnAjdzQ.34tsXCqrCY7dJssgKdwsG42LT5ql0ge6yDn5POhQKFjQGruYgbzQ7BEoqxWIfaqjqbrxQfgcQjq6jbUvzDrOo3bgsgt4v9I49LLoVo4hCu3abq5QAma5DnuCPzbvTt_TqT_5eHgCdRp2yP5YrkGWVVP9Y2x0XojkU1T8n.ll4VKvhxPfVhV8OcL5E7kcHYX9YlcqhgYOWZwdodqZCZw2zfSiVB239yfj40fV9N5f2AAMdbrpoEOmKDNE8nHveFWkO.Z0F.3a_D55NomWERzGCjYLKBLtmyLHAGi3BeKb8aHheIfjCz_ASmmB3twlj8u3rTYBgjA9uevg3egoEbQ6VDUI1kYKB53LGWB8OIXw6_o_3isb7VNTO3KCqvmicfc1nm6CLgcyx1zm1PR5flb6WfQ338IEe3ClOQ9j3KhqE1uSYHZve4G0z4xDcD0VNRlnyzddQA7oh6BAiBCHNCT14vvqvtNmu0iKxj31hT76U3kMUD3xpR7Sv3TO9BnHOTtEpcg8PwuSoW6QLWyrnGDkvy3Q7venMW7feTgpp0IE7s6fAyw_iZovMUzjm_EWjwMYK31Js2lTlDpFMEcechbLifxyYEAQDgErSJGgwLTHgpN_xCCMRTZtl3nJwuA3FUE19RMbKhLk5.uxpxGybO1qfaeHoClBItr0.ExP3Vcwgdatxm5GfOTp.yqM.eOh5f6eIkgiuxdVJTe5wm2jc3aRu6wXI3n.A5J07pMpU5iHhroux48ILZT93elKOvlSdgVKbTmhzMKWOihGtTMtK2hARBI9jo3l3tB4G14257Ycu_w7ErXRMdh4Gt08h6h3O9JcVR_cvbBk2jbtWfSM8Rl3FJrQF2rBtBa4EFaI3fO3j3csPeSehVd3bVB1idaDQl940Zs2R0AcISxx0wZLLVjmlRuZRJDNgGmtuV99jgkSGRl4VqBb9UWJBsobq8UAGRuyUM8ABIfSo8cQNwireNIHybUnlLO2Hav0Vn4BjGLwuKwCocFrDPwUpOr8GgmaMAr1rwMUvopsChhGAPuqEf2G3rYpT5QnUB9iahH.dsBjTz4GUGitYzfSyQ2jwwu8ZzTj0Eu86DoaYZcCaT8dlqvMAUjGQUVzSRbXPQ3r_2O2bvxygeDHwcxFd3VLc1mOI9rj8JFLXGFUJiyXXNQ_xgS138CDFeh8neBvfdT_6IHEmZg7vmL7mg0_38zmm8McSrL8hhSaaMhelZ1OH2bKSAsUgjaiwnvRhF2rfpEqsDg_sV4Pc6kbvn.jJ8Jj3sZVK47ybF4fL.6clGbwxt36CBPEd7ljaWekvWT41b.WtCOObJyuMpJSdjG9wZnFEFzRY67SBGVacZVlCvLRKGviLEupdASDfMc.7.iso7giWKrKlCYLivH1UnpztVNo5ahHs2HN2pT9czZU3pFtu8IgkpVUWJdQxFAfWdHAQ2aky94dnkUDwg6birOUlrnK45laOFSKeKnHC5wBqZpMM38sISdtOiBDUucdexB722lH2_9OKJx.KUojsr.mmgOUjGNVd0aHydYVw1Jv0iTFRvBX2wDc_OINI1Lge8zS1S6Taqe8WmUq39C.2BjOZTcStRVrKBArdRFtchWHiO9zc8bEoEXqoiLO370t2NhRgoKuwbQGwz00mzMJ7yOZb5d6Ka3Nnpa24Ocup8unacKdJH39HeNjAsfdZgKJk6XUAT2hZK4kllw1.VC7DKtIBton1LF4MpUYWjcZMA0FeO3AOJXmZ61Cl9D2lS_.7QUa46FdRXfcuMuABUwUmx0N5rNN3MS5zEXwzDEnaUEbrv3cQl8cnK_P60vno8Nic11A32xY0RFF7bmY1xAexD8LpT.A5k4uAruI2ydZmGGKw.1_UN3tZBC2So0_qKpIs7dxkUGCCaMMoy9haF8frDQphpjMgIJ1yvr1O2vsf_ft0q_Cz4HNuuR_5PlbZ1_z0nG5Cm_6Xi_2Sg6SFov.ZilZ3t14wra1z9krU4r3S7NfD3NG.bzE8EaOOawcTqOtysJWj1_HgZDM5rY19j0P4IpIBr18C5h014zdWxXccJuEPAc1IC2b60ZEpY6wQrCXxnfey9zR2BhuAecplFkD30cjIsLt7Wmjn.GzcFBMwpynhGhO.qykwNSg0wLXIRBCXGfQBA7VecEIX2eRSTJGl2ZBFd5HzFtBKRWEvvmlYYoVmbiO.WUcltIOfWWuf3exr9Hb7pF3txT4IMUNkbdO8BprOLPYkvnD9FTBb5wL_56TJhKuUtgFG2ag4oo0mi2Yf0jVvpbDva_RW.T5hMn9QgWa9wi4Ms9kYx7phMizFyfpRrK3sqpe82D4onAF0uwPnNwfrOviRBNYKMhb4elsPITTvvtw0F4ol3itD7X3UGw8eEnWAMi_cNjPfd7TIuyTG9d_zQYyz138g8GvCm9Z1MOmpm3X9C9WkfCtoJOzStGLuMmxyuPjq582IKWHmpHW02N8VYctCjveK5MG_aR9s1qa.VZ_mX3XU27uBt.PerF1af0GZgKbs3.QIAMFM6QNjNhRdNvZDCe46Up7gzAFTKnaavRPPOe7jj1iZzFQBZ6M2Vjqts9e_wY6hWFM0JVJPYYnQN9X6R0PuQnepm3FHtImgPB9FDfNpdhOEcFkFrbzlMjAtrIBduAMTmbDIRUsy1n37OFlk4.MyvEUj2MZKxLvnxLDq2Xj4disSZUCerxLfJsNugZn_Ih8DB4MZ1Q_htE9wTkUqgT87oSChQCeTBt26_WJkJUMA.BLPUqSzYQN6PqXipPBxhUOZUqyoE22f0ZvrqzSik_iTKrIkPyDr4PTwt288TOf0xfmURrO2oSfqfyGlnybbmgSG77hZCFvKLvBv9DGdaXWbuosfz_9USoXLu1aUt7XSjk6Hde5KmcvDNYFOIs2QhxPe7bjz5Nm04Mpw0GsQ2K1xqy0JC6Q7Xmy1qPCaaS.g4pVSd5p4mseATRYBTq4meMMkGR49xd.HAY7lF_7Q43BK6sDkUiuoJ8ILyKB1.mGdpD9hbXmFxid_b4rP6Oob3HK3FzpxVhDjT18isX1GrYnjVWHC2LiOLyP3JTbw6yw.uPWlzKGd3hSGZ8HpPA2pjOkvYbNK9NVr2y01bJ6NDzumeIlaqDb81HOy0F6ir.UQDm6IATiio2VPLonIRGGr2SbULJ31tSSv83ELCw9appmUMaan74sIMehu9DilddTM4GxH3XvLCnA0vxQvTXEg8coMDhs4HNmUvM8BHLTMhMAXW5lavvgoVDiNUUQCIXfPrupU_ZLc5quYXT8dAypPytJvNEeci8A8YcnJhvsbKnUAmlWgwoNydhs1dagP9pySd5ntnXBWaSIPy50DpppGycECpN07ikBKQ0CTKVr0ukD7V6OicVPFQRIqJmCNwXj_edWSvX3Hbe1xE7qra1JKq50ZDCgo7nSPcrRU.mfHmvtJp5sd5VBD9723SY&33a6cf53a495141347747de6392c33b5c572f57464cbeb17a46ebca3ebcbf87e=TLfC8KRMaY8DnhM2VenZ20ZwhsB8B5Y1hjj7FdfYsUU-1741738151-1.1.1.1-yy3PnaX7fswTLZMdlSfWfNzDx4JMj3LkgjctEgvUNbSYnaDZJJa9XhtSPuRPqK.2HCZ3guTCDB5OYp_2HbOyDdqjqx5eFOp3t_dWKH17aLiBZxFMGVpKHFMg3NDd0uWJDp_5Od5LaIm4G5ynMGT7ROYxO7.VHlp06l66IWeWiHqRZyRXOLYandSa8zwHdQMB'
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': '_ga=GA1.2.1677074339.1741009246; _gid=GA1.2.662747815.1741724953; cf_clearance=S6a27Q4OI6JqnsSP4JTR22jXDyk_T8XfYBkrFY8HRdg-1741736212-1.2.1.1-kFdl21_xWUJN9Po4OBqWAW3vkMzKHUKSbf21sOFBQ67gZB2P3uGAFPpNfctbNEfasV5Dvw8NqY1cxvX5tm10d9KoibaZX8oelfudnbVoUaJaAz1ktfiAe3ygWLD3ll3FPi5oJVDX8JK2hUn9LzOEgqqgROZZDZ5cBM7b5rYRjE4UM0kpfug4itR0dDGud65m3n90Gak6rGnxBKsVePkaNUDV98bN0OF2LwRgBeKI7_bauvOpySdLPpT2k1i4sJARFP1lsISNlxZ3ngH2OymjaxR2DSgK0u4lcH_nHCGUu1JZ9AZQlKnAshmGVhWa7SPcRPmaysqvy7rArOWGRgfN6ikeM9G.Re._0wReNVkbzpnCCd1sdHPvHtTb6nyp9IPVHfaL_ZVG9pHZK0RAQCPWSXkTQwKsHssDPdASibKtTg4; _ga_F8DRSSE2S0=GS1.2.1741737779.3.0.1741737779.0.0.0; cf_clearance=nclvOmCb4wGHxHpiHPtS86FHqCuzTilCq4UOHoqXU1A-1741731400-1.2.1.1-Gk1hq5XKH4iR.0_PAlarvrYHwTYXdBKe3ZBA_vULU4_7f7WKrgxM4cTkEHNyG.V_gmmLE8DyVENjCm4xYFoyQUmJ1aNu__ECgbSy9IfzGJLM0n9bzbre7A08wc1qCOOxqZ2wYg7KvsxaupNJ2xE8M9jQAXnTAcHKDl46fs04nIELF0bGV3BZyx4CYZcEYQiIZwE2FpwJL1iylT0f0I8w0eGXha86CIJ0nwVYjNhpM6ITrHCzU.rwmbWb6gNQMSxsGz4i7Pe2bGKZmNFfz19kC1Yc_HV.fTCzPiuBLDOFmDXn9usZm4Z_de80NvtFF_LjwUhAYMvp5GNrFtBjXIUWFNmkfHLxLVhw7zSwnqY6eXfj1xqh99W2_HI9xC.7AsqBOnCDk_5jryTCK8scKP98VhaS4aJZDUCXvzC7zvMjVic',
  'origin': 'https://content.manganyaa.com',
  'priority': 'u=0, i',
  'referer': 'https://content.manganyaa.com/file/mnyaaa/spyfamily/pt/2/17.jpg?__cf_chl_tk=ZiGJMT9WVsArryUf.G1O_4iitwD66Jb3NZXrt22Bx6I-1741738138-1.0.1.1-3usksbQn5UCYA4eGC1y.kp4djhoNqBIQ59t8E3Oyt_U',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"131.0.6778.264"',
  'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.264", "Chromium";v="131.0.6778.264", "Not_A Brand";v="24.0.0.0"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Linux"',
  'sec-ch-ua-platform-version': '"6.8.0"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)








print(response.status_code)

# %%
# captira do site https://spyfamily.manganyaa.com/ler-online-gratis-portugues
# https://content.manganyaa.com/file/mnyaaa/spyfamily/pt/1/1.jpg

import requests
import os


for volume in range(1,81):
    folder = f'{volume}'.zfill(4)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print('pasta criada')
    else:
        print('manga já baixado')
        continue

    # baixar imagens
    i = 1
    while True:
        url = f"https://content.manganyaa.com/file/mnyaaa/spyfamily/pt/{volume}/{i}.jpg"
        print(f'imagens: {url}')
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200 and response.status_code != 304:
            break
        img_data = requests.get(url, headers=headers, data=payload).content
        file = f'{str(i).zfill(4)}.jpg'
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)
        i += 1

# %%
# verifica imagens vazias
from os import listdir, lstat
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)
imagensvazias = []

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        size = lstat(f'./{folder}/{file}').st_size
        if size == 0:
            print(f'./{folder}/{file} size {size}')
            imagensvazias.append(f'./{folder}/{file}')

print(imagensvazias)
# %%

for image in imagensvazias:
    xpath = image
    volume = int(image.split('/')[1])
    i = int(image.split('/')[2].replace('.jpg',''))

    url = f"https://content.manganyaa.com/file/mnyaaa/spyfamily/pt/{volume}/{i}.jpg"
    print(f'imagens: {url} -- {xpath}')
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 304:
        break
    img_data = requests.get(url, headers=headers, data=payload).content
    file = f'{str(i).zfill(4)}.jpg'
    with open(xpath, 'wb') as handler:
        handler.write(img_data)
# %%

# %%
# cria os readme.md
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

conteudo = '# Spy Family\n\n'
for folder in onlyfolders:
    #- [teste](/chap-0001/readme.md)
    conteudo += f'- [{folder}](/{folder}/readme.md)\n'
    # conteudo += f'<p style="text-align: center;"><button name="menu" onclick="/{folder}/readme.md">{folder}</button></p>'


print('./readme.md')
f = open('./readme.md', 'w')
f.write(conteudo)
f.close()

for i in range(len(onlyfolders)):
    chapterFolder = f'./{onlyfolders[i]}/'
    anterior = '/spy-family/'
    proximo = '/spy-family/'
    menu = '/spy-family/'
    if i - 1 >= 0: 
        anterior = f'/spy-family/{onlyfolders[i-1]}/'
    if i + 1 <= len(onlyfolders)-1: 
        proximo = f'/spy-family/{onlyfolders[i+1]}/'

    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    if 'readme.md' in onlyfiles:
        onlyfiles.remove('readme.md')
    # print(f'{onlyfolders[i]}:{onlyfiles}')
    navegacao = f'##### [ANTERIOR]({anterior})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MENU]({menu})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PRÓXIMO]({proximo})\n'
    conteudo = f'# {onlyfolders[i]}\n{navegacao}'

    for file in onlyfiles:
        conteudo += f'![{file}]({file})\n\n'
    
    conteudo += f'{navegacao}'

    print(f'{chapterFolder}readme.md')
    f = open(f'{chapterFolder}readme.md', 'w')
    f.write(conteudo)
    f.close()
# %%
