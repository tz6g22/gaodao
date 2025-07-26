def get_bagua_info(number):
    bagua_table = {
        1: ("乾", "天"),
        2: ("兑", "泽"),
        3: ("离", "火"),
        4: ("震", "雷"),
        5: ("巽", "风"),
        6: ("坎", "水"),
        7: ("艮", "山"),
        8: ("坤", "地")
    }
    return bagua_table.get(number, ("未知", "未知"))  # 加默认值防止返回 None

topnum = int(input("上卦，男看左："))
topgua = topnum % 8
if topgua == 0:
    topgua = 8  # 修正余数为 0 的情况
gua_name, gua_meaning = get_bagua_info(topgua)
print(f"上卦是：{gua_name}（{gua_meaning}）")


botnum = int(input("下卦，男看左："))
botgua = botnum % 8
if botgua == 0:
    botgua = 8  # 修正余数为 0 的情况
gua_name, gua_meaning = get_bagua_info(botgua)
print(f"上卦是：{gua_name}（{gua_meaning}）")


dongnum = int(input("取动爻，男看左："))
donggua = dongnum % 6
if donggua == 0:
    donggua = 6  #
print(donggua)

top_gua_name, top_gua_meaning = get_bagua_info(topgua)
bot_gua_name, bot_gua_meaning = get_bagua_info(botgua)

print(f"你的卦象是：上卦是：{top_gua_name}（{top_gua_meaning}），下卦是：{bot_gua_name}（{bot_gua_meaning}），动爻是：{donggua}")



