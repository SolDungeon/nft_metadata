import json as json
template = {}
template["name"] = "Name"
template["symbol"] = "D&D"
template["image"] = "https://www.arweave.net/qTdabwXjE5Lhn3GGKvbE3qyY-zHi32OPs7pv_x4L2qo/DungeonCrawler.gif"
template["description"] = "Earn 100 XP"
template["external_url"] = "https://www.sol-dungeon.com/"
template["seller_fee_basis_points"] =  0
template["properties"] = {}
template["properties"]["files"] = []
template["properties"]["files"].append({"uri": "https://www.arweave.net/h4YBqYkvF5bwaWxH8Hx9sG4Q8zRsY6ra-_n9WoE0xrs/DungeonCrawler.gif", "type": "image/gif"})
template["properties"]["files"].append({"uri": "https://www.arweave.net/h4YBqYkvF5bwaWxH8Hx9sG4Q8zRsY6ra-_n9WoE0xrs/DungeonCrawler.gif", "type": "image/gif", "cdn": True})
template["properties"]["category"] = "image"
template["attributes"] = []
template["attributes"].append({"trait_type": "Achievement", "value": "Dungeon Crawler"})

list = open("achievement_list.txt").readlines()
for i in range(len(list)):
	list[i] = list[i].strip("\n").split(",")

git_root = "https://raw.githubusercontent.com/SolDungeon/nft_metadata/main/Achievements/images/"
arweave_root = "https://www.arweave.net/zEoxAi--le-vSy8nCTYoDTyecVYADRKBdDvAp6S2k4E/"
for item in list:
	template["name"] = item[1]
	template["image"] = arweave_root + item[0] + ".gif"
	template["description"] = item[2]
	template["properties"]["files"][0]["uri"] = arweave_root + item[0] + ".gif"
	template["properties"]["files"][1]["uri"] = git_root + item[0] + ".gif"
	template["attributes"][0]["value"] = item[1]
	with open(item[0]+".json", 'w') as f:
    		json.dump(template, f, indent=4)
