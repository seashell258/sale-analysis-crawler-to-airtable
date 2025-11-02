 # get cerebro query result
    print("get cerebro query result")
    cerebro_result_dict = {}
    cerebro_query_id_list = [] ###########
    for asin, response in cerebro_query_id_dict.items():
        print(asin, end="\r")
        cerebro_query_id = ""
        try:
            cerebro_query_id = response.json()["data"]["id"] 
	    cerebro_query_id_list.append(cerebro_query_id) ###########3
        except KeyError:
            print("no result for this asin")
            continue

        cerebro_result_dict[asin] = get_cerebro_query_result(cerebro_query_id)
        print(cerebro_result_dict[asin].status_code, end="\r")
        time.sleep(5)


###########################  box id好像不需要。 result dict table data 裡面的id好像並不是black box id 。 畢竟一個filter給進去 只會有一個black box id。 然後一個id對應到很多asin 。 一個asin對應到一個c id 。  cerebro query id dict 裡面的 "id" 就是cerebro id

box_id=[]
for i in range (len(black_box_result_dict['data']['tableData'])):
    box_id.append (black_box_result_dict['data']['tableData'][i]['id'])



    # formatting data
    print("formatting data")
    data = []
    ordinal_number_asin = 0  ##############
    for asin, response in cerebro_result_dict.items():
        serialized_response = response.json()
        ordinal_number_asin = ordinal_number_asin+1
        try:
            search_id = serialized_response["data"]["searchId"]
            for organic_rank, record in enumerate(
                serialized_response["data"]["tableData"][:20]
            ):
                data.append( 
                    [
                        box_id[ordinal_number_asin],   ##############
                        asin,
                        search_id,
                        organic_rank + 1,
                        record["organicPosition"],
                        record["phraseId"],
                        record["phrase"],
                    ]
                )
        except KeyError as e:
            print(str(e))
            continue


##########
final_data = []      
for black_box_asin in cerebro_result_dict.keys() : 
        final_data = cerebro_result_dict[black_box_asin].json()['data']['tableData'].copy()
        for i in range(len(final_data)):
                final_data[i]['black_box_query_id'] =black_box_query_id #filter 01 的 black box id 
                final_data[i]['black_box_query_asin']=black_box_asin
                final_data[i]['cerebro_query_id']= cerebro_query_id_dict['B006NZEC3C'].json()['data']['id']
final_data


##################
#formatting data to fit airtable api requiement
airtable_data = {'records':[]}
for i in range(len(final_data)):
    airtable_data['records'].append({{'fields':{
        'black_box_query_id':'tempId',
        'black_box_query_asin':'tempAsin',
        'cerebro_query_id':'tempCerebroId',
        'phraseId':'tempPhraseId',
        'sponsoredPosition':'tempSponsoredPosition',
        'sponsoredScrapedAt':'tempSponsoredScrapedAt',
        'matchType':'tempMatchType',
        'organicPosition':'tempOrganicPosition',
        'organicScrapedAt':'tempOrganicScrapedAt',
        'phrase':'tempPhrase',
        'resultsNumber':'tempResultsNumber',
        'resultsNumberOver':'tempResultsNumberOver',
        'resultsNumberUpdatedAt':'tempResultsNumberUpdatedAt',
        'impressionExact30':'tempImpressionExact30',
        'exactTitleMatchProductsCount':'tempExactTitleMatchProductsCount',
        'iq':'tempIq',
        'sponsoredAsins':'tempSponsoredAsins',
        'amazonChoice':'tempAmazonChoice',
        'currentAsin':'tempCurrentAsin',
        'amzSuggestedPosition':'tempAmzSuggestedPosition',
        'amzSuggestedScrapedAt':'tempAmzSuggestedScrapedAt',
        'searchVolumeTrend30':'tempSearchVolumeTrend30',
        'newCprExact':'tempNewCprExact',
        'newCprBroad':'tempNewCprBroad',
        'monthlySales':'tempMonthlySales',
        'clickShareRate':'tempClickShareRate',
        'conversionShareRate':'tempConversionShareRate',
        'cpc':'tempCpc',
        'highCpc': None,
        'lowCpc': None,
        'searchFrequencyRank': None,
        'octoberSeasonalSearchVolume': None,
        'decemberSeasonalSearchVolume': None,
        'novemberSeasonalSearchVolume': None},
        },
        'id':i
        })
    print(i)
    
    airtable_data['records'][i]['black_box_query_id']=final_data['black_box_query_id']
    airtable_data['records'][i]['black_box_query_asin']=final_data['black_box_query_asin']
    airtable_data['records'][i]['cerebro_query_id']=final_data['cerebro_query_id']
    airtable_data['records'][i]['phraseId']=final_data['phraseId']
    airtable_data['records'][i]['sponsoredPosition']=final_data['sponsoredPosition']
    airtable_data['records'][i]['matchType']=final_data['matchType']
    airtable_data['records'][i]['organicPosition']=final_data['organicPosition']
    airtable_data['records'][i]['phrase']=final_data['phrase']
    airtable_data['records'][i]['resultsNumber']=final_data['resultsNumber']
    airtable_data['records'][i]['resultsNumberOver']=final_data['resultsNumberOver']
    airtable_data['records'][i]['resultsNumberUpdatedAt']=final_data['resultsNumberUpdatedAt']
    airtable_data['records'][i]['impressionExact30']=final_data['impressionExact30']
    airtable_data['records'][i]['exactTitleMatchProductsCount']=final_data['exactTitleMatchProductsCount']
    airtable_data['records'][i]['iq']=final_data['iq']
    airtable_data['records'][i]['sponsoredAsins']=final_data['sponsoredAsins']
    airtable_data['records'][i]['amazonChoice']=final_data['amazonChoice']
    airtable_data['records'][i]['currentAsin']=final_data['currentAsin']
    airtable_data['records'][i]['amzSuggestedPosition']=final_data['amzSuggestedPosition']
    airtable_data['records'][i]['amzSuggestedScrapedAt']=final_data['amzSuggestedScrapedAt']
    airtable_data['records'][i]['searchVolumeTrend30']=final_data['searchVolumeTrend30']
    airtable_data['records'][i]['newCprExact']=final_data['newCprExact']
    airtable_data['records'][i]['newCprBroad']=final_data['newCprBroad']
    airtable_data['records'][i]['monthlySales']=final_data['monthlySales']
    airtable_data['records'][i]['clickShareRate']=final_data['clickShareRate']
    airtable_data['records'][i]['conversionShareRate']=final_data['conversionShareRate']
    airtable_data['records'][i]['cpc']=final_data['cpc']
    airtable_data['records'][i]['highCpc']=final_data['highCpc']
    airtable_data['records'][i]['lowCpc']=final_data['lowCpc']
    airtable_data['records'][i]['searchFrequencyRank']=final_data['searchFrequencyRank']
    airtable_data['records'][i]['octoberSeasonalSearchVolume']=final_data['octoberSeasonalSearchVolume']
    airtable_data['records'][i]['decemberSeasonalSearchVolume']=final_data['decemberSeasonalSearchVolume']
    airtable_data['records'][i]['novemberSeasonalSearchVolume']=final_data['novemberSeasonalSearchVolume']




