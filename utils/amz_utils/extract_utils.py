

Best_Sellers = {}
ListItems = []
BS=""
LoL_ListItems=[]
#
def extact_items():
	for track in mydivs:
		str_track = str(track)
		if ("aria-label" in str_track):
			print ("-----------------------------------------")
			print (track['aria-label'])
	#
		if(LoL_ListItems):
			Best_Sellers[BS] = LoL_ListItems
			BS = track['aria-label']
			LoL_ListItems = []
		else:
			if ("data-rows" in str_track and "href" in str_track):
				start = str_track.find("data-rows=") + len("data-rows")+5
				end = str_track.find("</div")
				Product = str_track[start:end]
				Link = "https://www.amazon.com/"+track['href']
				#
				ListItems.append(Product)
				ListItems.append(Link)
	#
			if ("title" in str_track):
				ListItems.append(track['title'])
			if ("_p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z" in str_track):
				start = str_track.find("_p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z") + len("_p13n-zg-list-carousel-desktop_price_p13n-sc-price__3mJ9Z")+2
				end = str_track.find("</span")
				PriceSt = str_track[start:end]
				ListItems.append(PriceSt)
				LoL_ListItems.append(ListItems)
				ListItems = []
				#
	Best_Sellers[BS] = LoL_ListItems
	print ("********************************************************")
	print ((Best_Sellers[""]))
