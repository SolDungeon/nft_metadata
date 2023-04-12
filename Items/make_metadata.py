import json as json
template = {}
template["name"] = "Name"
template["symbol"] = "D&D"
template["image"] = "https://www.arweave.net/qTdabwXjE5Lhn3GGKvbE3qyY-zHi32OPs7pv_x4L2qo/DungeonCrawler.gif"
template["description"] = "Earn 100 XP"
template["external_url"] = "https://www.sol-dungeon.com/"
template["seller_fee_basis_points"] =  350
template["properties"] = {}
template["properties"]["files"] = []
template["properties"]["files"].append({"uri": "https://www.arweave.net/h4YBqYkvF5bwaWxH8Hx9sG4Q8zRsY6ra-_n9WoE0xrs/DungeonCrawler.gif", "type": "image/gif"})
template["properties"]["files"].append({"uri": "https://www.arweave.net/h4YBqYkvF5bwaWxH8Hx9sG4Q8zRsY6ra-_n9WoE0xrs/DungeonCrawler.gif", "type": "image/gif", "cdn": True})
template["properties"]["category"] = "image"
template["attributes"] = []
template["attributes"].append({"trait_type": "Rarity", "value": "Dungeon Crawler"})

list = open("item_list.txt").readlines()
for i in range(len(list)):
	list[i] = list[i].strip("\n").split(",")

git_root = "https://raw.githubusercontent.com/SolDungeon/nft_metadata/main/Items/images/"
arweave_root = "https://www.arweave.net/zEoxAi--le-vSy8nCTYoDTyecVYADRKBdDvAp6S2k4E/"
for item in list:
    token_id = item[0]
    token_name = item[1]
    token_desc = item[2]
    token_attrib = item[3]
    template["name"] = token_name
    template["image"] = git_root + token_id + ".gif"
    template["description"] = token_desc
    template["properties"]["files"][0]["uri"] = git_root + token_id + ".gif"
    template["properties"]["files"][1]["uri"] = git_root + token_id + ".gif"
    template["attributes"][0]["value"] = token_attrib
    with open("metadata/" + item[0]+".json", 'w') as f:
        json.dump(template, f, indent=4)
