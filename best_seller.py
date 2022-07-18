
def get_items(mydivs):
	Best_Sellers = {}
	ListItems = []
	BS = ""
	LoL_ListItems = []
	Items = []
	Item = 0
	for track in mydivs:
		str_track = str(track)
		if ("aria-label" in str_track):
			print("-----------------------------------------")
			#
			Key = track['aria-label']
			Key = Key.replace("Best Sellers in ", "")
			Key = Key.replace(" - See More", "")
			print(Key)
			#
			Items.append(Key)
			if (LoL_ListItems):
				if (len(LoL_ListItems) == 6):
					Best_Sellers[Items[Item]] = LoL_ListItems
				BS = Key
				LoL_ListItems = []
				Item = Item + 1
		else:
			if ("data-rows" in str_track and "href" in str_track):
				start = str_track.find("data-rows=") + len("data-rows") + 5
				end = str_track.find("</div")
				Product = str_track[start:end]
				li = list(Product.split("-"))
				Link = "https://www.amazon.com/" + track['href']
				#
				ListItems.append(Key)
				ListItems.append(li)
				# ListItems.append(Link)
				#
			if ("title" in str_track):
				ListItems.append(track['title'])
			if ("_p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z" in str_track):
				Exp = "_p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z"
				#
				end_sep = "</span"
				result = []
				tmp = str_track.split(Exp)
				for par in tmp:
					if (end_sep in par):
						result.append(par.split(end_sep)[0])
				if (len(result) == 2):
					Result = str(result[0][2:len(result[0])]) + " - " + str(result[1][2:len(result[1])])
				else:
					Result = str(result[0][2:len(result[0])])
				Result1 = list(Result.split("-"))
				ListItems.append(Result1)
				#
				LoL_ListItems.append(ListItems)
				ListItems = []
	#
	listoflist_1 = []
	Best_Sellers[Items[Item]] = LoL_ListItems
	print("********************************************************")
	for key1 in Best_Sellers:
		print(key1, "-", len(Best_Sellers[key1]))
	print("********************************************************")
	# for key in Best_Sellers:
	# 	for listoflist in Best_Sellers[key]:
	# 		listoflist_1.append(listoflist)
	# print(Best_Sellers)
	return Best_Sellers
